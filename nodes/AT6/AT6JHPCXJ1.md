---
tag: AT6JHPCXJ1
kind: definition
name: Riesz potential
msc: [31B15, 47G40, 26A33]
defines: 1V2N8MFSHC
uses: [0H5SYBSED9, 2Z29JN3VES, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
---

## Definition

Let $n \ge 1$ and $0 < \alpha < n$.
Let $\Gamma$ be the [[gamma function|0H5SYBSED9]] and let
$$c_\alpha = \pi^{n/2} \, 2^\alpha \, \frac{\Gamma(\alpha/2)}{\Gamma((n - \alpha)/2)}.$$
For a measurable function $f$ on $\R^n$, the *Riesz potential* of order $\alpha$ of $f$ is
$$I_\alpha f(x) = \frac{1}{c_\alpha} \int_{\R^n} \frac{f(y)}{\abs{x - y}^{n - \alpha}} \, dy,$$
at each $x \in \R^n$ where the integral converges absolutely.

## Remarks

So $I_\alpha f$ is the [[convolution|2Z29JN3VES]] of $f$ with the kernel $\abs{x}^{\alpha - n} / c_\alpha$.
If $f \in L^p(\R^n)$ with $1 \le p < n/\alpha$, the integral converges absolutely for almost every $x$.
With the [[Fourier transform|DPVM34ADZV]] $\hat f(\xi) = \int f(x) e^{-2\pi i x \cdot \xi} \, dx$, the constant $c_\alpha$ is chosen so that $\widehat{I_\alpha f}(\xi) = (2\pi \abs{\xi})^{-\alpha} \hat f(\xi)$ for Schwartz functions $f$, that is, $I_\alpha = (-\Delta)^{-\alpha/2}$.
The semigroup law $I_\alpha I_\beta = I_{\alpha + \beta}$ holds for $\alpha + \beta < n$.

Example: for $n \ge 3$ and $\alpha = 2$, one has $c_2 = 4 \pi^{n/2} / \Gamma(n/2 - 1) = (n - 2) \sigma_{n-1}$, where $\sigma_{n-1} = 2 \pi^{n/2} / \Gamma(n/2)$ is the area of the unit sphere.
Indeed $\Gamma(n/2) = (n/2 - 1) \Gamma(n/2 - 1)$, so $(n - 2) \cdot 2 \pi^{n/2} / \Gamma(n/2) = 4 \pi^{n/2} / \Gamma(n/2 - 1)$.
So $I_2 f(x) = \frac{1}{(n-2) \sigma_{n-1}} \int f(y) \abs{x - y}^{2-n} \, dy$, and $-\Delta I_2 f = f$ for smooth $f$ with compact support.

Non-example: the constant function $f = 1$ has no Riesz potential.
For every $x$ the integral $\int \abs{x - y}^{\alpha - n} \, dy$ diverges, since $\abs{y}^{\alpha - n}$ is not integrable at infinity when $\alpha > 0$.
