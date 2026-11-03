---
tag: ZEG4M5MQQH
kind: definition
name: Ocean wave spectrum
msc: [86A05, 76B15, 62M15]
defines: GYQCDP4VN8
uses: [DT0QXJE705, DPVM34ADZV, R9WC0Z7Z69, R5P8M6SBG7]
sources:
  - url: https://en.wikipedia.org/wiki/Sea_state
---

## Definition

Let $\eta(t)$ be the elevation of the sea surface above its mean level at a fixed point, at time $t$.
Assume that $\eta$ is a real [[stationary random process|DT0QXJE705]] with mean $0$ and autocovariance $R(\tau) = E[\eta(t) \eta(t + \tau)]$, and that $R$ is integrable.
The *(frequency) wave spectrum* is the one-sided spectral density
$$S(\omega) = \frac{1}{\pi} \int_{-\infty}^{\infty} R(\tau) \, e^{-i \omega \tau} \, d\tau, \qquad \omega \ge 0.$$
It satisfies $S(\omega) \ge 0$ and
$$E[\eta^2] = R(0) = \int_0^\infty S(\omega) \, d\omega.$$
The *directional spectrum* $F(\omega, \theta) \ge 0$ also resolves the direction of propagation $\theta$, with $\int_0^{2\pi} F(\omega, \theta) \, d\theta = S(\omega)$.

## Remarks

Example: the process $\eta(t) = a \cos(\omega_0 t + \phi)$, with $a > 0$ and a phase $\phi$ uniform on $[0, 2\pi)$, is stationary with $R(\tau) = \tfrac12 a^2 \cos(\omega_0 \tau)$.
Its spectrum is $S(\omega) = \tfrac12 a^2 \, \delta(\omega - \omega_0)$, a point mass, and the variance is $\tfrac12 a^2$, as for a single sinusoid.
Here $R$ is not integrable, so the spectrum is a measure rather than a function; a real sea has a spread of frequencies.

Non-example: a sea that is growing under a rising wind has a variance $E[\eta(t)^2]$ that increases with $t$, so $\eta$ is not stationary and has no time-independent spectrum.
In practice the spectrum is estimated over records of 20 to 30 minutes, during which the sea is close to stationary.

The moments $m_j = \int_0^\infty \omega^j S(\omega) \, d\omega$ give standard sea-state parameters, such as the significant wave height $H_s \approx 4 \sqrt{m_0}$.
In linear wave theory each frequency belongs to a [[water wave|R9WC0Z7Z69]] whose wavenumber is fixed by the [[dispersion relation|R5P8M6SBG7]], $\omega^2 = g k$ in deep water, so $S$ also gives the wavenumber spectrum.
The definition uses the [[Fourier transform|DPVM34ADZV]] of the autocovariance (the Wiener–Khinchin theorem).
