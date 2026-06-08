---
layout: page
title: Research
description: "Research areas and ongoing projects of Alessandro Bondielli."
permalink: /research/
---

My research is in **Natural Language Processing**, with a primary focus on understanding *how* language models work internally. I combine mechanistic analysis with applied work on disinformation detection and multimodal reasoning — three threads that share a common question: what do models actually know, and how do they know it?

I am a member of the [CoLingLab](https://colinglab.fileli.unipi.it) (Computational Linguistics Laboratory) at the Department of Philology, Literature and Linguistics, University of Pisa.

## Research Areas

<div class="research-areas">

  <div class="research-card">
    <h3>Mechanistic Interpretability</h3>
    <p>My current primary focus. Rather than asking what a model can do, mechanistic interpretability asks <em>how</em> it does it — mapping internal representations, circuits, and features back to human-interpretable concepts. I am particularly interested in sparse dictionary learning techniques (Sparse Autoencoders) as a tool for decomposing model activations into interpretable directions, and in applying these methods to smaller and multilingual models where ground truth is more tractable.</p>
    <p class="research-card-pubs">
      <strong>Representative work:</strong>
      <a href="https://aclanthology.org/2025.clicit-1.11.pdf" target="_blank" rel="noopener">Sparse Autoencoders Find Partially Interpretable Features in Italian Small Language Models</a> (CLiC-it 2025)
    </p>
  </div>

  <div class="research-card">
    <h3>Disinformation &amp; Fake News Detection</h3>
    <p>A long-standing research thread, from early NLP-based detection pipelines to large-scale benchmarking and LLM-assisted debunking. I approach misinformation as a structured NLP problem — classification, claim verification, stance detection — rather than a content-moderation one. Recent work extends this to multimodal settings (text + image) and to personalised counter-narrative generation with LLMs.</p>
    <p class="research-card-pubs">
      <strong>Representative work:</strong>
      <a href="https://www.sciencedirect.com/science/article/pii/S0020025519304372" target="_blank" rel="noopener">A Survey on Fake News and Rumour Detection Techniques</a> (Information Sciences, 2019, 800+ citations) &middot;
      <a href="https://www.sciencedirect.com/science/article/pii/S2352340924004098" target="_blank" rel="noopener">Dataset for Multimodal Fake News Detection and Verification</a> (Data in Brief, 2024) &middot;
      <a href="https://www.sciencedirect.com/science/article/pii/S0020025526003385" target="_blank" rel="noopener">An Experimental Comparison of Fake News Detection Approaches</a> (Information Sciences, 2026)
    </p>
  </div>

  <div class="research-card">
    <h3>Multimodal NLP</h3>
    <p>How do vision-language models integrate visual and linguistic information, and how well do they actually reason across modalities? I work on benchmarking multimodal models on tasks that require genuine cross-modal understanding — causal reasoning, event plausibility, abstract concept grounding — going beyond accuracy on perception-level tasks to probe deeper representational alignment.</p>
    <p class="research-card-pubs">
      <strong>Representative work:</strong>
      <a href="https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.1091.pdf" target="_blank" rel="noopener">All-in-One: Understanding and Generation in Multimodal Reasoning (MAIA)</a> (EMNLP Findings, 2025) &middot;
      <a href="https://aclanthology.org/2025.clicit-1.42.pdf" target="_blank" rel="noopener">Seeing Cause and Time: a Visually Grounded Evaluation of Multimodal Models</a> (CLiC-it 2025) &middot;
      <a href="https://arpi.unipi.it/handle/11568/1113566" target="_blank" rel="noopener">Leveraging CLIP for Image Emotion Recognition</a> (2021)
    </p>
  </div>

</div>

## Further Interests

<div class="further-interests">

  <div class="further-item">
    <h4>Causal Reasoning in LLMs</h4>
    <p>How well do large language models handle explicit causal relations — both in English and in Italian? I have worked on benchmark design and evaluation of LLMs on causal reasoning tasks, finding consistent gaps between surface-level and genuine causal understanding. Related works: <a href="https://aclanthology.org/2025.findings-acl.891/" target="_blank" rel="noopener">ExpliCa: Evaluating Explicit Causal Reasoning in LLMs</a> (ACL Findings 2025) &middot; <a href="https://aclanthology.org/2025.clicit-1.10.pdf" target="_blank" rel="noopener">LLMs Struggle on Explicit Causality in Italian</a> (CLiC-it 2025)</p>
  </div>

  <div class="further-item">
    <h4>BabyLMs &amp; Data-Efficient Language Modelling</h4>
    <p>Can we train competent language models on small, cognitively plausible data budgets? I have participated in the BabyLM Challenge exploring curriculum learning strategies and instruction-tuning approaches for small-scale models trained from scratch. Related works: <a href="https://aclanthology.org/2024.conll-babylm.16/" target="_blank" rel="noopener">ConcreteGPT: A Baby GPT-2 Based on Lexical Concreteness and Curriculum Learning</a> (BabyLM 2024) &middot; <a href="https://aclanthology.org/2025.babylm-main.30/" target="_blank" rel="noopener">CLASS-IT: Conversational and Lecture-Aligned Small-Scale Instruction Tuning</a> (BabyLM 2025)</p>
  </div>

</div>

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
