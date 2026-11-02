---
tag: QT3M720TCV
kind: concept
name: Multidimensional Laplace transform
msc: [44A30, 44A10]
specializes: [4PVP1C3JZG, 0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Multidimensional_transform
---

## Summary

The multidimensional Laplace transform takes a function of $n$ variables on the orthant $[0, \infty)^n$ to a function of $n$ complex variables, by integrating against $e^{-s_1 x_1 - \cdots - s_n x_n}$.
It is the [[Laplace transform|0V49JEZW06]] applied in each variable in turn.
It turns partial derivatives into multiplication by the variables $s_j$, up to boundary terms.
So it is used for linear partial differential equations with constant coefficients.
In probability it gives the joint Laplace transform of nonnegative random vectors.

## Explanations

### L1 human

The ordinary Laplace transform weighs a function of time by a decaying exponential.
In several variables one uses one decay rate for each variable.
For example, for $f(x_1, x_2) = 1$ on the quarter plane the transform is $\int_0^\infty \int_0^\infty e^{-s_1 x_1 - s_2 x_2}\, dx_1\, dx_2 = \frac{1}{s_1 s_2}$ for $s_1, s_2 > 0$.
A product of functions of single variables becomes a product of one-variable Laplace transforms.
