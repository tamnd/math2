---
tag: 0GWD21EWRW
kind: definition
name: Hyperbolic sine
msc: [33B10]
defines: 0H1JFKE7H4
uses: [0RMVS7RXZX]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Exponential definitions
---

## Definition

The hyperbolic sine is the function $\sinh \colon \mathbb{R} \to \mathbb{R}$ defined by
$$\sinh x = \frac{e^x - e^{-x}}{2}.$$

## Remarks

It is odd and strictly increasing, and it is a bijection of $\mathbb{R}$ onto $\mathbb{R}$.
Its power series is $\sinh x = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}$, the sine series without the signs.
Mathlib defines it as `Real.sinh`.

## Explanations

### L1 human

The hyperbolic sine is the odd part of $e^x$.
For large $x$, it is close to $e^x / 2$.
