---
tag: S82TXJB05T
kind: concept
name: Quantum circuit
msc: [81P68, 68Q12, 81P65]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_circuit
same_as:
  wikidata: Q2122210
  wikipedia: Quantum circuit
---

## Summary

A quantum circuit is a finite sequence of quantum gates applied to chosen qubits of a register.
It is the standard model of quantum computation, the quantum analogue of a [[Boolean circuit|SQXNFGVADX]].
Its size is the number of gates and its depth is the number of layers of gates that act on disjoint qubits.
The cost of a quantum algorithm is usually measured by the size of its circuits.

## Explanations

### L1 human

Picture each qubit as a horizontal wire, with time running from left to right.
Gates are boxes placed on one or more wires.
The circuit applies the boxes one after another, and the overall effect is the product of their matrices.
For example, a Hadamard gate on the first wire followed by a controlled-NOT from the first wire to the second turns $\lvert 00 \rangle$ into the entangled state $(\lvert 00 \rangle + \lvert 11 \rangle)/\sqrt2$.
