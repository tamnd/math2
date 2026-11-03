---
tag: TVXX3W8GMD
kind: definition
name: Seismic anisotropy
msc: [86A15, "74E10", 74J05]
defines: XXB2TQX6KW
uses: [NMDDYDXT0V, EK3A1GMMFM, 6W00ZECYT0, 80737NDZ4V]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_anisotropy
---

## Definition

Let a homogeneous [[linearly elastic|6W00ZECYT0]] medium have density $\rho > 0$ and stiffness tensor $c_{ijkl}$.
For a unit vector $n$, let $\lambda_1, \lambda_2, \lambda_3$ be the eigenvalues of the matrix $\Gamma_{ik}(n) = c_{ijkl} n_j n_l$.
By the [[Christoffel equation|EK3A1GMMFM]], plane waves travelling in the direction $n$ have the speeds $v = \sqrt{\lambda_k / \rho}$.
The medium shows *seismic anisotropy* if at least one of these speeds depends on $n$.
This is [[elastic anisotropy|NMDDYDXT0V]] as seen by waves.

## Remarks

Example: a transversely isotropic medium with vertical symmetry axis has five independent stiffnesses $C_{11}, C_{33}, C_{44}, C_{66}, C_{13}$ in Voigt notation.
Its P-speed is $\sqrt{C_{33}/\rho}$ along the axis and $\sqrt{C_{11}/\rho}$ across it, so it is anisotropic whenever $C_{11} \ne C_{33}$.
Thomsen's parameters $\varepsilon = (C_{11} - C_{33})/(2C_{33})$, $\gamma = (C_{66} - C_{44})/(2C_{44})$ and $\delta = \big((C_{13} + C_{44})^2 - (C_{33} - C_{44})^2\big)/\big(2C_{33}(C_{33} - C_{44})\big)$ measure the anisotropy; all vanish for an isotropic medium.
Non-example: an isotropic medium has $c_{ijkl} = \lambda\delta_{ij}\delta_{kl} + \mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$ with [[Lamé parameters|80737NDZ4V]] $\lambda, \mu$.
Then $\Gamma = (\lambda + \mu) n n^T + \mu I$, whose eigenvalues $\lambda + 2\mu$, $\mu$, $\mu$ do not depend on $n$, so it shows no anisotropy.
Non-example: speed that changes from place to place, but not with direction, is heterogeneity, not anisotropy.
