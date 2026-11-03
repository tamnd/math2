---
tag: FJ34XJZMXB
kind: definition
name: Internal wave
msc: [76B55, 86A05]
defines: GPKN5XHJ1F
uses: [TXQQQG9T2S, XQ82TE42FH]
sources:
  - url: https://en.wikipedia.org/wiki/Internal_wave
---

## Definition

Consider an inviscid, non-rotating fluid in the [[Boussinesq approximation|TXQQQG9T2S]], stratified at rest with constant [[Brunt–Väisälä frequency|XQ82TE42FH]] $N > 0$.
Let $(u, v, w)$ be the velocity, $p$ the pressure perturbation divided by the reference density, and $b$ the buoyancy.
The linearised equations for small perturbations of the rest state are
$$\partial_t u = -\partial_x p, \quad \partial_t v = -\partial_y p, \quad \partial_t w = -\partial_z p + b, \quad \partial_t b = -N^2 w, \quad \partial_x u + \partial_y v + \partial_z w = 0.$$
An *internal wave* is a nonzero plane-wave solution of these equations.
In it every field is proportional to $\cos(k x + l y + m z - \omega t + \alpha)$, with a phase $\alpha$ that may differ between the fields.
Here $(k, l, m)$ is the wavevector, with $(k, l) \ne (0, 0)$, and $\omega > 0$ is the frequency.
Such a solution exists exactly when
$$\omega^2 = N^2 \, \frac{k^2 + l^2}{k^2 + l^2 + m^2}.$$

## Remarks

Eliminating $u$, $v$, $p$ and $b$ gives the single equation $\partial_t^2 \Delta w + N^2 (\partial_x^2 + \partial_y^2) w = 0$, and inserting a plane wave gives the dispersion relation.
If $\Theta$ is the angle between the wavevector and the horizontal, the relation is $\omega = N \cos \Theta$, so the frequency depends only on the direction of the wavevector and $0 < \omega \le N$.

Example: a wave with $m = k$ and $l = 0$ has wavevector at $45$ degrees and frequency $\omega = N / \sqrt{2}$.

Non-example: a disturbance forced at a frequency $\omega > N$ cannot propagate as an internal wave; the relation has no real wavevector, and the response decays away from the source.

The group velocity is perpendicular to the wavevector, so energy moves along the crests.
This is visible in the St. Andrew's cross pattern made by an oscillating cylinder in a stratified tank.
In a rotating fluid with Coriolis parameter $f$ the relation becomes $\omega^2 = \big( N^2 (k^2 + l^2) + f^2 m^2 \big) / (k^2 + l^2 + m^2)$.
