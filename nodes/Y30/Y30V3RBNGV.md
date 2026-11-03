---
tag: Y30V3RBNGV
kind: concept
name: Fredholm module
msc: [19K33, 58B34, 46L87]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_module
same_as:
  wikidata: Q5499350
  wikipedia: Fredholm module
---

## Summary

A Fredholm module over a C*-algebra $A$ is a representation of $A$ on a Hilbert space with an extra operator $F$.
The operator $F$ behaves like the phase of an elliptic operator.
It is unitary and self-adjoint up to compact operators, and it commutes with $A$ up to compact operators.
Fredholm modules are the cycles of K-homology, and they pair with K-theory through Fredholm indices.
They are the bounded counterpart of [[spectral triples|FTQMQR3YS7]] in Connes' noncommutative geometry.

## Explanations

### L1 human

On a closed manifold, an elliptic differential operator $D$ such as the Dirac operator gives a Fredholm operator.
Its bounded "phase" $F = D (1 + D^2)^{-1/2}$ almost commutes with multiplication by continuous functions, with a compact error.
A Fredholm module keeps just these features: a Hilbert space on which the algebra acts, and an operator $F$ that is almost a symmetry and almost commutes with the algebra.
This abstract form makes sense for noncommutative algebras, where there are no points or differential operators.
