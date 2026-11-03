---
tag: D7VX8KGS1C
kind: definition
name: SIC-POVM
msc: [81P15, 81P18, 05B25]
defines: B8QDT4CCWG
uses: [33BRW6TMY4, A4Q88T5695]
sources:
  - url: https://en.wikipedia.org/wiki/SIC-POVM
---

## Definition

Let $d \ge 2$ and let $\C^d$ carry its standard inner product $\ip{\cdot}{\cdot}$.
A *SIC-POVM* in $\C^d$ consists of unit vectors $\psi_1, \dots, \psi_{d^2}$ in $\C^d$ such that
$$\abs{\ip{\psi_j}{\psi_k}}^2 = \frac{1}{d+1} \quad \text{for all } j \ne k.$$
It is used as the [[POVM|33BRW6TMY4]] whose elements are $E_j = \frac1d \lvert \psi_j \rangle \langle \psi_j \rvert$ for $j = 1, \dots, d^2$.

## Remarks

The equal overlaps force $\sum_j \lvert \psi_j \rangle \langle \psi_j \rvert = d\, I$, so $\sum_j E_j = I$ and the $E_j$ do form a POVM.
The $E_j$ are linearly independent and span all operators on $\C^d$, so the probabilities $\tr(E_j\rho)$ determine every state $\rho$.

Example: for $d = 2$, let $r_1, \dots, r_4$ be the vertices of a regular tetrahedron on the unit sphere of $\R^3$, so $r_j \cdot r_k = -1/3$ for $j \ne k$.
Let $\psi_j$ be the qubit state with [[Bloch vector|A4Q88T5695]] $r_j$.
Then $\abs{\ip{\psi_j}{\psi_k}}^2 = (1 + r_j \cdot r_k)/2 = 1/3 = 1/(d+1)$.

Non-example: the six eigenvectors of the three Pauli matrices in $\C^2$ are not a SIC-POVM.
There are $6 \ne d^2 = 4$ of them, and their pairwise overlaps take the values $0$ and $1/2$, not $1/3$.

The phrase "SIC" also denotes the set of vectors $\psi_j$ or the lines they span.
