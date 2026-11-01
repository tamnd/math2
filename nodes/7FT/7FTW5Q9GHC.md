---
tag: 7FTW5Q9GHC
kind: concept
name: Schwarz–Christoffel mapping
msc: [30C30, 30C20]
specializes: [0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz%E2%80%93Christoffel_mapping
same_as:
  wikidata: Q769569
  wikipedia: Schwarz–Christoffel mapping
---

## Summary

A Schwarz–Christoffel mapping is a conformal map from the upper half-plane onto the interior of a polygon.
Such maps have an explicit integral form, in which the derivative is a product of powers of linear factors, one for each vertex.
The exponents come from the angles of the polygon, while the positions of the preimages of the vertices must usually be found numerically.
The formula is one of the few cases where the Riemann mapping theorem comes with a concrete map.
It is much used in engineering and in numerical conformal mapping.

## Explanations

### L1 human

A conformal map from the half-plane must bend the straight boundary line into the edges of a polygon.
Along the real axis, the direction of the image changes only at a few points, where it turns by the exterior angle of a corner.
A factor $(z - x_k)^{\alpha_k - 1}$ in the derivative does exactly this: it turns the direction by a fixed angle when $z$ passes $x_k$.
For instance, $z \mapsto z^{1/2}$ maps the upper half-plane onto the quarter-plane, a polygon with one corner of angle $\pi/2$ at $0$ and one at infinity.
