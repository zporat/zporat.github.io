---
layout: blog
permalink: /archive
---

## Blog Archive

Here is a complete archive of my blog posts reverse chronologically by post date:
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> ({{ post.confDate }})
    </li>
  {% endfor %}
</ul>

---

<a href="https://zporat.github.io" class="button" style="font-size:12px;"><i class="fas fa-home" aria-hidden="true"></i>&nbsp; Website Home</a> <a href="https://zporat.github.io/blog.html" class="button" style="font-size:12px;"><i class="fas fa-blog" aria-hidden="true"></i>&nbsp; Blog Home</a>