---
tag: FAQ8ZJ4M0M
kind: definition
name: Stone algebra
msc: ["06D15"]
defines: ESYKDNZF8E
uses: [72V1Z82M5F, 0HM0HQCK6N, WMR73J0S26]
sources:
  - url: https://en.wikipedia.org/wiki/Stone_algebra
---

## Definition

A *Stone algebra* is a [[bounded lattice|72V1Z82M5F]] $(L, \vee, \wedge, 0, 1)$ such that:

1. $L$ is a [[distributive lattice|0HM0HQCK6N]].
2. Every $a \in L$ has a [[pseudocomplement|WMR73J0S26]] $a^*$.
3. $a^* \vee a^{**} = 1$ for every $a \in L$.

## Remarks

Example: every bounded chain $C$ with $0 \ne 1$ is a Stone algebra.
Its pseudocomplement is $0^* = 1$ and $a^* = 0$ for $a \ne 0$.
If $a = 0$ then $a^* \vee a^{**} = 1 \vee 0 = 1$, and if $a \ne 0$ then $a^* \vee a^{**} = 0 \vee 1 = 1$.

Non-example: the lattice of open sets of $\R$, with $U^* = \operatorname{int}(\R \setminus U)$, satisfies clauses 1 and 2 but not 3.
For $U = (0, \infty)$, one has $U^* = (-\infty, 0)$ and $U^{**} = (0, \infty)$, so $U^* \cup U^{**} = \R \setminus \set{0} \ne \R$.

Every Boolean algebra is a Stone algebra, with $a^* = \neg a$ and $a^{**} = a$.
