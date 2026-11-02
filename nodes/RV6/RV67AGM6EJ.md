---
tag: RV67AGM6EJ
kind: definition
name: Multidimensional Mellin transform
msc: [44A30, 44A15]
defines: 92JY94ZJD8
uses: [N5PVGRJE1T, 4PVP1C3JZG]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Definition

Let $n \ge 1$ and let $f \colon (0, \infty)^n \to \C$ be locally integrable.
For $s = (s_1, \dots, s_n) \in \C^n$ and $x \in (0, \infty)^n$ write $x^{s - 1} = x_1^{s_1 - 1} \cdots x_n^{s_n - 1}$.
The *$n$-dimensional Mellin transform* of $f$ is the function
$$(\mathcal{M} f)(s) = \int_{(0, \infty)^n} x^{s - 1} f(x)\, dx,$$
defined at those $s \in \C^n$ where the integral converges absolutely.

## Remarks

For $n = 1$ this is the [[Mellin transform|N5PVGRJE1T]].
Absolute convergence at $s$ depends only on $(\operatorname{Re} s_1, \dots, \operatorname{Re} s_n)$, and the set of such real parts is convex.

Example: $f(x) = e^{-x_1 - \cdots - x_n}$.
The integral splits into a product, and $(\mathcal{M} f)(s) = \Gamma(s_1) \cdots \Gamma(s_n)$ for $\operatorname{Re} s_j > 0$, by the [[gamma function|0H5SYBSED9]] integral.

Non-example: $f = 1$ has no Mellin transform.
For every $s$, the factor $\int_0^\infty x_1^{\operatorname{Re} s_1 - 1}\, dx_1$ diverges, at $0$ or at $\infty$.
