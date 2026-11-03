---
tag: ZKF5C5ST8H
kind: definition
name: Moyal product
msc: [53D55, 81S30]
defines: J3A8CFHZZM
uses: [2S0MXDT4YH, RFNGJ09WDR, 3MKSJ1J04K]
sources:
  - url: https://en.wikipedia.org/wiki/Moyal_product
---

## Definition

Let $n \ge 1$ and let $\hbar$ be a formal parameter.
Write points of $\R^{2n}$ as $(x, p)$ with $x, p \in \R^n$.
Let $f, g$ be smooth functions on $\R^{2n}$.
Their *Moyal product* is the formal power series
$$(f \star g)(x, p) = \left[ \exp\!\left( \frac{i\hbar}{2} \sum_{j=1}^n \left( \frac{\partial}{\partial x_j}\frac{\partial}{\partial p'_j} - \frac{\partial}{\partial p_j}\frac{\partial}{\partial x'_j} \right) \right) f(x, p)\, g(x', p') \right]_{x' = x,\ p' = p}.$$
The exponential is expanded as its power series.
So the coefficient of $\hbar^k$ is a bidifferential operator of order $k$ in each argument.

## Remarks

The first terms are $f \star g = fg + \frac{i\hbar}{2}\{f, g\} + O(\hbar^2)$, where $\{\cdot, \cdot\}$ is the [[Poisson bracket|2S0MXDT4YH]].
The product is associative, and $f \star g - g \star f = i\hbar \{f, g\} + O(\hbar^3)$.
If $f$ or $g$ is a polynomial, the series stops after finitely many terms, and then $\hbar$ can be given a numerical value.
For Schwartz functions and a positive number $\hbar$, an integral formula defines a product $f \star g$ with $\mathrm{Op}^w(f \star g) = \mathrm{Op}^w(f)\, \mathrm{Op}^w(g)$.
Here $\mathrm{Op}^w$ is the [[Weyl quantization|RFNGJ09WDR]], and the series above is the asymptotic expansion of this product as $\hbar \to 0$.

Example: for $n = 1$, $x \star p = xp + \frac{i\hbar}{2}$ and $p \star x = xp - \frac{i\hbar}{2}$, since all derivatives of order $2$ vanish.
So $x \star p - p \star x = i\hbar$, which matches $[X, P] = i\hbar$.

Non-example: the ordinary pointwise product $fg$ is the term of order $0$ only; it is commutative, so it does not reproduce the commutator $x \star p - p \star x = i\hbar$.

The Moyal product is a star product in the sense of [[deformation quantization|3MKSJ1J04K]] for the standard Poisson structure on $\R^{2n}$.
