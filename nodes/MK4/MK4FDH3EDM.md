---
tag: MK4FDH3EDM
kind: definition
name: Dickey–Fuller test
msc: [62M07, 62M10, 91B84]
defines: 26E0HYRDS8
uses: [2JC96FMGA1, KTDVZP4DF2, 087P03NEND, YM708KHV2W, 22735FGJV6, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Dickey%E2%80%93Fuller_test
---

## Definition

Let $y_0, y_1, \dots, y_n$ follow the [[autoregressive model|2JC96FMGA1]] $y_t = \rho y_{t-1} + u_t$.
Here the $u_t$ are independent and identically distributed with mean $0$ and variance $\sigma^2 > 0$.
Write it as $\Delta y_t = \delta y_{t-1} + u_t$ with $\Delta y_t = y_t - y_{t-1}$ and $\delta = \rho - 1$.
Let $\hat\delta$ be the [[ordinary least squares|YM708KHV2W]] estimate of $\delta$ in the regression of $\Delta y_t$ on $y_{t-1}$.
Let $\operatorname{se}(\hat\delta)$ be its usual standard error, and let $\tau = \hat\delta / \operatorname{se}(\hat\delta)$.
The *Dickey–Fuller test* is the [[test|087P03NEND]], based on $\tau$, of
$$H_0 \colon \delta = 0 \ (\text{a unit root}) \qquad \text{against} \qquad H_1 \colon \delta < 0 \ (\text{stationarity}).$$
It rejects $H_0$ when $\tau$ is below a critical value of the Dickey–Fuller distribution.

## Remarks

Under $H_0$, the series $y_t$ is a [[random walk|04VZE3FZXF]], an [[ARIMA($0$, $1$, $0$) process|KTDVZP4DF2]], and the usual central limit theory fails.
If $y_0 = 0$, then as $n \to \infty$
$$\tau \to \frac{W(1)^2 - 1}{2 \left( \int_0^1 W(r)^2 \, dr \right)^{1/2}}$$
in distribution, where $W$ is a standard [[Wiener process|22735FGJV6]].
This limit is skewed to the left, so its critical values lie well below those of the standard normal distribution; they are tabulated.
Variants add a constant, or a constant and a linear trend, to the regression, and each variant has its own limiting distribution and critical values.
The *augmented* Dickey–Fuller test adds lagged differences $\Delta y_{t-1}, \dots, \Delta y_{t-k}$ to the regression, to allow for autocorrelated errors.

Example: for a series with $\hat\delta = -0.2$ and $\operatorname{se}(\hat\delta) = 0.05$, the statistic is $\tau = -4$.
This lies far in the left tail of the Dickey–Fuller distribution, so the unit root hypothesis is rejected at the usual levels.

Non-example: comparing $\tau$ with the critical values of the Student $t$ distribution is not the Dickey–Fuller test.
That rule rejects a true unit root far too often, because the null distribution of $\tau$ is not a $t$ distribution.
