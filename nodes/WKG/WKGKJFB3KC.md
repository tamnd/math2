---
tag: WKGKJFB3KC
kind: example
name: Dipole antenna radiation
msc: [78A50, 78A40]
illustrates: [AC6R5A3M1C, TVH1J6B1G9]
uses: [AC6R5A3M1C, TVH1J6B1G9, K0NV8SE4QV]
sources:
  - url: https://en.wikipedia.org/wiki/Dipole_antenna
---

## Example

Take a thin, straight, centre-fed wire along the $z$-axis from $z = -\lambda/4$ to $z = \lambda/4$, the *half-wave dipole*, in vacuum.
Assume the standard sinusoidal current $I(z) = I_0 \cos(kz)$ with time factor $e^{-i\omega t}$, where $k = 2\pi/\lambda = \omega/c$.
Treat the wire as a sum of [[Hertzian dipoles|K0NV8SE4QV]] and keep only the terms of order $1/r$.
Use spherical coordinates with distance $r$ and polar angle $\theta$.
In the [[far field|TVH1J6B1G9]] the electric field is along $\hat{\boldsymbol{\theta}}$ with
$$\abs{E_\theta} = \frac{\eta_0 I_0}{2\pi r} \left| \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \right|,$$
where $\eta_0 = \sqrt{\mu_0/\varepsilon_0} \approx 377\ \Omega$ is the impedance of free space.
Check: the factor comes from $\int_{-\lambda/4}^{\lambda/4} \cos(kz) \, e^{-ikz\cos\theta} \, dz = \dfrac{2\cos\left(\frac{\pi}{2}\cos\theta\right)}{k \sin^2\theta}$, multiplied by the Hertzian far-field factor $\sin\theta$.
The pattern vanishes along the wire ($\theta = 0, \pi$) and is largest in the plane $\theta = \pi/2$.
Integrating the power flux over a large sphere gives a radiation resistance of about $73\ \Omega$.
The directivity is about $1.64$, slightly more than the value $1.5$ of a Hertzian dipole.

## Explanations

### L1 human

A half-wave dipole is two metal rods, each a quarter wavelength long, fed in the middle, like old television "rabbit ears".
Charges rush back and forth along the rods and throw off [[electromagnetic radiation|AC6R5A3M1C]].
The radiation is shaped like a doughnut around the wire: strongest sideways, zero off the ends.
Its input resistance of about $73\ \Omega$ is close to the impedance of common cables, which is one reason this antenna is so popular.
