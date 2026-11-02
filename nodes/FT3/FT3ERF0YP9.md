---
tag: FT3ERF0YP9
kind: definition
name: Hopf algebra structure on cohomology
msc: [55P45, 16T05, 57T05]
defines: WJXK0V9NE9
uses: [EASHTX8EG5, RDT4785M4D, JX47MS1R1H, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $(X, e, \mu)$ be a path-connected [[H-space|EASHTX8EG5]] with the homotopy type of a CW complex.
Assume that each $H^n(X; k)$ is finite-dimensional.
By the Künneth theorem, the cross product gives an isomorphism $H^*(X; k) \otimes_k H^*(X; k) \cong H^*(X \times X; k)$.
The *[[Hopf algebra|7XFYP0N84H]] structure on cohomology* of $X$ consists of:

1. the [[cohomology ring|RDT4785M4D]] $H^*(X; k)$, with the [[cup product|JX47MS1R1H]] as multiplication and $1$ as unit;
2. the comultiplication $\Delta \colon H^*(X; k) \to H^*(X; k) \otimes_k H^*(X; k)$, defined as $\mu^*$ followed by the inverse of the Künneth isomorphism;
3. the counit $H^*(X; k) \to k$ given by restriction to the basepoint $e$.

With these maps, $H^0(X; k) = k$, $\Delta$ is a counital homomorphism of graded algebras, and $\Delta(x) = x \otimes 1 + 1 \otimes x + \sum x'_i \otimes x''_i$ with $0 < \abs{x'_i}, \abs{x''_i} < \abs{x}$ for $\abs{x} > 0$.
If $\mu$ is homotopy associative, $\Delta$ is also coassociative and $H^*(X; k)$ is a connected, graded-commutative Hopf algebra.

## Remarks

In the homotopy associative case the antipode exists automatically, because the bialgebra is connected: $H^0(X; k) = k$.

Example: for $X = S^3$, the unit quaternions, $H^*(S^3; k) = k \oplus k x$ with $\abs{x} = 3$.
By degrees, $\Delta(x) = x \otimes 1 + 1 \otimes x$, and $\Delta(x)^2 = 0 = \Delta(x^2)$, as $x \otimes x$ and $-x \otimes x$ cancel by the sign rule.

Non-example: on $H^*(S^2; \Q) = \Q[x]/(x^2)$ with $\abs{x} = 2$, the only candidate $\Delta(x) = x \otimes 1 + 1 \otimes x$ is not an algebra map, since $\Delta(x)^2 = 2 x \otimes x \ne 0 = \Delta(x^2)$.
This reflects the fact that $S^2$ is not an H-space.

Hopf's theorem: if $k$ has characteristic $0$ and $H^*(X; k)$ is finite-dimensional, then $H^*(X; k)$ is an exterior algebra on finitely many generators of odd degree.
