---
tag: F1K9J81GCT
kind: concept
name: Quantum operation
msc: [81P47, 81P16, 46L60]
specializes: [CGY299QMC3]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_operation
same_as:
  wikidata: Q7269080
  wikipedia: Quantum operation
---

## Summary

A quantum operation is a linear map on density operators that describes a physical process applied to a quantum system.
The process may include the selection of a measurement outcome.
It is a [[completely positive map|CGY299QMC3]] that does not increase the trace.
Unitary evolution, interaction with an environment followed by discarding it, and a measurement with a recorded outcome are all quantum operations.
Those that preserve the trace are the [[quantum channels|10VZYJ4552]].

## Explanations

### L1 human

A quantum operation is the most general thing one can do to a quantum state, as long as the result is again a possible state, up to scaling.
Complete positivity means that it still gives valid states when the system is entangled with another one that is left untouched.
The trace may decrease because an operation can include the event "outcome $k$ occurred", whose probability is the trace of the output.
For example, projecting a qubit onto $e_0$ maps $\rho$ to $P\rho P$ with $P = e_0e_0^*$, and the trace of the output is the probability of the outcome $0$.
