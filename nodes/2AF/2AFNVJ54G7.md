---
tag: 2AFNVJ54G7
kind: concept
name: Projection method for integral equations
msc: [45L05, 65R20, 47A58]
sources:
  - url: https://en.wikipedia.org/wiki/Galerkin_method
---

## Summary

A projection method approximates the solution of an operator equation by an element of a finite-dimensional subspace.
The main case is an [[integral equation of the second kind|8KJCN49V64]].
One chooses subspaces $X_n$ and projections $P_n$ onto them, and asks that the equation holds after applying $P_n$.
This gives a finite linear system for the coefficients of the approximation.
The [[Galerkin method|Y5B0PEBKE8]] (orthogonal projection) and the collocation method (interpolation) are the two main cases.

## Explanations

### L1 human

An integral equation asks for a whole function, which is infinitely many numbers.
A projection method looks only among simple functions, for instance polynomials of degree at most $n$ or piecewise linear functions on a grid.
It cannot satisfy the equation exactly, so it asks that the error is invisible to the projection: zero at chosen points (collocation) or orthogonal to the chosen functions (Galerkin).
For example, for $\varphi(x) - \int_0^1 x t \, \varphi(t) \, dt = x$ on $[0, 1]$ with $X_1$ the multiples of $x$, the Galerkin method gives $\varphi = \frac{3}{2} x$, which here is the exact solution.
