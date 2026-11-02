---
tag: A1X6T9ZD9E
kind: definition
name: Fourier transform as Laplace transform on the imaginary axis
msc: [44A10, 42A38]
defines: J7Z1H328BC
uses: [6J2AGD0BYY, DPVM34ADZV, X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
---

## Definition

Let $f \colon \R \to \C$ be measurable.
Its two-sided Laplace transform is $\mathcal{B}f(s) = \int_{\R} f(x) e^{-sx} \, dx$, for $s \in \C$ at which $x \mapsto f(x) e^{-sx}$ is [[integrable|X7GTF3D98F]].
Let $\sigma \in \R$ be such that $x \mapsto e^{-\sigma x} f(x)$ is integrable.
The *restriction of $\mathcal{B}f$ to the line $\operatorname{Re} s = \sigma$* is the function $\xi \mapsto \mathcal{B}f(\sigma + 2\pi i \xi)$ on $\R$.
For $\sigma = 0$, that is, for $f$ integrable, this is the restriction of $\mathcal{B}f$ to the imaginary axis, and it equals the [[Fourier transform|DPVM34ADZV]]:
$$\hat f(\xi) = \int_{\R} f(x) e^{-2\pi i x \xi} \, dx = \mathcal{B}f(2\pi i \xi), \qquad \xi \in \R.$$

## Remarks

In general $\mathcal{B}f(\sigma + 2\pi i \xi) = \widehat{f_\sigma}(\xi)$ with $f_\sigma(x) = e^{-\sigma x} f(x)$, by writing $e^{-(\sigma + 2\pi i \xi) x} = e^{-\sigma x} e^{-2\pi i x \xi}$.
Example: $f(x) = e^{-\abs{x}}$ is integrable, and $\mathcal{B}f(s) = \frac{1}{1 + s} + \frac{1}{1 - s} = \frac{2}{1 - s^2}$ for $\abs{\operatorname{Re} s} < 1$.
At $s = 2\pi i \xi$ this gives $\hat f(\xi) = 2/(1 + 4\pi^2 \xi^2)$, the known Fourier transform of $e^{-\abs{x}}$.
Non-example: $f(x) = e^{x}$ for $x \ge 0$ and $f(x) = 0$ for $x < 0$ is not integrable, so the imaginary axis is not in its region of convergence.
Here $\mathcal{B}f(s) = 1/(s - 1)$ for $\operatorname{Re} s > 1$, and this function is not the Fourier transform of $f$, which does not exist as an integral.
With the convention $\int f(x) e^{-i \omega x} \, dx$, the same relation reads $\hat f(\omega) = \mathcal{B}f(i\omega)$.
