<div class="publications">
<ul style="margin-left:-20px">

{% for link in site.data.talks.main %}

<li>
<div class="pub-row">
  <div class="col-sm-9">
      <div class="title"><b>{{ link.title }}</b></div>
        <ul class="fa-ul" style="margin-left:-10px">
        <li><span class="fa-li"><i class="fas fa-map-pin"></i></span><a href="{{ link.conf_website }}">{{ link.location }}</a></li>
        <li><span class="fa-li"><i class="fas fa-calendar-alt"></i></span>{{ link.date }}</li>
        </ul>
  </div>
</div>
</li>

<br>

{% endfor %}

</ul>
</div>

