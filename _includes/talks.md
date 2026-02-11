<div class="talks">
<ul style="margin-left:-20px">

{% for link in site.data.talks.upcoming %}

<li style="margin-bottom:1rem">
  <div class="col-sm-9">
      <div class="title">
      {% if link.conf %}      
        {% if link.spec_session %}
          <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b>, {{ link.spec_session}} {{ link.location }} - Upcoming ({{ link.date }})
        {% else %}
          <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b> {{ link.location }} - Upcoming ({{ link.date }})
        {% endif %}
      {% else %}
        <b><a href="{{ link.conf_website }}">{{ link.location }}</a></b> - Upcoming ({{ link.date }})
      </div>
  </div>
</li>

{% endfor %}

{% for link in site.data.talks.past %}

<li style="margin-bottom:1rem">
  <div class="col-sm-9">
      <div class="title"><b>{{ link.title }}</b> - {{ link.date }}</div>
      <ul class="fa-ul" style="margin-left:25px">
      {% if link.spec_session %}
        <li><span class="fa-li"><i class="fas fa-map-pin"></i></span><a href="{{ link.conf_website }}">{{ link.conf }}</a>: {{ link.spec_session}} {{ link.location }}</li>
      {% else %}
        <li><span class="fa-li"><i class="fas fa-map-pin"></i></span><a href="{{ link.conf_website }}">{{ link.conf }}</a> {{ link.location }}</li>
      {% endif %}
      </ul>
  </div>
</li>

{% endfor %}

</ul>
</div>

