---
tag: CC8KNGMZYS
kind: definition
name: Lebesgue–Stieltjes integration
msc: [26A42, 28A25]
defines: FK3QBZAZH7
uses: [0WFF6AZPBP, QV75XJBFCS, X7GTF3D98F, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration
---

## Definition

Let $g \colon \R \to \R$ be a [[non-decreasing|0WFF6AZPBP]], right-continuous function.
Let $\mu_g$ be its [[Lebesgue–Stieltjes measure|QV75XJBFCS]], the Borel measure with $\mu_g((a, b]) = g(b) - g(a)$ for all $a < b$.
Let $f \colon \R \to \R$ be a Borel measurable function that is [[integrable|X7GTF3D98F]] with respect to $\mu_g$.
The *Lebesgue–Stieltjes integral* of $f$ with respect to $g$ is the [[Lebesgue integral|DWJF7ABPR1]]
$$\int_\R f \, dg = \int_\R f \, d\mu_g.$$

## Remarks

Example: let $g = \mathbf{1}_{[0, \infty)}$, the Heaviside step function with $g(0) = 1$, which is non-decreasing and right-continuous.
Then $\mu_g$ is the Dirac measure at $0$, so $\int f \, dg = f(0)$ for every Borel function $f$.
For $g(x) = x$ the measure $\mu_g$ is Lebesgue measure, and the integral is the usual Lebesgue integral.

Non-example: $g(x) = -x$ is not non-decreasing, so the definition does not apply directly.
The formula $\mu_g((a, b]) = g(b) - g(a)$ would give negative mass.

For $g$ of bounded variation and right-continuous, one writes $g = g_1 - g_2$ with $g_1, g_2$ non-decreasing and right-continuous, and sets $\int f \, dg = \int f \, dg_1 - \int f \, dg_2$.
On $[a, b]$ one writes $\int_{(a, b]} f \, dg$, and the endpoints matter when $g$ jumps there.
If $f$ is continuous on $[a, b]$, the integral over $(a, b]$ equals the Riemann–Stieltjes integral $\int_a^b f \, dg$.
If $g$ is absolutely continuous on bounded intervals, then $\int f \, dg = \int f(x) g'(x) \, dx$.
