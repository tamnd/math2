---
tag: BBNT588JY9
kind: definition
name: Radiative heat transfer in participating media
msc: [80A21, 85A25, 78A40]
defines: FYYQNDT6X2
uses: [S6XR2K4N8G, A2RMYX8A65, 1Y36434YTE, 2TNXJANSF9]
sources:
  - url: https://en.wikipedia.org/wiki/Radiative_transfer
---

## Definition

Let a medium fill a region $D \subseteq \R^3$.
Let $I_\lambda(x, s)$ be the spectral intensity (radiance) of [[thermal radiation|S6XR2K4N8G]] at the point $x \in D$ in the unit direction $s$, at wavelength $\lambda$.
Let $\kappa_\lambda(x) \ge 0$ be the absorption coefficient and $\sigma_{s\lambda}(x) \ge 0$ the scattering coefficient.
Let $I_{b\lambda}(T(x))$ be the [[black-body|A2RMYX8A65]] spectral intensity at the local temperature $T(x)$.
Let $\Phi_\lambda(s', s) \ge 0$ be the scattering phase function, normalised so that its average over all $s'$ is $1$.
The medium is *participating* if $\kappa_\lambda$ or $\sigma_{s\lambda}$ is not zero.
*Radiative heat transfer in the participating medium* is the transport of radiation governed by the radiative transfer equation:
$$s \cdot \nabla_x I_\lambda = \kappa_\lambda I_{b\lambda} - (\kappa_\lambda + \sigma_{s\lambda}) I_\lambda + \frac{\sigma_{s\lambda}}{4\pi} \int_{S^2} I_\lambda(x, s') \, \Phi_\lambda(s', s) \, d\Omega'.$$
It yields the radiative [[heat flux|1Y36434YTE]] $q_r(x) = \int_0^\infty \int_{S^2} I_\lambda(x, s) \, s \, d\Omega \, d\lambda$.

## Remarks

The terms on the right are emission, attenuation by absorption and out-scattering, and in-scattering from other directions.
The extinction coefficient is $\beta_\lambda = \kappa_\lambda + \sigma_{s\lambda}$, and the optical thickness of a path of length $\ell$ is $\int_0^\ell \beta_\lambda \, ds$.

Example: a cold, purely absorbing medium with constant $\kappa_\lambda$, where emission and scattering are negligible.
The equation along a ray becomes $dI_\lambda/ds = -\kappa_\lambda I_\lambda$, so $I_\lambda(\ell) = I_\lambda(0) e^{-\kappa_\lambda \ell}$, which is the [[Beer–Lambert law|2TNXJANSF9]].

Non-example: dry air at ordinary temperatures.
Its nitrogen and oxygen hardly absorb or scatter thermal radiation, so $\kappa_\lambda$ and $\sigma_{s\lambda}$ are practically zero, and only surface-to-surface exchange matters.

The energy equation of the medium contains the source term $-\nabla \cdot q_r$.
