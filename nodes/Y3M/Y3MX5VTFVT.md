---
tag: Y3MX5VTFVT
kind: definition
name: Kozai mechanism
msc: [70F15, 70F07]
defines: VWPBTNNZG0
uses: [WW0JHSBE6D, K6KNWEVRY4, JE1Z920QKT]
sources:
  - url: https://en.wikipedia.org/wiki/Kozai_mechanism
---

## Definition

Consider a hierarchical [[three-body problem|JE1Z920QKT]].
A body of negligible mass orbits a primary on an inner orbit.
A distant perturber of mass $m'$ moves about the primary on a circular outer orbit, of radius much larger than the inner semi-major axis.
Measure the inclination $i$ of the inner orbit from the plane of the outer orbit, and let $e$ be its eccentricity.
Average the [[perturbation|WW0JHSBE6D]] by the perturber over both orbital periods and keep the leading, quadrupole, term.
In this secular approximation the inner semi-major axis $a$ and the quantity
$$\sqrt{1 - e^2}\, \cos i$$
are constant.
The *Kozai mechanism* is the resulting coupled periodic oscillation of $e$ and $i$, in which $e$ grows when $\abs{\cos i}$ decreases and conversely.

## Remarks

The conserved quantity is, up to a factor, the component of the inner angular momentum normal to the outer orbit.
If the inner orbit starts nearly circular with inclination $i_0$, then large eccentricities occur exactly when $\cos^2 i_0 < 3/5$, that is $39.2^\circ \lesssim i_0 \lesssim 140.8^\circ$.
In that case the maximal eccentricity is
$$e_{\max} = \sqrt{1 - \tfrac{5}{3} \cos^2 i_0}.$$
Example: $i_0 = 60^\circ$ gives $\cos^2 i_0 = 1/4$ and $e_{\max} = \sqrt{1 - 5/12} = \sqrt{7/12} \approx 0.76$.
Non-example: $i_0 = 20^\circ$ gives $\cos^2 i_0 \approx 0.88 > 3/5$, and a nearly circular orbit stays nearly circular.
The [[orbital elements|K6KNWEVRY4]] $e$ and $i$ oscillate together with the argument of periapsis $\omega$, which in the high-inclination case can librate about $90^\circ$ or $270^\circ$.
The mechanism was found by Lidov in 1961 for artificial satellites and by Kozai in 1962 for asteroids.
