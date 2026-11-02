---
tag: 8XAT77QQTN
kind: definition
name: Cohomology of Lie groups
msc: [57T10, 17B56]
defines: HKZABKRPN6
uses: [7JBRGCVJRB, 6N7BC70CX0, JX47MS1R1H, WJXK0V9NE9, GX74C07T0G]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra_cohomology
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] and let $k$ be a field.
The *cohomology* of $G$ with coefficients in $k$ is the graded $k$-algebra $H^*(G; k) = \bigoplus_{n \ge 0} H^n(G; k)$.
Here $H^n(G; k)$ is the [[singular cohomology|6N7BC70CX0]] of the underlying manifold of $G$, and the product is the [[cup product|JX47MS1R1H]].
When $G$ is connected and each $H^n(G; k)$ is finite-dimensional, the multiplication $\mu \colon G \times G \to G$ also gives a coproduct $\mu^*$, which makes $H^*(G; k)$ a [[Hopf algebra|WJXK0V9NE9]].

## Remarks

Example: $G = S^1$, the circle group.
Then $H^0(S^1; \R) = \R$, $H^1(S^1; \R) = \R x$, and all other groups vanish.
So $H^*(S^1; \R)$ is the exterior algebra on one generator $x$ of degree $1$, with $\mu^*(x) = x \otimes 1 + 1 \otimes x$.

Non-example: the cohomology of $G$ as an abstract group, $H^*(BG^\delta; k)$, or the continuous cohomology of $G$, is a different object.
For $G = S^1$ the continuous cohomology with coefficients in $\R$ vanishes in positive degrees, while $H^1(S^1; \R) \ne 0$.

For $k = \R$, the de Rham theorem identifies $H^*(G; \R)$ with the [[de Rham cohomology|GX74C07T0G]] of $G$.
If $G$ is compact and connected, averaging over $G$ shows that each class has a left- and right-invariant representative.
This gives an isomorphism $H^*(G; \R) \cong H^*(\mathfrak{g}; \R)$ with the Lie algebra cohomology of the Lie algebra $\mathfrak{g}$.
