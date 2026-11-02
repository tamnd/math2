---
tag: 5FM1TC4FG4
kind: definition
name: Spectral density estimation
msc: [62M15, 62G07]
defines: TTH1V4SWY6
uses: [DT0QXJE705, 3ZYM0HXA3E, YCZHYY8VE5, B1HNX0YT0Z]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_density_estimation
---

## Definition

Let $(X_t)_{t \in \Z}$ be a real weakly [[stationary process|DT0QXJE705]] with autocovariance $\gamma$ satisfying $\sum_{h} \abs{\gamma(h)} < \infty$.
Its *spectral density* is
$$f(\omega) = \frac{1}{2\pi} \sum_{h \in \Z} \gamma(h) e^{-i h \omega}, \qquad \omega \in [-\pi, \pi],$$
so that $\gamma(h) = \int_{-\pi}^{\pi} e^{i h \omega} f(\omega) \, d\omega$.
*Spectral density estimation* is the construction of estimators $\hat f_n(\omega)$ of $f(\omega)$ from observations $X_1, \dots, X_n$.
Such an estimator is a function of the data that should be close to $f$ for large $n$.

## Remarks

Nonparametric estimators smooth the [[periodogram|3ZYM0HXA3E]] $I_n$.
Let $\hat\gamma$ be the sample autocovariance, defined with the [[autocorrelation function|YCZHYY8VE5]].
Let $w$ be a weight function with $w(0) = 1$, and let $r = r_n$ be a truncation point.
A lag-window estimator has the form
$$\hat f_n(\omega) = \frac{1}{2\pi} \sum_{\abs{h} \le r} w(h / r) \, \hat\gamma(h) e^{-i h \omega}.$$
Under standard conditions, such as $r_n \to \infty$ and $r_n / n \to 0$, it is consistent.
Averaging periodograms of several segments of the data, as in the methods of Bartlett and Welch, is another common choice.

Parametric estimators fit an [[ARMA model|B1HNX0YT0Z]] and use its spectral density $\frac{\sigma^2}{2\pi} \abs{\theta(e^{-i\omega})}^2 / \abs{\phi(e^{-i\omega})}^2$.

Example: for a white noise with variance $\sigma^2$, the spectral density is the constant $\sigma^2 / (2\pi)$, and the averaged estimate $\frac{1}{2\pi} \cdot \frac{1}{m} \sum_j I_n(\omega_j)$ over $m$ Fourier frequencies near $\omega$ estimates it.

The rescaled periodogram $I_n(\omega) / (2\pi)$ is the simplest estimator, but it is not consistent.
Under standard conditions, for $0 < \abs{\omega} < \pi$, it is asymptotically unbiased while its variance tends to $f(\omega)^2$ rather than to $0$.
