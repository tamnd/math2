---
tag: VC7EH3FZX3
kind: definition
name: BK-space
msc: [46B45, 46A45]
defines: 8HEZ9TW1NK
uses: [XYTN19EPF2, 0BDTTM24DP, 0X3WGX95FE, 71DMQHW6JZ, 08P6T2WH6R]
sources:
  - url: https://en.wikipedia.org/wiki/BK-space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $X$ be a [[sequence space|XYTN19EPF2]] over $\mathbb{K}$.
A *BK-space* is such an $X$ together with a norm $\norm{\cdot}$ on $X$ such that:

1. $(X, \norm{\cdot})$ is a [[Banach space|0BDTTM24DP]].
2. For each $n$, the coordinate map $X \to \mathbb{K}$, $x \mapsto x_n$, is [[continuous|0X3WGX95FE]].

## Remarks

Equivalently, a BK-space is an [[FK-space|71DMQHW6JZ]] whose topology is given by a norm.

Example: $\ell^\infty$ with $\norm{x}_\infty = \sup_n \abs{x_n}$ is a BK-space.
It is a Banach space, and $\abs{x_n} \le \norm{x}_\infty$ shows that each coordinate map is continuous.
In the same way, the [[spaces ℓ^p|08P6T2WH6R]] for $1 \le p < \infty$, the space $c$ of convergent sequences and the space $c_0$ of null sequences are BK-spaces.

Non-example: the space $\omega$ of all sequences is an FK-space but not a BK-space.
Its FK topology, the topology of coordinatewise convergence, is not given by any norm, because no neighbourhood of $0$ in it is bounded.
