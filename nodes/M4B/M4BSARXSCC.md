---
tag: M4BSARXSCC
kind: concept
name: Quantum error correction
msc: [81P73, 81P70]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_error_correction
same_as:
  wikidata: Q1536431
  wikipedia: Quantum error correction
---

## Summary

Quantum error correction protects quantum information from noise by encoding it into a subspace of a larger system.
It plays for quantum states the role that [[error-correcting codes|TAE6K8NQ46]] play for bits.
It is possible despite the [[no-cloning theorem|F2DKVY1NPT]] and despite the continuum of possible errors.
It is the basis of fault-tolerant quantum computation.

## Explanations

### L1 human

Classical data are protected by redundancy, for example by sending each bit three times and taking a majority vote.
Qubits cannot be copied, and measuring them destroys superpositions, so this simple idea does not carry over directly.
Quantum codes spread one logical qubit over several physical qubits as an entangled state.
One can then measure only which error happened, the syndrome, without learning the encoded state, and undo that error.
The three-qubit code that encodes $a\lvert 0 \rangle + b \lvert 1 \rangle$ as $a \lvert 000 \rangle + b \lvert 111 \rangle$ corrects a flip of any one qubit.
