<div class="talks">
<ul style="margin-left:-20px">

{% for link in site.data.talks.upcoming %}

<li style="margin-bottom:0.5rem">
  <div class="col-sm-9">
      {% if link.conf %}      
        {% if link.spec_session %}
          <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b>, {{ link.spec_session}} {{ link.location }} - Upcoming ({{ link.date }})
        {% else %}
          <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b> {{ link.location }} - Upcoming ({{ link.date }})
        {% endif %}
      {% else %}
        {% if link.conf_website %}
          <b><a href="{{ link.conf_website }}">{{ link.location }}</a></b> - Upcoming ({{ link.date }})
        {% else%}
          <b>{{ link.location }}</b> - Upcoming ({{ link.date }})
        {% endif %}
      {% endif %}
  </div>
</li>

{% endfor %}

{% for link in site.data.talks.past %}

<li>
  <div class="col-sm-9">
      {% if link.conf %}      
        {% if link.spec_session %}
          <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b>, {{ link.spec_session}} {{ link.location }} - {{ link.date }}
        {% else %}
          <b><a href="{{ link.conf_website }}">{{ link.conf }}</a></b> {{ link.location }} - {{ link.date }}
        {% endif %}
      {% else %}
        {% if link.conf_website %}
          <b><a href="{{ link.conf_website }}">{{ link.location }}</a></b> - {{ link.date }}
        {% else%}
          <b>{{ link.location }}</b> - {{ link.date }}
        {% endif %}
      {% endif %}
  </div>
</li>

{% endfor %}

</ul>
</div>

