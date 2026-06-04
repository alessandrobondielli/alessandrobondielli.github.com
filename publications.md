---
layout: page
title: Publications
description: "List of publications by Alessandro Bondielli."
permalink: /publications/
---

{% assign pubs = site.data.publications %}

{% if pubs == nil or pubs.size == 0 %}
<div class="pub-note">
  Publications are fetched from <a href="https://scholar.google.com/citations?user=zcXQk6YAAAAJ" target="_blank" rel="noopener">Google Scholar</a>. Run <code>python _scripts/fetch_scholar.py</code> locally and commit <code>_data/publications.json</code> to populate this page.
</div>

{% else %}

{% assign pubs_by_year = pubs | group_by: "year" | sort: "name" | reverse %}

{% for year_group in pubs_by_year %}
## {{ year_group.name | default: "In press" }}

<div class="pub-year-group">
<div class="pub-list">
{% for pub in year_group.items %}
  <div class="pub-item">

    <div class="pub-title">
      {% if pub.url and pub.url != "" %}
        <a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a>
      {% else %}
        {{ pub.title }}
      {% endif %}
    </div>

    {% if pub.authors and pub.authors.size > 0 %}
    <div class="pub-authors">
      {% for author in pub.authors %}
        {% if author contains "Bondielli" %}<strong>{{ author }}</strong>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}
      {% endfor %}
    </div>
    {% endif %}

    {% if pub.venue and pub.venue != "" %}
    <div class="pub-venue">{{ pub.venue }}</div>
    {% endif %}

    <div class="pub-links">
      {% if pub.url and pub.url != "" %}
        <a href="{{ pub.url }}" class="pub-link" target="_blank" rel="noopener">Paper</a>
      {% endif %}
      {% if pub.citations and pub.citations > 0 %}
        <span class="pub-link pub-link--muted">{{ pub.citations }} citation{% if pub.citations != 1 %}s{% endif %}</span>
      {% endif %}
      {% if pub.bibtex and pub.bibtex != "" %}
        <button class="pub-link pub-cite-btn" onclick="toggleBibtex(this)">Cite</button>
      {% endif %}
    </div>

    {% if pub.bibtex and pub.bibtex != "" %}
    <div class="pub-bibtex-block" hidden>
      <div class="pub-bibtex-toolbar">
        <span class="pub-bibtex-label">BibTeX</span>
        <button class="pub-bibtex-copy" onclick="copyBibtex(this)">Copy</button>
      </div>
      <pre class="pub-bibtex-pre">{{ pub.bibtex | escape }}</pre>
    </div>
    {% endif %}

  </div>
{% endfor %}
</div>
</div>
{% endfor %}

{% endif %}

<script>
function toggleBibtex(btn) {
  const block = btn.closest('.pub-item').querySelector('.pub-bibtex-block');
  const hidden = block.hasAttribute('hidden');
  block.toggleAttribute('hidden', !hidden);
  btn.textContent = hidden ? 'Hide' : 'Cite';
}

function copyBibtex(btn) {
  const text = btn.closest('.pub-bibtex-block').querySelector('pre').textContent;
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = 'Copy', 2000);
  });
}
</script>
