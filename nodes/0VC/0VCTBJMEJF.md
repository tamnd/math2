---
tag: 0VCTBJMEJF
kind: definition
name: Improper integral
msc: [26A42, 40A10]
defines: 05KQ3F99BQ
uses: [0QM4TXT3DR, 0Y12QYTJK3, 0909PWZR62]
sources:
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Convergence of the integral
inventory: [DPKBRR863S]
---

## Definition

Let $f \colon [a, \infty) \to \mathbb{R}$ be Riemann integrable on $[a, b]$ for each $b > a$.
The improper integral of $f$ over $[a, \infty)$ converges if the following [[limit|0Y12QYTJK3]] exists in $\mathbb{R}$:
$$\int_a^\infty f(x) \, dx = \lim_{b \to \infty} \int_a^b f(x) \, dx.$$
Similarly, let $f \colon (a, b] \to \mathbb{R}$ be Riemann integrable on $[c, b]$ for each $c \in (a, b)$.
Then $\int_a^b f(x) \, dx = \lim_{c \to a^+} \int_c^b f(x) \, dx$, if this [[one-sided limit|0909PWZR62]] exists.

## Remarks

If the limit does not exist, the improper integral diverges.
For an integral over $(-\infty, \infty)$, or with several bad points, we split the interval. Each piece must converge separately.
For example, $\int_1^\infty \frac{dx}{x^2} = 1$, and $\int_0^1 \frac{dx}{\sqrt{x}} = 2$. But $\int_1^\infty \frac{dx}{x}$ diverges.

## Explanations

### L1 human

The Riemann integral needs a bounded interval and a bounded function.
An improper integral removes these limits by a limit of ordinary integrals.
