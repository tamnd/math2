---
tag: 3NFC6F0Z9F
kind: definition
name: Complemented subspace
msc: [46B20, 46B03]
defines: Q0TY362K0V
uses: [06GZ956657, 00YC1D652K, 0ZCK8DQYN1, 0M83V17KHX]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$, and let $M$ be a [[closed|0ZCK8DQYN1]] [[linear subspace|00YC1D652K]] of $X$.
The subspace $M$ is *complemented* in $X$ if there is a closed linear subspace $N$ of $X$ such that $M \cap N = \set{0}$ and $M + N = X$.
In other words, $M$ and $N$ are [[complementary subspaces|0M83V17KHX]].

## Remarks

Equivalently, $M$ is complemented if and only if there is a continuous linear map $P \colon X \to X$ with $P^2 = P$ and $P(X) = M$, a bounded [[projection|033DA1WE8Y]] onto $M$.
Given such $P$, take $N = \ker P$; given $N$, the algebraic projection onto $M$ along $N$ has closed graph, so it is continuous by the [[closed graph theorem|GXM8BX8YM7]].
Example: in a [[Hilbert space|HM2HHE3J51]] every closed subspace $M$ is complemented by its orthogonal complement $M^\perp$, which is closed with $M \cap M^\perp = \set{0}$ and $M + M^\perp$ equal to the whole space.
Every finite-dimensional subspace of a Banach space is complemented: extend a dual basis by the [[Hahn–Banach theorem|QB5AE3VYZZ]] to build the projection.
Non-example: $c_0$ is a closed subspace of $\ell^\infty$ that is not complemented; every closed subspace $N$ with $c_0 \cap N = \set{0}$ has $c_0 + N \ne \ell^\infty$.
A theorem of Lindenstrauss and Tzafriri says that a Banach space in which every closed subspace is complemented is isomorphic to a Hilbert space.
