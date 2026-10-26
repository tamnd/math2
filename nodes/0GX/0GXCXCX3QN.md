---
tag: 0GXCXCX3QN
kind: statement
role: proposition
name: Integral of sine
msc: [26A36]
uses: [0WB57D9488, 0V2DV29EGT, 0XYAFCN0PT]
sources:
  - url: https://en.wikipedia.org/wiki/Lists_of_integrals
    locator: Trigonometric functions
---

## Statement

For all real numbers $a$ and $b$,
$$\int_a^b \sin x \, dx = \cos a - \cos b.$$

## Remarks

The [[derivative of cosine|0V2DV29EGT]] is $-\sin$, so $-\cos$ is an antiderivative of $\sin$.
For example, $\int_0^\pi \sin x \, dx = 2$.
Mathlib states it as `integral_sin`.

## Explanations

### L1 human

The area under one arch of the sine curve is exactly $2$.
This follows from the antiderivative $-\cos x$.
