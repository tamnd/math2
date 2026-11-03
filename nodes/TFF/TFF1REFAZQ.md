---
tag: TFF1REFAZQ
kind: definition
name: Constitutive relations of electromagnetism
msc: [78A25, 78A48, 35Q61]
defines: 604T74VWDK
uses: [9BWWD4QK8Y, NJVXQZ780B, ASQAH710WN, A2WZA4QA3V, F768YN0P2V, 5MJQ5J5H8Z]
sources:
  - url: https://en.wikipedia.org/wiki/Constitutive_equation
---

## Definition

Let a material fill a region of space, with electric field $E$ and magnetic field $B$.
Let $P$ be its [[polarization density|ASQAH710WN]] and $M$ its [[magnetization|A2WZA4QA3V]], and let $\varepsilon_0, \mu_0 > 0$ be the vacuum permittivity and permeability.
The auxiliary fields are the [[electric displacement field|NJVXQZ780B]] and the magnetizing field
$$D = \varepsilon_0 E + P, \qquad H = \frac{1}{\mu_0} B - M.$$
The *constitutive relations* of the material are equations that determine $D$ and $H$ as functions or functionals of $E$ and $B$.
When the material conducts, they also determine the free current density $J_f$ in this way.

## Remarks

With constitutive relations, the macroscopic [[Maxwell's equations|9BWWD4QK8Y]]
$$\nabla \cdot D = \rho_f, \quad \nabla \cdot B = 0, \quad \nabla \times E = -\partial_t B, \quad \nabla \times H = J_f + \partial_t D$$
become a closed system for $E$ and $B$ given the free charge density $\rho_f$ and any external currents.

Example: a linear, isotropic, non-dispersive material has
$$D = \varepsilon E, \qquad B = \mu H, \qquad J_f = \sigma E,$$
with constants $\varepsilon$, the [[permittivity|F768YN0P2V]], $\mu$, the [[permeability|5MJQ5J5H8Z]], and $\sigma$, the conductivity; the last relation is Ohm's law.
Vacuum is the case $\varepsilon = \varepsilon_0$, $\mu = \mu_0$, $\sigma = 0$.

More general cases: in an anisotropic crystal $\varepsilon$ and $\mu$ are $3 \times 3$ matrices.
In a dispersive medium the relations are convolutions in time, $D(t) = \varepsilon_0 E(t) + \varepsilon_0 \int_0^\infty \chi(s) E(t - s) \, ds$, equivalently multiplications by frequency-dependent constants after a Fourier transform.
In nonlinear optics $P$ contains terms of degree two or more in $E$.

Non-example: Gauss's law $\nabla \cdot D = \rho_f$ relates $D$ to the charges, not to $E$ and $B$, and it holds in every material, so it is not a constitutive relation.
