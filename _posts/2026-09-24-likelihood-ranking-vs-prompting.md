---
layout: post
title: "arXiv paper: “Likelihood Ranking doesn't Scale Like Prompting in LLMs”"
tags: [research, NLP, evaluation, LLMs]
excerpt: "A large-scale comparison of prompted answering and likelihood ranking of declarative statements across 95 LLMs shows that the two scale very differently."
---

Our new preprint is on arXiv: **"Likelihood Ranking doesn't Scale Like Prompting in LLMs"**, with Lucia Passaro, Davide Bacciu and Alessandro Lenci (University of Pisa).

- Paper: [arxiv.org/abs/2609.29390](https://arxiv.org/abs/2609.29390)

## The question

LLMs are usually evaluated in one of two ways: by **prompting** them to produce an answer (typically on multiple-choice questions), or by **scoring candidate outputs with likelihood-based metrics**. Prompting requires the model to map its internal preferences onto a discrete decision, conditioned on instructions and output format. That mapping is a learned behaviour, shaped by scale and alignment. Likelihood, on the other hand, looks at how probability mass is spread over alternatives.

Standard likelihood-based multiple-choice scoring still happens in the context of the question and the answer options, so it can lean on the same answer-selection interface as prompting. We study a complementary protocol that gets rid of it.

## Setup

<figure>
  <img src="{{ '/assets/img/posts/likelihood-ranking/fig1-overview.png' | relative_url }}" alt="Overview of the experimental setting comparing prompting-based evaluation and declarative-statement likelihood ranking">
  <figcaption><strong>Figure 1.</strong> Overview of the experimental setting. The same questions are used for prompting-based evaluation and for declarative-statement likelihood ranking.</figcaption>
</figure>

We take 10 multiple-choice datasets (88,910 questions in total, including MMLU-Pro, ARC, OpenBookQA, QASC, SciQ, BIG-Bench Hard, CommonsenseQA, TruthfulQA, a health benchmark and mCSQA) and run two tasks on the same data:

- **Prompted answering (APX, accuracy on prompt execution):** the model is asked to answer the multiple-choice question and we check the answer.
- **Statement ranking (APS, accuracy on perplexity score):** for each question, we turn every answer option into a declarative statement (generated with gpt-oss-20b, keeping the original wording as much as possible), compute the perplexity of each statement independently, and check whether the correct statement gets the lowest one.

We validated the generated statements on a stratified sample: high similarity to the source question–answer pair (BLEU 0.69, BERTScore F1 0.68 on average), 99% meaning preservation according to two LLM judges, and a shared structural template across candidates in 95% of cases. We then evaluated **95 open-weights decoder-only models, from about 0.1B to 104B parameters**, both base and instruction-tuned when available. Mixture-of-experts and reasoning models were excluded to limit confounds.

## What we found

<figure>
  <img src="{{ '/assets/img/posts/likelihood-ranking/fig2-scaling.png' | relative_url }}" alt="Accuracy of APS and APX versus model size on a log scale, for base and instruct models">
  <figcaption><strong>Figure 2.</strong> Accuracy under prompting (APX) and declarative-statement likelihood (APS) across model scales, with fitted scaling curves and 95% bootstrap confidence intervals.</figcaption>
</figure>

- **Statement likelihood scales weakly.** APS improves slowly with size, stays in a narrow range, and saturates well below the best prompted results. Instruction-tuning has only a limited effect on it.
- **Prompted answering scales sharply.** Small models often do *worse* when prompted than when evaluated via statement likelihood, but APX grows quickly with scale and overtakes APS by a wide margin. We call the point where this happens the *prompting break-even point*.
- **Instruction-tuning moves the break-even point earlier.** The slopes for base and instruct models are similar, but instruct models cross APS at much smaller sizes.
- **Standard likelihood-based multiple-choice scoring behaves like prompting.** In a control experiment, scoring options in the original multiple-choice context follows APX-like scaling, which supports the idea that statement ranking captures a different signal.

## Interpretation

The gap between correct and incorrect statements is typically tiny: for most models the perplexity difference between the first and second choice is close to zero. The model's distributional preferences are diffuse, and scale only slowly sharpens them. Prompting gains, on the other hand, seem to reflect not only sharper distributions but also a better *interface* between those preferences and a discrete decision. We read instruction-tuning as mainly optimising this interface, rather than reshaping what was learned in pre-training.

## Takeaway

Prompting-based evaluation, standard likelihood-based multiple-choice scoring and declarative-statement likelihood ranking measure related but different things, and shouldn't be used interchangeably. As models grow and are increasingly tuned for interactive use, we should keep apart *latent likelihood preferences* and *how effectively models are trained to act on them*.

## Limitations

We only look at multiple-choice QA and open-weights models, model families are not evenly spread across sizes, and we don't control for training tokens. APS depends on automatically generated statements and remains sensitive to surface form, so it should be read as a controlled likelihood signal, not an exhaustive measure of model knowledge. More details, controls, per-dataset breakdowns and the full model list are in the [paper](https://arxiv.org/abs/2609.29390).
