---
tag: P270MSQ0SZ
kind: definition
name: Admissibility condition for wavelets
msc: [42C40, 42A38]
defines: 2BBB8NY5ZA
uses: [SASP14MA1Z, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_wavelet_transform
---

## Definition

Let $\psi \in L^2(\R)$ (see [[Lp space|SASP14MA1Z]]), and let $\hat\psi(\xi) = \int_\R \psi(t) e^{-2\pi i t \xi} \, dt$ be its [[Fourier transform|DPVM34ADZV]].
The function $\psi$ satisfies the *admissibility condition*, and is called an *admissible wavelet*, if
$$C_\psi = \int_\R \frac{\abs{\hat\psi(\xi)}^2}{\abs{\xi}} \, d\xi < \infty.$$

## Remarks

If $\psi$ is also in $L^1(\R)$, then $\hat\psi$ is continuous, and admissibility implies $\hat\psi(0) = \int_\R \psi(t) \, dt = 0$.
Conversely, if $\int_\R (1 + \abs{t}) \abs{\psi(t)} \, dt < \infty$ and $\int_\R \psi = 0$, then $\hat\psi$ is Lipschitz with $\hat\psi(0) = 0$, and $\psi$ is admissible.
The constant $C_\psi$ is the factor in Calderón's identity for the continuous wavelet transform.

Example: the Mexican hat $\psi(t) = (1 - t^2) e^{-t^2/2}$ is admissible.
It decays fast and $\int_\R \psi = \int_\R e^{-t^2/2} \, dt - \int_\R t^2 e^{-t^2/2} \, dt = \sqrt{2\pi} - \sqrt{2\pi} = 0$, so the converse criterion applies.

Non-example: the Gaussian $\psi(t) = e^{-\pi t^2}$ has $\hat\psi(\xi) = e^{-\pi \xi^2}$.
Near $\xi = 0$ the integrand behaves like $1/\abs{\xi}$, which is not integrable, so $C_\psi = \infty$.
