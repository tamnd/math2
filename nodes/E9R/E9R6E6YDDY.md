---
tag: E9R6E6YDDY
kind: definition
name: Matter power spectrum
msc: [85A40, 60G60]
defines: FWRHZ27J6Q
uses: [DT0QXJE705, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Matter_power_spectrum
---

## Definition

Let $\rho(x)$ be the matter density at the comoving position $x \in \R^3$ at a fixed time, and let $\bar\rho$ be its mean.
The density contrast is $\delta(x) = (\rho(x) - \bar\rho)/\bar\rho$.
Assume that $\delta$ is a statistically homogeneous and isotropic random field of mean $0$.
That is, its law is invariant under translations and rotations, so it is a [[stationary|DT0QXJE705]] field in space.
Let $\xi(r) = \langle \delta(x) \, \delta(x + r) \rangle$ be its two-point correlation function, where $\langle \cdot \rangle$ is the ensemble average; it depends only on $\abs{r}$.
The *matter power spectrum* is the [[Fourier transform|DPVM34ADZV]] of $\xi$:
$$P(k) = \int_{\R^3} \xi(r) \, e^{-i k \cdot r} \, d^3 r .$$
By isotropy, $P$ depends only on $k = \abs{k}$.

## Remarks

With the convention $\tilde\delta(k) = \int \delta(x) e^{-i k \cdot x} \, d^3x$, the same quantity appears in $\langle \tilde\delta(k) \, \tilde\delta(k')^{*} \rangle = (2\pi)^3 \delta_D(k - k') \, P(k)$, where $\delta_D$ is the Dirac delta.
The dimensionless power spectrum is $\Delta^2(k) = k^3 P(k) / (2\pi^2)$, and the variance of the field is $\langle \delta^2 \rangle = \xi(0) = \int_0^\infty \Delta^2(k) \, dk/k$.
The variance of $\delta$ smoothed with a window of radius $R$ is $\sigma_R^2 = \int_0^\infty \Delta^2(k) \, \abs{W(kR)}^2 \, dk / k$, where $W$ is the Fourier transform of the window.

Example: if $\xi(r) = A e^{-r^2/(2R^2)}$ with $A > 0$, the Gaussian integral gives $P(k) = A (2\pi)^{3/2} R^3 e^{-k^2 R^2/2}$, which is finite, non-negative and depends only on $k$.

Non-example: a density field with a fixed large-scale gradient, $\langle \delta(x) \rangle = g \cdot x$ with $g \ne 0$, is not statistically homogeneous.
Its correlations depend on the position $x$ and not only on the separation $r$, so it has no power spectrum in this sense.
