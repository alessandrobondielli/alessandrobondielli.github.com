---
layout: post
title: "Parts-of-Speech as Emergent Categories in SAE Latent Space (EMNLP 2026)"
tags: [research, NLP, interpretability, EMNLP]
excerpt: "Our paper on how part-of-speech categories are organised in the latents of a Sparse AutoEncoder was presented at EMNLP 2026."
---

I'm happy to share that our paper **"Parts-of-Speech as Emergent Categories in SAE Latent Space"** was presented at the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP). It is joint work with Lucia Passaro, Serena Auriemma and Alessandro Lenci, from the CoLingLab and the Department of Computer Science at the University of Pisa.

- Paper: [aclanthology.org/2026.emnlp-main.2656](https://aclanthology.org/2026.emnlp-main.2656.pdf)
- Code and data: [github.com/colinglab/pos-sae-latents](https://github.com/colinglab/pos-sae-latents)

Below is a short summary of what we did and what we found.

## The question

Sparse AutoEncoders (SAEs) are widely used to inspect what language models represent. They map dense activations to a very high-dimensional sparse vector, whose dimensions (the *latents*) are hoped to be more interpretable, ideally one meaningful feature per latent. But linguistic categories are not obviously "one feature" objects: they result from a combination of lexical, morphological, syntactic and distributional cues. So **do SAE latents expose linguistic categories as individual units, or as structured groups of features?**

We use part-of-speech (POS) tags as a controlled testbed. They are discrete, independently annotated, and differ a lot in frequency, lexical openness and syntactic role (open classes such as nouns and verbs versus closed classes such as determiners and conjunctions).

## Setup

We take LLaMA-3-8B and an open pre-trained SAE (`EleutherAI/sae-llama-3-8b-32x`, 131,072 latents) on the last-layer residual stream. We encode every token of the English GUM treebank (Universal Dependencies, 17 UPOS tags, about 252k tokens), and study the gold POS tags in this latent space. We also built a small controlled dataset of minimal sentences (e.g. *I see a dog*, *There is a loyal dog*, *I walk quickly*) to check what happens when tokens are added one at a time.

<figure>
  <img src="{{ '/assets/img/posts/pos-sae/fig1-overview.png' | relative_url }}" alt="Overview of the workflow: recoverability, localization, compactness, then validation on held-out and controlled data">
  <figcaption><strong>Overview of the workflow.</strong> We test POS recoverability from token-level SAE activations, identify and compact POS-relevant latent groups, and validate them on held-out and controlled data.</figcaption>
</figure>

The analysis goes beyond plain probing accuracy, in three steps:

1. **Recoverability (RQ1).** One-vs-rest L1-regularised logistic regression probes, one per POS tag, on the sparse SAE activations.
2. **Localization (RQ2).** The probe coefficients rank the latents for each tag (*feature salience*). We then measure how many top latents are needed to be active on at least 95% of the tokens of a tag (*coverage*), and train a multi-class classifier using only the union of these latents.
3. **Validation (RQ3).** We check whether these latent groups stay active on the held-out GUM test split and on the controlled sentences.

## What we found

### POS is clearly recoverable, but not uniformly

Probes recover POS distinctions well from SAE activations. Closed classes and low-variability labels such as punctuation are easiest; rare or heterogeneous tags (INTJ, SYM, X) are hardest. Nouns and verbs are the best-performing open classes.

<figure>
  <img src="{{ '/assets/img/posts/pos-sae/fig2-probing-f1.png' | relative_url }}" alt="Bar chart of one-vs-rest F1 per POS tag">
  <figcaption><strong>Figure 2.</strong> One-vs-rest probing performance per POS (5-fold cross-validation on GUM train). Red: open class, blue: closed class, dark: other.</figcaption>
</figure>

This is not just lexical memorisation. A control probe trained on random labels assigned to word types reaches 0.54 accuracy (0.42 macro F1), against 0.88 accuracy for the real probe. The SAE probe is also on par with probes on the raw residual stream (0.88 accuracy at the embedding layer, 0.92 at layer 30), while using about 8 times fewer features. We do not claim SAEs are better probes: their contribution is decomposition and localization, which dense probes don't offer as easily.

### Categories live in groups of latents, not single latents

For each tag, only some latents receive positive weight, and always more than one. **There is no one-latent-per-category mapping.** Open classes (NOUN, ADJ, VERB) use many more non-zero latents than closed ones.

<figure>
  <img src="{{ '/assets/img/posts/pos-sae/fig3-nonzero-coefs.png' | relative_url }}" alt="Number of non-zero coefficients per one-vs-rest classifier">
  <figcaption><strong>Figure 3.</strong> Non-zero coefficients (latents) for each one-vs-rest classifier.</figcaption>
</figure>

The coverage analysis tells the same story. Some tags (PUNCT, PART, DET, PRON) reach 95% coverage with a handful of latents, while others (ADJ, ADV, PROPN, VERB) need several dozen.

<figure>
  <img src="{{ '/assets/img/posts/pos-sae/fig4-k95.png' | relative_url }}" alt="Number of latents needed to reach 95% coverage per POS tag">
  <figcaption><strong>Figure 4.</strong> Number of salient latents required to activate on at least 95% of the gold tokens of each POS.</figcaption>
</figure>

The union of these category-specific groups is small: **498 latents** (out of about 130k attested ones), 12% of which are shared by two or more POS. A multi-class classifier trained on only these latents performs comparably to the one trained on the full SAE representation (about 0.89 accuracy, 0.81 macro F1 in our train/test setting). If we randomly replace some of them, performance collapses (0.69 accuracy with 50% of the selected latents, 0.23 with none), so the selected latents really are POS-relevant.

<figure>
  <img src="{{ '/assets/img/posts/pos-sae/fig5-confusion.png' | relative_url }}" alt="Row-normalised confusion matrix of the compact-feature classifier">
  <figcaption><strong>Figure 5.</strong> Row-normalised confusion matrix of the multi-class POS classifier using only the 498 selected latents.</figcaption>
</figure>

### The groups are stable, but only partly category-specific

On held-out test data, the latents selected for a tag remain active on unseen tokens of that tag (recall mostly at or above 0.95). However, they also fire on other categories: the average distinctiveness score is 0.27, well above the 0.06 chance level but far from exclusive.

<figure>
  <img src="{{ '/assets/img/posts/pos-sae/fig6-coactivation.png' | relative_url }}" alt="Co-activation heatmap of selected latent groups on the held-out treebank test set">
  <figcaption><strong>Figure 6.</strong> Co-activation of the selected latent groups on the held-out test set. The diagonal is per-category recall; off-diagonal cells are spurious co-activation rates.</figcaption>
</figure>

The overlaps are linguistically sensible: ADJ with NOUN, ADV and PROPN; PROPN with NOUN; SCONJ with ADP (*by*, *after*, *since*); VERB with NOUN in homographs (*to drink / the drink*). Some also reflect annotation conventions (INTJ). In other words, the latents track not only abstract syntactic function but also surface form, lemma sharing and local syntactic context.

### On controlled sentences, activations are largely additive

In minimal sentences, adding a word brings in more latents of its category: adding *loyal* to *There is a dog* activates more ADJ-related latents, adding an adverb to *I walk* more ADV ones. Recall on these templates is high (0.94 on average) but precision is low, partly because of a set of "first-token" latents that confound the picture. Prefixing the sentence with a token of a different POS shifts those activations onto the new first token.

<figure>
  <img src="{{ '/assets/img/posts/pos-sae/fig7-controlled.png' | relative_url }}" alt="Active selected latents per POS in each controlled template variant">
  <figcaption><strong>Figure 7.</strong> Active selected latents per relevant POS in each template variant. Each square is a latent active on at least 25% of the template's examples; darker means more active.</figcaption>
</figure>

## Takeaways

- POS information is **explicitly and robustly available** in SAE latents.
- It is organised in **compact but distributed groups** of latents, whose size varies with the nature of the category: closed classes (small inventories of word forms) get compact, selective groups, while open classes need broader, less selective ones.
- A strict one-to-one mapping between linguistic categories and latents holds only to a limited extent. Interpretability claims at the latent level should be checked against theoretically grounded category inventories, and not only against top-activating examples.

## Limitations

We study a single model (LLaMA-3-8B), one layer and one public SAE, on English only, and POS is just one level of linguistic abstraction. Probe coefficients are a salience signal, not causal evidence: interventions would be needed to show that the model actually uses these latents. Extending to other models, layers, languages and richer linguistic levels (morphological features, dependencies, semantic roles) is the natural next step.

If you want to dig deeper, the [paper](https://aclanthology.org/2026.emnlp-main.2656.pdf) has appendices with sensitivity analyses and per-category results, and the [code and data](https://github.com/colinglab/pos-sae-latents) are available.
