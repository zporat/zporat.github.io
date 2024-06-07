<div class="publications">
<ul style="margin-left:-20px">

{% for link in site.data.talks.main %}

<li>
<div class="pub-row">
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
      <div class="title"><b>{{ link.title }}</b></div>
      <div class="author"> <i class="fa-solid fa-map-pin"></i> <a href="{{ link.conf_website }}"> {{ link.location }} </a></div>
      <div class="periodical"> <i class="fa-solid fa-calendar-days"></i> {{ link.date }}</div>
  </div>
</div>
</li>

<br>

{% endfor %}

</ul>
</div>

