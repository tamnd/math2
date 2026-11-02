---
tag: CCR7BAQ5N5
kind: concept
name: Oscillator representation
msc: ["22E46", "22E70", 11F27]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillator_representation
same_as:
  wikidata: Q7106417
  wikipedia: Oscillator representation
---

## Summary

The oscillator representation is a unitary representation of the [[metaplectic group|8B0JM2YDE2]], the double cover of the real symplectic group, on $L^2(\R^n)$.
It exists because symplectic linear maps preserve the canonical commutation relations, and the [[Stone–von Neumann theorem|Z877XDBMQ3]] then gives an intertwining operator for each of them.
It is the real case of the Weil representation, and it underlies the theory of theta functions and the [[theta correspondence|ZBGT50BW0Z]].
Its name comes from the quantum harmonic oscillator, whose Hamiltonian generates the action of a compact one-parameter subgroup.

## Explanations

### L1 human

Linear changes of the coordinates $(x, \xi)$ of position and momentum that keep the symplectic area form are the symplectic maps.
Quantum mechanics replaces $(x, \xi)$ by operators on wave functions $\psi(x)$.
Each symplectic change of coordinates then corresponds to a unitary operator on wave functions, defined up to a sign.
For example, a quarter turn in the $(x, \xi)$ plane corresponds, up to a constant, to the Fourier transform, which swaps position and momentum.
These operators together form the oscillator representation.
