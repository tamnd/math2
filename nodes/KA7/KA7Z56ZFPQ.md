---
tag: KA7Z56ZFPQ
kind: problem
name: Geodesics on an ellipsoid
msc: [86A30, 53A05]
uses: [NSYMQMHPDN, R9XX7TNJCH, 6QBV95NG6E, 5K7ZVAQM4A]
about: [NSYMQMHPDN, R9XX7TNJCH]
sources:
  - url: https://en.wikipedia.org/wiki/Geodesics_on_an_ellipsoid
same_as:
  wikidata: Q1408386
  wikipedia: Geodesics on an ellipsoid
history:
  posed_by: "Alexis Clairaut"
  first_stated: "1735"
  notes: "Clairaut found the conserved quantity of geodesics on an ellipsoid of revolution; Bessel and Helmert later gave methods of solution."
---

## Problem

Let $\mathcal{E}$ be an oblate [[ellipsoid of revolution|R9XX7TNJCH]] with semi-major axis $a$ and flattening $f$, where $0 < f < 1$.
Points of $\mathcal{E}$ are given by [[geodetic coordinates|6QBV95NG6E]] $(\varphi, \lambda)$ with $h = 0$.
The azimuth of a curve at a point is the angle from north to its tangent, measured clockwise.
Solve the two geodesic problems on $\mathcal{E}$:

1. Direct problem: given a point $P_1$, an azimuth $\alpha_1$ and a length $s$, consider the [[geodesic|NSYMQMHPDN]] of length $s$ from $P_1$ with azimuth $\alpha_1$. Find its endpoint $P_2$ and its azimuth $\alpha_2$ at $P_2$.
2. Inverse problem: given points $P_1$ and $P_2$, find the length $s$ of a shortest geodesic from $P_1$ to $P_2$. Find also its azimuths $\alpha_1, \alpha_2$ at both ends.

## Remarks

Both problems are solved.
Clairaut (1735) found the constant of motion now called Clairaut's relation: along a geodesic, $\cos\beta \sin\alpha$ is constant, where $\beta$ is the reduced latitude, $\tan\beta = (1 - f)\tan\varphi$.
Legendre and Oriani (1806) and Bessel (1825) reduced the problem to integrals on an auxiliary sphere, where the geodesic becomes a great circle.
[[Vincenty's formulae|YY1941K7CB]] (1975) solve both problems by iteration; the inverse iteration can fail to converge for nearly antipodal points.
Karney (2013) gave algorithms that are accurate to machine precision and converge for all pairs of points.
For $f = 0$ the problems reduce to [[great-circle distance|5K7ZVAQM4A]] computations on a sphere.
Unlike on the sphere, a geodesic on $\mathcal{E}$ that is not a meridian or the equator does not close up in general.

## Explanations

### L1 human

On a squashed Earth, what is the shortest route between two places, and in which direction should one set off?
And if one walks straight ahead for a given distance, where does one arrive?
On a sphere these questions have simple answers with great circles.
On the ellipsoid the answers need integrals, which the geodesists of the nineteenth century reduced to series.
Today computers solve both questions to a precision of nanometres.
