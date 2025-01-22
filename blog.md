---
layout: blog
permalink: /blog
---

## A Mostly Mathematical Travelogue

Welcome to my blog!  Here, I chronicle my mostly mathematical travels as a grad student studying number theory.  

A complete archive of my blog posts can be found [here](https://zporat.github.io/archive.html).  Copy my RSS feed link to add this blog to your favorite RSS reader: <a href="https://zporat.github.io/feed" class="button" style="font-size:12px;"><i class="fas fa-rss" aria-hidden="true"></i>&nbsp; RSS Feed</a>

Here is a map of the places I have been because of math!  Click the pins to see what conferences took me where, and find the blog post about that conference if I have one! 

<div id="map">
</div>
<script>
var map = L.map('map').setView([40, -96], 3.5);
L.tileLayer('http://basemaps.cartocdn.com/rastertiles/voyager/{5}/{x}/{y}{r}.png',{
tileSize: 512,
zoomOffset: -1,
minZoom: 1,
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> Contributors | &copy; <a href="https://carto.com/attributions">CARTO</a>',
crossOrigin: true
}).addTo(map);

var marker = L.marker([42.38671656025372, -72.53139561620192]).addTo(map);
marker.bindPopup("<b>AMS Fall Eastern Sectional Meeting</b><br>University of Massachusetts, Amherst (2022)")

var marker = L.marker([41.813850048276755, -72.24530786395005]).addTo(map);
marker.bindPopup("<b>Connecticut Summer School in Number Theory Conference</b><br>University of Connecticut (2024, 2022, 2020)")

var marker = L.marker([42.81806585736163, -73.92945616036035]).addTo(map);
marker.bindPopup("<b>10th Annual Upstate Number Theory Conference </b><br>Union College (2021)")

var marker = L.marker([46.781893208622165, -71.27477458903167]).addTo(map);
marker.bindPopup("<b>Québec-Maine Number Theory Conference</b><br>Université Laval (2024) | <a href='https://zporat.github.io/2024/10/29/Maine-Quebec.html'>Blog Post</a>")

var marker = L.marker([36.12695329683634, -97.07361084686573]).addTo(map);
marker.bindPopup("<b>36th Automorphic Forms Workshop</b><br>Oklahoma State University (2024)")

var marker = L.marker([42.36040006373788, -71.09417772764208]).addTo(map);
marker.bindPopup("<b>ANTS XVI</b><br>Massachusetts Institute of Technology (2024) | <a href='https://zporat.github.io/2024/07/27/ANTS.html'>Blog Post</a>")

var marker = L.marker([32.23215218707289, -110.95356216073793]).addTo(map);
marker.bindPopup("<b>Arizona Winter School: Abelian Varieties</b><br>University of Arizona (2024) | <a href='https://zporat.github.io/2024/07/20/Mazur-and-Me.html'>Blog Post</a>")
</script>
<br>
If you have somehow stumbled here accidentally and were actually looking for information about me, please visit my [homepage](https://zporat.github.io). 

All opinions expressed here are my own and do not necessarily reflect the opinions of the institutions that I represent.  

---

{% for post in site.posts %}

<h3 style="font-size: 120%; margin-bottom: 3pt; padding-bottom: 0" ><a href="{{ post.url }}">{{ post.title }}</a></h3> 
<p style="color: #595959; font-size:13px; margin-top: 0; padding-top: 0"> Posted on {{ post.pubDate }} </p>
<p> {{ post.content }} </p>
   
---
{% endfor %}
