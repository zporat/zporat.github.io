<div class="publications">
<ol class="bibliography">

{% for link in site.data.talks.main %}

<li>
<div class="pub-row">
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
      <div class="title"><b>{{ link.title }}</b></div>
      <div class="author"><a href="{{ link.conf_website }}"> {{ link.location }} </a></div>
      <div class="periodical">{{ link.date }}</div>
  </div>
</div>
</li>

<br>

{% endfor %}

</ol>
</div>

