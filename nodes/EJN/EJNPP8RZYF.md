---
tag: EJNPP8RZYF
kind: definition
name: FK-space
msc: [46A45, 40H05]
defines: 71DMQHW6JZ
uses: [XYTN19EPF2, 3GAA614673, 0X3WGX95FE, 0GBG8B49AA, 08P6T2WH6R]
sources:
  - url: https://en.wikipedia.org/wiki/FK-space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $X$ be a [[sequence space|XYTN19EPF2]] over $\mathbb{K}$.
An *FK-space* is such an $X$ together with a topology $\tau$ on $X$ such that:

1. $(X, \tau)$ is a [[Fréchet space|3GAA614673]], that is, a complete metrizable locally convex topological vector space.
2. For each $n$, the coordinate map $X \to \mathbb{K}$, $x \mapsto x_n$, is [[continuous|0X3WGX95FE]].

## Remarks

Example: the space $\omega$ of all sequences, with the [[product topology|0GBG8B49AA]] of $\mathbb{K}^{\N}$, is an FK-space.
This topology is given by the seminorms $p_n(x) = \abs{x_n}$, so it is locally convex and makes each coordinate continuous.
It is metrizable by $d(x, y) = \sum_n 2^{-n} \min(1, \abs{x_n - y_n})$, and it is complete because a Cauchy sequence converges in each coordinate.

Example: each [[space ℓ^p|08P6T2WH6R]] with $1 \le p \le \infty$ and its usual norm is an FK-space, since $\abs{x_n} \le \norm{x}_p$.

Non-example: the space of sequences with finitely many nonzero terms, with the norm $\sup_n \abs{x_n}$, is not an FK-space under this norm, because it is not complete.
The sequences $(1, 1/2, \dots, 1/k, 0, 0, \dots)$ form a Cauchy sequence whose coordinatewise limit $(1/n)$ is not in the space.

An FK-space whose topology is given by a complete norm is a BK-space.
By the closed graph theorem, a sequence space has at most one FK topology, and every inclusion map between FK-spaces is continuous.
