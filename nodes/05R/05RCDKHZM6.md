---
tag: 05RCDKHZM6
kind: statement
role: theorem
name: Additivity of the integral over intervals
msc: [26A42]
uses: [021WEM680W]
sources:
  - url: https://en.wikipedia.org/wiki/Integral
    locator: Linearity
---

## Statement

Let $a < c < b$ and let $f \colon [a, b] \to \mathbb{R}$.
Then $f$ is Riemann integrable on $[a, b]$ if and only if it is Riemann integrable on $[a, c]$ and on $[c, b]$.
In this case,
$$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx.$$

## Remarks

With the sign convention of the [[definite integral|021WEM680W]], the formula holds for any order of $a$, $b$, $c$.
This needs $f$ to be integrable on the largest of the intervals.
Mathlib states it as `intervalIntegral.integral_add_adjacent_intervals`.

## Explanations

### L1 human

The area over $[a, b]$ is the area over $[a, c]$ plus the area over $[c, b]$.
We can cut the interval at any point and add the two pieces.
