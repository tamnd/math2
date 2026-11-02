---
tag: 2R4H0RFQZZ
kind: definition
name: Bochner–Riesz means
msc: [42B08, 42B15]
defines: AFS2DCWCD3
uses: [DPVM34ADZV, CG9JEATW3Q, RAGR38Q40B]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%E2%80%93Riesz_mean
    locator: Definition
---

## Definition

Let $n \ge 1$, let $\delta \ge 0$ and let $R > 0$.
Let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi} \, dx$ be the [[Fourier transform|DPVM34ADZV]] of a [[Schwartz function|CG9JEATW3Q]] $f$ on $\R^n$, and let $t_+ = \max(t, 0)$, with the convention $t_+^0 = \mathbf{1}_{t > 0}$.
The *Bochner–Riesz mean* of order $\delta$ and radius $R$ of $f$ is
$$S^\delta_R f(x) = \int_{\R^n} \Big(1 - \frac{\abs{\xi}^2}{R^2}\Big)_+^\delta \hat f(\xi) \, e^{2\pi i x \cdot \xi} \, d\xi.$$
The operator $S^\delta = S^\delta_1$ is the Bochner–Riesz operator of order $\delta$.

## Remarks

Example: for $\delta = 0$, $S^0_R f$ is the spherical partial sum, the inverse Fourier transform of $\hat f$ restricted to the open ball of radius $R$.
For $n = 1$ and $\delta = 1$, the multiplier is $(1 - \xi^2/R^2)_+$, which is a continuous function with compact support.

The multiplier of $S^\delta_R$ is the dilate of the multiplier of $S^\delta$ by $R$, and dilations do not change $L^p$ operator norms.
So $S^\delta_R$ is bounded on $L^p(\R^n)$ uniformly in $R$ if and only if $(1 - \abs{\xi}^2)_+^\delta$ is an [[$L^p$ multiplier|RAGR38Q40B]].
In that case, $S^\delta_R f \to f$ in $L^p(\R^n)$ as $R \to \infty$ for every $f \in L^p(\R^n)$, $1 \le p < \infty$.

Non-example of convergence: for $\delta = 0$, $n \ge 2$ and $p \ne 2$, the ball multiplier is not an $L^p$ multiplier, by [[Fefferman's ball multiplier theorem|4A5MJY4XPV]].

For $\delta > (n - 1)/2$, the kernel of $S^\delta$ is integrable, so $S^\delta$ is bounded on $L^p(\R^n)$ for all $1 \le p \le \infty$.
The value $(n - 1)/2$ is the critical index.
