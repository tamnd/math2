---
tag: MBQS4B0TPA
kind: definition
name: Index theory
msc: [58J20, 19K56, 47A53]
defines: 675MAXBQN6
uses: [44GBFZ16SG, QDCD33CS21, MT9P2X85V8]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Definition

Let $M$ be a closed smooth manifold, let $E$ and $F$ be complex vector bundles over $M$, and let $P \colon C^\infty(M; E) \to C^\infty(M; F)$ be an [[elliptic differential operator|MT9P2X85V8]].
Its [[analytic index|44GBFZ16SG]] $\operatorname{ind} P = \dim \ker P - \dim \operatorname{coker} P$ is a finite integer.
*Index theory* is the part of global analysis that computes such indices, and their refinements, in terms of topological data.
Its main tool is the [[topological index|QDCD33CS21]], which depends only on the homotopy class of the principal symbol of $P$.

## Remarks

The Atiyah–Singer index theorem states that the analytic index and the topological index of $P$ are equal.
Refinements replace the integer index by an element of a representation ring (equivariant index) or of a K-theory group of a parameter space (families index).
Other refinements add correction terms on manifolds with boundary.

Example: on the circle $S^1 = \R / 2\pi\Z$, the operator $P = d/d\theta$ on complex functions is elliptic.
Its kernel is the constants and its image is the functions of mean zero, so $\operatorname{ind} P = 1 - 1 = 0$.

Non-example: the dimension of the kernel alone is not an index quantity, because it is not stable.
For $P_c = d/d\theta + c$ with $c \in \C$, $\dim \ker P_c$ is $1$ when $c \in i\Z$ and $0$ otherwise, while $\operatorname{ind} P_c = 0$ for all $c$.
