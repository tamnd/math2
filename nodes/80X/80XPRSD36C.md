---
tag: 80XPRSD36C
kind: proof
name: Proof of the Cauchy criterion for series
msc: [40A05]
proves: 06PVXMY0TH
uses: [0ZA4AX4MW3, 0QZMTN5AXX, 0NB643K60Q, 0CVVKY7GY2]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_convergence_test
---

## Proof

We apply the Cauchy criterion to the sequence of partial sums.

1. Let $s_n = \sum_{k=0}^{n} a_k$ be the [[partial sums|0NB643K60Q]]. For natural numbers $n > m$, we have $s_n - s_m = \sum_{k=m+1}^{n} a_k$.
2. By definition, $\sum a_n$ is a [[convergent series|0CVVKY7GY2]] exactly when $(s_n)$ converges.
3. By the [[Cauchy criterion for sequences|0ZA4AX4MW3]], $(s_n)$ converges if and only if it is a [[Cauchy sequence|0QZMTN5AXX]].
4. Assume that $(s_n)$ is Cauchy, and let $\varepsilon > 0$. There is $N$ with $\abs{s_n - s_m} < \varepsilon$ for all $m, n \ge N$. For $n > m \ge N$, step 1 turns this into $\abs{\sum_{k=m+1}^{n} a_k} < \varepsilon$.
5. Conversely, assume the condition of the statement, and let $\varepsilon > 0$. Take $N$ as in the condition, and let $m, n \ge N$.
6. If $m = n$, then $\abs{s_n - s_m} = 0 < \varepsilon$. If $n > m$, step 1 and the condition give $\abs{s_n - s_m} < \varepsilon$. If $m > n$, swap the roles of $m$ and $n$.
7. So $(s_n)$ is a Cauchy sequence.
8. By steps 2 to 7, the series converges if and only if the condition holds.

## Idea

A block sum $a_{m+1} + \cdots + a_n$ is the difference $s_n - s_m$ of two partial sums. So the condition says exactly that the partial sums form a Cauchy sequence, and Cauchy sequences of reals converge.
