---
tag: P2TBJXVGEC
kind: concept
name: Stabilizer code
msc: [81P70, 81P73, 94B60]
specializes: [M4BSARXSCC]
sources:
  - url: https://en.wikipedia.org/wiki/Stabilizer_code
same_as:
  wikidata: Q2981610
  wikipedia: Stabilizer_code
---

## Summary

A stabilizer code is a quantum code defined as the common $+1$ eigenspace of an abelian group of Pauli operators.
Most quantum codes in use are of this kind, including the Shor code, the Steane code and surface codes.
The stabilizer formalism turns questions about these codes into linear algebra over the field with two elements.
It also connects quantum codes to classical linear codes.

## Explanations

### L1 human

A Pauli operator is a tensor product of the matrices $I$, $X$, $Y$, $Z$ on several qubits.
A stabilizer code picks a few commuting Pauli operators and keeps only the states that each of them leaves unchanged.
Measuring these operators reveals the syndrome of an error without disturbing the encoded state.
For example, the states fixed by $Z_1 Z_2$ and $Z_2 Z_3$ form the span of $\lvert 000 \rangle$ and $\lvert 111 \rangle$, the three-qubit bit-flip code.
