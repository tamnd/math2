---
tag: A8D05RKX8M
kind: concept
name: Fidelity of quantum states
msc: [81P47, 81P16]
sources:
  - url: https://en.wikipedia.org/wiki/Fidelity_of_quantum_states
same_as:
  wikidata: Q5446796
  wikipedia: Fidelity of quantum states
---

## Summary

The fidelity of two quantum states is a number between $0$ and $1$ that measures how close they are.
It equals $1$ exactly when the states are equal, and it equals $0$ when the states can be told apart with certainty.
For pure states it is the squared overlap of the state vectors.
It is used to judge the quality of state preparation, teleportation, cloning and error correction.

## Explanations

### L1 human

Fidelity answers the question "how similar are these two quantum states?"
For two unit vectors $\psi$ and $\phi$ it is $\abs{\ip{\psi}{\phi}}^2$, the square of the cosine of the angle between them.
So $\lvert 0 \rangle$ and $\lvert 1 \rangle$ have fidelity $0$, while $\lvert 0 \rangle$ and $(\lvert 0 \rangle + \lvert 1 \rangle)/\sqrt 2$ have fidelity $1/2$.
For mixed states the formula is more involved, but it keeps the same meaning.
