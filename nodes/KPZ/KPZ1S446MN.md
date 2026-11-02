---
tag: KPZ1S446MN
kind: definition
name: Mellin transform
msc: [44A15, 44A05]
defines: N5PVGRJE1T
uses: [SGZZ4Y0D36, DWJF7ABPR1, 0RNGDMHT7M]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Definition

Let $f \colon (0, \infty) \to \C$ be measurable and let $s \in \C$.
For $x > 0$, let $x^{s-1} = e^{(s-1)\log x}$ be the [[complex power|0RNGDMHT7M]] with the real logarithm.
Assume that $f$ is [[Mellin convergent|SGZZ4Y0D36]] at $s$, that is, $x \mapsto x^{s-1} f(x)$ is integrable on $(0, \infty)$.
The *Mellin transform* of $f$ at $s$ is the [[Lebesgue integral|DWJF7ABPR1]]
$$\mathcal{M}f(s) = \int_0^\infty x^{s-1} f(x) \, dx.$$
As a function, $\mathcal{M}f$ is defined on the set of $s$ at which $f$ is Mellin convergent.

## Remarks

Since $\abs{x^{s-1}} = x^{\operatorname{Re} s - 1}$, this set depends only on $\operatorname{Re} s$ and is a union of vertical lines; it is a vertical strip, possibly empty or degenerate.
Example: $f(x) = e^{-x}$.
Near $0$, $\abs{x^{s-1} e^{-x}} \le x^{\operatorname{Re} s - 1}$, which is integrable on $(0, 1)$ when $\operatorname{Re} s > 0$; near $\infty$, the factor $e^{-x}$ beats every power.
So $\mathcal{M}f(s) = \Gamma(s)$ for $\operatorname{Re} s > 0$, the [[gamma function|0H5SYBSED9]].
Non-example: $f(x) = 1$.
Integrability of $x^{\operatorname{Re} s - 1}$ on $(0, 1)$ needs $\operatorname{Re} s > 0$, and on $(1, \infty)$ it needs $\operatorname{Re} s < 0$, so $f$ is Mellin convergent at no $s$.
Other notations are $\tilde f(s)$, $F(s)$ and $\set{\mathcal{M} f}(s)$.
Some authors call the open strip of convergence the fundamental strip and write it $\langle \alpha, \beta \rangle$.
