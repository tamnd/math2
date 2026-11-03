---
tag: DAG32VT3VA
kind: definition
name: Wiener filter
msc: [60G35, 62M20, "93E11"]
defines: K1GQXRY0K9
uses: [DT0QXJE705, 05NZ1HHQMV, DPVM34ADZV, QYY4NMDY5H]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_filter
---

## Definition

Let $s(t)$ and $x(t)$, $t \in \R$, be real, jointly wide-sense [[stationary processes|DT0QXJE705]] with mean $0$; $s$ is the signal and $x$ the observation.
Let $R_{xx}(\tau) = \mathbb{E}[x(t + \tau) x(t)]$ and $R_{sx}(\tau) = \mathbb{E}[s(t + \tau) x(t)]$, and let $S_{xx}$ and $S_{sx}$ be their [[Fourier transforms|DPVM34ADZV]], assumed to exist, with $S_{xx}(\omega) > 0$ for all $\omega$.
For an integrable impulse response $h$, the filtered estimate is $\hat s(t) = \int_{\R} h(\tau)\, x(t - \tau)\, d\tau$.

1. The *non-causal Wiener filter* is the $h$ that minimizes the [[mean squared error|05NZ1HHQMV]] $\mathbb{E}[(s(t) - \hat s(t))^2]$ over all such $h$, when a minimizer exists. Its frequency response is $H(\omega) = S_{sx}(\omega) / S_{xx}(\omega)$.
2. The *causal Wiener filter* is the $h$ that minimizes the same error over all $h$ with $h(\tau) = 0$ for $\tau < 0$. It solves the [[Wiener–Hopf equation|QYY4NMDY5H]] $R_{sx}(\sigma) = \int_0^\infty h(\tau) R_{xx}(\sigma - \tau)\, d\tau$ for $\sigma \ge 0$.

## Remarks

The error is stationary, so it does not depend on $t$.
The optimal $h$ is characterized by the orthogonality principle: the error $s(t) - \hat s(t)$ is uncorrelated with every observation $x(t - \sigma)$ that the filter may use.
Example: let $x = s + n$ with $n$ a noise uncorrelated with $s$, with spectral densities $S_{ss}$ and $S_{nn}$.
Then $S_{sx} = S_{ss}$ and $S_{xx} = S_{ss} + S_{nn}$, so the non-causal filter is $H = S_{ss}/(S_{ss} + S_{nn})$, which lies between $0$ and $1$ at each frequency.
Non-example: the identity filter $H = 1$, which outputs $x$ itself, is not the Wiener filter unless $S_{nn} = 0$, since it leaves all the noise in the estimate.
The causal filter is found by spectral factorization of $S_{xx}$.
