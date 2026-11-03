---
tag: Z68Y2VSGVM
kind: definition
name: Lomb–Scargle periodogram
msc: [62M15, 85A04]
defines: EJM2Z7PE30
uses: [3ZYM0HXA3E, 0BYTQ4X1HC, EA3MF4VTEH]
sources:
  - url: https://en.wikipedia.org/wiki/Least-squares_spectral_analysis
---

## Definition

Let $(t_j, y_j)$, $j = 1, \dots, N$, be observations of a real [[time series|EA3MF4VTEH]] at times $t_j \in \R$.
Let $\bar y$ be the mean of the $y_j$.
For an angular frequency $\omega > 0$, choose $\tau \in \R$ with $\sum_{j} \sin\big(2\omega(t_j - \tau)\big) = 0$.
Write $c_j = \cos\omega(t_j - \tau)$ and $s_j = \sin\omega(t_j - \tau)$.
Assume $\sum_j c_j^2 > 0$ and $\sum_j s_j^2 > 0$.
The *Lomb–Scargle periodogram* at $\omega$ is
$$P(\omega) = \frac{1}{2}\left[\frac{\big(\sum_j (y_j - \bar y)\, c_j\big)^2}{\sum_j c_j^2} + \frac{\big(\sum_j (y_j - \bar y)\, s_j\big)^2}{\sum_j s_j^2}\right].$$

## Remarks

The condition on $\tau$ is $\tan(2\omega\tau) = \sum_j \sin 2\omega t_j / \sum_j \cos 2\omega t_j$, and it makes $\sum_j c_j s_j = 0$.
So the two columns $(c_j)$ and $(s_j)$ are orthogonal.
Then $2P(\omega)$ is the drop in the residual sum of squares when $y_j - \bar y \approx a c_j + b s_j$ is fitted by [[least squares|0BYTQ4X1HC]].
$P(\omega)$ does not change when all $t_j$ are shifted by the same amount.
Example: for $y_j = \cos(\omega_0 t_j)$ at many well-spread times, $P$ has a sharp peak near $\omega = \omega_0$.
Non-example: the squared modulus of the discrete Fourier transform of unevenly sampled data is not the Lomb–Scargle periodogram; it lacks the shift $\tau$ and the normalisations.
For evenly spaced $t_j$ and Fourier frequencies, $P$ agrees with the classical [[periodogram|3ZYM0HXA3E]] up to a constant factor.
Many texts divide $P$ by the sample variance of the $y_j$.
