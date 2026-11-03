---
tag: J66PRV75BY
kind: definition
name: Map projection
msc: [86A30, 53A05]
defines: Y2C8D9VC7D
uses: [P9CM4GQ2T0, R9XX7TNJCH, 6QBV95NG6E]
sources:
  - url: https://en.wikipedia.org/wiki/Map_projection
---

## Definition

Let $S$ be a [[sphere|P9CM4GQ2T0]] or a [[reference ellipsoid|R9XX7TNJCH]], with points given by latitude $\varphi$ and longitude $\lambda$ as in [[geodetic coordinates|6QBV95NG6E]].
Let $U \subseteq S$ be an open set.
A *map projection* of $U$ is a map $P \colon U \to \R^2$, $(\varphi, \lambda) \mapsto (x, y)$, such that:

1. $P$ is smooth;
2. $P$ is injective;
3. the differential of $P$ is invertible at every point of $U$.

## Remarks

Example: on the sphere of radius $R$, the equirectangular projection $(\varphi, \lambda) \mapsto (R\lambda, R\varphi)$ on $U = \set{\abs{\varphi} < \pi/2, \ -\pi < \lambda < \pi}$ is smooth and injective, with invertible differential.
Non-example: the orthographic projection $(X, Y, Z) \mapsto (X, Y)$ of the whole unit sphere minus the poles fails clause 2, since $(X, Y, Z)$ and $(X, Y, -Z)$ have the same image.
Usually $U$ is the sphere minus a meridian or a pole, since the whole sphere does not embed in the plane.
The distortion of a projection at a point is described by [[Tissot's indicatrix|RCMYJPDMGJ]].
