---
tag: 2P4RDS0A6X
kind: concept
name: List of integral transforms
msc: [44A05, 44A15, 44A20]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_transforms
---

## Summary

Each [[integral transform|YCK709QB06]] has the form $(Tf)(u) = \int_{t_1}^{t_2} f(t)\, K(t, u)\, dt$, and it is fixed by its [[kernel|9M0NNNFJGM]] and its interval of integration.
The table below lists common transforms with one standard normalisation; books differ in constants and signs.

| Transform | Kernel $K(t, u)$ | Interval |
|---|---|---|
| [[Laplace transform|0V49JEZW06]] | $e^{-ut}$ | $(0, \infty)$ |
| [[Two-sided Laplace transform|6J2AGD0BYY]] | $e^{-ut}$ | $(-\infty, \infty)$ |
| [[Fourier transform|DPVM34ADZV]] | $e^{-2\pi i u t}$ | $(-\infty, \infty)$ |
| [[Mellin transform|N5PVGRJE1T]] | $t^{u - 1}$ | $(0, \infty)$ |
| [[Hankel transform|2P9YWDGKC4]] | $t\, J_\nu(ut)$ | $(0, \infty)$ |
| [[Stieltjes transform|RG1HFAYD98]] | $1/(u + t)$ | $(0, \infty)$ |
| [[Hilbert transform|NSCEBXM7ZM]] | $\frac{1}{\pi}\frac{1}{u - t}$ (principal value) | $(-\infty, \infty)$ |
| [[Weierstrass transform|5HYB6DDZH8]] | $\frac{1}{\sqrt{4\pi}} e^{-(u - t)^2/4}$ | $(-\infty, \infty)$ |
| [[Hartley transform|WEHYECYAVJ]] | $\frac{1}{\sqrt{2\pi}}(\cos ut + \sin ut)$ | $(-\infty, \infty)$ |

Here $J_\nu$ is the Bessel function of the first kind of order $\nu$.
Some transforms do not fit this one-line form.
The [[Radon transform|VJNZJ352PC]] integrates over lines, and the [[Abel transform|QMW1MWQH6J]] has a variable domain of integration.

## Explanations

### L1 human

All these transforms follow one recipe: multiply $f$ by a kernel and integrate.
What changes is the kernel and the range of integration.
Exponential kernels suit differential equations, power kernels $t^{u-1}$ suit problems with scaling, and Bessel kernels suit problems with circular symmetry.
For example, the Mellin transform of $e^{-t}$ is the gamma function $\Gamma(u)$.
