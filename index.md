---
layout: default
title: Home
---

# Data Structures & Algorithms Notes

Below are the solutions found in your folders:

<ul>
  {% for p in site.pages %}
    {% if p.path contains "sections/" and p.ext == ".md" %}
      <li>
        <a href="{{ p.url | relative_url }}">
          {{ p.title | default: p.name | replace: ".md", "" | replace: "-", " " | capitalize }}
        </a>
      </li>
    {% endif %}
  {% endfor %}
</ul>