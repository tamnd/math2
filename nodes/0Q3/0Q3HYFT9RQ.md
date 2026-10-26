---
tag: 0Q3HYFT9RQ
kind: statement
role: proposition
name: Integral of a power
msc: [26A36]
uses: [0JZGW75C5Z, 0XYAFCN0PT]
sources:
  - url: https://en.wikipedia.org/wiki/Lists_of_integrals
    locator: Integrals of simple functions
---

## Statement

Let $n \ge 0$ be an integer and let $a, b \in \mathbb{R}$.
Then
$$\int_a^b x^n \, dx = \frac{b^{n+1} - a^{n+1}}{n + 1}.$$

## Remarks

By the [[power rule|0JZGW75C5Z]], $x^{n+1}/(n + 1)$ is an antiderivative of $x^n$. Apply the [[second fundamental theorem|0XYAFCN0PT]].
The same formula holds for each real exponent $r \ne -1$, on intervals inside $(0, \infty)$. The case $r = -1$ gives the [[logarithm|0K1N1Y4EGZ]].
Mathlib states it as `integral_pow`.

## Explanations

### L1 human

To integrate $x^n$, raise the power by one and divide by the new power.
For example, $\int_0^1 x^2 \, dx = 1/3$.
