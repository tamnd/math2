---
tag: YRFN9GKZ80
kind: definition
name: Helioseismology
msc: [85A15, 76Q05]
defines: YFK8GRFF0Z
uses: [QW9QPV0HHG, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Helioseismology
---

## Definition

Model the Sun as a self-gravitating, rotating fluid sphere with sound speed $c(r)$, density $\rho(r)$ and angular velocity $\Omega(r, \theta)$.
Here $r$ is the radius and $\theta$ the colatitude.
Its global oscillations are [[pulsation modes|QW9QPV0HHG]] with frequencies $\nu_{n\ell m}$.
They are labelled by a radial order $n$ and by the degree $\ell$ and azimuthal order $m$ of a [[spherical harmonic|3F32Y21HP4]] $Y_\ell^m$.
*Helioseismology* is the determination of $c$, $\rho$, $\Omega$ and related quantities inside the Sun from the observed frequencies $\nu_{n\ell m}$ and other properties of these oscillations.

## Remarks

Example: the splitting $\nu_{n\ell m} - \nu_{n\ell 0}$ of a multiplet is to first order $m / (2\pi)$ times an integral of $\Omega(r, \theta)$ against a kernel concentrated in the region sampled by the mode.
Inverting many splittings gives the internal rotation profile.
Non-example: inferring the interior of the Sun only from its luminosity and radius through a stellar model is not helioseismology, because no oscillation data enter.
For high radial order $n$ and low degree $\ell$, the p-mode frequencies follow the asymptotic relation $\nu_{n\ell} \approx \Delta\nu \, (n + \ell/2 + \varepsilon)$.
Here $\Delta\nu = \big(2 \int_0^R dr / c(r)\big)^{-1}$ is the large separation, $R$ is the solar radius and $\varepsilon$ is a constant of order $1$.
Local helioseismology studies wave travel times and local wave fields instead of global mode frequencies.
