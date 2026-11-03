---
tag: Q9FRKED7PF
kind: definition
name: Photon sphere
msc: ["83C57", "83C10"]
defines: F6NZF2N77J
uses: [BY4QYYS788, RNRTS8WWNM]
sources:
  - url: https://en.wikipedia.org/wiki/Photon_sphere
---

## Definition

Let $I \subset (0, \infty)$ be an open interval and let $f, h \colon I \to (0, \infty)$ be smooth functions.
Consider the static, spherically symmetric [[Lorentzian manifold|BY4QYYS788]] $\R \times I \times S^2$ with the metric
$$g = -f(r)\, dt^2 + h(r)\, dr^2 + r^2 \left(d\theta^2 + \sin^2\theta \, d\phi^2\right).$$
A *photon sphere* is a sphere $r = r_0$, with $r_0 \in I$, such that some null [[geodesic|RNRTS8WWNM]] stays at $r = r_0$ for all values of its affine parameter.
This holds exactly when
$$\frac{d}{dr}\left(\frac{f(r)}{r^2}\right)\Big|_{r = r_0} = 0.$$

## Remarks

By symmetry one may take the geodesic in the plane $\theta = \pi/2$.
The quantities $E = f \dot t$ and $L = r^2 \dot\phi$ are conserved, and the null condition gives $f h\, \dot r^2 = E^2 - L^2 f(r)/r^2$.
So a circular orbit $r = r_0$ needs both $E^2 = L^2 f(r_0)/r_0^2$ and a critical point of $f/r^2$ at $r_0$.

Example: for the Schwarzschild metric, $f(r) = 1 - 2M/r$ on $I = (2M, \infty)$, so $f/r^2 = r^{-2} - 2M r^{-3}$.
Its derivative $-2r^{-3} + 6M r^{-4}$ vanishes only at $r = 3M$.
This is the photon sphere, and $f/r^2$ has a maximum there, so the circular orbits are unstable.

Non-example: for Minkowski space, $f = 1$ and $f/r^2 = r^{-2}$ is strictly decreasing.
No radius satisfies the condition, so flat space has no photon sphere.

For the rotating Kerr metric there are no circular light orbits at a single radius for all directions.
Equatorial circular light orbits exist at one radius for co-rotating light and at another for counter-rotating light.
