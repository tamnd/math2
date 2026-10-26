---
tag: 0NR82KMYKD
kind: statement
role: theorem
name: Triangle inequality for integrals
msc: [26A42]
uses: [0MBWQKM8QR, 0W3K3QPEWT]
sources:
  - url: https://en.wikipedia.org/wiki/Integral
    locator: Inequalities
---

## Statement

Let $f \colon [a, b] \to \mathbb{R}$ be Riemann integrable.
Then $|f|$ is Riemann integrable on $[a, b]$, and
$$\Big| \int_a^b f(x) \, dx \Big| \le \int_a^b |f(x)| \, dx.$$

## Remarks

The inequality follows from $-|f| \le f \le |f|$ and the [[monotonicity of the integral|0MBWQKM8QR]].
The converse of the first claim fails. On $[0, 1]$, let $f = 1$ on the rationals and $f = -1$ elsewhere. Then $|f| = 1$ is integrable, but $f$ is not.
Mathlib states the inequality as `intervalIntegral.norm_integral_le_integral_norm`.

## Explanations

### L1 human

Cancellation can only make an integral smaller in size.
The size of the integral is at most the integral of the size of the function.
