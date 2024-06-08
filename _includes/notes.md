<div class="expository notes">
<ul style="margin-left:-20px">

{% for link in site.data.notes.main %}

<li style="margin-bottom:1rem">
  <div class="col-sm-9">
    <div class="title"><a href="{{ link.pdf }}"><b>{{ link.title }}</b></a></div>
    <div class="description">
    {% if link.description %} 
    ({{ link.description }})
    {% endif %}
    </div>
    <div class="links">
      {% if link.code %} 
      <a href="{{ link.code }}" class="button" style="font-size:12px;"><i class="fas fa-code-branch"></i> Code</a>
      {% endif %}
    </div>
  </div>
</li>

{% endfor %}

</ul>
</div>
