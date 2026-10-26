---
tag: 0BS0NJPKVE
kind: statement
role: theorem
name: Quotient rule
msc: [26A24]
uses: [0V9A43H7WV, 0QD4E5JYPT]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_rule
    locator: lead section
same_as:
  wikidata: Q531392
  wikipedia: Quotient rule
---

## Statement

Let $f$ and $g$ be real functions on an open interval $I$, both differentiable at $a \in I$, with $g(a) \ne 0$.
Then $f/g$ is differentiable at $a$, and
$$\left( \frac{f}{g} \right)'(a) = \frac{f'(a) g(a) - f(a) g'(a)}{g(a)^2}.$$

## Remarks

Write $f/g = f \cdot (1/g)$, and use the [[product rule|0V9A43H7WV]] and the [[reciprocal rule|0QD4E5JYPT]].
For example, it gives $(\tan x)' = 1/\cos^2 x$.
Mathlib states it as `HasDerivAt.div`.

## Explanations

### L1 human

The rule gives the slope of a quotient from the values and slopes of the numerator and the denominator.
A common memory aid is "low d-high minus high d-low, over low squared".
