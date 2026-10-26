---
tag: 0MWYQTZ07Z
kind: definition
name: Hyperbolic tangent
msc: [33B10]
defines: 0X6C0MAF84
uses: [0GWD21EWRW, 0EQFWKJ37J]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Exponential definitions
---

## Definition

The hyperbolic tangent is the function $\tanh \colon \mathbb{R} \to \mathbb{R}$ defined by
$$\tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}.$$

## Remarks

The quotient is defined everywhere, since $\cosh x \ge 1$.
It is odd and strictly increasing, with range $(-1, 1)$. Also $\tanh x \to \pm 1$ as $x \to \pm \infty$.
Mathlib defines it as `Real.tanh`.

## Explanations

### L1 human

The hyperbolic tangent is an S-shaped curve between $-1$ and $1$.
It is close to $x$ near $0$ and close to $\pm 1$ far away.
