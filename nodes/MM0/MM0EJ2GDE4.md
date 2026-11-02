---
tag: MM0EJ2GDE4
kind: concept
name: Unitary operator
msc: [47B15, 47A05]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_operator
same_as:
  wikidata: Q1972470
  wikipedia: Unitary operator
---

## Summary

A unitary operator is a bounded linear operator $U$ on a Hilbert space with $U^*U = UU^* = I$.
Equivalently, it is a surjective linear map that preserves the inner product.
Unitary operators are the isomorphisms of Hilbert spaces, so two operators that differ by conjugation with a unitary operator have the same properties.
They extend [[unitary matrices|0AR68JTMDT]] to infinite dimensions and describe the time evolution in quantum mechanics.

## Explanations

### L1 human

A unitary operator is a rigid motion of a Hilbert space that can be undone.
It keeps all lengths and all angles, and every vector is hit by it.
The Fourier transform on $L^2(\R)$, suitably normalized, is a unitary operator.
A simpler example is the shift on two-sided sequences, $(Ux)_n = x_{n-1}$ on $\ell^2(\Z)$: it moves every entry one step to the right and is undone by the shift to the left.
