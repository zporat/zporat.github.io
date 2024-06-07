<div class="publications">
<ul style="margin-left:-20px">

{% for link in site.data.talks.main %}

<li>
<div class="pub-row">
  <div class="col-sm-9">
      <div class="title"><b>{{ link.title }} ({{ link.date }})</b></div>
        <ul class="fa-ul" style="margin-left:25px">
        <li><span class="fa-li"><i class="fas fa-map-pin"></i></span><a href="{{ link.conf_website }}">{{ link.conf }}</a> {{ link.location }}</li>
        </ul>
  </div>
</div>
</li>

{% endfor %}

</ul>
</div>

