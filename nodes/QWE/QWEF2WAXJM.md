---
tag: QWEF2WAXJM
kind: statement
role: theorem
name: Sanov's theorem
msc: [60F10, 94A17]
uses: [00MRN0FARV, 059TJN0NZ1, 0ACRGYNHSR, MNPWBBNCAD, PQBW43X5RE]
about: [Q702WCDQQ3, PQBW43X5RE]
sources:
  - url: https://en.wikipedia.org/wiki/Sanov%27s_theorem
same_as:
  wikidata: Q7418899
  wikipedia: Sanov's theorem
---

## Statement

Let $\Sigma$ be a Polish space, and let $M_1(\Sigma)$ be the set of [[probability measures|059TJN0NZ1]] on $\Sigma$ with the topology of weak convergence.
Let $X_1, X_2, \dots$ be [[i.i.d.|00MRN0FARV]] random elements of $\Sigma$ with law $\mu$.
Let $L_n = \frac{1}{n} \sum_{k=1}^{n} \delta_{X_k}$ be the empirical measure, where $\delta_x$ is the [[Dirac measure|0ACRGYNHSR]] at $x$.
Then the laws of $L_n$ satisfy the [[large deviation principle|MNPWBBNCAD]] on $M_1(\Sigma)$ with the good rate function $\nu \mapsto D(\nu \,\|\, \mu)$, the [[Kullback–Leibler divergence|PQBW43X5RE]] of $\nu$ from $\mu$.

## Remarks

For a finite set $\Sigma = \set{1, \dots, m}$, the proof is a counting argument.
The probability that $L_n$ equals a given type $\nu$, with $n \nu(i)$ an integer for each $i$, is a multinomial probability.
By Stirling's formula, it equals $e^{-n D(\nu \| \mu) + O(\log n)}$, and there are only polynomially many types.
The general case reduces to finite partitions of $\Sigma$, or uses Cramér's theorem in a space of measures.

Example: for fair coin tosses, $\mu$ is uniform on $\set{0, 1}$.
The event that the fraction of ones is at least $0.6$ has probability $e^{-n c + o(n)}$, where $c = D(\nu \| \mu)$ for $\nu = (0.4, 0.6)$, that is $c = 0.6 \log 1.2 + 0.4 \log 0.8 \approx 0.020$.

## Explanations

### L1 human

Draw many independent samples from a known distribution and make a histogram.
The histogram almost always resembles the true distribution.
Sanov's theorem says that the chance that it resembles some other distribution $\nu$ instead is about $e^{-n D(\nu \| \mu)}$, where $D$ is the Kullback–Leibler divergence.

### L2 human

Sanov's theorem gives the Kullback–Leibler divergence a probabilistic meaning and is a basic link between probability and information theory.
By the contraction principle, it implies Cramér's theorem for bounded continuous functions of the samples.
In statistics it yields error exponents of tests, such as Stein's lemma for hypothesis testing.
The conditional limit theorem, or Gibbs conditioning principle, also follows: given a rare constraint on $L_n$, the empirical measure concentrates near the minimiser of $D(\cdot \| \mu)$ under the constraint.
