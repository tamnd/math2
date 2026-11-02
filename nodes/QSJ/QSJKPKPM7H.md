---
tag: QSJKPKPM7H
kind: concept
name: Singular values of a compact operator
msc: [47B10, 47B07, 15A18]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value
---

## Summary

The singular values of a compact operator $T$ between Hilbert spaces are the eigenvalues of the positive operator $\abs{T} = (T^* T)^{1/2}$, listed in decreasing order.
They extend the singular values of matrices to infinite dimensions and form a sequence that tends to $0$.
They measure how well $T$ can be approximated by finite-rank operators.
Their rate of decay defines the Schatten classes, among them the trace class and the Hilbert–Schmidt operators.

## Explanations

### L1 human

A compact operator stretches the unit ball into an infinite-dimensional ellipsoid whose axes shrink to zero.
The singular values are the lengths of these semi-axes, from the longest to the shortest.
For example, the operator on square-summable sequences that multiplies the $n$-th coordinate by $(-1)^n / n$ has singular values $1, 1/2, 1/3, \ldots$.
The faster the singular values decrease, the closer the operator is to a matrix of small size.
