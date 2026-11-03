---
tag: 4V7X2RMT4B
kind: definition
name: Silk damping
msc: [85A40]
defines: A0TAWJYRBQ
uses: [EH021K5438, J70F32P86W, SJY21N1SNZ]
sources:
  - url: https://en.wikipedia.org/wiki/Diffusion_damping
---

## Definition

Before [[recombination|EH021K5438]], let $n_e$ be the density of free electrons, $\sigma_T$ the Thomson cross-section and $\lambda = 1/(n_e \sigma_T)$ the mean free path of a photon.
Let $a$ be the [[scale factor|J70F32P86W]] and $\eta$ the conformal time, $d\eta = c \, dt / a$.
Consider a perturbation of the photon-baryon fluid with comoving wavenumber $k$.
Define the damping wavenumber $k_D$, with the integral running up to the time of decoupling, by
$$k_D^{-2} \sim \int \frac{d \eta}{6 \, a \, n_e \sigma_T}.$$
*Silk damping* is the suppression by photon diffusion of the amplitude of the perturbation by a factor of about $e^{-k^2 / k_D^2}$.
Perturbations with $k \ll k_D$ are almost unaffected, and perturbations with $k \gg k_D$ are erased.

## Remarks

The integral says that the comoving damping length $1/k_D$ is of the order of a geometric mean.
It is the mean of the comoving mean free path and the comoving distance light travels, which is the length of a random walk.
Precise treatments add factors that depend on the baryon-to-photon density ratio and on polarisation.

Example: in the [[CMB angular power spectrum|SJY21N1SNZ]], the acoustic peaks above $\ell$ of roughly $1000$ have strongly decreasing heights; this damping tail is Silk damping.

Non-example: the drop of fluctuations on scales larger than the horizon is not Silk damping; photons cannot diffuse over such scales, and the factor $e^{-k^2/k_D^2}$ is then close to $1$.
