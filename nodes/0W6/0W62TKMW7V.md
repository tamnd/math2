---
tag: 0W62TKMW7V
kind: statement
role: corollary
name: Law of total probability for an event and its complement
msc: [60A05]
uses: [0E5G5FMT2R, 0PQEBTYDZM]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_total_probability
    locator: Statement
---

## Statement

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $A, B \in \mathcal{F}$ with $0 < P(B) < 1$. Let $B^c = \Omega \setminus B$.
Then
$$P(A) = P(A \mid B) \, P(B) + P(A \mid B^c) \, (1 - P(B)).$$

## Remarks

This is the [[law of total probability|0E5G5FMT2R]] for the partition $\{B, B^c\}$, together with $P(B^c) = 1 - P(B)$.
The formula is the denominator of [[Bayes' theorem|0NM6E9VW04]] in the case of two hypotheses.

## Explanations

### L1 human

Either $B$ happens or it does not.
So the chance of $A$ is its chance when $B$ happens times $P(B)$, plus its chance when $B$ does not happen times $1 - P(B)$.
