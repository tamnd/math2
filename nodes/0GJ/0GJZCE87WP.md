---
tag: 0GJZCE87WP
kind: statement
role: proposition
name: Addition formulas for hyperbolic functions
msc: [33B10]
uses: [0GWD21EWRW, 0EQFWKJ37J, 0E8HNVBCSP]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Sums and differences of arguments
---

## Statement

For all real numbers $x$ and $y$,
$$\sinh(x + y) = \sinh x \cosh y + \cosh x \sinh y,$$
$$\cosh(x + y) = \cosh x \cosh y + \sinh x \sinh y.$$

## Remarks

Expand the right sides with the definitions and use [[$e^{x+y} = e^x e^y$|0E8HNVBCSP]].
With $y = x$, they give $\sinh 2x = 2 \sinh x \cosh x$ and $\cosh 2x = \cosh^2 x + \sinh^2 x$.
Mathlib states the first formula as `Real.sinh_add`.

## Explanations

### L1 human

These formulas look like the trigonometric addition formulas.
The only change is the plus sign in the formula for $\cosh$.
