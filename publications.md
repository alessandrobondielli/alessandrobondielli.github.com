---
layout: page
title: Publications
description: "List of publications by Alessandro Bondielli."
permalink: /publications/
---

{% assign pubs = site.data.publications %}

{% if pubs == nil or pubs.size == 0 %}
<div class="pub-note">
  Publications are fetched automatically from <a href="https://scholar.google.com/citations?user=zcXQk6YAAAAJ" target="_blank" rel="noopener">Google Scholar</a> on each site build. The list will appear after the first successful deployment.
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
    <div class="pub-authors">
      {% for author in pub.authors %}
        {% if author contains "Bondielli" %}<strong>{{ author }}</strong>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}
      {% endfor %}
    </div>
    {% if pub.venue and pub.venue != "" %}
    <div class="pub-venue">{{ pub.venue }}</div>
    {% endif %}
    {% if pub.citations and pub.citations > 0 %}
    <div class="pub-links">
      <span class="pub-link" style="cursor:default; border-color: var(--color-border); color: var(--color-text-muted);">
        {{ pub.citations }} citation{% if pub.citations != 1 %}s{% endif %}
      </span>
    </div>
    {% endif %}
  </div>
{% endfor %}
</div>
</div>
{% endfor %}

{% endif %}
