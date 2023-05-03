[![HACS Custom][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Community Forum][community_forum_shield]][community_forum]
[![Ko-Fi][ko_fi_shield]][ko_fi]
[![buycoffee.to][buycoffee_to_shield]][buycoffee_to]
[![PayPal.Me][paypal_me_shield]][paypal_me]
[![Revolut.Me][revolut_me_shield]][revolut_me]


[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Custom&style=popout&color=orange&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/faq/custom_repositories

[latest_release]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Custom-Templates/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Custom-Templates.svg?style=popout

[releases]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Custom-Templates/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/PiotrMachowski/Home-Assistant-custom-components-Custom-Templates/total

[community_forum_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Forum&style=popout&color=41bdf5&logo=HomeAssistant&logoColor=white
[community_forum]: https://community.home-assistant.io/t/custom-templates/528378

[ko_fi_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Ko-Fi&color=F16061&logo=ko-fi&logoColor=white
[ko_fi]: https://ko-fi.com/piotrmachowski

[buycoffee_to_shield]: https://shields.io/badge/buycoffee.to-white?style=flat&labelColor=white&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhmlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVh1YQcchQnayIijhKFYtgobQVWnUweemP0KQhSXFxFFwLDv4sVh1cnHV1cBUEwR8QVxcnRRcp8b6k0CLGC4/3cd49h/fuA4R6malmxzigapaRisfEbG5FDLzChxB6MIZ+iZl6Ir2QgWd93VM31V2UZ3n3/Vm9St5kgE8knmW6YRGvE09vWjrnfeIwK0kK8TnxqEEXJH7kuuzyG+eiwwLPDBuZ1BxxmFgstrHcxqxkqMRTxBFF1ShfyLqscN7irJarrHlP/sJgXltOc53WEOJYRAJJiJBRxQbKsBClXSPFRIrOYx7+QcefJJdMrg0wcsyjAhWS4wf/g9+zNQuTE25SMAZ0vtj2xzAQ2AUaNdv+PrbtxgngfwautJa/UgdmPkmvtbTIEdC3DVxctzR5D7jcAQaedMmQHMlPSygUgPcz+qYcELoFulfduTXPcfoAZGhWSzfAwSEwUqTsNY93d7XP7d+e5vx+AIahcq//o+yoAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5wETCy4vFNqLzwAAAVpJREFUOMvd0rFLVXEYxvHPOedKJnKJhrDLuUFREULE7YDCMYj+AydpsCWiaKu29hZxiP4Al4aWwC1EdFI4Q3hqEmkIBI8ZChWXKNLLvS0/Qcza84V3enm/7/s878t/HxGkeTaIGziP+EB918nawu7Dq1d0e1+2J2bepnk2jFEUVVF+qKV51o9neBCaugfge70keoxxUbSWjrQ+4SUyzKZ5NlnDZdzGG7w4DIh+dtZEFntDA98l8S0MYwctNGrYz9WqKJePFLq80g5Sr+EHlnATp+NA+4qLaZ7FfzMrzbMBjGEdq8GrJMZnvAvFC/8wfAwjWMQ8XmMzaW9sdevNRgd3MFhvNpbaG1u/Dk2/hOc4gadVUa7Um425qii/7Z+xH9O4jwW8Cqv24Tru4hyeVEU588cfBMgpPMI9nMFe0BkFzVOYrYqycyQgQJLwTC2cDZCPeF8V5Y7jGb8BUpRicy7OU5MAAAAASUVORK5CYII=
[buycoffee_to]: https://buycoffee.to/piotrmachowski

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/PiMachowski

[revolut_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Revolut&logo=revolut
[revolut_me]: https://revolut.me/314ma


# Custom Templates

This integration adds possibility to use new functions in Home Assistant Jinja2 templating engine:
- `ct_state_translated` - returns translated state of an entity
- `ct_state_attr_translated` - returns translated value of an attribute of an entity
- `ct_translated` - returns translation for a given key
- `ct_all_translations` - returns all available translations (that can be used with `ct_translated`)
- `ct_eval` - evaluates text as a template

## Usage

### `ct_state_translated`

This function returns translated state of an entity.

<table>
<tr>
<th>
Input
</th>
<th>
Output
</th>
</tr>
<tr>
<td>

```
State: {{ states("sun.sun") }}
Translated en: {{ ct_state_translated("sun.sun", "en") }}
Translated en: {{ "sun.sun" | ct_state_translated("en") }}
Translated nl: {{ ct_state_translated("sun.sun", "nl") }}
Translated nl: {{ "sun.sun" | ct_state_translated("nl") }}
```

</td>
<td>

```
State: below_horizon
Translated en: Below horizon
Translated en: Below horizon
Translated nl: Onder de horizon
Translated nl: Onder de horizon
```

</td>
</tr>
</table>

### `ct_state_attr_translated`

This function returns translated value of an attribute of an entity.

<table>
<tr>
<th>
Input
</th>
<th>
Output
</th>
</tr>
<tr>
<td>

```
Attribute: {{ state_attr("automation.example", "mode") }}
Translated en: {{ ct_state_attr_translated("automation.example", "mode", "en") }}
Translated en: {{ "automation.example" | ct_state_attr_translated("mode", "en") }}
Translated nl: {{ ct_state_attr_translated("automation.example", "mode", "nl") }}
Translated nl: {{ "automation.example" | ct_state_attr_translated("mode", "nl") }}
```

</td>
<td>

```
Attribute: single
Translated en: Single
Translated en: Single
Translated nl: Enkelvoudig
Translated nl: Enkelvoudig
```

</td>
</tr>
</table>

### `ct_translated`

This function returns translation for a given key. You can use `ct_all_translations` to check available keys.

<table>
<tr>
<th>
Input
</th>
<th>
Output
</th>
</tr>
<tr>
<td>

```yaml
Translated en: {{ ct_translated("component.sun.state._.below_horizon", "en") }}
Translated en: {{ "component.sun.state._.below_horizon" | ct_translated("en") }}
Translated nl: {{ ct_translated("component.sun.state._.below_horizon", "nl") }}
Translated nl: {{ "component.sun.state._.below_horizon" | ct_translated("nl") }}
```

</td>
<td>

```
Translated en: Below horizon
Translated en: Below horizon
Translated nl: Onder de horizon
Translated nl: Onder de horizon
```

</td>
</tr>
</table>

### `ct_all_translations`

This function returns all available translations.

<table>
<tr>
<th>
Input
</th>
<th>
Output
</th>
</tr>
<tr>
<td>

```
{{ ct_all_translations("en") }}
```

</td>
<td>

```json
{
  "component.sun.state._.above_horizon": "Above horizon",
  "component.sun.state._.below_horizon": "Below horizon"
}
```

</td>
</tr>
</table>

### `ct_eval`

This function evaluates text as a template.

<table>
<tr>
<th>
Input
</th>
<th>
Output
</th>
</tr>
<tr>
<td>

```yaml
{% set template_text = "{{ states('sun.sun') }}" %}
{{ ct_eval(template_text) }}
{{ template_text | ct_eval }}
```

</td>
<td> 

```
below_horizon
below_horizon
```

</td>
</tr>
</table>

## Configuration

To use this integration you have to add following config in `configuration.yaml`:

```yaml
custom_templates:
  preload_translations:
    - en
    - nl
```

Section `preload_translations` should contain a list of languages you want to use with `ct_state_translated` function.

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

* In _Integrations_ section add this repository `https://github.com/PiotrMachowski/Home-Assistant-custom-components-Custom-Templates` with type `integration`
* Install added repository
 
### Manual

Download [*custom_templates.zip*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Custom-Templates/releases/latest/download/custom_templates.zip) and extract its contents to `config/custom_components/custom_templates` directory:
```bash
mkdir -p custom_components/custom_templates
cd custom_components/custom_templates
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Custom-Templates/releases/latest/download/custom_templates.zip
unzip custom_templates.zip
rm custom_templates.zip
```

Finally, restart Home Assistant and configure the integration.



<a href='https://ko-fi.com/piotrmachowski' target='_blank'><img height='35px' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' />
<a href="https://buycoffee.to/piotrmachowski" target="_blank"><img src="https://buycoffee.to/btn/buycoffeeto-btn-primary.svg" height="35px" alt="Postaw mi kawę na buycoffee.to"></a>
<a href="https://paypal.me/PiMachowski" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" border="0" alt="PayPal Logo" height="35px" style="height: auto !important;width: auto !important;"></a>
<a href="https://revolut.me/314ma" target="_blank"><img src="https://www.revolut.com/favicon/android-chrome-192x192.png" height="35px" alt="Revolut"></a>
