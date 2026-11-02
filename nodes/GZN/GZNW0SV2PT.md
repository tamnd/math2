---
tag: GZNW0SV2PT
kind: definition
name: Knot invariant
msc: [57K10, 57K14]
defines: GZQ5ZE3X6G
uses: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Knot_invariant
---

## Definition

Let $\mathcal{K}$ be the set of [[knots|QYEAZTYGPT]] in $\R^3$, and let $S$ be a set.
A *knot invariant* with values in $S$ is a map $f \colon \mathcal{K} \to S$ such that $f(K) = f(K')$ whenever the knots $K$ and $K'$ are equivalent.

## Remarks

Equivalently, a knot invariant is a map on the set of equivalence classes of knots.
The values may be numbers, polynomials, groups up to isomorphism, or homology theories up to isomorphism.
Example: the [[crossing number|SWJZ4QRF9W]] is a knot invariant with values in $\N$, because it is a minimum taken over the diagrams of all knots equivalent to $K$.
Non-example: the number of crossings of one chosen diagram of $K$ is not an invariant of $K$.
Indeed, a twist in a diagram of the unknot adds a crossing without changing the knot.
An invariant is *complete* if $f(K) = f(K')$ implies that $K$ and $K'$ are equivalent.
The same notion is used for links.
