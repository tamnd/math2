---
tag: 0V9ME8GQE7
kind: statement
role: theorem
name: Dirichlet's test
msc: [40A05]
uses: [0KN22AAW5R, 0NB643K60Q, 06PVXMY0TH]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_test
    locator: Statement
same_as:
  wikidata: Q1149255
  wikipedia: Dirichlet's test
---

## Statement

Let $(a_n)$ be a [[monotone|0KN22AAW5R]] real sequence with $a_n \to 0$.
Let $(b_n)$ be a real sequence whose [[partial sums|0NB643K60Q]] are bounded. That is, there is $M$ with $\left| \sum_{k=1}^{n} b_k \right| \le M$ for all $n$.
Then the series $\sum_{n=1}^{\infty} a_n b_n$ converges.

## Remarks

The proof uses summation by parts and the [[Cauchy criterion for series|06PVXMY0TH]].
With $b_n = (-1)^n$ it gives the [[alternating series test|0PK8QH1W1V]].
It also shows that $\sum \sin(n x) / n$ converges for each real $x$.
Mathlib states a form with a Cauchy sequence of partial sums, as `Monotone.cauchySeq_series_mul_of_tendsto_zero_of_bounded`.

## History

The test is named after Peter Gustav Lejeune Dirichlet. It was published after his death, in 1862.

## Explanations

### L1 human

The partial sums of $\sum b_n$ do not grow, and the weights $a_n$ shrink steadily to $0$.
Together these give enough cancellation for $\sum a_n b_n$ to converge.
