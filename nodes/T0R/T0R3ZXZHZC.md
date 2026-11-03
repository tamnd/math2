---
tag: T0R3ZXZHZC
kind: definition
name: Nonlinear optics
msc: [78A60]
defines: SZA12YB8V2
uses: [ASQAH710WN, YZ7Q9DP8RT, 604T74VWDK, 0MZB06ST2B]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_optics
---

## Definition

Consider a medium in which an [[electric field|YZ7Q9DP8RT]] $\mathbf{E}$ induces a [[polarization density|ASQAH710WN]] $\mathbf{P}$, as part of the [[constitutive relations|604T74VWDK]].
The medium responds *linearly* when $\mathbf{P}$ is a linear function of $\mathbf{E}$, and *nonlinearly* otherwise.
*Nonlinear optics* is the study of the propagation of light in media that respond nonlinearly.
In the usual setting, the response is a [[power series|0MZB06ST2B]] in the field:
$$P_i = \varepsilon_0 \Big( \sum_j \chi^{(1)}_{ij} E_j + \sum_{j,k} \chi^{(2)}_{ijk} E_j E_k + \sum_{j,k,l} \chi^{(3)}_{ijkl} E_j E_k E_l + \cdots \Big).$$
Here $\varepsilon_0$ is the vacuum permittivity, and the terms of order at least $2$ are the nonlinear part.

## Remarks

The power series is valid when the field is weak compared with the fields that bind electrons in atoms, so that each term is much smaller than the one before.
This is why nonlinear effects need intense light.

Example: if $\chi^{(2)} \ne 0$ and $\mathbf{E}$ oscillates at frequency $\omega$, the term $\chi^{(2)} E^2$ oscillates at $0$ and at $2\omega$.
The medium then radiates light at $2\omega$, which is second-harmonic generation.

Non-example: in vacuum $\mathbf{P} = 0$ for every field in classical electrodynamics, so Maxwell's equations are linear and there is no nonlinear optics.
