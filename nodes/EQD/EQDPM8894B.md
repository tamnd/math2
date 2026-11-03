---
tag: EQDPM8894B
kind: concept
name: Quantum dynamical semigroup
msc: [81S22, 47D07, 46L57]
specializes: [EVF180QJXY]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Markov_semigroup
same_as:
  wikidata: Q107285103
  wikipedia: Quantum Markov semigroup
---

## Summary

A quantum dynamical semigroup, or quantum Markov semigroup, is a continuous one-parameter family of [[quantum channels|10VZYJ4552]] $(T_t)_{t \ge 0}$ with $T_0 = \id$ and $T_{s+t} = T_s T_t$.
It models the time evolution of an [[open quantum system|6D9YCNZ7X9]] without memory, the quantum analogue of a Markov process.
Its generator has a standard form, given by the Gorini–Kossakowski–Sudarshan–Lindblad theorem in the norm-continuous case.

## Explanations

### L1 human

For a closed system, time evolution is a family of unitary maps, and evolving for time $s$ and then for time $t$ is the same as evolving for $s + t$.
For an open system without memory of its past, the same composition rule holds, but each step is a quantum channel rather than a unitary map.
Such a family is a quantum dynamical semigroup.
For example, a qubit that loses coherence at a constant rate keeps its diagonal entries and has its off-diagonal entries multiplied by $e^{-\gamma t}$ after time $t$.
