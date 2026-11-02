---
tag: TD5XK5AHNV
kind: concept
name: Mikusiński operational calculus
msc: [44A40]
specializes: [8050R3Z6HA]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Summary

The Mikusiński operational calculus, created by Jan Mikusiński, is an algebraic foundation of [[operational calculus|8050R3Z6HA]] that does not use integral transforms.
Functions on $[0, \infty)$ are elements of the [[Mikusiński field of operators|82YAXZMMQ1]], in which differentiation is multiplication by an element $s$ up to initial values.
Linear differential equations with constant coefficients become linear equations in this field, and the solution is read off by algebra.
Unlike the Laplace transform approach, it needs no growth condition on the functions.

## Explanations

### L1 human

Mikusiński replaced the Laplace transform by pure algebra.
He made fractions of functions, with convolution as multiplication, much as one makes fractions of whole numbers.
In this world the derivative is multiplication by a fixed element $s$, corrected by the initial value.
Solving $y' = a y$, $y(0) = 1$ becomes $s y - 1 = a y$, so $y = 1/(s - a)$, and one checks that this fraction is the function $e^{at}$.
