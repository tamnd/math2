---
tag: P5SCM8NKMQ
kind: example
name: Interior Schwarzschild metric
msc: [83C15, 83C55]
instance_of: [BY4QYYS788]
illustrates: [2T335F8H8F, HC0AA1J8PR]
uses: [6Y50T68WKY, H4FNPG6ZY1]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_Schwarzschild_metric
same_as:
  wikidata: Q25113032
  wikipedia: Interior Schwarzschild metric
---

## Example

Use units where the gravitational constant and the speed of light equal $1$.
Fix a radius $R > 0$ and a constant density $\rho > 0$, and let $M = \frac{4}{3}\pi \rho R^3$ be the total mass.
Assume $R > \frac{9}{4} M$.
On the ball $0 \le r \le R$, with coordinates $(t, r, \theta, \phi)$, the *interior Schwarzschild metric* is
$$g = -\left(\frac{3}{2}\sqrt{1 - \frac{2M}{R}} - \frac{1}{2}\sqrt{1 - \frac{2M r^2}{R^3}}\right)^2 dt^2 + \left(1 - \frac{2M r^2}{R^3}\right)^{-1} dr^2 + r^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right).$$
It solves the Einstein equations with a static [[perfect fluid|H4FNPG6ZY1]] of density $\rho$ and pressure
$$p(r) = \rho \, \frac{\sqrt{1 - 2Mr^2/R^3} - \sqrt{1 - 2M/R}}{3\sqrt{1 - 2M/R} - \sqrt{1 - 2Mr^2/R^3}}.$$

Check at the surface: at $r = R$ both square roots equal $\sqrt{1 - 2M/R}$.
So $g_{tt} = -(1 - 2M/R)$ and $g_{rr} = (1 - 2M/R)^{-1}$, which are the values of the exterior [[Schwarzschild metric|6Y50T68WKY]] of mass $M$, and the two metrics join continuously.
The numerator of $p$ vanishes at $r = R$, so the pressure drops to $0$ at the surface, as it must for a star in vacuum.

Check at the centre: at $r = 0$ the denominator of $p$ is $3\sqrt{1 - 2M/R} - 1$.
It is positive exactly when $1 - 2M/R > 1/9$, that is, when $R > \frac{9}{4} M$.
When $R$ decreases to $\frac{9}{4}M$, the central pressure tends to infinity.
This is the bound of [[Buchdahl's theorem|HC0AA1J8PR]], and here it is sharp.
The pressure profile solves the [[Tolman–Oppenheimer–Volkoff equation|2T335F8H8F]] with constant density.

## Explanations

### L1 human

This metric describes the inside of an idealized star made of a fluid that cannot be compressed, so its density is the same everywhere.
Outside the star, spacetime is the ordinary Schwarzschild geometry, and the two descriptions match at the surface.
The pressure is largest at the centre and falls to zero at the surface.
If the star is squeezed until its radius reaches $9/4$ of its mass in these units, the central pressure becomes infinite.
So no such star can be more compact than that, which already hints that very compact stars must collapse.
