---
tag: 06QCTRFBM0
kind: statement
role: proposition
name: cosh^2 - sinh^2 = 1
msc: [33B10]
uses: [0GWD21EWRW, 0EQFWKJ37J]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Useful relations
---

## Statement

For every real $x$,
$$\cosh^2 x - \sinh^2 x = 1.$$

## Remarks

The left side factors as $(\cosh x - \sinh x)(\cosh x + \sinh x) = e^{-x} e^{x} = 1$.
So the point $(\cosh t, \sinh t)$ lies on the right branch of the hyperbola $x^2 - y^2 = 1$.
Dividing by $\cosh^2 x$ gives $1 - \tanh^2 x = \operatorname{sech}^2 x$. Mathlib states the identity as `Real.cosh_sq_sub_sinh_sq`.

## Explanations

### L1 human

This is the hyperbolic version of $\cos^2 x + \sin^2 x = 1$, with a minus sign.
It follows directly from the definitions with $e^x$ and $e^{-x}$.
