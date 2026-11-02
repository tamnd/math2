---
tag: 91RZ5YARTM
kind: concept
name: Hörmander's condition
msc: [35H10, 35H20]
sources:
  - url: https://en.wikipedia.org/wiki/H%C3%B6rmander%27s_condition
same_as:
  wikidata: Q5964696
  wikipedia: Hörmander's condition
---

## Summary

Hörmander's condition is a property of a family of [[vector fields|0299VCW1TH]].
It says that the fields and their iterated [[Lie brackets|68FGQEBD6J]] span the tangent space at every point.
Hörmander's theorem says that under this condition the second-order operator $\sum_j X_j^2 + X_0$ is [[hypoelliptic|K9DSR21DQC]], even though it may be far from elliptic.
The condition is central in sub-Riemannian geometry and in stochastic analysis, where it gives smooth densities for solutions of stochastic differential equations.

## Explanations

### L1 human

Suppose you can only move in a few allowed directions, such as driving a car, which cannot slide sideways.
By combining moves, such as going forward while turning and then backing up, you can still reach every nearby position; the Lie brackets record these combined moves.
Hörmander's condition says that the allowed directions, together with their brackets, reach every direction.
Then diffusion along the allowed directions still spreads in all directions and smooths everything out.
In the plane, the fields $\partial_x$ and $x \partial_y$ satisfy it, because their bracket is $\partial_y$.
