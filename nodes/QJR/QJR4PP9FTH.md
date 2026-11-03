---
tag: QJR4PP9FTH
kind: definition
name: Optical transfer function
msc: [78A10, 94A08, 42B10]
defines: Z7S3Z4KGRS
uses: [HHWESQD7QB, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_transfer_function
---

## Definition

Let an incoherent imaging system be linear and shift invariant on intensities, with [[point spread function|HHWESQD7QB]] $h \colon \R^2 \to [0, \infty)$.
Assume that $h$ is integrable and that $\int_{\R^2} h(x) \, dx > 0$.
The *optical transfer function* of the system is the function $H \colon \R^2 \to \C$ given by
$$H(\nu) = \frac{\int_{\R^2} h(x) \, e^{-2\pi i \, \nu \cdot x} \, dx}{\int_{\R^2} h(x) \, dx},$$
where $\nu \in \R^2$ is a spatial frequency.
Its modulus $\abs{H}$ is the *modulation transfer function*, and its argument $\arg H$ is the *phase transfer function*.

## Remarks

So $H$ is the [[Fourier transform|DPVM34ADZV]] of $h$, scaled so that $H(0) = 1$.
Since $h \ge 0$, one has $\abs{H(\nu)} \le H(0) = 1$, and since $h$ is real, $H(-\nu) = \overline{H(\nu)}$.
If the object intensity is $f$, the image intensity is $h * f$, so the spectrum of the image is the spectrum of $f$ times $H$, up to the constant factor $\int h$.

Example: the Gaussian blur $h(x) = e^{-\pi \abs{x}^2}$ has $\int h = 1$ and Fourier transform $e^{-\pi \abs{\nu}^2}$.
So $H(\nu) = e^{-\pi \abs{\nu}^2}$, which is real and positive, and the phase transfer function is $0$.

Non-example: the constant function $h = 1$ is not integrable on $\R^2$, so the formula does not define an optical transfer function.

For an aberration-free system, $H$ is the autocorrelation of the pupil function, in scaled coordinates, normalised to $1$ at the origin.
