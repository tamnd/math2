---
tag: MXRC891TQS
kind: concept
name: Complex Monge–Ampère operator
msc: [32W20, 32U15]
sources:
  - url: https://en.wikipedia.org/wiki/Monge%E2%80%93Amp%C3%A8re_equation
---

## Summary

The complex Monge–Ampère operator sends a function $u$ on an open subset of $\C^n$ to the determinant of its complex Hessian.
The complex Hessian is the matrix $\left(\partial^2 u / \partial z_j \partial \bar z_k\right)$, and the determinant is viewed as a measure.
In the language of forms it is the $n$-th exterior power $(dd^c u)^n$.
For $n = 1$ it is the Laplacian, so it is the nonlinear analogue of the Laplacian in pluripotential theory.
It is the operator of the complex [[Monge–Ampère equation|14AKAC0S0T]], which appears in the construction of Kähler–Einstein metrics and in the study of [[plurisubharmonic functions|FF2P7ER3QT]].

## Explanations

### L1 human

For a smooth function of several complex variables, one can form the matrix of its mixed second derivatives in $z_j$ and $\bar z_k$.
The complex Monge–Ampère operator takes the determinant of this matrix.
For a plurisubharmonic function the matrix is positive semidefinite, so the determinant is nonnegative and can be read as a density of mass.
For example, for $u(z) = \abs{z_1}^2 + \cdots + \abs{z_n}^2$ the matrix is the identity and the determinant is $1$ everywhere.
For $u(z) = \abs{z_1}^2$ in $\C^2$ the determinant is $0$, because $u$ does not depend on $z_2$.
