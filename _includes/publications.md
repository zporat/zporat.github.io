<div class="publications">
<ol reversed style="margin-left:-20px">

{% for link in site.data.publications.main %}

<li>
  <div class="col-sm-9">
      <div class="title"><a href="{{ link.pdf }}"><b>{{ link.title }}</b></a></div> <div class="author">({{ link.authors }})</div> <div class="periodical"><a href="{{ link.doi }}"> <em>{{ link.journal }}</em> <b>{{ link.volume }}</b>:{{ link.number }}</a> ({{ link.year }}), {{ link.pages }}.
      </div>
    <div class="links">
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:14px;">PDF</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:14px;">Code</a>
      {% endif %}
      {% if link.mr %} 
      <a href="{{ link.mr }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:14px;">MathSciNet</a>
      {% endif %}
      {% if link.arxiv %} 
      <a href="{{ link.arxiv }}" class="button" style="font-size:14px;">arXiv</a>
      {% endif %}
      {% if link.notes %} 
      <strong> <i style="color:#e74d3c">{{ link.notes }}</i></strong>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
  </div>
</li>

<br>

{% endfor %}

</ol>
</div>

