---
tag: 0RH4E3CAV9
kind: definition
name: Projection
msc: [15A04]
defines: 033DA1WE8Y
uses: [0PTF1PTJK0, 041JTZCK9Q]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Definitions
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A *projection* on $V$ is an [[endomorphism|0J7H0YBFDJ]] $P \colon V \to V$ with $P \circ P = P$.

## Remarks

If $P$ is a projection, then $V = \im P \oplus \ker P$, and $P$ acts as the identity on $\im P$.
Conversely, for each [[direct sum|0XYYT5KNTX]] $V = U \oplus W$, the map $u + w \mapsto u$ is a projection with image $U$ and kernel $W$.
If $P$ is a projection, then $I - P$ is the projection with image $\ker P$ and kernel $\im P$.
In an inner product space, an [[orthogonal projection|0B8KZRT28M]] is a projection whose kernel is orthogonal to its image.

## Explanations

### L1 human

A projection maps space onto a subspace and leaves the vectors of that subspace where they are.
Projecting a second time changes nothing.
The shadow of an object on the floor, in light from a fixed direction, is a picture of a projection.
