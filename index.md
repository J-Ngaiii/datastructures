---
layout: default
title: Home
---

# Data Structures & Algorithms Notes
Below are my solutions organized by category.

## Debugging: All Found Files
<ul>
  {% for file in site.html_pages %}
    {% if file.path contains "sections/" %}
      <li>
        <a href="{{ file.url | relative_url }}">
          {{ file.title | default: file.name }}
        </a>
        <br><small>Path: {{ file.path }}</small>
      </li>
    {% endif %}
  {% endfor %}
</ul>