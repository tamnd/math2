---
tag: SF1VEDT29F
kind: definition
name: Scorer's function
msc: [33C10, 34B30]
defines: JJQEGRK2DG
uses: [1N5D4PN92W, PNESAD6R5T]
sources:
  - url: https://en.wikipedia.org/wiki/Scorer%27s_function
---

## Definition

For real $x$, *Scorer's functions* are
$$\operatorname{Gi}(x) = \frac{1}{\pi} \int_0^\infty \sin\left( \frac{t^3}{3} + x t \right) dt, \qquad \operatorname{Hi}(x) = \frac{1}{\pi} \int_0^\infty \exp\left( -\frac{t^3}{3} + x t \right) dt,$$
where the first integral is an improper Riemann integral.

## Remarks

They solve the inhomogeneous [[Airy equations|PNESAD6R5T]] $\operatorname{Gi}'' - x \operatorname{Gi} = -\frac{1}{\pi}$ and $\operatorname{Hi}'' - x \operatorname{Hi} = \frac{1}{\pi}$.
Check for $\operatorname{Hi}$: differentiating under the integral sign, $\operatorname{Hi}'' - x \operatorname{Hi} = \frac{1}{\pi} \int_0^\infty (t^2 - x)\, e^{-t^3/3 + xt}\, dt = -\frac{1}{\pi} \left[ e^{-t^3/3 + xt} \right]_0^\infty = \frac{1}{\pi}$.
By comparing with the integral that defines the [[Airy function|1N5D4PN92W]] $\operatorname{Bi}$, one has $\operatorname{Gi} + \operatorname{Hi} = \operatorname{Bi}$.
A non-example: $\operatorname{Bi}$ itself is not a Scorer function; it solves the homogeneous equation $y'' - x y = 0$, not one with right-hand side $\pm \frac{1}{\pi}$.
Both functions extend to entire functions of $z \in \C$.
