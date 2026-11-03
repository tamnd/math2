---
tag: MW7HC0YKQ5
kind: definition
name: Entanglement witness
msc: [81P42, 81P40]
defines: B666NC2H30
uses: [EY0X2NKA3S, V1JTB52E8C, 7F386TSFRW, 0P17NGQQMQ, 0XC1RDBY7A]
sources:
  - url: https://en.wikipedia.org/wiki/Entanglement_witness
---

## Definition

Let $H_A$ and $H_B$ be finite-dimensional complex Hilbert spaces.
An *entanglement witness* is a [[Hermitian|0P17NGQQMQ]] operator $W$ on $H_A \otimes H_B$ such that:

1. $\tr(W \sigma) \ge 0$ for every [[separable state|7F386TSFRW]] $\sigma$ on $H_A \otimes H_B$.
2. $\tr(W \rho) < 0$ for at least one [[density matrix|V1JTB52E8C]] $\rho$ on $H_A \otimes H_B$.

A state $\rho$ with $\tr(W\rho) < 0$ is said to be *detected* by $W$.

## Remarks

Example: let $H_A = H_B = \C^2$ and let $W = F$ be the swap operator, $F(u \otimes v) = v \otimes u$.
For a product state, $\tr(F \, \sigma_A \otimes \sigma_B) = \tr(\sigma_A \sigma_B) \ge 0$, and clause 1 follows by linearity.
For the singlet $\psi = (|01\rangle - |10\rangle)/\sqrt{2}$, one has $F\psi = -\psi$, so $\tr(F |\psi\rangle\langle\psi|) = -1$ and clause 2 holds.

Non-example: the identity $I$ satisfies clause 1 but fails clause 2, since $\tr(I\rho) = 1$ for every state.
The operator $-F$ fails clause 1, since $\tr(-F \, |00\rangle\langle 00|) = -1$.

Since the separable states form a compact [[convex set|02AS45T3H9]], the separating hyperplane theorem gives: for every entangled state $\rho$ there is a witness $W$ that detects $\rho$.
