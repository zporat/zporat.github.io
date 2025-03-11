<div class="talks">
<ul style="margin-left:-20px">

{% for link in site.data.talks.main %}

<li style="margin-bottom:1rem">
  <div class="col-sm-9">
      <div class="title"><b>{{ link.title }}</b> - {{ link.date }}</div>
      {% if link.spec_session %}
      <ul class="fa-ul" style="margin-left:25px">
        <li><span class="fa-li"><i class="fas fa-map-pin"></i></span><a href="{{ link.conf_website }}">{{ link.conf }}</a>: {{ link.spec_session}} ({{ link.location }})</li>
      </ul>
      {% else %}
      <ul class="fa-ul" style="margin-left:25px">
        <li><span class="fa-li"><i class="fas fa-map-pin"></i></span><a href="{{ link.conf_website }}">{{ link.conf }}</a> ({{ link.location }})</li>
      </ul>
      {% endif %}
  </div>
</li>

{% endfor %}

</ul>
</div>

