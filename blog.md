---
layout: blog
permalink: /blog
---

## A Mostly Mathematical Travelogue

Welcome to my blog!  Here, I chronicle my mostly mathematical travels as a grad student studying number theory.  

A complete archive of my blog posts can be found [here](https://zporat.github.io/archive.html).  Copy my RSS feed link to add this blog to your favorite RSS reader: <a href="https://zporat.github.io/feed" class="button" style="font-size:12px;"><i class="fas fa-rss" aria-hidden="true"></i>&nbsp; RSS Feed</a>

If you have somehow stumbled here accidentally and were actually looking for information about me, please visit my [homepage](https://zporat.github.io). 

All opinions expressed here are my own and do not necessarily reflect the opinions of the institutions that I represent.  

---

{% for post in site.posts %}

<h3 style="font-size: 120%"><a href="{{ post.url }}">{{ post.title }}</a></h3> 
<p> {{ post.content }} </p>
<p style="color: #595959; font-size:13px"> Posted on {{ post.pubDate }} </p>   

---
{% endfor %}
