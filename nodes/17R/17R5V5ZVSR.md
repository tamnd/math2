---
tag: 17R5V5ZVSR
kind: concept
name: Polyharmonic function
msc: [31B30, 35J30]
sources:
  - url: https://en.wikipedia.org/wiki/Biharmonic_equation
---

## Summary

A polyharmonic function of order $m$ is a function whose $m$-fold iterated [[Laplacian|0E0B6RA8K0]] vanishes: $\Delta^m u = 0$.
For $m = 1$ these are the [[harmonic functions|0DEB0JMN0W]], and for $m = 2$ the solutions of the [[biharmonic equation|AS8A9F5SKE]].
Polyharmonic functions are the model solutions of higher-order elliptic equations.
They appear in elasticity and in the study of polyharmonic splines and interpolation.

## Explanations

### L1 human

Take the Laplacian of a function, then the Laplacian of the result, and so on, $m$ times.
If you end up with zero, the function is polyharmonic of order $m$.
For example, $\abs{x}^2$ on $\R^n$ is not harmonic, but its Laplacian is the constant $2n$, so it is polyharmonic of order $2$.
Every polynomial of degree less than $2m$ is polyharmonic of order $m$, because each Laplacian lowers the degree by $2$.
