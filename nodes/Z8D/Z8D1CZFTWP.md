---
tag: Z8D1CZFTWP
kind: statement
role: theorem
name: Euler integral for the gamma function
msc: [33B15, 30D30]
uses: [0V3FZMVB4K, 0F9VKJPWCA, 0NAHXR1FRH, 0YBVKMYX0W]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $H = \set{s \in \C : \operatorname{Re} s > 0}$, and for $t > 0$ let $t^{s-1} = e^{(s-1)\ln t}$.

1. For every $s \in H$ the integral $\int_0^\infty t^{s-1} e^{-t} \, dt$ converges [[absolutely|0F9VKJPWCA]].
2. The function $G(s) = \int_0^\infty t^{s-1} e^{-t} \, dt$ is [[holomorphic|0NAHXR1FRH]] on $H$.
3. For real $s > 0$, $G(s) = \Gamma(s)$, where $\Gamma$ is the [[gamma function|0V3FZMVB4K]].

So $G$ is the unique holomorphic extension of $\Gamma$ from $(0, \infty)$ to $H$, and $\Gamma(s) = G(s)$ for all $s \in H$.

## Remarks

Absolute convergence follows from $\abs{t^{s-1} e^{-t}} = t^{\sigma - 1} e^{-t}$ with $\sigma = \operatorname{Re} s > 0$, which is the real integrand.
For holomorphy, the truncated integrals $\int_{1/n}^{n}$ are entire in $s$ and converge to $G$ uniformly on each strip $a \le \operatorname{Re} s \le b$ with $0 < a < b$, so the limit is holomorphic.
Uniqueness comes from the [[identity theorem|0YBVKMYX0W]], since $(0, \infty)$ has accumulation points in the connected set $H$.
The integral diverges at $t = 0$ when $\operatorname{Re} s \le 0$; the extension of $\Gamma$ beyond $H$ uses the functional equation $\Gamma(s + 1) = s\,\Gamma(s)$ instead.
In Mathlib the statement is `Complex.Gamma_eq_integral`.

## Explanations

### L1 human

Euler's integral is the most common formula for the gamma function.
It works not only for positive real numbers but for every complex number with positive real part.
For example, at $s = 1$ it gives $\int_0^\infty e^{-t}\,dt = 1 = \Gamma(1)$.

### L2 human

The integral is the gamma function's Mellin transform description: $\Gamma(s)$ is the Mellin transform of $e^{-t}$.
Many identities, such as the formula linking the [[beta function|QHNWVSC6AQ]] with $\Gamma$, start from this integral and a change of variables.
The integral alone only defines $\Gamma$ on the right half-plane; the [[meromorphic|0NSD1TPHR0]] extension to $\C$ comes from the functional equation.
