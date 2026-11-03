---
tag: K0NV8SE4QV
kind: example
name: Hertzian dipole
msc: [78A40, 78A50]
illustrates: [AC6R5A3M1C, TVH1J6B1G9]
uses: [AC6R5A3M1C, TVH1J6B1G9, 8PEMR2J7EF, 9Q1NE5EP37]
sources:
  - url: https://en.wikipedia.org/wiki/Dipole_antenna
---

## Example

A *Hertzian dipole* is a current element in vacuum, with time factor $e^{-i\omega t}$.
Its current has constant complex amplitude $I_0$ and flows along the $z$-axis over a length $\ell$ much smaller than the wavelength $\lambda$.
Let $k = \omega/c = 2\pi/\lambda$ and $\eta_0 = \sqrt{\mu_0/\varepsilon_0}$.
Its retarded [[vector potential|8PEMR2J7EF]] is $\mathbf{A} = \dfrac{\mu_0 I_0 \ell}{4\pi} \dfrac{e^{ikr}}{r} \hat{\mathbf{z}}$, and $\mathbf{H} = \mu_0^{-1} \nabla \times \mathbf{A}$ gives, in spherical coordinates $(r, \theta, \varphi)$,
$$H_\varphi = \frac{I_0 \ell \sin\theta}{4\pi} \, e^{ikr} \left( \frac{1}{r^2} - \frac{ik}{r} \right).$$
Check: $\nabla \times (g \hat{\mathbf{z}}) = -g'(r) \sin\theta \, \hat{\boldsymbol{\varphi}}$ for a radial function $g$, and $\dfrac{d}{dr} \dfrac{e^{ikr}}{r} = e^{ikr}\left(\dfrac{ik}{r} - \dfrac{1}{r^2}\right)$.
For $kr \ll 1$ the $1/r^2$ term dominates: this is the [[near field|TVH1J6B1G9]], which looks like the static Biot–Savart field of the current element.
For $kr \gg 1$ the $1/r$ term dominates, and the radiated field is $E_\theta = \eta_0 H_\varphi \approx -\dfrac{i \eta_0 k I_0 \ell \sin\theta}{4\pi r} e^{ikr}$.
The time-averaged radiated power is
$$P = \frac{\eta_0 k^2 \abs{I_0}^2 \ell^2}{12\pi},$$
obtained by integrating $\abs{E_\theta}^2/(2\eta_0)$ over a sphere with $\int \sin^2\theta \, d\Omega = 8\pi/3$.
Writing $P = \frac{1}{2} R \abs{I_0}^2$ gives the radiation resistance $R = \dfrac{2\pi \eta_0}{3} \left(\dfrac{\ell}{\lambda}\right)^2 \approx 789 \left(\dfrac{\ell}{\lambda}\right)^2 \Omega$.

## Explanations

### L1 human

The Hertzian dipole is the simplest possible antenna: a tiny piece of wire carrying an oscillating current.
Close to it, the field looks like the magnetic field of an ordinary current and mostly sloshes energy back and forth.
Far from it, the field becomes a wave that carries energy away, falling off like $1/r$ and shaped like a doughnut around the wire.
Every real antenna can be built up as a sum of such tiny pieces, which is why this example comes first in antenna theory.
