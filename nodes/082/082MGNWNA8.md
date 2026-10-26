---
tag: 082MGNWNA8
kind: statement
role: theorem
name: Absolutely convergent series in a Banach space converge
msc: [40A05]
uses: [0BDTTM24DP, 0MCK8K2D7Z, 08EWT7J0SC]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
    locator: Proof that any absolutely convergent series in a Banach space is convergent
  - url: https://en.wikipedia.org/wiki/Banach_space
    locator: Characterization in terms of series
---

## Statement

Let $(V, \|\cdot\|)$ be a [[Banach space|0BDTTM24DP]] and let $(x_n)_{n \ge 1}$ be a sequence in $V$ with $\sum_{n \ge 1} \|x_n\| < \infty$.
Then the partial sums $s_N = \sum_{n=1}^{N} x_n$ converge to a point $s \in V$, and $\|s\| \le \sum_{n \ge 1} \|x_n\|$.

## Remarks

Proof: for $M > N$, the triangle inequality gives $\|s_M - s_N\| \le \sum_{n=N+1}^{M} \|x_n\|$. This tends to $0$, so $(s_N)$ is a [[Cauchy sequence|0MCK8K2D7Z]], and it converges because $V$ is [[complete|08EWT7J0SC]].
The converse holds: a normed space in which each absolutely convergent series converges is a Banach space.
For $V = \mathbb{R}$, this is the fact that absolutely convergent real series converge.

## Explanations

### L1 human

If the lengths of the terms have a finite sum, then the series converges in a Banach space.
This is a practical test for completeness, and it is often used to build solutions as sums of series.
