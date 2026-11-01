---
tag: AHE58SGQYW
kind: definition
name: Graphon
msc: [05C80, 05C63]
defines: QMJ5PNSF9X
sources:
  - url: https://en.wikipedia.org/wiki/Graphon
---

## Definition

A *graphon* is a measurable function $W \colon [0, 1]^2 \to [0, 1]$, for the Lebesgue measure on $[0, 1]^2$, such that $W(x, y) = W(y, x)$ for all $x, y \in [0, 1]$.

## Remarks

Example: let $W(x, y) = 1$ if exactly one of $x, y$ is less than $1/2$, and $W(x, y) = 0$ otherwise.
It takes values in $\set{0, 1}$, and it is measurable because it is constant on four rectangles.
It is symmetric, since swapping $x$ and $y$ does not change whether exactly one of them is below $1/2$.
It is the limit of the complete bipartite graphs $K_{n,n}$.

Non-example: $W(x, y) = x$ is measurable with values in $[0, 1]$, but it is not symmetric, since $W(1, 0) = 1 \ne 0 = W(0, 1)$.

A graph $G$ on $\set{1, \ldots, n}$ gives a step graphon $W_G$: $W_G(x, y) = 1$ if $\ceil{nx}$ and $\ceil{ny}$ are adjacent in $G$, and $0$ otherwise (with $\ceil{0}$ read as $1$).
For a finite graph $F$ on $\set{1, \ldots, k}$, the homomorphism density of $F$ in $W$ is
$$t(F, W) = \int_{[0,1]^k} \prod_{\set{i, j} \in E(F)} W(x_i, x_j) \, dx_1 \cdots dx_k.$$
Graphons that differ on a set of measure zero, or by a measure-preserving change of variables, are usually identified.
Some authors allow any standard probability space in place of $[0, 1]$.
