---
tag: JYHQQGGZJZ
kind: concept
name: Channel capacity of a quantum channel
msc: [81P47, 94A40, 81P45]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_capacity
same_as:
  wikidata: Q7269015
  wikipedia: Quantum capacity
---

## Summary

The quantum capacity of a [[quantum channel|10VZYJ4552]] is the largest rate at which quantum information can be sent reliably through many uses of the channel.
The rate is counted in qubits per channel use.
The Lloyd–Shor–Devetak theorem expresses it through the coherent information.
A channel also has a classical capacity, for sending bits, which is a different quantity.

## Explanations

### L1 human

A quantum channel is a noisy link that carries quantum states, such as an optical fibre that loses photons.
One may encode many qubits into many uses of the channel and decode at the other end.
The quantum capacity is the best number of qubits per use that can be sent with an error that goes to zero.
A perfect qubit channel has capacity $1$.
A channel whose output does not depend on its input has capacity $0$.
