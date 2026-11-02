---
tag: FSD6S7DR8D
kind: concept
name: Jacobi equation
msc: [49K05]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_field
---

## Summary

The Jacobi equation of a variational problem is the linear second-order differential equation $-(P h')' + Q h = 0$ obtained from the [[second variation|4C3BANJ8AH]] along an extremal.
It is the [[Euler–Lagrange equation|PS0VV149ET]] of the quadratic functional $\int (P h'^2 + Q h^2) \, dx$, and also the linearisation of the Euler–Lagrange equation along the extremal.
Its solutions describe how nearby extremals spread apart, and their zeros define conjugate points.
For the length functional on a Riemannian manifold it becomes the equation of a [[Jacobi field|9AHMM41PJ3]].

## Explanations

### L1 human

Take an extremal curve and wiggle it slightly into a family of nearby extremals.
The small gap between the curve and its neighbours, to first order, solves the Jacobi equation.
For the functional $\int (y'^2 - y^2) \, dx$ the Jacobi equation is $h'' + h = 0$, with solutions $h = c \sin(x - x_0)$.
These solutions vanish again after a distance $\pi$, which is why this extremal stops being a minimiser on intervals longer than $\pi$.
