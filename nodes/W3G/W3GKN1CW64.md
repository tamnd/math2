---
tag: W3GKN1CW64
kind: definition
name: Plateau–Rayleigh instability
msc: ["76E17", 76B45]
defines: XGPK6NW3B2
uses: [Z9TBETJAP6, H028A17Z55]
sources:
  - url: https://en.wikipedia.org/wiki/Plateau–Rayleigh_instability
---

## Definition

Consider an infinitely long cylinder of inviscid incompressible liquid with radius $R$, density $\rho$ and surface tension $\sigma > 0$, at rest and without gravity.
Its surface is in equilibrium, with the pressure jump $\sigma / R$ of the [[Young–Laplace equation|Z9TBETJAP6]].
Perturb the surface to the axisymmetric shape $r = R + \varepsilon(t) \cos kz$, with wavenumber $k > 0$, and linearise the Euler equations with the Young–Laplace condition at the surface.
The *Plateau–Rayleigh instability* is the exponential growth in time of such a mode, $\varepsilon(t) \propto e^{st}$ with $s > 0$.

## Remarks

The linear modes satisfy Rayleigh's dispersion relation
$$s^2 = \frac{\sigma}{\rho R^3} \, kR \left( 1 - k^2 R^2 \right) \frac{I_1(kR)}{I_0(kR)},$$
where $I_0$ and $I_1$ are modified Bessel functions of the first kind.
So a mode is unstable exactly when $kR < 1$, that is, when its wavelength $2\pi / k$ exceeds the circumference $2\pi R$.
The growth rate is largest at $kR \approx 0.697$, a wavelength of about $9.02 R$, which sets the typical spacing of the drops.

Example: for $kR = 1/2$, the perturbed column with the same volume has smaller surface area than the straight one, and $s^2 > 0$.
Non-example: for $kR = 2$, the wavelength $\pi R$ is shorter than the circumference, the area increases, and $s^2 < 0$, so the mode oscillates as a capillary wave on the jet.
