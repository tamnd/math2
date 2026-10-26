---
tag: 0FR1BDKK10
kind: statement
role: theorem
name: Comparison test for improper integrals
msc: [40A10]
uses: [0VCTBJMEJF, 0MBWQKM8QR, 0KJXHN0TW0]
sources:
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Convergence of the integral
---

## Statement

Let $f, g \colon [a, \infty) \to \mathbb{R}$ be Riemann integrable on each $[a, b]$, with $0 \le f(x) \le g(x)$ for all $x \ge a$.
If $\int_a^\infty g(x) \, dx$ converges, then $\int_a^\infty f(x) \, dx$ converges, and
$$\int_a^\infty f(x) \, dx \le \int_a^\infty g(x) \, dx.$$
If $\int_a^\infty f(x) \, dx$ diverges, then $\int_a^\infty g(x) \, dx$ diverges.

## Remarks

The function $b \mapsto \int_a^b f$ is increasing, and it is bounded by $\int_a^\infty g$ by [[monotonicity|0MBWQKM8QR]]. A [[bounded monotone function has a limit|0KJXHN0TW0]].
For example, $0 \le e^{-x^2} \le e^{-x}$ for $x \ge 1$. So $\int_1^\infty e^{-x^2} \, dx$ converges.
The same test holds for integrals that are improper at a finite endpoint.

## Explanations

### L1 human

If a larger function has finite area, a smaller nonnegative function also has finite area.
This lets us prove convergence without computing the integral.
