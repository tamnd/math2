---
tag: M3MS1YP76J
kind: definition
name: Quantum teleportation
msc: [81P48, 81P45]
defines: R27Q22DS55
uses: [E9QTT3XBXS, CA57HMCRQQ, XAQCW3D4QQ, F5EB23T03M, EY0X2NKA3S, F2DKVY1NPT, ESN2Y09QGQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_teleportation
---

## Definition

Let $X$ and $Z$ be the [[Pauli matrices|XAQCW3D4QQ]] $\sigma_x$ and $\sigma_z$.
Let $|\Phi^\pm\rangle, |\Psi^\pm\rangle$ be the [[Bell states|CA57HMCRQQ]] of two [[qubits|E9QTT3XBXS]].
Alice holds a qubit $S$ in a state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, and Alice and Bob share two qubits $A$ and $B$ in the state $|\Phi^+\rangle_{AB}$.
*Quantum teleportation* is the following [[LOCC|F5EB23T03M]] protocol.

1. Alice measures the pair $SA$ in the Bell basis $|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle$.
2. Alice sends the outcome, two classical bits, to Bob.
3. Bob applies to $B$ the correction $I$, $Z$, $X$ or $ZX$ for the outcomes $\Phi^+$, $\Phi^-$, $\Psi^+$, $\Psi^-$ respectively.

After step 3, the qubit $B$ is in the state $|\psi\rangle$, up to a global phase.

## Remarks

The check rests on the identity
$$|\psi\rangle_S |\Phi^+\rangle_{AB} = \tfrac12 \big( |\Phi^+\rangle_{SA} |\psi\rangle_B + |\Phi^-\rangle_{SA} Z|\psi\rangle_B + |\Psi^+\rangle_{SA} X|\psi\rangle_B + |\Psi^-\rangle_{SA} XZ|\psi\rangle_B \big),$$
which follows by expanding both sides in the standard basis.
Each outcome has probability $\tfrac14$, and the correction undoes the Pauli factor, since $Z^2 = X^2 = I$ and $ZX \cdot XZ = I$.

Non-example: if Bob applies no correction, then for the outcomes $\Phi^-$, $\Psi^+$, $\Psi^-$ he holds $Z|\psi\rangle$, $X|\psi\rangle$ or $XZ|\psi\rangle$, which in general differ from $|\psi\rangle$.
Averaged over Alice's outcomes, his state is $\tfrac12 I$, independent of $\psi$.
This is the [[no-communication theorem|ESN2Y09QGQ]] at work: without the classical bits, Bob learns nothing.

At the end, the qubits $S$ and $A$ are in a Bell state that carries no information about $\psi$, in agreement with the [[no-cloning theorem|F2DKVY1NPT]].
The protocol works by linearity for mixed states and for a qubit that is entangled with other systems.
