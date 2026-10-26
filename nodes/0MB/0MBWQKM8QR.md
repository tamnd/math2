---
tag: 0MBWQKM8QR
kind: statement
role: theorem
name: Monotonicity of the integral
msc: [26A42]
uses: [021WEM680W, 0HBY48G8G1]
sources:
  - url: https://en.wikipedia.org/wiki/Integral
    locator: Inequalities
---

## Statement

Let $f, g \colon [a, b] \to \mathbb{R}$ be Riemann integrable with $f(x) \le g(x)$ for all $x \in [a, b]$.
Then
$$\int_a^b f(x) \, dx \le \int_a^b g(x) \, dx.$$

## Remarks

Each [[Riemann sum|0HBY48G8G1]] of $f$ is at most the Riemann sum of $g$ for the same tagged partition.
In particular, if $m \le f \le M$ on $[a, b]$, then $m (b - a) \le \int_a^b f \le M (b - a)$.
Mathlib states it as `intervalIntegral.integral_mono_on`.

## Explanations

### L1 human

A larger function has a larger integral.
If one graph lies below another, the area under it is smaller.
