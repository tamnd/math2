---
tag: Q5EWVTA2RW
kind: statement
role: theorem
name: Riemannian Penrose inequality
msc: ["53C21", "83C57"]
uses: [7CBT4SM83Y, ZHX2VYQDZ3, 41X0YW2R9N, 5XVEF5DKAG, 6Y50T68WKY, PYRPXHNQTB]
about: [ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Riemannian_Penrose_inequality
same_as:
  wikidata: Q7333121
  wikipedia: Riemannian Penrose inequality
---

## Statement

Let $(M, g)$ be a complete, asymptotically flat, three-dimensional [[Riemannian manifold|7CBT4SM83Y]] with nonnegative [[scalar curvature|ZHX2VYQDZ3]].
Assume that the boundary $\partial M$ is an outermost [[minimal surface|41X0YW2R9N]], possibly with several components.
This means that $\partial M$ is a closed minimal surface and that no other closed minimal surface in $M$ encloses it.
Let $A$ be the total area of $\partial M$ and let $m$ be the ADM mass of $(M, g)$.
Then
$$m \ge \sqrt{\frac{A}{16\pi}}.$$
Equality holds if and only if $(M, g)$ is isometric to the spatial [[Schwarzschild metric|6Y50T68WKY]] of mass $m$ outside its horizon.

## Remarks

Huisken and Ilmanen proved the inequality in 2001 when $A$ is the area of a largest component of $\partial M$, using a weak form of [[inverse mean curvature flow|5XVEF5DKAG]].
Along this flow the Hawking mass of the evolving surface does not decrease, a monotonicity first observed by Geroch.
The Hawking mass equals $\sqrt{A/16\pi}$ on the horizon and tends to at most $m$ at infinity.
Bray proved the version with total area in 2001 by a conformal flow of metrics.
For the spatial Schwarzschild metric of mass $m$, the horizon is the sphere $r = 2m$ of area $16\pi m^2$, so both sides equal $m$.
Nonnegative scalar curvature is needed: without it the mass can even be negative.

## Explanations

### L1 human

In general relativity, a black hole has a horizon with a certain area.
The inequality says that the total mass of the space is at least a fixed multiple of the square root of that area.
So black holes cannot carry more horizon than their mass allows.
The Schwarzschild black hole is the extreme case where the two sides are equal.

### L2 human

The statement is the time-symmetric case of a conjecture of Penrose; the scalar curvature condition encodes nonnegative energy density.
It strengthens the [[positive mass theorem|PYRPXHNQTB]], which gives $m \ge 0$ when there is no horizon.
The two proofs use different flows: inverse mean curvature flow of surfaces, and a flow of conformal metrics.
The general case of the Penrose conjecture, without time symmetry, is still open.
