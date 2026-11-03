---
tag: W8MJBCX8MP
kind: definition
name: Quantum information
msc: [81P45, 94A15]
defines: MJC22KY2WW
uses: [HM2HHE3J51, EY0X2NKA3S, V1JTB52E8C, 10VZYJ4552, 33BRW6TMY4]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_information
---

## Definition

Quantum information theory uses the following framework.

1. A *quantum system* is described by a finite-dimensional complex [[Hilbert space|HM2HHE3J51]] $H$.
2. A *state* of the system is a [[density matrix|V1JTB52E8C]] on $H$, that is, a positive semidefinite operator of trace $1$.
3. A *process* from a system $H$ to a system $K$ is a [[quantum channel|10VZYJ4552]].
   It is a completely positive trace-preserving linear map from operators on $H$ to operators on $K$.
4. A *measurement* with finitely many outcomes is a [[POVM|33BRW6TMY4]] $(E_j)_j$ on $H$, and outcome $j$ occurs with probability $\tr(E_j \rho)$.
5. Two systems $H_A$ and $H_B$ together form the system $H_A \otimes H_B$, their [[tensor product|EY0X2NKA3S]].

*Quantum information* is the information carried by states in this framework and transformed by channels and measurements.

## Remarks

Example: a qubit is the system $H = \C^2$, and $\rho = \tfrac12 I$ is a state, since it is positive semidefinite with trace $1$.

Non-example: the matrix $\mathrm{diag}(\tfrac32, -\tfrac12)$ has trace $1$ but a negative eigenvalue, so clause 2 fails and it is not a state.

Classical information is the special case where all states and measurement operators are diagonal in one fixed basis.
Then states are probability vectors and channels are stochastic matrices.
The unit of quantum information is the qubit, and its measures include the von Neumann entropy.
