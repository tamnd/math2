---
tag: Q5D54R3RGE
kind: concept
name: Zonal spherical harmonics
msc: [33C55, 43A90]
specializes: [3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Zonal_spherical_harmonics
same_as:
  wikidata: Q8073864
  wikipedia: Zonal spherical harmonics
---

## Summary

Fix a point $y$ of the sphere and a degree $\ell$.
The zonal spherical harmonic $Z_y^{(\ell)}$ is the spherical harmonic of degree $\ell$ that reproduces the value at $y$ of every harmonic of degree $\ell$.
It is invariant under the rotations that fix $y$, so it depends only on the angle between $x$ and $y$.
It is a multiple of a [[Gegenbauer polynomial|5TRFA6F79B]] in $x \cdot y$, and of the [[Legendre polynomial|QFYGJVA996]] $P_\ell(x \cdot y)$ on the sphere in $\R^3$.
It is the building block of expansions in [[spherical harmonics|3F32Y21HP4]] and of the Poisson kernel of the ball.

## Explanations

### L1 human

Pick a point $y$ on a globe, as if it were the north pole.
A zonal function is one that is constant along each circle of latitude around $y$, so it only depends on the distance from $y$.
Among the spherical harmonics of a given degree there is, up to a factor, exactly one zonal one.
With the right factor, integrating any harmonic of that degree against it returns the value of that harmonic at $y$.
On the ordinary sphere it is $\frac{2\ell + 1}{4\pi} P_\ell(\cos \theta)$, where $\theta$ is the angle from $y$.
