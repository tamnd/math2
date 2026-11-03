---
tag: GZYWNET8N6
kind: definition
name: Quantum logic gate
msc: [81P65, 81P68]
defines: 71CFM8DEM8
uses: [E9QTT3XBXS, MM0EJ2GDE4, EY0X2NKA3S, XAQCW3D4QQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_logic_gate
---

## Definition

Let $k \ge 1$.
A *$k$-qubit quantum logic gate* is a [[unitary operator|MM0EJ2GDE4]] $G$ on the space $(\C^2)^{\otimes k}$ of $k$ [[qubits|E9QTT3XBXS]].
It is written as a $2^k \times 2^k$ unitary matrix in the computational basis $\lvert x \rangle$, $x \in \set{0,1}^k$.
Let $n \ge k$ and let $t = (t_1, \dots, t_k)$ be distinct indices in $\set{1, \dots, n}$.
*Applying $G$ to the qubits $t$* of an $n$-qubit register means applying an operator on $(\C^2)^{\otimes n}$.
This operator acts as $G$ on the factors $t_1, \dots, t_k$, in this order, and as the identity on the other factors.

## Remarks

Example: the Hadamard gate is
$$H = \frac{1}{\sqrt2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$
It is unitary, since $H^* H = \frac12 \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I$.
Other standard one-qubit gates are the [[Pauli matrices|XAQCW3D4QQ]] $X$, $Y$, $Z$, the phase gate $S = \operatorname{diag}(1, i)$ and $T = \operatorname{diag}(1, e^{i\pi/4})$.
The controlled-NOT gate on two qubits maps $\lvert a, b \rangle$ to $\lvert a, a \oplus b \rangle$.

Non-example: the projection $\lvert 0 \rangle\langle 0 \rvert$ is not a gate.
It is not unitary, since it maps $\lvert 1 \rangle$ to $0$.
It describes part of a measurement, not a reversible step.

Two gates that differ by a global phase factor $e^{i\alpha}$ have the same effect on states.
The set $\set{H, T, \mathrm{CNOT}}$ is universal: products of these gates applied to various qubits approximate every unitary on $(\C^2)^{\otimes n}$ to any accuracy.
