---
tag: M435YDQWQ4
kind: definition
name: Bessel potential
msc: [31B15, "46E35", 47G40]
defines: V2HG4GN7TN
uses: [DPVM34ADZV, 2Z29JN3VES, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_potential
---

## Definition

Let $n \ge 1$ and $\alpha > 0$.
Use the [[Fourier transform|DPVM34ADZV]] $\hat g(\xi) = \int_{\R^n} g(x) e^{-2\pi i x \cdot \xi} \, dx$.
Let $G_\alpha$ be the integrable function on $\R^n$ whose Fourier transform is
$$\widehat{G_\alpha}(\xi) = (1 + 4 \pi^2 \abs{\xi}^2)^{-\alpha/2}.$$
For $f \in L^p(\R^n)$ with $1 \le p \le \infty$, the *Bessel potential* of order $\alpha$ of $f$ is the [[convolution|2Z29JN3VES]]
$$J_\alpha f = G_\alpha * f.$$

## Remarks

The kernel $G_\alpha$ exists, is positive, and has integral $\widehat{G_\alpha}(0) = 1$.
So $J_\alpha$ is a bounded operator on each $L^p$ with norm at most $1$, by Young's inequality.
On Schwartz functions $J_\alpha = (I - \Delta)^{-\alpha/2}$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]], since $-\Delta$ has symbol $4 \pi^2 \abs{\xi}^2$.
The semigroup law $J_\alpha J_\beta = J_{\alpha + \beta}$ holds for all $\alpha, \beta > 0$.
Near $0$, $G_\alpha(x)$ is comparable to $\abs{x}^{\alpha - n}$ when $0 < \alpha < n$, and $G_\alpha(x)$ decays like $e^{-c\abs{x}}$ for some $c > 0$ as $\abs{x} \to \infty$.

Example: for $n = 1$ and $\alpha = 2$, the kernel is $G_2(x) = \frac12 e^{-\abs{x}}$.
Check: $\int_{\R} \frac12 e^{-\abs{x}} e^{-2\pi i x \xi} \, dx = \frac12 \cdot \frac{2}{1 + 4\pi^2 \xi^2} = (1 + 4\pi^2 \xi^2)^{-1}$.
So $u = J_2 f$ solves $u - u'' = f$ for nice $f$.

Non-example: the kernel $\abs{x}^{\alpha - n}$ of the Riesz potential is not the Bessel kernel, since it is not integrable on $\R^n$, while $G_\alpha$ must be integrable with integral $1$.
