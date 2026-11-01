---
tag: VR89YHC0TX
kind: concept
name: Eigenvalue perturbation
msc: [15A18, 47A55, 65F15]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalue_perturbation
same_as:
  wikidata: Q5348914
  wikipedia: Eigenvalue perturbation
---

## Summary

Eigenvalue perturbation studies how the [[eigenvalues|0BQAA2BK3Q]] and [[eigenvectors|0N6960W0BV]] of a matrix change when the matrix is changed by a small amount.
For a simple eigenvalue, the change is smooth, and its first-order term is given by left and right eigenvectors.
Bounds such as [[Weyl's inequality|RACSNQXDQV]] and the [[Bauer–Fike theorem|AK9J4RNZ51]] control the change without expansions.
The subject matters for numerical computation, where matrices are known only up to rounding errors.
It also matters in physics, where it is the base of perturbation theory.

## Explanations

### L1 human

Change the entries of a matrix a little and ask how its eigenvalues move.
For a symmetric matrix they move by at most the size of the change.
For example, the eigenvalues of $\begin{pmatrix} 1 & \varepsilon \\ \varepsilon & 2 \end{pmatrix}$ are $1 - \varepsilon^2 + \dots$ and $2 + \varepsilon^2 + \dots$, so they barely move.
For some non-symmetric matrices a tiny change can move the eigenvalues a lot.
