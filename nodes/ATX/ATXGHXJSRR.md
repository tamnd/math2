---
tag: ATXGHXJSRR
kind: definition
name: Whittle likelihood
msc: [62M15, 62M10]
defines: W0B5CQVV8V
uses: [DT0QXJE705, 3ZYM0HXA3E, TTH1V4SWY6, 0VW9E4QXR6, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Whittle_likelihood
---

## Definition

Let $x_1, \dots, x_n$ be observations of a weakly [[stationary process|DT0QXJE705]] with mean $0$.
Let $\set{f_\theta : \theta \in \Theta}$ be a parametric family of spectral densities on $[-\pi, \pi]$, with $f_\theta > 0$.
Let $I(\omega) = \frac{1}{2\pi n} \abs{\sum_{t=1}^n x_t e^{-i t \omega}}^2$ be the [[periodogram|3ZYM0HXA3E]], scaled to estimate the spectral density, and let $\omega_j = 2\pi j / n$ for $j = 1, \dots, m$ with $m = \floor{(n-1)/2}$.
The *Whittle log-likelihood* is
$$\ell_W(\theta) = -\sum_{j=1}^{m} \left( \log f_\theta(\omega_j) + \frac{I(\omega_j)}{f_\theta(\omega_j)} \right).$$
The *Whittle estimator* is a maximizer $\hat\theta$ of $\ell_W$ over $\Theta$.

## Remarks

The idea is that, for a Gaussian process with smooth spectral density, the values $I(\omega_j)$ are approximately independent and exponentially distributed with means $f_\theta(\omega_j)$.
The log [[likelihood|0VW9E4QXR6]] of independent exponential variables with these means is exactly $\ell_W(\theta)$.
A version with an integral, $-\frac{n}{4\pi} \int_{-\pi}^{\pi} \left( \log f_\theta(\omega) + I(\omega) / f_\theta(\omega) \right) d\omega$, is also common.
Under standard conditions the Whittle estimator is consistent and asymptotically normal with the same limit as the Gaussian [[maximum likelihood|0FREPFKNS7]] estimator.

Example: for white noise, $f_\theta(\omega) = \theta / (2\pi)$ with $\theta = \sigma^2 > 0$.
Setting the derivative of $\ell_W(\theta) = -\sum_j \left( \log \frac{\theta}{2\pi} + \frac{2\pi I(\omega_j)}{\theta} \right)$ to zero gives $m/\theta = 2\pi \sum_j I(\omega_j) / \theta^2$, so $\hat\theta = \frac{2\pi}{m} \sum_{j=1}^{m} I(\omega_j)$.

Non-example: let $\Gamma_n = [\gamma_\theta(s - t)]_{s,t=1}^n$ be the covariance matrix of the data.
The exact Gaussian log-likelihood $-\frac12 \log \det \Gamma_n - \frac12 x^T \Gamma_n^{-1} x$, up to a constant, is not the Whittle likelihood.
The Whittle likelihood approximates it by treating $\Gamma_n$ as if it were diagonal in the Fourier basis.
