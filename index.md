---
layout: default
title: Home
---

# Data Structures & Algorithms Notes

Below are my solutions organized by category.

{% assign sections = site.pages | group_by_exp: "item", "item.path | split: '/' | slice: 1" %}

{% for section in sections %}
  {% if section.name contains "sections" %}
    ## {{ section.name | replace: "sections,", "" | capitalize }}
    <ul>
      {% for file in section.items %}
        {% if file.extension == ".md" %}
          <li>
            <a href="{{ file.url | relative_url }}">
              {{ file.title | default: file.name | replace: ".md", "" | replace: "-", " " | capitalize }}
            </a>
          </li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}