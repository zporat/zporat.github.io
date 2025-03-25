<div id="map">
<style>
img.huechange { filter: hue-rotate(120deg); }
</style>
<script>
var map = L.map('map').setView([40, -96], 3.5);
L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{@2x}.png',{
minZoom: 1,
maxZoom: 18,
subdomains: 'abcd',
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> Contributors | &copy; <a href="https://carto.com/attributions">CARTO</a>',
crossOrigin: true
}).addTo(map);

{% for conf in site.data.map.upcoming %}

var marker = L.marker([{{ conf.coordinates }}]).addTo(map);
marker.bindPopup("<b>{{ conf.title }}</b><br>{{ conf.location }} (Upcoming)");
marker._icon.classList.add("huechange");

{% for conf in site.data.map.past %}

  {% if conf.blog_post %}

var marker = L.marker([{{ conf.coordinates }}]).addTo(map);
marker.bindPopup("<b>{{ conf.title }}</b><br>{{ conf.location }} ({{ conf.date }}) | <a href="{{ conf.blog_post }}">Blog Post</a>");

  {% else %}

var marker = L.marker([{{ conf.coordinates }}]).addTo(map);
marker.bindPopup("<b>{{ conf.title }}</b><br>{{ conf.location }} ({{ conf.date }})");

</script>
</div>