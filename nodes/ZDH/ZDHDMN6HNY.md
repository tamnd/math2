---
tag: ZDHDMN6HNY
kind: definition
name: Kolmogorov microscales
msc: [76F05, 76F02]
defines: NYRS1BJKRQ
uses: [VY307F8Z0S, NM5Q4845Z4, JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_microscales
---

## Definition

Consider a [[turbulent|VY307F8Z0S]] flow of an incompressible fluid with kinematic [[viscosity|NM5Q4845Z4]] $\nu > 0$.
Let $\varepsilon > 0$ be the mean rate of dissipation of kinetic energy per unit mass.
The *Kolmogorov microscales* are the length, time and velocity scales
$$\eta = \left( \frac{\nu^3}{\varepsilon} \right)^{1/4}, \qquad \tau_\eta = \left( \frac{\nu}{\varepsilon} \right)^{1/2}, \qquad u_\eta = (\nu \varepsilon)^{1/4}.$$

## Remarks

They are the unique combinations of $\nu$, with units $\mathrm{m^2/s}$, and $\varepsilon$, with units $\mathrm{m^2/s^3}$, with units of length, time and velocity.
They satisfy $\eta = u_\eta \tau_\eta$ and $u_\eta \eta / \nu = 1$, so the [[Reynolds number|JH9EJ0HA0R]] of the smallest eddies is $1$, the balance of inertia and viscosity.
If $L$ is the size of the large eddies and $u$ their speed, with $\varepsilon \sim u^3 / L$, then $L / \eta \sim \mathrm{Re}^{3/4}$ with $\mathrm{Re} = u L / \nu$.
So a full simulation in three dimensions needs of the order of $\mathrm{Re}^{9/4}$ grid points.

Example: in air with $\nu = 1.5 \times 10^{-5}\ \mathrm{m^2/s}$ and $\varepsilon = 1\ \mathrm{m^2/s^3}$, one gets $\eta \approx 0.24\ \mathrm{mm}$, $\tau_\eta \approx 3.9\ \mathrm{ms}$ and $u_\eta \approx 6.2\ \mathrm{cm/s}$; indeed $0.24\ \mathrm{mm} / 3.9\ \mathrm{ms} \approx 6.2\ \mathrm{cm/s}$.
Non-example: the quantity $(\nu / \varepsilon)^{1/4}$ is not a microscale; it has units $\mathrm{s^{1/2}}$, neither a length nor a time.
