---
tag: 0K1N1Y4EGZ
kind: statement
role: proposition
name: Integral of 1/x
msc: [26A36]
uses: [0044CPHJBV, 07X1QA6BRW, 0XYAFCN0PT]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Integration
---

## Statement

Let $a, b$ be real numbers of the same sign, both nonzero.
Then
$$\int_a^b \frac{dx}{x} = \ln \frac{b}{a}.$$
In particular, $\int_1^x \frac{dt}{t} = \ln x$ for $x > 0$.

## Remarks

The function $\ln |x|$ is an antiderivative of $1/x$ on each of $(0, \infty)$ and $(-\infty, 0)$, by the [[derivative of the logarithm|07X1QA6BRW]].
Some texts use the second formula as the definition of the [[natural logarithm|0044CPHJBV]].
The integral over an interval that contains $0$ does not exist.
Mathlib states it as `integral_inv`, under the hypothesis $0 \notin [a, b]$.

## Explanations

### L1 human

The power rule fails for $x^{-1}$, since it would divide by $0$.
The logarithm fills this gap: its derivative is $1/x$.
