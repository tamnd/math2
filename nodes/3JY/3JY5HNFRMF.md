---
tag: 3JY5HNFRMF
kind: concept
name: Square root of a positive operator
msc: [47A60, 47B65]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_a_matrix
---

## Summary

Every [[positive operator|77020CY5ZW]] $A$ on a Hilbert space has exactly one positive operator $B$ with $B^2 = A$, written $A^{1/2}$ or $\sqrt{A}$.
It extends the [[square root of a positive semidefinite matrix|0BJVDCF38Y]] to infinite dimensions.
The square root defines the absolute value $\abs{T} = (T^*T)^{1/2}$ of an operator, which enters the polar decomposition and the definition of singular values.

## Explanations

### L1 human

A positive operator behaves like a nonnegative number, so it should have a square root that is again nonnegative.
For a diagonal operator with nonnegative entries $d_1, d_2, \ldots$, the square root is the diagonal operator with entries $\sqrt{d_1}, \sqrt{d_2}, \ldots$.
An operator can have many square roots, for instance $I$ and $-I$ both square to $I$, but only one of them is positive.
