---
tag: 07T2TKGZ4J
kind: statement
role: proposition
name: Derivatives of the hyperbolic functions
msc: [33B10, 26A24]
uses: [0GWD21EWRW, 0EQFWKJ37J, 0MWYQTZ07Z, 0EX9GFJ0B3, 0BS0NJPKVE, 06QCTRFBM0]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Derivatives
---

## Statement

The functions $\sinh$, $\cosh$ and $\tanh$ are differentiable on $\mathbb{R}$, and for every real $x$
$$\sinh'(x) = \cosh x, \qquad \cosh'(x) = \sinh x, \qquad \tanh'(x) = \frac{1}{\cosh^2 x} = 1 - \tanh^2 x.$$

## Remarks

The first two follow from [[$\exp' = \exp$|0EX9GFJ0B3]] and $(e^{-x})' = -e^{-x}$.
The third follows from the [[quotient rule|0BS0NJPKVE]] and the identity [[$\cosh^2 - \sinh^2 = 1$|06QCTRFBM0]].
So $\sinh'' = \sinh$ and $\cosh'' = \cosh$. Mathlib states the first one as `Real.hasDerivAt_sinh`.

## Explanations

### L1 human

Unlike sine and cosine, there is no minus sign here.
Each of $\sinh$ and $\cosh$ is the derivative of the other.
