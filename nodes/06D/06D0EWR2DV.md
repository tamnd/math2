---
tag: 06D0EWR2DV
kind: statement
role: proposition
name: Integral of the exponential function
msc: [26A36]
uses: [0RMVS7RXZX, 0EX9GFJ0B3, 0XYAFCN0PT]
sources:
  - url: https://en.wikipedia.org/wiki/Lists_of_integrals
    locator: Exponential functions
---

## Statement

For all real numbers $a$ and $b$,
$$\int_a^b e^x \, dx = e^b - e^a.$$

## Remarks

The [[exponential function|0RMVS7RXZX]] is [[its own derivative|0EX9GFJ0B3]], so it is its own antiderivative.
More generally, $\int_a^b e^{c x} \, dx = (e^{c b} - e^{c a})/c$ for $c \ne 0$.
Mathlib states it as `integral_exp`.

## Explanations

### L1 human

The exponential function does not change under differentiation.
So it also does not change under integration, up to the constant.
