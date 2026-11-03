---
tag: 71CFM8DEM8
kind: concept
name: Quantum logic gate
msc: [81P65, 81P68]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_logic_gate
same_as:
  wikidata: Q2118982
  wikipedia: Quantum logic gate
---

## Summary

A quantum logic gate is a unitary operation on a small number of qubits.
Gates are the elementary steps of a quantum computation, as logic gates are for classical circuits.
Common gates are the Pauli gates, the Hadamard gate, the phase gates and the controlled-NOT gate.
A small set of gates is universal: its products approximate every unitary operation.

## Explanations

### L1 human

A classical gate, such as NOT, takes bits to bits.
A quantum gate takes the state of a few qubits to a new state by a unitary matrix, so it can always be undone.
The NOT gate becomes the matrix that swaps $\lvert 0 \rangle$ and $\lvert 1 \rangle$.
The Hadamard gate has no classical analogue: it turns $\lvert 0 \rangle$ into an equal superposition of $\lvert 0 \rangle$ and $\lvert 1 \rangle$.
The controlled-NOT gate flips a second qubit when the first one is $1$, and it can create entanglement.
