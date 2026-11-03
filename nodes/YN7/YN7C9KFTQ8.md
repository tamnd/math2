---
tag: YN7C9KFTQ8
kind: definition
name: Capillary wave
msc: [76B45, 76B15]
defines: 5JNTHCYJ7K
uses: [R9WC0Z7Z69, CNCGSCVQB8]
sources:
  - url: https://en.wikipedia.org/wiki/Capillary_wave
---

## Definition

Consider small waves of wavenumber $k > 0$ on the surface of a liquid of density $\rho > 0$ and large depth, with surface tension $\sigma > 0$ and gravity $g \ge 0$.
In the linear theory of [[water waves|R9WC0Z7Z69]] with surface tension, a wave $\eta = a\cos(kx - \omega t)$ satisfies
$$\omega^2 = gk + \frac{\sigma k^3}{\rho}.$$
The wave is a *capillary wave* when the surface tension term dominates, that is when $k \gg k_m$ with $k_m = \sqrt{\rho g / \sigma}$, and then $\omega^2 \approx \sigma k^3 / \rho$.
A *pure capillary wave* is the case $g = 0$, where $\omega^2 = \sigma k^3 / \rho$ exactly.
Waves with $k$ of the order of $k_m$, where both terms matter, are called gravity–capillary waves.

## Remarks

Example: for clean water, $\sigma \approx 0.073$ N/m and $\rho \approx 1000$ kg/m$^3$, so $2\pi / k_m \approx 1.7$ cm, and a ripple of wavelength $2$ mm has $k \approx 8.5\, k_m$, well inside the capillary range.
Non-example: an ocean swell of wavelength $100$ m has $\sigma k^3/\rho$ smaller than $gk$ by a factor of about $10^{-8}$.
So it is a gravity wave, described by [[Airy wave theory|CNCGSCVQB8]] without surface tension.
For pure capillary waves the phase speed is $c = \sqrt{\sigma k / \rho}$ and the group velocity is $\tfrac{3}{2}c$, so energy moves faster than the crests.
The phase speed of gravity–capillary waves on deep water has the minimum $c_{\min} = (4g\sigma/\rho)^{1/4}$, about $0.23$ m/s for water, at $k = k_m$.
On water of finite depth $h$, the right-hand side is multiplied by $\tanh(kh)$.
