---
tag: DEYYNVCV9J
kind: concept
name: Fredholm equation of the second kind
msc: [45B05, 45A05]
specializes: [526TCVMSHP, 8KJCN49V64]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Summary

A Fredholm equation of the second kind is an integral equation $\varphi(x) - \lambda \int_a^b K(x, y) \varphi(y) \, dy = f(x)$ with fixed limits $a$ and $b$.
The unknown $\varphi$ appears both outside and under the integral.
It is the [[Fredholm integral equation|526TCVMSHP]] form of an [[integral equation of the second kind|8KJCN49V64]].
Boundary value problems for differential equations lead to it, and its theory is very complete.
For all but a discrete set of values of the parameter $\lambda$, it has exactly one solution for every right-hand side.

## Explanations

### L1 human

The unknown function equals a known function plus a weighted average of its own values.
So the equation describes a balance, such as the temperature at a point being fed by the temperature at all other points.
When $\lambda$ is small, the averaged part is only a small correction, and one can solve by repeated substitution.
For example, on $[0, 1]$ the equation $\varphi(x) - \int_0^1 x y \, \varphi(y) \, dy = x$ has the solution $\varphi(x) = 3x/2$.
