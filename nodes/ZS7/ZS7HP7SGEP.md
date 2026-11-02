---
tag: ZS7HP7SGEP
kind: definition
name: Inverse Fourier transform
msc: [42B10, 42A38]
defines: JB8QMT8DCH
uses: [DPVM34ADZV, X7GTF3D98F, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_inversion_theorem
---

## Definition

Let $n \ge 1$ and let $g \colon \R^n \to \C$ be a Lebesgue [[integrable function|X7GTF3D98F]].
The *inverse Fourier transform* of $g$ is the function $\check g \colon \R^n \to \C$ given by the [[Lebesgue integral|DWJF7ABPR1]]
$$\check g(x) = \int_{\R^n} g(\xi) \, e^{2\pi i \, x \cdot \xi} \, d\xi, \qquad x \in \R^n,$$
where $x \cdot \xi = x_1 \xi_1 + \cdots + x_n \xi_n$.
It is also written $\mathcal{F}^{-1} g$.

## Remarks

This matches the convention $\hat f(\xi) = \int f(x) e^{-2\pi i x \cdot \xi} \, dx$ for the [[Fourier transform|DPVM34ADZV]].
So $\check g(x) = \hat g(-x)$, and $\check g$ is continuous, bounded by $\int \abs{g}$, and tends to $0$ at infinity.
With the convention $\hat f(\xi) = \int f(x) e^{-i x \cdot \xi} \, dx$ the inverse transform carries the factor $(2\pi)^{-n}$.

Example: for $n = 1$ and $g = \mathbf{1}_{[-1/2, 1/2]}$,
$$\check g(x) = \int_{-1/2}^{1/2} e^{2\pi i x \xi} \, d\xi = \frac{\sin(\pi x)}{\pi x} \quad (x \ne 0), \qquad \check g(0) = 1.$$

Non-example: the constant function $g = 1$ on $\R$ is not integrable, and the integral $\int_\R e^{2\pi i x \xi} \, d\xi$ diverges for every $x$.
Its inverse Fourier transform exists only in the sense of tempered distributions, where it is the Dirac delta at $0$.

The name is justified by the [[Fourier inversion theorem|T4Z8YQZKZV]]: if $f$ and $\hat f$ are integrable, then $(\hat f)^\vee = f$ almost everywhere.
