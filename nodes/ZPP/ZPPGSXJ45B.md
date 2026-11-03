---
tag: ZPPGSXJ45B
kind: concept
name: Bra–ket notation
msc: ["81Q10", "46C05"]
sources:
  - url: https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation
same_as:
  wikidata: Q59090
  wikipedia: Bra–ket notation
---

## Summary

Bra–ket notation, or Dirac notation, is the standard notation for vectors, linear functionals and operators on a complex [[Hilbert space|HM2HHE3J51]] in quantum mechanics.
A vector is a ket $\lvert \psi \rangle$, and the functional of inner product with $\varphi$ is a bra $\langle \varphi \rvert$.
Their pairing is the bracket $\langle \varphi \vert \psi \rangle$.
By the [[Riesz representation theorem|TTC40N49M6]], bras are exactly the continuous linear functionals.
The notation makes compositions such as $\lvert \psi \rangle\langle \varphi \rvert$ and $\langle \varphi \vert A \vert \psi \rangle$ easy to read and to compute.

## Explanations

### L1 human

A ket $\lvert \psi \rangle$ is a column vector, and a bra $\langle \varphi \rvert$ is the row vector of the complex conjugates of the entries of $\varphi$.
Putting a bra before a ket multiplies a row by a column and gives a number, the bracket $\langle \varphi \vert \psi \rangle$.
Putting a ket before a bra multiplies a column by a row and gives a matrix, $\lvert \psi \rangle\langle \varphi \rvert$.
For $\lvert 0 \rangle = (1, 0)$ and $\lvert 1 \rangle = (0, 1)$, one has $\langle 0 \vert 1 \rangle = 0$, and $\lvert 0 \rangle\langle 0 \rvert$ is the matrix $\mathrm{diag}(1, 0)$.
