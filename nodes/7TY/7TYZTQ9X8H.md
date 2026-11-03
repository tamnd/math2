---
tag: 7TYZTQ9X8H
kind: definition
name: Quantum superposition
msc: ["81P16", "81P05"]
defines: 2HMDSKEZFP
uses: [HM2HHE3J51, 0V8F3E48E6, 4NQN47A92F, CKCMBP5S2P]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_superposition
---

## Definition

Let $\mathcal{H}$ be the complex [[Hilbert space|HM2HHE3J51]] of a quantum system, and let $\psi_1, \dots, \psi_k$ be unit vectors of $\mathcal{H}$, state vectors of pure [[quantum states|4NQN47A92F]].
A *superposition* of $\psi_1, \dots, \psi_k$ is a unit vector of the form
$$\psi = c_1 \psi_1 + \dots + c_k \psi_k,$$
a [[linear combination|0V8F3E48E6]] with complex coefficients $c_1, \dots, c_k$.
The *superposition principle* says that every such unit vector is the state vector of a pure state of the system.

## Remarks

Every nonzero linear combination $\chi$ gives a superposition $\chi / \norm{\chi}$.
If $\psi_1, \dots, \psi_k$ are orthonormal, the condition $\norm{\psi} = 1$ reads $\abs{c_1}^2 + \dots + \abs{c_k}^2 = 1$.

Example: in $\C^2$ with orthonormal basis $\lvert 0 \rangle, \lvert 1 \rangle$, the vector $\lvert + \rangle = (\lvert 0 \rangle + \lvert 1 \rangle)/\sqrt{2}$ has norm $1$, so it is a superposition of $\lvert 0 \rangle$ and $\lvert 1 \rangle$.
The vector $(\lvert 0 \rangle - \lvert 1 \rangle)/\sqrt{2}$ has the same moduli of coefficients, but it is orthogonal to $\lvert + \rangle$, so it is a different state.

Non-example: the [[mixed state|CKCMBP5S2P]] $\frac12 \lvert 0 \rangle\langle 0 \rvert + \frac12 \lvert 1 \rangle\langle 1 \rvert = \frac12 I$ is not a superposition of $\lvert 0 \rangle$ and $\lvert 1 \rangle$.
It is not of the form $\lvert \psi \rangle\langle \psi \rvert$ for any unit vector $\psi$, since its square is $\frac14 I$, not itself.
