---
layout: page
title: Research
description: "Research areas and ongoing projects of Alessandro Bondielli."
permalink: /research/
---

My research focuses on **Natural Language Processing** and the development of computational methods to understand, process, and generate human language. I am particularly interested in applications that bridge NLP with real-world challenges across different domains.

## Research Areas

<div class="research-areas">
  <div class="research-card">
    <h3>Information Extraction</h3>
    <p>Named entity recognition, relation extraction, and event detection from unstructured text, with a focus on domain-specific corpora.</p>
  </div>
  <div class="research-card">
    <h3>Text Classification</h3>
    <p>Automated categorization of textual documents, including stance detection, sentiment analysis, and topic classification.</p>
  </div>
  <div class="research-card">
    <h3>Misinformation &amp; Fake News</h3>
    <p>Computational approaches to detecting and characterizing misinformation in social media and news articles.</p>
  </div>
  <div class="research-card">
    <h3>Language Models</h3>
    <p>Evaluation and fine-tuning of large language models for specialized NLP tasks, with a focus on robustness and interpretability.</p>
  </div>
</div>

## Current Projects

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. *(Replace this with descriptions of your active projects, grants, or collaborations.)*

---

## Related Posts

{% assign research_posts = site.posts | where_exp: "post", "post.tags contains 'research'" %}
{% if research_posts.size > 0 %}
<div class="post-list">
{% for post in research_posts %}
  <div class="post-item">
    <div class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</div>
    <div class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></div>
    {% if post.excerpt %}<p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>{% endif %}
    <a href="{{ post.url | relative_url }}" class="read-more">Read more &rarr;</a>
  </div>
{% endfor %}
</div>
{% else %}
<p style="color: var(--color-text-muted); font-size: 0.9rem;">No research posts yet. Blog posts tagged <code>research</code> will appear here automatically.</p>
{% endif %}
