---
tag: 06PVXMY0TH
kind: statement
role: theorem
name: Cauchy criterion for series
msc: [40A05]
uses: [0ZA4AX4MW3, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_convergence_test
    locator: Statement
same_as:
  wikidata: Q859102
  wikipedia: Cauchy's convergence test
---

## Statement

Let $(a_n)$ be a real sequence.
The series $\sum a_n$ converges if and only if the following holds for each $\varepsilon > 0$.
There is a natural number $N$ such that
$$\left| \sum_{k=m+1}^{n} a_k \right| < \varepsilon \quad \text{for all natural numbers } n > m \ge N.$$

## Remarks

The sum in the condition is $s_n - s_m$, a difference of [[partial sums|0NB643K60Q]]. So the condition says that $(s_n)$ is a Cauchy sequence, and the result is the [[Cauchy criterion for sequences|0ZA4AX4MW3]].
With $n = m + 1$ it gives the [[term test|0VVY4H92G2]].
It proves that [[absolutely convergent series converge|0Y123X48GA]].

## Explanations

### L1 human

A series converges exactly when its tails become small.
Each block of consecutive terms far out in the series must have a small sum.
