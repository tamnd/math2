---
tag: PSK6VJQR9B
kind: concept
name: Amoeba
msc: [14T10, 32A60]
sources:
  - url: https://en.wikipedia.org/wiki/Amoeba_(mathematics)
same_as:
  wikidata: Q2328765
  wikipedia: Amoeba (mathematics)
---

## Summary

The amoeba of a complex polynomial in $n$ variables is the image of its zero set in $(\C^\times)^n$ under a logarithmic map.
This map takes the logarithm of the absolute value of each coordinate.
The name, given by Gelfand, Kapranov and Zelevinsky, comes from its shape: a body with thin tentacles going off to infinity.
Each connected component of the complement is convex, and the number of these components is bounded by the [[Newton polytope|CYTTX8KHC8]].
Amoebas link complex algebraic geometry with convex geometry and degenerate to tropical varieties, see [[tropical geometry|7YTC3BHK60]].

## Explanations

### L1 human

Take the complex solutions of $1 + z + w = 0$ and record only the sizes $\abs{z}$ and $\abs{w}$, on a logarithmic scale.
The resulting region in the plane looks like a creature with three long arms.
The arms reach to infinity in three directions, where one of $z$, $w$ is tiny or both are huge.
Between the arms lie three convex holes.
Zooming out, the region shrinks to three rays from a point, the tropical line.
