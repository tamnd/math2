---
tag: 0RH4E3CAV9
kind: definition
name: Projection
msc: ["15A04"]
topics: [QHKTJ89V6S]
audience: ug1
defines: 033DA1WE8Y
uses: [0PTF1PTJK0, 041JTZCK9Q]
formal:
  - system: lean4
    library: mathlib
    decl: IsIdempotentElem
    match: exact
  - system: lean4
    library: mathlib
    decl: LinearMap.IsProj
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Definitions
  - book: isbn:9783031410253
    locator: Section 3E
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A *projection* on $V$ is an [[endomorphism|0PTF1PTJK0]] $P \colon V \to V$ with $P \circ P = P$.

If $V = U \oplus W$ is a [[direct sum|041JTZCK9Q]], the *projection onto $U$ along $W$* is the map $P_{U, W}(u + w) = u$ for $u \in U$ and $w \in W$.

## Notation

We write $P^2 = P$ for $P \circ P = P$.
An endomorphism with this property is also called *idempotent*.

## Remarks

If $P$ is a projection, then $V = \operatorname{im} P \oplus \ker P$, and $P$ acts as the identity on $\operatorname{im} P$.
Conversely, $P_{U, W}$ is a projection with image $U$ and kernel $W$.
These two constructions are inverse to each other, by the [[theorem on projections and decompositions|~d025ab24]].
If $P$ is a projection, then $I - P$ is the projection with image $\ker P$ and kernel $\operatorname{im} P$.
In an inner product space, an [[orthogonal projection|0B8KZRT28M]] is a projection whose kernel is orthogonal to its image.

## Explanations

### L1 human

A projection maps space onto a subspace and leaves the vectors of that subspace where they are.
Projecting a second time changes nothing.
The shadow of an object on the floor, in light from a fixed direction, is a picture of a projection.

### L2 human

For $P(x, y) = (x + y, 0)$ on $\R^2$, we get $P(P(x, y)) = P(x + y, 0) = (x + y, 0) = P(x, y)$.
So $P$ is a projection, with image the $x$-axis and kernel the line $\R(1, -1)$.
