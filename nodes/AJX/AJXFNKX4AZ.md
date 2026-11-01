---
tag: AJXFNKX4AZ
kind: definition
name: Riemann–Liouville integral
msc: [26A33]
defines: JTKCZ44NN3
uses: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Liouville_integral
---

## Definition

Let $a < b$ be real numbers, possibly $b = \infty$, and let $f$ be a locally integrable real function on $[a, b)$.
Let $\alpha > 0$ be real.
The *Riemann–Liouville integral* of order $\alpha$ of $f$, with lower terminal $a$, is the function
$$I_a^\alpha f(x) = \frac{1}{\Gamma(\alpha)} \int_a^x (x - t)^{\alpha - 1} f(t) \, dt, \qquad a < x < b,$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]].

## Remarks

The integral converges for almost every $x$, and for every $x$ when $f$ is continuous on $[a, b)$, because $(x - t)^{\alpha - 1}$ is integrable near $t = x$ for $\alpha > 0$.
Example: for $\beta > -1$ and $a = 0$, the substitution $t = xs$ and the beta integral give $I_0^\alpha t^\beta = \frac{\Gamma(\beta + 1)}{\Gamma(\alpha + \beta + 1)} x^{\alpha + \beta}$.
For $\beta = 0$ this is $x^\alpha / \Gamma(\alpha + 1)$.
Non-example: for $\alpha = -\tfrac{1}{2}$ and $f = 1$, the integrand $(x - t)^{-3/2}$ is not integrable near $t = x$, so the formula defines nothing; negative orders need a derivative, as in [[fractional calculus|T73XK15SA2]].
The operators satisfy the semigroup law $I_a^\alpha I_a^\beta f = I_a^{\alpha + \beta} f$ for $\alpha, \beta > 0$.
For $\alpha = 1$, $I_a^1 f(x) = \int_a^x f(t) \, dt$.

## Explanations

### L1 human

The definition averages the past values of $f$ with the weight $(x - t)^{\alpha - 1}$.
When $\alpha$ is a whole number, this is the usual repeated integral.
When $\alpha$ is not a whole number, for example $\alpha = \tfrac{1}{2}$, the same formula gives an integral of fractional order.
