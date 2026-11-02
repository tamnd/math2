---
tag: 6HSJBJ8TTQ
kind: concept
name: Hilbert space adjoint
msc: [47A05, 47B02]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
---

## Summary

The adjoint of a bounded operator $T \colon H \to K$ between Hilbert spaces is the bounded operator $T^* \colon K \to H$ characterised by $\ip{Tx}{y} = \ip{x}{T^* y}$.
It extends the [[adjoint of a linear map|0R9NMSM1ZP]] between finite-dimensional inner product spaces, and the conjugate transpose of matrices.
The adjoint is used to define self-adjoint, normal, unitary and positive operators, and it makes the bounded operators on a Hilbert space a C*-algebra.

## Explanations

### L1 human

The adjoint lets one move an operator from one side of an inner product to the other.
For a complex matrix, it is the conjugate transpose.
For the right shift on square-summable sequences, which moves every entry one place to the right, the adjoint is the left shift, which deletes the first entry.
Operators equal to their own adjoint play the role of real numbers among operators.
