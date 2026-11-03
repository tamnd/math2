---
tag: 2Z7BWWRT3Y
kind: definition
name: Boussinesq approximation for water waves
msc: [76B15, 35Q35]
defines: 6EPTRN9AQE
uses: [R9WC0Z7Z69, NT73Y95RY5]
sources:
  - url: https://en.wikipedia.org/wiki/Boussinesq_approximation_(water_waves)
---

## Definition

Consider the [[water wave problem|R9WC0Z7Z69]] in one horizontal dimension, for water of undisturbed depth $h > 0$ with flat bottom and gravity $g > 0$.
Let $a$ be a typical wave amplitude and $\lambda$ a typical wavelength, and set $\varepsilon = a/h$ and $\mu = (h/\lambda)^2$.
The *Boussinesq approximation* derives model equations for the surface elevation $\eta(x, t)$ and a horizontal velocity $u(x, t)$.
It expands the velocity potential in powers of the height above the bottom.
It assumes $\varepsilon$ and $\mu$ small and of the same order, and keeps terms up to first order in $\varepsilon$ and $\mu$.
A standard result, with $u$ the depth-averaged horizontal velocity, is the system
$$\eta_t + \big((h + \eta)u\big)_x = 0, \qquad u_t + u u_x + g\eta_x = \frac{h^2}{3}u_{xxt}.$$

## Remarks

Example: for the linearised system, $\eta = A\cos(kx - \omega t)$ and $u = (\omega / (kh))\,\eta$ solve the equations when $\omega^2 = \frac{ghk^2}{1 + k^2h^2/3}$.
This agrees with the exact relation $\omega^2 = gk\tanh(kh)$ up to the first correction in $kh$, since both expand as $ghk^2(1 - k^2h^2/3 + O(k^4h^4))$.
Non-example: the [[shallow water equations|NT73Y95RY5]], without the term $\frac{h^2}{3}u_{xxt}$, keep the nonlinearity but drop the dispersion, so they are of zeroth order in $\mu$ and not a Boussinesq system.
Other choices of the velocity variable, such as the velocity at a given depth, give other Boussinesq systems.
They are equivalent to the same order but differ in their higher-order behaviour.
The ratio $\varepsilon / \mu = a\lambda^2/h^3$ is the Ursell number, which is of order one in the Boussinesq regime.
