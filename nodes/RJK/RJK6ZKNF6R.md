---
tag: RJK6ZKNF6R
kind: statement
role: theorem
name: Fundamental convergence theorem
msc: [31B05, 31C15]
uses: [X4V2S56YQQ, C95QJ7YH5T, 02BH3MCBQB]
about: [X4V2S56YQQ, C95QJ7YH5T]
sources:
  - url: https://en.wikipedia.org/wiki/Fine_topology_(potential_theory)
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]].
Let $(u_i)_{i \in I}$ be a nonempty family of [[superharmonic functions|X4V2S56YQQ]] on $\Omega$ that is locally uniformly bounded below.
Let $u = \inf_{i \in I} u_i$, and let $\hat u$ be its lower semicontinuous regularisation, $\hat u(x) = \min\left(u(x), \liminf_{y \to x} u(y)\right)$.
Then:

1. $\hat u$ is superharmonic on $\Omega$, and $\hat u \le u$.
2. The set $\set{x \in \Omega : \hat u(x) < u(x)}$ is a [[polar set|C95QJ7YH5T]].

## Remarks

The infimum $u$ satisfies the super-mean value inequality but need not be lower semicontinuous, so it need not be superharmonic.
Idea of the proof: Choquet's topological lemma gives a countable subfamily with the same regularised infimum.
Replacing it by its finite minima, which are superharmonic, reduces the problem to a decreasing sequence.
For a decreasing sequence, the limit keeps the super-mean value inequality by monotone convergence, and its regularisation is then shown to be superharmonic.
The exceptional set is shown to be polar by a capacity argument.
Example: in $\R^3$ let $u_k(y) = \min\left(1, k^{-1}\abs{y}^{-1}\right)$, which are positive superharmonic functions.
Their infimum is $0$ for $y \ne 0$ and $1$ at $y = 0$, while $\hat u = 0$; the exceptional set $\set{0}$ is polar.
The lower bound is needed: the constants $u_k = -k$ on $\R^n$ are superharmonic, but their infimum is $-\infty$ everywhere.

## Explanations

### L1 human

Take the lowest values of many superharmonic functions.
The result may fail to be superharmonic only because of a few bad points.
After a small repair at those points it is superharmonic again, and the bad points form a set that potential theory cannot see.

### L2 human

The theorem is the tool behind most limiting constructions in classical potential theory.
It shows that regularised reduced functions are superharmonic, which gives balayage and equilibrium potentials.
It also yields that the set where a reduced function differs from its regularisation is polar, and hence the quasi-everywhere statements of capacity theory.
