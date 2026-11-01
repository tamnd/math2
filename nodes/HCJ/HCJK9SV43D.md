---
tag: HCJK9SV43D
kind: definition
name: Hilbert transform
msc: [44A15, 42A50, 30H10]
defines: NSCEBXM7ZM
uses: [0SYR10HD4R, 050F2FMTKF]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_transform
---

## Definition

Let $1 \le p < \infty$ and let $f \in L^p(\R)$, a function in the $L^p$ space of $\R$.
The *Hilbert transform* of $f$ is the function
$$Hf(x) = \frac{1}{\pi}\, \lim_{\varepsilon \to 0^+} \int_{\abs{x - y} > \varepsilon} \frac{f(y)}{x - y}\, dy,$$
the [[Cauchy principal value|0SYR10HD4R]] of $\frac{1}{\pi} \int_\R \frac{f(y)}{x - y}\, dy$.
The limit exists for almost every $x \in \R$.

## Remarks

Example: for $f(x) = \frac{1}{1 + x^2}$, one has $Hf(x) = \frac{x}{1 + x^2}$.
Check: $F(z) = \frac{i}{z + i}$ is holomorphic on the upper half-plane and tends to $0$ at infinity.
On $\R$ it equals $\frac{1}{1 + x^2} + i \frac{x}{1 + x^2}$, so its imaginary part is the [[harmonic conjugate|050F2FMTKF]] of its real part.

Non-example: the integral is singular at $y = x$, so the principal value is needed.
The integral $\int_\R \frac{f(y)}{x - y}\, dy$ diverges absolutely at every $x$ near which $f$ is continuous and nonzero.

On the Fourier transform side, $\widehat{Hf}(\xi) = -i \sgn(\xi)\, \hat f(\xi)$ for $f \in L^2(\R)$.
Hence $H$ is an isometry of $L^2(\R)$ with $H^2 = -\id$.
For $1 < p < \infty$, $H$ is a bounded operator on $L^p(\R)$, a theorem of Marcel Riesz; for $p = 1$ it is only of weak type $(1, 1)$.
