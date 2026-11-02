---
tag: XEZXGBT42J
kind: concept
name: Adjoint integral equation
msc: [45A05, 45B05]
specializes: [8KJCN49V64]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

Let an [[integral equation of the second kind|8KJCN49V64]] have kernel $K(x, s)$ and parameter $\lambda$.
Its adjoint is the equation of the same kind with the kernel $\overline{K(s, x)}$ and the parameter $\bar\lambda$.
Its integral operator is the [[adjoint|0R9NMSM1ZP]] of the original integral operator for the $L^2$ inner product.
The Fredholm alternative uses it: the original equation is solvable exactly when its right side is orthogonal to the solutions of the homogeneous adjoint equation.
For a real kernel the adjoint kernel is the transposed kernel $K(s, x)$.

## Explanations

### L1 human

The adjoint equation swaps the roles of the two variables of the kernel, like transposing a matrix.
For complex kernels one also takes complex conjugates, as in the conjugate transpose of a matrix.
The original equation and its adjoint have solvability properties that mirror each other.
For example, the adjoint of $\varphi(x) = f(x) + \lambda \int_0^1 x \, \varphi(s) \, ds$ is $\psi(x) = g(x) + \bar\lambda \int_0^1 s \, \psi(s) \, ds$.
