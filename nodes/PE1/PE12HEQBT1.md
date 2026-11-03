---
tag: PE12HEQBT1
kind: definition
name: Qubit
msc: [81P45, 81P68]
defines: E9QTT3XBXS
uses: [HM2HHE3J51, 4NQN47A92F, V1JTB52E8C, 2HMDSKEZFP]
sources:
  - url: https://en.wikipedia.org/wiki/Qubit
---

## Definition

A *qubit* is a quantum system whose [[Hilbert space|HM2HHE3J51]] is $\C^2$ with its standard inner product.
The standard basis vectors are written $|0\rangle = (1, 0)$ and $|1\rangle = (0, 1)$ and form the *computational basis*.
A pure [[state|4NQN47A92F]] of a qubit is given by a unit vector
$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \qquad \alpha, \beta \in \C, \quad \abs{\alpha}^2 + \abs{\beta}^2 = 1.$$
Here two unit vectors give the same state when they differ by a factor $e^{i\theta}$ with $\theta \in \R$.
A general state of a qubit is a [[density matrix|V1JTB52E8C]] on $\C^2$.

## Remarks

Example: $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ is a pure state, since $\abs{1/\sqrt2}^2 + \abs{1/\sqrt2}^2 = 1$.
It is a [[superposition|2HMDSKEZFP]] of the two basis states, and a measurement in the computational basis gives each outcome with probability $\tfrac12$.

Non-example: the vector $|0\rangle + |1\rangle$ has squared norm $2$, so it is not a unit vector and does not define a state as written.

For example, $|\psi\rangle$ and $-|\psi\rangle$ describe the same state.
Since unit vectors that differ by a phase give the same state, the pure states form the complex projective line $\mathbb{CP}^1$.
A system of $n$ qubits has Hilbert space $(\C^2)^{\otimes n}$, with computational basis $|x_1 \cdots x_n\rangle$ for $x_i \in \set{0, 1}$.
