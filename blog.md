---
layout: blog
permalink: /blog
---

## A Mostly Mathematical Travelogue

Welcome to my blog!  Here, I chronicle my mostly mathematical travels as a grad student studying number theory.  

If you have somehow stumbled here accidentally and were actually looking for information about me, please visit my [homepage](https://zporat.github.io). 

---

{% for post in site.posts %}

<style>
    h3 + p {
        line-height: 0px;
        margin-top: 0px;
    }
</style>

<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>

<p style="color: #595959"> <font size="-1"> Posted on {{ post.pubDate }} </font>  </p>    

<p> {{ post.content }} </p>

---
{% endfor %}
