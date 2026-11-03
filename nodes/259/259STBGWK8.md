---
tag: 259STBGWK8
kind: concept
name: Quantum statistical mechanics
msc: [82B10, 82C10, 46L60]
specializes: [X3QSEMFQWW]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_statistical_mechanics
same_as:
  wikidata: Q845260
  wikipedia: Quantum statistical mechanics
---

## Summary

Quantum statistical mechanics is [[statistical mechanics|X3QSEMFQWW]] for systems obeying quantum mechanics.
Probability distributions over microstates are replaced by density operators on a Hilbert space, and averages by traces.
The thermal equilibrium state at inverse temperature $\beta$ is the Gibbs state $e^{-\beta H} / \tr e^{-\beta H}$, and for infinite systems it is replaced by a [[KMS state|HJ7TMS0WKY]].
It explains phenomena with no classical analogue, such as Bose–Einstein condensation and the specific heat of solids at low temperature.

## Explanations

### L1 human

In quantum mechanics a system can be in a superposition of states, and measurements are random even when the state is known.
Quantum statistical mechanics adds a second layer of randomness: we also do not know which quantum state the system is in.
Both layers are packed into one object, the density operator.
For a spin that is equally likely to point up or down, the density operator is half the identity matrix.
Then every measurement of the spin along any axis gives $\pm 1$ with equal probability.
