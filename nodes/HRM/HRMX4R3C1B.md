---
tag: HRMX4R3C1B
kind: statement
role: theorem
name: Peres–Horodecki criterion
msc: [81P42, 81P40]
uses: [EY0X2NKA3S, V1JTB52E8C, 7F386TSFRW, CHNXT8CCK7, 09DXWYRD43, 01MMVW8CKC]
about: [7F386TSFRW]
sources:
  - url: https://en.wikipedia.org/wiki/Peres–Horodecki_criterion
same_as:
  wikidata: Q7167895
  wikipedia: Peres–Horodecki criterion
---

## Statement

Let $H_A = \C^m$ and $H_B = \C^n$, and let $\rho$ be a [[density matrix|V1JTB52E8C]] on $H_A \otimes H_B$.
Let $T$ be the [[transpose|09DXWYRD43]] map on $n \times n$ matrices.
The *partial transpose* of $\rho$ is $\rho^{T_B} = (\id \otimes T)(\rho)$, so that $(|i\rangle\langle j| \otimes |k\rangle\langle l|)^{T_B} = |i\rangle\langle j| \otimes |l\rangle\langle k|$.

1. If $\rho$ is [[separable|7F386TSFRW]], then $\rho^{T_B}$ is [[positive semidefinite|01MMVW8CKC]].
2. If $mn \le 6$, that is, for $2 \times 2$ and $2 \times 3$ systems, then $\rho$ is separable if and only if $\rho^{T_B}$ is positive semidefinite.

## Remarks

For part 1, write $\rho = \sum_i p_i \, \rho_i^A \otimes \rho_i^B$.
Then $\rho^{T_B} = \sum_i p_i \, \rho_i^A \otimes (\rho_i^B)^T$, and the transpose of a positive semidefinite matrix is positive semidefinite.
Part 2 uses a result of Størmer and Woronowicz on positive maps from $2 \times 2$ matrices to $2 \times 2$ or $3 \times 3$ matrices.
Each such map is a completely positive map plus a completely positive map composed with the transpose.

Example: for the Bell state $\psi = (|00\rangle + |11\rangle)/\sqrt{2}$, the partial transpose of $|\psi\rangle\langle\psi|$ is $\tfrac12 F$, where $F$ is the swap operator.
Its eigenvalues are $\tfrac12, \tfrac12, \tfrac12, -\tfrac12$, so the state is [[entangled|CHNXT8CCK7]].

The bound $mn \le 6$ is necessary.
In dimensions $3 \times 3$ and $2 \times 4$ there are entangled states with positive semidefinite partial transpose.
These states have bound entanglement: no entanglement can be distilled from them.

The spectrum of $\rho^{T_B}$ does not depend on the choice of basis of $H_B$, and $\rho^{T_A}$ has the same spectrum, since $\rho^{T_A} = (\rho^{T_B})^T$.

## Explanations

### L1 human

Transposing the second half of a two-part state is a simple matrix operation.
For an unentangled state, the result is still a valid state, with no negative eigenvalues.
So a negative eigenvalue after this operation proves that the state is entangled.
For two qubits, or a qubit and a qutrit, the converse also holds, so the test decides entanglement completely.

### L2 human

The criterion is the most used separability test, because it reduces to an eigenvalue computation.
It is an instance of the positive-map criterion: $\rho$ is separable if and only if $(\id \otimes \Lambda)(\rho) \ge 0$ for every positive map $\Lambda$.
The transpose is positive but not completely positive, which is what makes it detect entanglement.
The negativity, built from the negative eigenvalues of $\rho^{T_B}$, is a computable entanglement measure based on this criterion.
