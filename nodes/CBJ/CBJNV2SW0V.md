---
tag: CBJNV2SW0V
kind: example
name: Two-state quantum system
msc: [81Q80, 81Q05]
illustrates: [VXDEQB46GV]
uses: [VXDEQB46GV, XAQCW3D4QQ, E9QTT3XBXS, 0P17NGQQMQ, A4Q88T5695]
sources:
  - url: https://en.wikipedia.org/wiki/Two-state_quantum_system
same_as:
  wikidata: Q243821
  wikipedia: Two-state quantum system
---

## Example

A *two-state quantum system* has the state space $\C^2$, and its [[Hamiltonian|VXDEQB46GV]] is a $2 \times 2$ [[Hermitian matrix|0P17NGQQMQ]] $H$.
Every such matrix can be written $H = a I + b_1 \sigma_x + b_2 \sigma_y + b_3 \sigma_z$ with $a \in \R$ and $b = (b_1, b_2, b_3) \in \R^3$, where $\sigma_x, \sigma_y, \sigma_z$ are the [[Pauli matrices|XAQCW3D4QQ]].
Since $(b_1\sigma_x + b_2\sigma_y + b_3\sigma_z)^2 = \abs{b}^2 I$, the eigenvalues of $H$ are $a \pm \abs{b}$.

Rabi oscillation: let $\Omega > 0$ and $H = \frac{\hbar\Omega}{2} \sigma_x$, and start in the state $e_0 = (1, 0)$.
Because $\sigma_x^2 = I$, the evolution operator is $e^{-iHt/\hbar} = \cos(\Omega t/2) I - i \sin(\Omega t/2) \sigma_x$.
So the state at time $t$ is $\cos(\Omega t/2) e_0 - i \sin(\Omega t/2) e_1$ with $e_1 = (0, 1)$.
The probability of finding the system in $e_1$ is $\sin^2(\Omega t/2)$, which swings between $0$ and $1$.

## Explanations

### L1 human

The simplest quantum system has just two basic states, such as spin up and spin down.
Every state is a combination of the two, and the energy is a $2 \times 2$ Hermitian matrix.
Under a constant coupling, the system swings back and forth between the two states, like two linked pendulums trading energy.
The same model describes a [[qubit|E9QTT3XBXS]], and its states can be drawn as points of the [[Bloch sphere|A4Q88T5695]].
