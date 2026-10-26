---
tag: 0D37QFPEZE
kind: statement
role: theorem
name: Integration by substitution
aliases: [change-of-variables-formula]
msc: [26A42]
uses: [0RXX2PT1MQ, 0XYAFCN0PT, 0NC2A3HWGT, 06SKCHDQT5]
sources:
  - url: https://en.wikipedia.org/wiki/Integration_by_substitution
    locator: Statement for definite integrals
same_as:
  wikidata: Q1071270
  wikipedia: Integration by substitution
---

## Statement

Let $g \colon [a, b] \to \mathbb{R}$ be [[continuously differentiable|06SKCHDQT5]], and let $f$ be continuous on an interval that contains $g([a, b])$.
Then
$$\int_a^b f(g(x)) \, g'(x) \, dx = \int_{g(a)}^{g(b)} f(u) \, du.$$

## Remarks

Let $F$ be an [[antiderivative|0NC2A3HWGT]] of $f$. By the [[chain rule|0RXX2PT1MQ]], $F \circ g$ is an antiderivative of $(f \circ g) \, g'$. Both sides equal $F(g(b)) - F(g(a))$.
The function $g$ need not be injective.
For example, with $u = x^2$, $\int_0^1 2x \cos(x^2) \, dx = \int_0^1 \cos u \, du = \sin 1$.
Mathlib states it as `intervalIntegral.integral_comp_mul_deriv`.

## Explanations

### L1 human

Substitution is the chain rule read backwards.
We replace an expression $g(x)$ by a new variable $u$, and $g'(x) \, dx$ by $du$.
