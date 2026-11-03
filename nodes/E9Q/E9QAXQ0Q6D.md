---
tag: E9QAXQ0Q6D
kind: definition
name: Quantum state
msc: ["81P16", "46N50"]
defines: 4NQN47A92F
uses: [HM2HHE3J51, V1JTB52E8C, 0B8KZRT28M, RC1C7WXX1H]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_state
---

## Definition

Let $\mathcal{H}$ be the complex [[Hilbert space|HM2HHE3J51]] of a quantum system.
A *quantum state* of the system is a [[density operator|V1JTB52E8C]] $\rho$ on $\mathcal{H}$.
The state is *pure* when $\rho$ is an [[orthogonal projection|0B8KZRT28M]] of rank $1$, that is, $\rho \chi = \ip{\psi}{\chi}\, \psi$ for all $\chi \in \mathcal{H}$, for some unit vector $\psi \in \mathcal{H}$.
Here $\ip{\cdot}{\cdot}$ is conjugate-linear in the first argument and linear in the second.

## Remarks

The unit vector $\psi$ of a pure state is unique up to a factor $e^{i\theta}$ with $\theta \in \R$.
So the pure states correspond one to one to the points of the [[projective Hilbert space|RC1C7WXX1H]] of $\mathcal{H}$, and one often calls $\psi$ itself the state, or the *state vector*.

A density operator $\rho$ is pure if and only if $\rho^2 = \rho$, if and only if $\operatorname{tr}(\rho^2) = 1$.

Example: on $\C^2$ with $\psi = (1, 1)/\sqrt{2}$, the state is $\rho = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
It is positive with trace $1$, and $\rho^2 = \rho$, so it is a pure state.

Non-example: the identity $I$ on $\C^2$ is positive, but its trace is $2$, so it is not a state.
Its multiple $\frac12 I$ is a state, but not a pure one, since $(\frac12 I)^2 = \frac14 I \ne \frac12 I$.
