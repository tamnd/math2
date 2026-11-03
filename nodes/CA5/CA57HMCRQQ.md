---
tag: CA57HMCRQQ
kind: example
name: Bell state
msc: [81P40]
instance_of: [CHNXT8CCK7]
uses: [EY0X2NKA3S, SQ3J7AVMKM]
sources:
  - url: https://en.wikipedia.org/wiki/Bell_state
same_as:
  wikidata: Q2898260
  wikipedia: Bell state
---

## Example

Let $|0\rangle, |1\rangle$ be the standard basis of $\C^2$, and write $|jk\rangle = |j\rangle \otimes |k\rangle$ in $\C^2 \otimes \C^2$.
The four *Bell states* are
$$|\Phi^{\pm}\rangle = \frac{|00\rangle \pm |11\rangle}{\sqrt{2}}, \qquad |\Psi^{\pm}\rangle = \frac{|01\rangle \pm |10\rangle}{\sqrt{2}}.$$
They are unit vectors and pairwise orthogonal, so they form an orthonormal basis of $\C^2 \otimes \C^2$, the *Bell basis*.
Each of them is [[entangled|CHNXT8CCK7]].
For $|\Phi^+\rangle$, the coefficient matrix in the standard basis is $\tfrac{1}{\sqrt 2} I$, which has rank $2$, so it is not a product vector.
The same holds for the other three, whose coefficient matrices are also invertible.

## Remarks

The [[partial trace|SQ3J7AVMKM]] of $|\Phi^+\rangle\langle\Phi^+|$ over either factor is $\tfrac12 I$.
So each qubit alone is maximally mixed, while the pair is in a pure state: the Bell states are maximally entangled.
The state $|\Psi^-\rangle$ is the singlet; it is the unique state, up to a phase, with $(U \otimes U)|\Psi^-\rangle = \det(U)\,|\Psi^-\rangle$ for every unitary $U$ on $\C^2$.

## Explanations

### L1 human

The Bell states are the four simplest entangled states of two qubits.
In $|\Phi^+\rangle$, both qubits read $0$ or both read $1$, each with probability one half.
Neither qubit has a definite value, but they always agree.
They are the basic resource used in teleportation and superdense coding.
