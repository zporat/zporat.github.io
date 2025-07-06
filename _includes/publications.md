<div class="publications">
<ol reversed style="margin-left:-20px">

{% for link in site.data.publications.main %}

<li style="margin-bottom:1rem">
  <div class="col-sm-9">
      {% if link.authors %}
        {% if link.journal %}
          <div class="title"><a href="{{ link.pdf }}"><b>{{ link.title }}</b></a> ({{ link.authors }}), <a href="{{ link.doi }}"> <em>{{ link.journal }}</em> <b>{{ link.volume }}</b>:{{ link.number }}</a> ({{ link.year }}), {{ link.pages }}.
          </div>
        {% else %}
          <div class="title"><b>{{ link.title }}</b> ({{ link.authors }}), {{ link.status }}. </div>
        {% endif %}
      {% else %}
        {% if link.arxiv %} 
          <div class="title"><b>{{ link.title }}</b>, {{ link.status }}. </div>
        {% else %}
          <div class="title"><a href="{{ link.pdf }}"><b>{{ link.title }}</b></a>, <a href="{{ link.doi }}"> <em>{{ link.journal }}</em> <b>{{ link.volume }}</b>:{{ link.number }}</a> ({{ link.year }}), {{ link.pages }}. </div>
        {% endif %}
      {% endif %}
      <div style="height:5px;font-size:1px;">&nbsp;</div>
      <div class="links">
      {% if link.mr %} 
      <a href="{{ link.mr }}" class="button" style="font-size:12px;"><i class="fas fa-external-link-alt" aria-hidden="true"></i>&nbsp; MathSciNet</a>
      {% endif %}
      {% if link.arxiv %} 
      <a href="{{ link.arxiv }}" class="button" style="font-size:12px;"><i class="fas fa-external-link-alt" aria-hidden="true"></i>&nbsp; arXiv</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="button" style="font-size:12px;"><i class="fas fa-code-branch" aria-hidden="true"></i>&nbsp; Code</a>
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

