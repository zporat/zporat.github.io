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