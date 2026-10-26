---
tag: 08ZWFDJP3H
kind: concept
name: Eigenvalue method for linear systems
msc: [34A30]
uses: [0VJF99CZ0Z, 0MQ24RBG93]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_differential_equation
    locator: Solution in matrix form
  - url: https://en.wikipedia.org/wiki/Phase_plane
    locator: Solving using eigenvalues
---

## Summary

The eigenvalue method solves a [[homogeneous linear system with constant coefficients|0VJF99CZ0Z]] $x' = A x$ with the eigenvalues and eigenvectors of $A$.
If $A v = \lambda v$ with $v \ne 0$, then $x(t) = e^{\lambda t} v$ is a solution.
If $A$ has $n$ linearly independent eigenvectors $v_1, \dots, v_n$ with eigenvalues $\lambda_1, \dots, \lambda_n$, then each solution is $x(t) = c_1 e^{\lambda_1 t} v_1 + \dots + c_n e^{\lambda_n t} v_n$ for unique constants $c_k$.
For a complex eigenvalue $\lambda$ of a real matrix with eigenvector $v$, the real and imaginary parts of $e^{\lambda t} v$ are two real solutions.

## Remarks

Example: $A = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}$ has the eigenvalues $3$ and $-1$, with eigenvectors $(1, 2)$ and $(1, -2)$. So $x(t) = c_1 e^{3t} (1, 2) + c_2 e^{-t} (1, -2)$.
If $A$ has too few eigenvectors, generalized eigenvectors give solutions of the form $e^{\lambda t}$ times a polynomial in $t$ with vector coefficients.
The eigenvalues decide the [[stability of the system|0SKVEMXJWF]].

## Explanations

### L1 human

Along an eigenvector, the matrix $A$ acts as multiplication by a number.
So on this line the system is the simple equation $y' = \lambda y$, with solution $e^{\lambda t}$.
Write the start vector in a basis of eigenvectors, and let each part grow or decay at its own rate.
