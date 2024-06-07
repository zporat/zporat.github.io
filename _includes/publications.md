<div class="publications">
<ol reversed style="margin-left:-20px">

{% for link in site.data.publications.main %}

<li style="margin-bottom:10px">
  <div class="col-sm-9">
      <div class="title"><a href="{{ link.pdf }}"><b>{{ link.title }}</b></a> ({{ link.authors }}), <a href="{{ link.doi }}"> <em>{{ link.journal }}</em> <b>{{ link.volume }}</b>:{{ link.number }}</a> ({{ link.year }}), {{ link.pages }}.
      </div>
    <div class="links">
      {% if link.code %} 
      <a href="{{ link.code }}" class="button" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.mr %} 
      <a href="{{ link.mr }}" class="button" style="font-size:12px;">MathSciNet</a>
      {% endif %}
      {% if link.arxiv %} 
      <a href="{{ link.arxiv }}" class="button" style="font-size:12px;">arXiv</a>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
  </div>
</li>

{% endfor %}

</ol>
</div>

