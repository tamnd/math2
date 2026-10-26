---
tag: ~b0f8baa0
kind: statement
role: theorem
name: Bayes' theorem
aliases: [bayes-rule, bayes-law, bayes-formula]
msc: [62F15]
uses: [~36328f4b, ~202ef84b]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes'_theorem
    locator: Statement of theorem
same_as:
  wikidata: Q182505
  wikipedia: Bayes' theorem
---

## Statement

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $A, B \in \mathcal{F}$ with $P(A) > 0$ and $P(B) > 0$.
Then
$$P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}.$$

## Remarks

Let $A_1, A_2, \dots$ be a finite or countable partition of $\Omega$ into events of positive probability. With the [[law of total probability|~202ef84b]], $P(A_j \mid B) = \dfrac{P(B \mid A_j) \, P(A_j)}{\sum_i P(B \mid A_i) \, P(A_i)}$.
In Bayesian language, $P(A)$ is the [[prior probability|~585bd2e3]], $P(B \mid A)$ is the likelihood and $P(A \mid B)$ is the [[posterior probability|~645676f4]].
The proof: both $P(A \mid B) \, P(B)$ and $P(B \mid A) \, P(A)$ are equal to $P(A \cap B)$.

## History

The theorem is named after Thomas Bayes. Pierre-Simon Laplace found it independently and developed it further.

## Explanations

### L1 human

Bayes' theorem turns "the chance of the evidence given the cause" into "the chance of the cause given the evidence".
A medical test tells you how often sick people test positive. Bayes' theorem tells you how likely a person with a positive test is to be sick.
