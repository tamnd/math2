---
tag: GSMBXT7FPK
kind: concept
name: Kernel of an integral equation
msc: [45A05, 45P05]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Summary

The kernel of a linear [[integral equation|R3SG1SN7JQ]] is the function $K(x, s)$ of two variables that multiplies the unknown function inside the integral.
In $\varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds$ it is $K$.
The properties of the kernel, such as continuity, symmetry or the form of its singularity, decide which theory applies to the equation.

## Explanations

### L1 human

The kernel says how strongly the value of the unknown at the point $s$ influences the equation at the point $x$.
It is like an infinite matrix whose rows are indexed by $x$ and whose columns are indexed by $s$.
The integral $\int K(x, s) \varphi(s) \, ds$ is the continuous version of multiplying a matrix by a vector.
For example, in $\varphi(x) = 1 + \int_0^1 (x + s) \varphi(s) \, ds$ the kernel is $K(x, s) = x + s$.
