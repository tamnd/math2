---
tag: KE4HEWEG38
kind: definition
name: Periodogram
msc: [62M15]
defines: 3ZYM0HXA3E
uses: [EA3MF4VTEH, TST0GH66A5, YCZHYY8VE5]
sources:
  - url: https://en.wikipedia.org/wiki/Periodogram
---

## Definition

Let $x_1, \dots, x_n$ be observations of a real [[time series|EA3MF4VTEH]].
The *periodogram* of the data is the function
$$I_n(\omega) = \frac{1}{n} \abs{\sum_{t=1}^{n} x_t e^{-i t \omega}}^2, \qquad \omega \in [-\pi, \pi].$$
It is usually evaluated at the *Fourier frequencies* $\omega_j = 2\pi j / n$ with $-\pi < \omega_j \le \pi$, where it equals $\frac1n \abs{\hat x_j}^2$ for the [[discrete Fourier transform|TST0GH66A5]] $\hat x_j = \sum_{t=1}^n x_t e^{-2\pi i j t / n}$.

## Remarks

Some authors divide by $2\pi n$ instead of $n$, so that the periodogram estimates the spectral density $f(\omega) = \frac{1}{2\pi} \sum_h \gamma(h) e^{-i h \omega}$ directly.
At every Fourier frequency $\omega_j \ne 0$, the periodogram equals $\sum_{\abs{h} < n} \hat\gamma(h) e^{-i h \omega_j}$, where $\hat\gamma$ is the sample autocovariance from the [[autocorrelation function|YCZHYY8VE5]].
So the periodogram is the Fourier transform of the sample autocovariance.

Example: let $n = 12$ and $x_t = \cos(2\pi t / 4)$, a cycle of period $4$, so the frequency is $\omega_3 = 2\pi \cdot 3/12$.
Writing $\cos u = (e^{iu} + e^{-iu})/2$ and using $\sum_{t=1}^{12} e^{2\pi i k t / 12} = 0$ for $k \not\equiv 0 \pmod{12}$, one gets $\sum_t x_t e^{-i t \omega_3} = 12/2 = 6$.
Hence $I_{12}(\omega_3) = 36/12 = 3$, while $I_{12}(\omega_j) = 0$ at all other Fourier frequencies in $[0, \pi]$.

Non-example: the function $\omega \mapsto \abs{\sum_t x_t e^{-it\omega}}$ without the square is not the periodogram; it is the amplitude spectrum of the data, and its square divided by $n$ is the periodogram.

For a stationary process with summable autocovariances, $E[I_n(\omega)] \to 2\pi f(\omega)$ for $\omega \ne 0$.
But the variance of $I_n(\omega)$ does not tend to $0$, so the periodogram is not a consistent estimator of the spectral density.
