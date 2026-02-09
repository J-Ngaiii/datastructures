---
layout: default
title: Home
---

# My Coding Solutions

## Navigation
{% for file in site.static_files %}
  {% if file.path contains "sections" and file.extname == ".md" %}
    * [{{ file.basename | replace: "-", " " | capitalize }}]({{ file.path | relative_url }})
  {% endif %}
{% endfor %}

## Pages Found
<ul>
  {% for p in site.pages %}
    {% if p.path contains "sections" %}
      <li>
        <a href="{{ p.url | relative_url }}">{{ p.title | default: p.name }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>