---
tag: QETCC3GZXC
kind: definition
name: Ahlfors theory
msc: ["30D35", "30D30"]
defines: M8611CV76A
uses: [0NSD1TPHR0, 0CDMXGPSES, YT6Z0GWS0W]
sources:
  - url: https://en.wikipedia.org/wiki/Ahlfors_theory
---

## Definition

Ahlfors theory studies a [[meromorphic function|0NSD1TPHR0]] $f$ on $\C$ through the covering surfaces $f(\set{\abs{z} < r})$ over the [[Riemann sphere|0CDMXGPSES]].
These surfaces are measured in the spherical metric $\abs{dw}/(1 + \abs{w}^2)$, for which the whole sphere has area $\pi$.
Its basic quantities, for $r > 0$, are:

1. the *mean sheet number*
$$S(r) = \frac{1}{\pi} \iint_{\abs{z} < r} \left(\frac{\abs{f'(z)}}{1 + \abs{f(z)}^2}\right)^2 dx \, dy,$$
the spherical area of the image counted with multiplicity, divided by the area of the sphere;
2. the *boundary length*
$$L(r) = \int_{\abs{z} = r} \frac{\abs{f'(z)}}{1 + \abs{f(z)}^2} \, \abs{dz},$$
the spherical length of the image of the circle $\abs{z} = r$.

## Remarks

Example: for $f(z) = z$, $S(r) = \frac{1}{\pi}\int_0^r \frac{2\pi t}{(1+t^2)^2} dt = \frac{r^2}{1+r^2}$, which tends to $1$, the sheet number of a map that covers the sphere once.
Here $L(r) = 2\pi r/(1 + r^2)$ tends to $0$, so the boundary becomes negligible.
The Ahlfors–Shimizu characteristic $T_0(r) = \int_0^r S(t)/t \, dt$ differs from the [[Nevanlinna characteristic|YT6Z0GWS0W]] $T(r, f)$ by a bounded function.
The main results compare, for disjoint regions $D_1, \dots, D_q$ of the sphere, the number of times the surface covers each $D_j$ with $S(r)$, with an error proportional to $L(r)$.
For a transcendental meromorphic function on $\C$ the ratio $L(r)/S(r)$ tends to $0$ along a sequence of radii.
This leads to the Ahlfors five islands theorem.
Let $f$ be a transcendental meromorphic function on $\C$, and let $D_1, \dots, D_5$ be Jordan domains on the sphere with pairwise disjoint closures.
Then $f$ maps some bounded simply connected domain in $\C$ conformally onto one of the $D_j$.
