---
layout: blog
permalink: /archive
---

## Blog Archive

Here is a complete archive of my blog posts chronologically:
<ul>
  {% for post in site.posts %}
    <li>
      {{ post.date }}: <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

