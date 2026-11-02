---
tag: KHY35P4AKF
kind: concept
name: Lusin area integral
msc: [42B25, 31B10]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood%E2%80%93Paley_theory
---

## Summary

The Lusin area integral is a square function built from the harmonic extension $u$ of a function $f$ on $\R^n$ to the upper half-space.
At a point $x$ it integrates $\abs{\nabla u}^2$, suitably weighted, over the cone of points $(y, t)$ with $\abs{y - x} < t$.
For $1 < p < \infty$ its $L^p$ norm is comparable to that of $f$, as for the [[Littlewood–Paley square function|H4E1PW67Z1]].
It was introduced by Lusin for holomorphic functions on the disc, and it plays a key role in the real-variable theory of Hardy spaces.

## Explanations

### L1 human

Extend $f$ to a harmonic function $u$ one dimension up, using the Poisson kernel.
Over each point $x$ stand an upside-down cone with vertex at $x$, and measure how much $u$ varies inside the cone.
The total variation, measured by a weighted integral of $\abs{\nabla u}^2$, is the area integral at $x$.
For a holomorphic function $F$ on the unit disc, one integrates $\abs{F'}^2$ over a cone-shaped region.
The result is the area of the image of that region, counted with multiplicity, which explains the name.
