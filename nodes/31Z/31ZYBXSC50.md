---
tag: 31ZYBXSC50
kind: statement
role: proposition
name: Geodetic effect
msc: [83C10, 83B05]
uses: [6Y50T68WKY, RNRTS8WWNM, NX9NYGFTRV, CFE9SNEHMP, WFCMWBVAEB, 2TAW8GAMM1]
about: [6Y50T68WKY, CFE9SNEHMP]
sources:
  - url: https://en.wikipedia.org/wiki/Geodetic_effect
same_as:
  wikidata: Q2711882
  wikipedia: Geodetic effect
---

## Statement

Work in units with $G = c = 1$.
Let $M > 0$ and consider the [[Schwarzschild metric|6Y50T68WKY]] of mass $M$.
Let a gyroscope move along a circular timelike [[geodesic|RNRTS8WWNM]] of radius $r > 3M$ in the equatorial plane.
Let its spin vector be [[Fermi–Walker transported|NX9NYGFTRV]], which here means parallel transported.
Fix a direction defined by the distant stars.
Then after one revolution the spin vector has [[precessed|CFE9SNEHMP]] relative to it, in the sense of the orbital motion, by
$$\Delta\phi = 2\pi\left(1 - \sqrt{1 - \frac{3M}{r}}\right).$$
To first order in $M/r$, $\Delta\phi \approx 3\pi M/r$ per revolution.

## Remarks

Solving the parallel transport equations along the orbit shows that, relative to the radial direction, the spin turns backwards by the angle $2\pi\sqrt{1 - 3M/r}$ per revolution.
The radial direction itself turns forwards by $2\pi$, and the difference of the two angles is $\Delta\phi$.
In the weak field the same effect for a general orbit is the precession angular velocity $\boldsymbol{\Omega} = \frac{3}{2} \frac{GM}{c^2 r^3} \, \mathbf{r} \times \mathbf{v}$, in ordinary units.
De Sitter computed the effect for the Earth–Moon system orbiting the Sun in 1916.
Gravity Probe B, with gyroscopes in polar orbit around the Earth, predicted about $6606$ milliarcseconds per year and measured a value in agreement to better than one percent.
The geodetic effect does not need the central body to rotate; this distinguishes it from [[frame-dragging|WFCMWBVAEB]].

## Explanations

### L1 human

Carry a perfect gyroscope around a heavy body in a circular orbit.
In flat space its axis would come back pointing exactly where it started.
Around a mass it comes back turned by a small angle, because space near the mass is curved.
In the same way, a vector carried around a closed loop on a sphere comes back rotated.

### L2 human

The geodetic precession combines the curvature of space and the effect of the gravitational potential on the moving gyroscope.
It is a direct test of the [[parameterized post-Newtonian|2TAW8GAMM1]] parameter $\gamma$, since the weak-field rate is proportional to $\frac{1}{2} + \gamma$.
In binary pulsars the analogous geodetic precession of the pulsar spin changes the shape of the observed pulse profile over years.
