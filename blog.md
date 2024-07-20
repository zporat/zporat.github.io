---
layout: blog
permalink: /blog
---

## A Mostly Mathematical Travelogue

Welcome to my blog!  Here, I chronicle my mostly mathematical travels as a grad student studying number theory.  

If you have somehow stumbled here accidentally and were actually looking for information about me, please visit my [homepage](https://zporat.github.io). 

---

{% for post in site.posts %}

<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
<p><small> <i class="fas fa-calendar-alt"></i>&nbsp; {{ post.pubDate }}</small></p>    
<p> {{ post.content }} </p>

---
{% endfor %}
