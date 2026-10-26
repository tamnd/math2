---
tag: 04WTBQ7APQ
kind: statement
role: proposition
name: Integral of cosine
msc: [26A36]
uses: [0WB57D9488, 00R4MWW532, 0XYAFCN0PT]
sources:
  - url: https://en.wikipedia.org/wiki/Lists_of_integrals
    locator: Trigonometric functions
---

## Statement

For all real numbers $a$ and $b$,
$$\int_a^b \cos x \, dx = \sin b - \sin a.$$

## Remarks

The [[derivative of sine|00R4MWW532]] is $\cos$, so $\sin$ is an antiderivative of $\cos$.
For example, $\int_0^{\pi/2} \cos x \, dx = 1$.
Mathlib states it as `integral_cos`.

## Explanations

### L1 human

The sine function is an antiderivative of the cosine function.
So the integral of cosine is a difference of two sine values.
