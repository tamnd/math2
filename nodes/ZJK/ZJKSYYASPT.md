---
tag: ZJKSYYASPT
kind: concept
name: Banach–Mazur distance
msc: [46B20, 52A21, 46B07]
sources:
  - url: https://en.wikipedia.org/wiki/Banach%E2%80%93Mazur_compactum
---

## Summary

The Banach–Mazur distance measures how far two [[normed vector spaces|03J5RAKB30]] of the same finite dimension are from being isometric.
It is the smallest possible distortion $\norm{T} \norm{T^{-1}}$ of a [[linear isomorphism|0B8T10CE7N]] $T$ between them.
In geometric terms, it compares the unit balls up to linear maps.
With it, the isometry classes of $n$-dimensional normed spaces form the [[Banach–Mazur compactum|RH1WTN38RQ]].
Many questions of local Banach space theory and asymptotic convex geometry are estimates of this distance.

## Explanations

### L1 human

A norm on $\R^n$ is described by its unit ball, a symmetric convex body.
Two norms are close in the Banach–Mazur sense if a linear change of coordinates makes the unit balls nearly equal.
Then one unit ball fits inside the other, and the other fits inside a slightly enlarged copy of the first.
The distance is $1$ exactly when the two spaces are isometric.
For instance, the square ball of the maximum norm on $\R^2$ and the round disc of the Euclidean norm are at distance $\sqrt{2}$.
The disc fits in the square, and the square fits in the disc enlarged by $\sqrt{2}$.
