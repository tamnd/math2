---
tag: 31HDBNPAH4
kind: concept
name: Quantum key distribution
msc: [81P94, 94A60]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_key_distribution
same_as:
  wikidata: Q1027298
  wikipedia: Quantum key distribution
---

## Summary

Quantum key distribution is a way for two parties to build a shared secret key by sending quantum states and talking over a public channel.
Its security rests on the laws of quantum mechanics rather than on the hardness of a computational problem.
An eavesdropper who measures the quantum states disturbs them, and the parties can detect the disturbance.
The first protocol, BB84, was proposed by Bennett and Brassard in 1984.

## Explanations

### L1 human

Two people, Alice and Bob, want a common random key to encrypt messages with a one-time pad.
Alice sends Bob qubits prepared in one of two [[mutually unbiased bases|769RHWS4WK]], chosen at random.
An eavesdropper cannot copy the qubits, by the [[no-cloning theorem|F2DKVY1NPT]], and measuring them in a wrong basis causes errors.
Alice and Bob compare a sample of their results in public; if the error rate is low, they distill a short secret key from the rest.
Unlike [[public-key cryptography|01E9MNJYEX]], this security does not depend on a hard computational problem.
