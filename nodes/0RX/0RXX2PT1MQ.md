---
tag: 0RXX2PT1MQ
kind: statement
role: theorem
name: Chain rule
msc: [26A24]
uses: [0F1WR9C83K, 0NRQPQX3VA]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_rule
    locator: Statement
same_as:
  wikidata: Q207455
  wikipedia: Chain rule
---

## Statement

Let $f$ be a real function on an open interval $I$ that is differentiable at $a \in I$.
Let $g$ be a real function on an open interval $J$ with $f(I) \subseteq J$, and assume that $g$ is differentiable at $f(a)$.
Then $g \circ f$ is differentiable at $a$, and
$$(g \circ f)'(a) = g'(f(a)) \, f'(a).$$

## Remarks

A naive proof multiplies and divides by $f(a + h) - f(a)$. This fails when $f(a + h) = f(a)$ for small $h$. A correct proof uses the linear approximation of $g$ at $f(a)$.
For example, $(\sin(x^2))' = 2 x \cos(x^2)$.
In Leibniz notation, $\frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx}$. Mathlib states the rule as `HasDerivAt.comp`.

## History

Gottfried Wilhelm Leibniz seems to have used the rule first, in a memoir of 1676.

## Explanations

### L1 human

Suppose $y$ changes $f'(a)$ times as fast as $x$, and $z$ changes $g'(y)$ times as fast as $y$.
Then $z$ changes $g'(y) f'(a)$ times as fast as $x$.
The rates multiply.
