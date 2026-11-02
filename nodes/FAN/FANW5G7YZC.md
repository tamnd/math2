---
tag: FANW5G7YZC
kind: definition
name: Square-integrable kernel
msc: [45P05, 47G10]
defines: WWMWX7AD4V
uses: [GSMBXT7FPK, YYNCJSR0PJ, DWJF7ABPR1, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_integral_operator
---

## Definition

Let $a < b$.
A *square-integrable kernel* on $[a, b]$ is a [[kernel|GSMBXT7FPK]] $K \colon [a, b] \times [a, b] \to \C$ that is Lebesgue [[measurable|YYNCJSR0PJ]] and satisfies
$$\norm{K}_{2} = \left( \int_a^b \int_a^b \abs{K(x, s)}^2 \, ds \, dx \right)^{1/2} < \infty,$$
where the integral is the [[Lebesgue integral|DWJF7ABPR1]].

## Remarks

Example: $K(x, s) = \abs{x - s}^{-1/4}$ for $x \ne s$ on $[0, 1]$.
Here $\abs{K}^2 = \abs{x - s}^{-1/2}$, and $\int_0^1 \abs{x - s}^{-1/2} \, ds \le 2 \int_0^{1} t^{-1/2} \, dt = 4$ for each $x$, so $\norm{K}_2^2 \le 4$.

Non-example: $K(x, s) = \abs{x - s}^{-1/2}$ on $[0, 1]$.
For $0 < x < 1$, $\int_0^1 \abs{x - s}^{-1} \, ds = \infty$, so the double integral of $\abs{K}^2$ is infinite.

In other words, $K$ lies in the [[Lp space|SASP14MA1Z]] $L^2([a, b] \times [a, b])$.
Every continuous kernel on $[a, b]$ is square-integrable.
For $\varphi \in L^2(a, b)$, the function $(K \varphi)(x) = \int_a^b K(x, s) \varphi(s) \, ds$ lies in $L^2(a, b)$ and $\norm{K \varphi}_2 \le \norm{K}_2 \norm{\varphi}_2$, by the Cauchy–Schwarz inequality.
The same definition is used on a measurable subset of $\R^m$.
