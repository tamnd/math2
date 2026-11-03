---
tag: KZ7RZC8XC4
kind: concept
name: Weight space
msc: ["17B10", "17B20"]
sources:
  - url: https://en.wikipedia.org/wiki/Weight_(representation_theory)
---

## Summary

A weight space of a representation of a Lie algebra is a common eigenspace of a family of commuting operators.
For a linear form $\lambda$ on a subalgebra $\mathfrak{h}$, it is the set of vectors $v$ with $h \cdot v = \lambda(h) v$ for all $h \in \mathfrak{h}$.
A finite-dimensional representation of a complex semisimple Lie algebra is the direct sum of its weight spaces for a Cartan subalgebra.
The roots of a Lie algebra are the nonzero weights of its adjoint representation.

## Explanations

### L1 human

An eigenvector of one matrix is a vector that the matrix only stretches.
A weight vector is a vector that a whole family of commuting matrices only stretches, each by its own factor.
The list of factors is the weight, and all vectors with the same list form the weight space.
For example, the diagonal matrices of size $2$ act on $\C^2$, and the first basis vector spans the weight space where $\operatorname{diag}(a, b)$ acts by $a$.
