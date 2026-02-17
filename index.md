---
layout: default
title: Home
---

# JNgai's Datastructures, Algorithms and SQL Notes

## Instructions
Welcome! Select a module below to view all conceptual notes and code solutions for that topic.

<ul>
  {% for p in site.pages %}
    {% if p.path contains "sections/" %}
      <li>
        <a href="{{ p.url | relative_url }}" style="font-size: 1.2rem; font-weight: bold;">
          {{ p.title | default: p.name | replace: ".md", "" | capitalize }}
        </a>
      </li>
    {% endif %}
  {% endfor %}
</ul>