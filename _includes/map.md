{% for conf in site.data.map.main %}

  {% if conf.blog_post %}

var marker = L.marker([{{ conf.coordinates }}]).addTo(map);
marker.bindPopup("<b>{{ conf.title }}</b><br>{{ conf.location }} ({{ conf.date }}) | <a href="{{ conf.blog_post }}">Blog Post</a>");

  {% else %}

var marker = L.marker([{{ conf.coordinates }}]).addTo(map);
marker.bindPopup("<b>{{ conf.title }}</b><br>{{ conf.location }} ({{ conf.date }})");

