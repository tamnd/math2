---
tag: 0KY08TWDMQ
kind: statement
role: theorem
name: Derivative of x^a
msc: [26A24, 26A09]
uses: [0TV07AQT62, 0RXX2PT1MQ, 0EX9GFJ0B3, 07X1QA6BRW]
sources:
  - url: https://en.wikipedia.org/wiki/Power_rule
    locator: Proof for real exponents
---

## Statement

Let $a$ be a real number. The function $x \mapsto x^a$ is differentiable on $(0, \infty)$, and
$$\frac{d}{dx} x^a = a x^{a-1} \quad \text{for } x > 0.$$

## Remarks

Write $x^a = e^{a \ln x}$. The [[chain rule|0RXX2PT1MQ]] with [[$\exp' = \exp$|0EX9GFJ0B3]] and [[$\ln' x = 1/x$|07X1QA6BRW]] gives $e^{a \ln x} \cdot \frac{a}{x} = a x^{a-1}$.
For example, $\frac{d}{dx} \sqrt{x} = \frac{1}{2 \sqrt{x}}$.
Similarly, $\frac{d}{dx} a^x = a^x \ln a$ for a fixed $a > 0$. Mathlib states the main claim as `Real.hasDerivAt_rpow_const`.

## Explanations

### L1 human

The power rule for whole exponents also works for real exponents, if $x > 0$.
Bring the exponent down and lower it by one.
