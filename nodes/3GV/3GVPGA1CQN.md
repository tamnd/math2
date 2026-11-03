---
tag: 3GVPGA1CQN
kind: definition
name: Quantum entanglement
msc: [81P40, 81P42]
defines: CHNXT8CCK7
uses: [EY0X2NKA3S, 4NQN47A92F, V1JTB52E8C, 7F386TSFRW]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_entanglement
---

## Definition

Let $H_A$ and $H_B$ be complex Hilbert spaces, and let $H_A \otimes H_B$ be their [[tensor product|EY0X2NKA3S]].
A unit vector $\psi \in H_A \otimes H_B$, a pure [[quantum state|4NQN47A92F]], is a *product state* if $\psi = a \otimes b$ for some $a \in H_A$ and $b \in H_B$.
It is *entangled* if it is not a product state.
More generally, a [[density matrix|V1JTB52E8C]] $\rho$ on $H_A \otimes H_B$ is *entangled* if it is not a [[separable state|7F386TSFRW]].

## Remarks

Example: let $H_A = H_B = \C^2$ with basis $|0\rangle, |1\rangle$, and $\psi = (|00\rangle + |11\rangle)/\sqrt{2}$.
Suppose $\psi = (a_0|0\rangle + a_1|1\rangle) \otimes (b_0|0\rangle + b_1|1\rangle)$.
Comparing coefficients gives $a_0 b_0 = a_1 b_1 = 1/\sqrt{2}$ and $a_0 b_1 = a_1 b_0 = 0$.
The last two equations force one of $a_0, b_1$ and one of $a_1, b_0$ to vanish, which contradicts the first two, so $\psi$ is entangled.

Non-example: $(|00\rangle + |01\rangle)/\sqrt{2} = |0\rangle \otimes (|0\rangle + |1\rangle)/\sqrt{2}$ is a product state, so it is not entangled.

For pure states the two definitions agree: the projection $|\psi\rangle\langle\psi|$ is separable exactly when $\psi$ is a product vector.
In finite dimension, a vector $\psi = \sum_{i,j} c_{ij} e_i \otimes f_j$ is a product state exactly when the coefficient matrix $(c_{ij})$ has rank $1$.
