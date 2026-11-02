---
tag: MAKCYGGERD
kind: concept
name: Laplace transform on a convex cone
msc: [44A30, 44A10]
specializes: [4PVP1C3JZG]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Summary

The Laplace transform on a convex cone integrates a function on a closed [[convex cone|6VE4KA12VD]] $\Gamma \subseteq \R^n$ against $e^{-\ip{y}{x}}$.
Here $y$ runs over the interior of the [[dual cone|QFY1JR1TK4]].
For the orthant $\Gamma = [0, \infty)^n$ it is the [[multidimensional Laplace transform|QT3M720TCV]].
For a function of moderate growth, the transform extends to a holomorphic function on a tube domain over the interior of the dual cone.
On the cone of positive definite matrices it gives the multivariate gamma function, and it is a basic tool of analysis on symmetric cones.

## Explanations

### L1 human

The ordinary Laplace transform lives on the half-line $[0, \infty)$, and the exponential $e^{-yx}$ decays there when $y > 0$.
In several variables the half-line is replaced by a cone, such as a quarter plane or the set of positive definite matrices.
The exponential $e^{-\ip{y}{x}}$ decays along the whole cone exactly when $y$ points into the dual cone.
For example, on the quarter plane with $f = 1$ the transform is $1/(y_1 y_2)$ for $y_1, y_2 > 0$.
