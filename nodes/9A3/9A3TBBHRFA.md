---
tag: 9A3TBBHRFA
kind: concept
name: Hurwitz-stable matrix
msc: [15A18, 34D20, 93D20]
specializes: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz-stable_matrix
same_as:
  wikidata: Q131293245
  wikipedia: Hurwitz-stable matrix
---

## Summary

A Hurwitz-stable matrix is a [[square matrix|0JXZKX526R]] whose [[eigenvalues|0BQAA2BK3Q]] all have negative real part.
These are exactly the matrices $A$ for which every solution of $x' = A x$ tends to $0$.
Through linearisation they also decide the [[exponential stability|VY180V8QY2]] of equilibria of nonlinear systems.
They are also called stable matrices or Hurwitz matrices.
See the [[definition|R3VWS51XY5]].

## Explanations

### L1 human

Each eigenvalue $\lambda$ of $A$ contributes terms like $e^{\lambda t}$ to the solutions of $x' = Ax$.
When the real part of $\lambda$ is negative, such a term dies out, possibly while rotating.
So a Hurwitz-stable matrix is one whose linear system always returns to rest.
For example, $\begin{pmatrix} -1 & 2 \\ 0 & -3 \end{pmatrix}$ is Hurwitz-stable, with eigenvalues $-1$ and $-3$.
