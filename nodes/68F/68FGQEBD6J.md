---
tag: 68FGQEBD6J
kind: concept
name: Lie bracket of vector fields
msc: [58A05, 53A45, 17B66]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_bracket_of_vector_fields
same_as:
  wikidata: Q5478310
  wikipedia: Lie bracket of vector fields
---

## Summary

The Lie bracket of two vector fields $X$ and $Y$ on a smooth manifold is a third vector field $[X, Y]$.
It measures how much the flows of $X$ and $Y$ fail to commute.
It is zero exactly when, for short times, moving along $X$ then $Y$ gives the same result as moving along $Y$ then $X$.
With this bracket the vector fields on a manifold form a Lie algebra.
It appears in the Frobenius theorem, in the definition of curvature and torsion, and in control theory.

## Explanations

### L1 human

Think of a car: it can drive forward and it can turn the wheels, but it cannot slide sideways.
By alternating small forward and turning moves, you can still end up shifted sideways, as in parallel parking.
The sideways motion comes from Lie brackets of the motions you are allowed.
On the plane, the fields $\partial_x$ and $x\,\partial_y$ have bracket $\partial_y$, a direction neither field gives at the origin.
