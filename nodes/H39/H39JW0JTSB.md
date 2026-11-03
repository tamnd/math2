---
tag: H39JW0JTSB
kind: definition
name: Elsasser number
msc: [76W05, 76U05, 86A25]
defines: P8TR5P8BVC
uses: [T8JWCBK9M6, 6HZRX3WSQD, T3R5FWV91P]
sources:
  - url: https://en.wikipedia.org/wiki/Elsasser_number
---

## Definition

Consider an electrically conducting fluid of density $\rho$ and electrical conductivity $\sigma$, rotating with angular speed $\Omega$, in a magnetic field of typical strength $B$.
The *Elsasser number* is
$$\Lambda = \frac{\sigma B^2}{\rho \, \Omega}.$$

## Remarks

With the magnetic diffusivity $\eta = 1/(\mu_0 \sigma)$, where $\mu_0$ is the vacuum permeability, the same number is $\Lambda = B^2/(\mu_0 \rho \, \eta \, \Omega)$.
A flow of speed $U$ induces currents of order $\sigma U B$ and so a Lorentz force of order $\sigma U B^2$ per unit volume.
The [[Coriolis force|6HZRX3WSQD]] per unit volume is of order $\rho \Omega U$.
So $\Lambda$ estimates the ratio of the two forces, and the speed $U$ cancels.
Some authors use $2\Omega$ in place of $\Omega$.
Example: for the Earth's core, $\sigma \approx 10^6$ S/m, $\rho \approx 10^4$ kg/m³, $\Omega \approx 7.3 \times 10^{-5}$ s⁻¹ and $B \approx 2 \times 10^{-3}$ T give $\Lambda \approx 5$, of order one.
It is one of the [[dimensionless numbers of fluid mechanics|T3R5FWV91P]] used in rotating [[magnetohydrodynamics|T8JWCBK9M6]].
