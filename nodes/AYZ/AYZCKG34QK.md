---
tag: AYZCKG34QK
kind: concept
name: Linear integral equation
msc: [45A05]
specializes: [R3SG1SN7JQ]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A linear integral equation is an [[integral equation|R3SG1SN7JQ]] in which the unknown function enters linearly, both outside and inside the integral.
Its general form is $a(x) \varphi(x) = f(x) + \lambda \int K(x, s) \varphi(s) \, ds$ with a given [[kernel|GSMBXT7FPK]] $K$.
The solutions form an affine space, so linear algebra and operator theory apply.
Fredholm and Volterra equations are the main classes.

## Explanations

### L1 human

Linear means that sums and multiples of solutions of the equation with $f = 0$ are again solutions.
The integral acts on the unknown like a matrix acts on a vector.
So a linear integral equation is a continuous version of a system of linear equations.
For example, $\varphi(x) = x + \int_0^1 x s \, \varphi(s) \, ds$ is linear, while an equation with $\varphi(s)^2$ under the integral is not.
