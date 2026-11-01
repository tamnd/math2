---
tag: KYF5SCYC64
kind: definition
name: Renewal theory
msc: [60K05, 60K15]
defines: 45V0W838BQ
uses: [00MRN0FARV, 0WQNRCNY3M, 0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Renewal_theory
---

## Definition

Let $T_1, T_2, \ldots$ be [[independent and identically distributed|00MRN0FARV]] random variables with values in $[0, \infty)$ and $P(T_1 = 0) < 1$.
Let $S_0 = 0$ and $S_n = T_1 + \cdots + T_n$ for $n \ge 1$; these are the renewal times.
The *renewal process* with holding times $T_i$ is the process
$$N(t) = \sup \set{n \ge 0 : S_n \le t}, \qquad t \ge 0.$$
Its *renewal function* is $m(t) = \mathbb{E}[N(t)]$.
Renewal theory is the study of $N$, of $m$, and of processes that start afresh at the times $S_n$.

## Remarks

The condition $P(T_1 = 0) < 1$ makes $S_n \to \infty$ almost surely, so $N(t)$ is finite for each $t$.
Example: if the $T_i$ are [[exponential|0E99F51GVB]] with rate $\lambda$, then $N$ is the Poisson process of rate $\lambda$, and $m(t) = \lambda t$.
Non-example: if $T_1, T_2, \ldots$ are not identically distributed, for instance $T_i = 2^{-i}$, then $N$ is not a renewal process, and here $N(t) = \infty$ for $t \ge 1$.
Let $\mu = \mathbb{E}[T_1] \in (0, \infty]$ be the [[expected value|0WQNRCNY3M]] of a holding time.
The elementary renewal theorem says $m(t)/t \to 1/\mu$ as $t \to \infty$, with $1/\infty = 0$; the strong law gives $N(t)/t \to 1/\mu$ almost surely.
