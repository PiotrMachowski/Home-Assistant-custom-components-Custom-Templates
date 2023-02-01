import asyncio
from collections import ChainMap
import logging

from homeassistant.exceptions import TemplateError
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED, STATE_UNKNOWN
from homeassistant.core import Event, HomeAssistant, valid_entity_id
from homeassistant.helpers.template import _get_state_if_valid, _RESERVED_NAMES, Template, TemplateEnvironment
from homeassistant.helpers.translation import _TranslationCache, TRANSLATION_FLATTEN_CACHE, TRANSLATION_LOAD_LOCK
from homeassistant.loader import bind_hass

from .const import (DOMAIN, CUSTOM_TEMPLATES_SCHEMA, CONF_PRELOAD_TRANSLATIONS, CONST_EVAL_FUNCTION_NAME,
                    CONST_STATE_TRANSLATED_FUNCTION_NAME)

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = CUSTOM_TEMPLATES_SCHEMA


class StateTranslated:

    def __init__(self, hass: HomeAssistant):
        self._hass = hass

    def __call__(self, entity_id: str, language: str):
        state = None
        if "." in entity_id:
            state = _get_state_if_valid(self._hass, entity_id)

        else:
            if entity_id in _RESERVED_NAMES:
                return None

            if not valid_entity_id(f"{entity_id}.entity"):
                raise TemplateError(f"Invalid domain name '{entity_id}'")  # type: ignore[arg-type]

        if state is None:
            return STATE_UNKNOWN
        domain = state.domain
        device_class = "_"
        if "device_class" in state.attributes:
            device_class = state.attributes["device_class"]
        translations = get_cached_translations(self._hass, language, "state", domain)
        key = f"component.{domain}.state.{device_class}.{state.state}"
        if len(translations) > 0 and key in translations:
            return str(translations[key])
        return state.state

    def __repr__(self):
        return "<template StateTranslated>"


class EvalTemplate:

    def __init__(self, hass: HomeAssistant):
        self._hass = hass

    def __call__(self, content: str):
        tpl = Template(content, self._hass)
        return tpl.async_render()

    def __repr__(self):
        return "<template EvalTemplate>"


def get_cached(
        self,
        language: str,
        category: str,
        components: set[str],
):
    cached = self.cache.get(language, {})
    return [cached.get(component, {}).get(category, {}) for component in components]


@bind_hass
async def load_translations_to_cache(
        hass: HomeAssistant,
        language: str,
):
    lock = hass.data.setdefault(TRANSLATION_LOAD_LOCK, asyncio.Lock())

    async with lock:
        cache = hass.data.setdefault(TRANSLATION_FLATTEN_CACHE, _TranslationCache(hass))
        await cache.async_fetch(language, "states", set(hass.config.components))


@bind_hass
def get_cached_translations(
        hass: HomeAssistant,
        language: str,
        category: str,
        integration=None,
):
    if integration is not None:
        components = {integration}
    elif category == "state":
        components = set(hass.config.components)
    else:
        components = {
            component for component in hass.config.components if "." not in component
        }

    cache = hass.data.setdefault(TRANSLATION_FLATTEN_CACHE, _TranslationCache(hass))
    cached = cache.get_cached(language, category, components)

    return dict(ChainMap(*cached))


def setup(hass, config):
    if DOMAIN not in config:
        return True
    if CONF_PRELOAD_TRANSLATIONS in config[DOMAIN]:
        languages = config[DOMAIN][CONF_PRELOAD_TRANSLATIONS]

        async def load_translations(_event: Event):
            for language in languages:
                await load_translations_to_cache(hass, language)

        hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STARTED, load_translations)

    _TranslationCache.get_cached = get_cached

    def is_safe_callable(self, obj):
        return isinstance(obj, (StateTranslated, EvalTemplate)) or self.is_safe_callable_old(obj)

    TemplateEnvironment.is_safe_callable_old = TemplateEnvironment.is_safe_callable
    TemplateEnvironment.is_safe_callable = is_safe_callable

    state_translated_template = StateTranslated(hass)
    eval_template = EvalTemplate(hass)
    tpl = Template("", hass)
    tpl._strict = False
    tpl._limited = False
    tpl._env.globals[CONST_STATE_TRANSLATED_FUNCTION_NAME] = state_translated_template
    tpl._env.globals[CONST_EVAL_FUNCTION_NAME] = eval_template
    tpl._env.filters[CONST_EVAL_FUNCTION_NAME] = eval_template
    tpl._strict = True
    tpl._limited = False
    tpl._env.globals[CONST_STATE_TRANSLATED_FUNCTION_NAME] = state_translated_template
    tpl._env.globals[CONST_EVAL_FUNCTION_NAME] = eval_template
    tpl._env.filters[CONST_EVAL_FUNCTION_NAME] = eval_template

    return True
