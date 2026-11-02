---
tag: X6GEZGZ8HQ
kind: definition
name: Fourier–Bessel series
msc: [42C10, 33C10]
defines: 34VJ4T7ZSB
uses: [SNJC87TBHD, EAV97QH9DF, SASP14MA1Z, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Bessel_series
---

## Definition

Let $\nu > -1$ and let $J_\nu$ be the [[Bessel function of the first kind|CZCMRDWDYW]] of order $\nu$, a solution of [[Bessel's equation|EAV97QH9DF]].
Let $0 < j_{\nu,1} < j_{\nu,2} < \cdots$ be the positive zeros of $J_\nu$.
Let $f$ be a measurable function on $(0, 1)$ with $\int_0^1 x \abs{f(x)}^2 \, dx < \infty$.
The *Fourier–Bessel series* of $f$ of order $\nu$ is
$$\sum_{k=1}^{\infty} c_k \, J_\nu(j_{\nu,k} x), \qquad c_k = \frac{2}{J_{\nu+1}(j_{\nu,k})^2} \int_0^1 x \, f(x) \, J_\nu(j_{\nu,k} x) \, dx.$$

## Remarks

The functions $J_\nu(j_{\nu,k} x)$ are orthogonal in the weighted [[Lebesgue space|SASP14MA1Z]] $L^2((0, 1), x \, dx)$, with
$$\int_0^1 x \, J_\nu(j_{\nu,k} x) \, J_\nu(j_{\nu,m} x) \, dx = \frac{\delta_{km}}{2} J_{\nu+1}(j_{\nu,k})^2.$$
So the series is the [[generalized Fourier series|SNJC87TBHD]] of $f$ with respect to this orthogonal family, and the formula for $c_k$ is the usual quotient of inner products.
The family is complete in $L^2((0, 1), x \, dx)$, so the series converges to $f$ in this space.
On an interval $[0, b]$ one uses $J_\nu(j_{\nu,k} x / b)$ instead.

Example: $\nu = 0$ and $f = 1$.
Since $\frac{d}{dt}\big(t J_1(t)\big) = t J_0(t)$, the substitution $t = j x$ gives $\int_0^1 x J_0(jx) \, dx = J_1(j)/j$.
Hence $c_k = \frac{2}{j_{0,k} J_1(j_{0,k})}$ and
$$1 = \sum_{k=1}^{\infty} \frac{2}{j_{0,k} \, J_1(j_{0,k})} \, J_0(j_{0,k} x) \quad \text{in } L^2((0,1), x\,dx).$$

Non-example: the functions $J_0(k\pi x)$, $k = 1, 2, \dots$, do not give a Fourier–Bessel series.
The numbers $k\pi$ are not zeros of $J_0$; for instance $J_0(\pi) \approx -0.304 \ne 0$.
