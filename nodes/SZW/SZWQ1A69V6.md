---
tag: SZWQ1A69V6
kind: concept
name: Second quantization
msc: [81V70, 81S05, 81T05]
sources:
  - url: https://en.wikipedia.org/wiki/Second_quantization
same_as:
  wikidata: Q1353947
  wikipedia: Second quantization
---

## Summary

Second quantization is the description of systems of many [[identical particles|Y64G7W4BEC]], with a variable number of them, on the [[Fock space|1TJ8TNH331]].
It lifts operators on the one-particle Hilbert space to operators on Fock space.
A unitary $U$ becomes $\Gamma(U)$, acting as $U$ on every particle.
A self-adjoint $A$ becomes $d\Gamma(A)$, the sum of $A$ over all particles.
For bounded $A$ and an orthonormal basis $(e_j)$, it reads $d\Gamma(A) = \sum_{j,k} \ip{e_j}{A e_k}\, a^*(e_j) a(e_k)$.
Here $a^*$ and $a$ are the [[creation and annihilation operators|7N0J4DF8N5]].
It is the bridge between many-body quantum mechanics and free quantum field theory.

## Explanations

### L1 human

First quantization turns a classical particle into a wave function.
Second quantization takes many copies of that quantum particle and allows their number to change.
Instead of writing a wave function with one argument per particle, one records how many particles occupy each one-particle state.
An operator such as the total kinetic energy then becomes "the kinetic energy of each particle, added up", written with creation and annihilation operators.
The simplest case is the number operator $d\Gamma(I)$, which counts the particles.
