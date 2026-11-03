---
tag: 1W0K0JXZRJ
kind: definition
name: Kompaneets equation
msc: [85A25, 35Q85, 82C40]
defines: QRX3A5S6SP
uses: [H8S9QE0B81, Z7BN231HNA, FVQWR7NS00]
sources:
  - url: https://en.wikipedia.org/wiki/Kompaneyets_equation
---

## Definition

Consider an isotropic, spatially homogeneous photon gas scattering off a thermal gas of free electrons with number density $n_e$ and temperature $T_e$.
Let $k_B$ be the Boltzmann constant, $m_e$ the electron mass, $c$ the speed of light, $h$ the Planck constant and $\nu$ the photon frequency.
Assume $k_B T_e \ll m_e c^2$ and $h\nu \ll m_e c^2$.
Let $x = h\nu / (k_B T_e)$ and let $n(x, t)$ be the photon occupation number at time $t$.
The *Kompaneets equation* is
$$\frac{\partial n}{\partial t} = \frac{k_B T_e}{m_e c^2} \, n_e \sigma_T c \, \frac{1}{x^2} \frac{\partial}{\partial x} \left[ x^4 \left( \frac{\partial n}{\partial x} + n + n^2 \right) \right],$$
where $\sigma_T$ is the [[Thomson|Z7BN231HNA]] cross-section.

## Remarks

Example: the Bose–Einstein distribution $n(x) = 1/(e^{x + \mu} - 1)$ with a constant $\mu \ge 0$ is a stationary solution, since $\partial n/\partial x = -e^{x+\mu}/(e^{x+\mu} - 1)^2 = -(n + n^2)$, so the bracket vanishes.
Non-example: a Planck distribution $n = 1/(e^{x'} - 1)$ at a temperature different from $T_e$, with $x' = h\nu / (k_B T_\gamma)$ and $T_\gamma \ne T_e$, is not stationary: the bracket does not vanish and the spectrum evolves.
The three terms in the bracket describe diffusion in energy, recoil and induced scattering.
The equation conserves the photon number $\int_0^\infty x^2 n \, dx$, since the right side is $x^{-2}$ times a derivative and the flux vanishes at $x = 0$ and $x = \infty$ for regular solutions.
One often writes it in terms of the Compton parameter $y$ with $dy = \frac{k_B T_e}{m_e c^2} n_e \sigma_T c \, dt$.
