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

A projection is a linear map from a space to itself that does nothing more when we apply it a second time.
Let $F$ be a field and let $V$ be a vector space over $F$.
A *projection* on $V$ is an [[endomorphism|0PTF1PTJK0]] $P \colon V \to V$ with $P \circ P = P$.

If $V = U \oplus W$ is a [[direct sum|041JTZCK9Q]], the *projection onto $U$ along $W$* is the map
$$P_{U, W}(u + w) = u, \qquad u \in U, \; w \in W.$$

## Notation

We write $P^2 = P$ for $P \circ P = P$.
An endomorphism with this property is also called *idempotent*.
Some books use "projection" only for orthogonal projections in an inner product space.

## Remarks

The definition has two parts, and each one matters.
The map must be linear and go from $V$ to $V$, because $P \circ P$ only makes sense when the target of $P$ is its source.
The equation $P^2 = P$ says that a vector that is already in the image does not move again.
For example, $P(x, y) = (x + y, 0)$ on $\R^2$ is a projection, since $P(x + y, 0) = (x + y, 0)$.
The map $N(x, y) = (y, 0)$ is linear, but $N(N(0, 1)) = N(1, 0) = (0, 0)$ while $N(0, 1) = (1, 0)$, so it fails the equation.

The second sentence of the definition needs the sum to be direct, so that the $U$-part $u$ of a vector is unique and $P_{U, W}$ is well defined.
The two descriptions are the same notion.
A projection $P$ gives $V = \operatorname{im} P \oplus \ker P$, and $P$ is the projection onto its image along its kernel.
Conversely $P_{U, W}$ is a projection with image $U$ and kernel $W$.
These two constructions are inverse to each other, by the [[theorem on projections and decompositions|2ZX5Q7V4VN]].

If $P$ is a projection, then $I - P$ is the projection with image $\ker P$ and kernel $\operatorname{im} P$.
In an inner product space, an [[orthogonal projection|0B8KZRT28M]] is a projection whose kernel is orthogonal to its image.
The concept page on the [[projection|033DA1WE8Y]] has more examples and the main properties.

## Explanations

### L1 human

A projection moves space onto a subspace and leaves the vectors of that subspace where they are.
So projecting a second time changes nothing.
The shadow of an object on the floor, in light that comes from one fixed direction, is a picture of a projection.

### L2 human

For $P(x, y) = (x + y, 0)$ on $\R^2$, we check the equation directly:
$$P(P(x, y)) = P(x + y, 0) = (x + y, 0) = P(x, y).$$
So $P$ is a projection.
Its image is the $x$-axis, and its kernel is the line $x + y = 0$, which is $\R(1, -1)$.
So $P$ is the projection onto the $x$-axis along $\R(1, -1)$, and the splitting of a vector is $(x, y) = (x + y, 0) + (-y, y)$.
