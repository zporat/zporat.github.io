---
layout: blog
permalink: /blog
---

| [**Home**](https://zporat.github.io) | [**Research**](/research) | [**Teaching**](/teaching) | <span style="color:#043361">**Blog**</span> |

---

## A Mostly Mathematical Travelogue

Welcome to my blog!  Here, I chronicle my mostly mathematical travels as a grad student studying number theory.  

A complete archive of my blog posts can be found [here](https://zporat.github.io/archive.html).  Copy my RSS feed link to add this blog to your favorite RSS reader: <a href="https://zporat.github.io/feed.xml" class="button" style="font-size:12px;"><i class="fas fa-rss" aria-hidden="true"></i>&nbsp; RSS Feed</a>

Below is a map of the places I have been because of math!  Click the pins to see what conferences took me where, and find the blog post about that conference if I have one!

{% include_relative _includes/map.html %}
<br>
If you have somehow stumbled here accidentally and were actually looking for information about me, please visit my [homepage](https://zporat.github.io). 

All opinions expressed here are my own and do not necessarily reflect the opinions of the institutions that I represent.  

---

{% for post in site.posts %}

<h3 style="font-size: 120%; margin-bottom: 3pt; padding-bottom: 0" ><a href="{{ post.url }}">{{ post.title }}</a></h3> 
<p style="color: #595959; font-size:13px; margin-top: 0; padding-top: 0"> Posted on {{ post.pubDate }} </p>
<p> {{ post.content | markdownify | strip_html | truncatewords: 53 }} </p>
<a href="{{ post.url }}" class="button" style="font-size:12px;">&nbsp;Continue Reading&nbsp;&nbsp;<i class="fas fa-angle-double-right" aria-hidden="true"></i>&nbsp;</a>

---
{% endfor %}
