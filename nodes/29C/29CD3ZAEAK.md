---
tag: 29CD3ZAEAK
kind: proof
name: Proof of the derivatives of the hyperbolic functions
msc: [33B10, 26A24]
proves: 07T2TKGZ4J
uses: [0GWD21EWRW, 0EQFWKJ37J, 0MWYQTZ07Z, 0RMVS7RXZX, 0EX9GFJ0B3, 0RXX2PT1MQ, 0M0TKFRX2A, 0BS0NJPKVE, 0P9BNBW2W3, 06QCTRFBM0]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Derivatives
---

## Proof

We differentiate the defining formulas with the standard rules.

1. Write $e^t = \exp(t)$ for the [[exponential function|0RMVS7RXZX]]. Let $E(x) = e^x$ and $F(x) = e^{-x}$ for real $x$.
2. By [[$\exp' = \exp$|0EX9GFJ0B3]], $E$ is differentiable on $\R$ with $E' = E$.
3. The map $x \mapsto -x$ is differentiable with derivative $-1$. By the [[chain rule|0RXX2PT1MQ]] and step 2, $F$ is differentiable on $\R$ with $F'(x) = e^{-x} \cdot (-1) = -F(x)$.
4. By the definitions of the [[hyperbolic sine|0GWD21EWRW]] and the [[hyperbolic cosine|0EQFWKJ37J]], $\sinh = \frac{1}{2} E - \frac{1}{2} F$ and $\cosh = \frac{1}{2} E + \frac{1}{2} F$.
5. By [[linearity of differentiation|0M0TKFRX2A]] and steps 2 and 3, $\sinh$ is differentiable on $\R$ with $\sinh'(x) = \frac{1}{2} e^x + \frac{1}{2} e^{-x} = \cosh x$.
6. In the same way, $\cosh$ is differentiable on $\R$ with $\cosh'(x) = \frac{1}{2} e^x - \frac{1}{2} e^{-x} = \sinh x$.
7. For each real $x$, $e^x > 0$ and $e^{-x} > 0$, since [[the exponential function is positive|0P9BNBW2W3]]. So $\cosh x > 0$, and in particular $\cosh x \ne 0$.
8. By the definition of the [[hyperbolic tangent|0MWYQTZ07Z]], $\tanh = \sinh / \cosh$.
9. By the [[quotient rule|0BS0NJPKVE]] and steps 5, 6 and 7, $\tanh$ is differentiable at each real $x$, with
$$\tanh'(x) = \frac{\cosh x \cosh x - \sinh x \sinh x}{\cosh^2 x} = \frac{\cosh^2 x - \sinh^2 x}{\cosh^2 x}.$$
10. By the identity [[$\cosh^2 - \sinh^2 = 1$|06QCTRFBM0]], the numerator in step 9 is $1$. So $\tanh'(x) = \frac{1}{\cosh^2 x}$.
11. Dividing that identity by $\cosh^2 x \ne 0$ gives $1 - \frac{\sinh^2 x}{\cosh^2 x} = \frac{1}{\cosh^2 x}$. So $\frac{1}{\cosh^2 x} = 1 - \tanh^2 x$.
12. Steps 5, 6, 10 and 11 give all three formulas, for every real $x$.

## Idea

The exponential is its own derivative, and $e^{-x}$ has derivative $-e^{-x}$. So differentiating swaps the sign between the two terms, which turns $\sinh$ into $\cosh$ and back. For $\tanh$, the quotient rule produces $\cosh^2 - \sinh^2$, which is $1$.
