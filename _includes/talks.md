<div class="talks">
<ul style="margin-left:-20px">

{% for link in site.data.talks.upcoming %}

<li style="margin-bottom:0.3rem">
  <div class="col-sm-9">
      {% if link.conf %}      
        {% if link.spec_session %}
          Upcoming ({{ link.date }}) - <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b>, {{ link.spec_session}} {{ link.location }}
        {% else %}
          Upcoming ({{ link.date }}) - <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b> {{ link.location }}
        {% endif %}
      {% else %}
        {% if link.conf_website %}
          Upcoming ({{ link.date }}) - <b><a href="{{ link.conf_website }}">{{ link.location }}</a></b>
        {% else%}
          Upcoming ({{ link.date }}) - <b>{{ link.location }}</b>
        {% endif %}
      {% endif %}
  </div>
</li>

{% endfor %}

{% for link in site.data.talks.past %}

<li style="margin-bottom:0.3rem">
  <div class="col-sm-9">
      {% if link.conf %}      
        {% if link.spec_session %}
          {{ link.date }} - <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b>, {{ link.spec_session}} {{ link.location }} 
        {% else %}
          {{ link.date }} - <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b> {{ link.location }}
        {% endif %}
      {% else %}
        {% if link.conf_website %}
          {{ link.date }} - <b><a href="{{ link.conf_website }}">{{ link.location }}</a></b>
        {% else%}
          {{ link.date }} - <b>{{ link.location }}</b>
        {% endif %}
      {% endif %}
  </div>
</li>

{% endfor %}

</ul>
</div>

