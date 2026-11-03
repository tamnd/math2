---
tag: PSR2K4RJ7B
kind: problem
name: Kepler problem in general relativity
msc: [83C10, 83C15]
uses: [6Y50T68WKY, RNRTS8WWNM, TYXD1T6FRX, 5AKNNW3W4Z, FF9ZPCZ59K]
about: [6Y50T68WKY, RNRTS8WWNM]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarzschild_geodesics
history:
  posed_by: Albert Einstein
  first_stated: "1915"
---

## Problem

Let $M > 0$ be a mass, $G$ the gravitational constant and $c$ the speed of light.
Let $r_s = 2GM/c^2$ and consider the exterior [[Schwarzschild metric|6Y50T68WKY]]
$$ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2 \left(d\theta^2 + \sin^2\theta \, d\varphi^2\right), \qquad r > r_s.$$
Determine all timelike and null [[geodesics|RNRTS8WWNM]] of this metric.
These describe the motion of a test body or a light ray around a spherical mass.
This is the analogue in general relativity of the Newtonian [[Kepler problem|TYXD1T6FRX]].

## Remarks

The problem is solved.
By spherical symmetry each geodesic stays in a plane, which can be taken to be $\theta = \pi/2$.
The [[Killing vector fields|5AKNNW3W4Z]] $\partial_t$ and $\partial_\varphi$ give two conserved quantities, the energy and the angular momentum per unit mass.
With $u = 1/r$, $h = r^2 \, d\varphi/d\tau$ and $\tau$ the proper time, a timelike geodesic obeys the orbit equation
$$\frac{d^2 u}{d\varphi^2} + u = \frac{GM}{h^2} + \frac{3GM}{c^2} u^2.$$
The last term is absent in the Newtonian problem.
The orbit equation can be integrated in terms of [[elliptic functions|FF9ZPCZ59K]].
Unlike Newtonian bound orbits, bound relativistic orbits are in general not closed ellipses: the perihelion advances from one orbit to the next.
There is no stable circular orbit with $r < 3 r_s$, and circular photon orbits exist only at $r = 3r_s/2$.
Einstein treated planetary motion in 1915 with an approximate solution, and Schwarzschild found the exact metric in 1916.

## Explanations

### L1 human

In Newton's theory a planet around a single star moves on an ellipse that closes on itself forever.
In general relativity the same question has a slightly different answer.
The orbit is almost an ellipse, but the ellipse turns slowly, so the planet traces a rosette.
Light also follows curved paths near the star, and close enough to the star there are no stable orbits at all.
