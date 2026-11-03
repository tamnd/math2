---
tag: NC41X0TA5W
kind: definition
name: Innermost stable circular orbit
msc: ["83C57", "83C10"]
defines: 3YF024G572
uses: [BY4QYYS788, RNRTS8WWNM]
sources:
  - url: https://en.wikipedia.org/wiki/Innermost_stable_circular_orbit
---

## Definition

Let $I \subset (0, \infty)$ be an open interval and let $f, h \colon I \to (0, \infty)$ be smooth functions.
Consider the static, spherically symmetric [[Lorentzian manifold|BY4QYYS788]] with the metric
$$g = -f(r)\, dt^2 + h(r)\, dr^2 + r^2 \left(d\theta^2 + \sin^2\theta \, d\phi^2\right), \qquad r \in I.$$
For a number $L \ge 0$ put $V_L(r) = f(r)\left(1 + L^2/r^2\right)$.
A timelike [[geodesic|RNRTS8WWNM]] in the plane $\theta = \pi/2$ with constant $r = r_0$ is a *circular orbit* of angular momentum $L$; it exists exactly when $V_L'(r_0) = 0$.
The circular orbit is *stable* if moreover $V_L''(r_0) > 0$.
The *innermost stable circular orbit* is the circular orbit at the radius
$$r_{\mathrm{ISCO}} = \inf \set{r_0 \in I : \text{some stable circular orbit has radius } r_0},$$
when this set is not empty.

## Remarks

For a timelike geodesic in the plane $\theta = \pi/2$ with proper time as parameter, $E = f \dot t$ and $L = r^2 \dot\phi$ are conserved.
The normalisation $g(\dot\gamma, \dot\gamma) = -1$ gives $f h\, \dot r^2 = E^2 - V_L(r)$, so $V_L$ plays the role of an effective potential.

Example: for the Schwarzschild metric, $f(r) = 1 - 2M/r$ on $(2M, \infty)$ with $M > 0$.
Then $V_L'(r) = 0$ gives $L^2 = M r^2 / (r - 3M)$, so circular orbits exist exactly for $r > 3M$.
A computation shows that $V_L''(r_0) > 0$ at such an orbit exactly when $r_0 > 6M$.
Hence $r_{\mathrm{ISCO}} = 6M$, where the orbit is marginally stable, with $L^2 = 12 M^2$.

Non-example: in Newtonian gravity the effective potential $-M/r + L^2/(2r^2)$ has a strict minimum at $r_0 = L^2/M$ for every $L > 0$.
Every radius carries a stable circular orbit, and the infimum is $0$, which is not the radius of any orbit.

For the Kerr metric of mass $M$ and spin parameter $a$, the equatorial ISCO depends on the direction of motion.
It moves inward towards $r = M$ for co-rotating orbits and outward towards $r = 9M$ for counter-rotating orbits as $\abs{a} \to M$.
