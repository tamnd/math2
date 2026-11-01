---
tag: DM59GHSMAJ
kind: definition
name: Hadamard matrix
msc: [05B20]
defines: J0N4J606X0
uses: [0N1MY1T0W9, 0W809K6AW0, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_matrix
---

## Definition

Let $n$ be a positive integer.
A Hadamard matrix of order $n$ is an $n \times n$ [[matrix|0N1MY1T0W9]] $H$ with entries in $\set{1, -1}$ such that $H H^T = n I_n$.
Here $H^T$ is the [[transpose|0W809K6AW0]] of $H$ and $I_n$ is the [[identity matrix|06DW9BAWB1]] of size $n$.

## Remarks

The condition says that any two distinct rows have dot product $0$, so they agree in exactly $n/2$ places.
Since $H^{-1} = H^T / n$, also $H^T H = n I_n$, so the columns are pairwise orthogonal as well.
Example: $H_2 = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ satisfies $H_2 H_2^T = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2 I_2$.
The [[Kronecker product|0JK6M18QZH]] of two Hadamard matrices is a Hadamard matrix, so the Kronecker powers of $H_2$ give Hadamard matrices of every order $2^k$.
Non-example: no $3 \times 3$ matrix with entries $\pm 1$ is Hadamard, since the dot product of two rows is a sum of three terms $\pm 1$, which is odd and so not $0$.
A Hadamard matrix of order $n$ can exist only if $n = 1$, $n = 2$ or $n$ is a multiple of $4$; the [[Hadamard conjecture|6X9S10E3M2]] asks whether all multiples of $4$ occur.
For such $H$, $\abs{\det H} = n^{n/2}$.
