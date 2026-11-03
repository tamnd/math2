---
tag: HNAKN39N1A
kind: definition
name: Density matrix
msc: ["81P16", "47B10", "46N50"]
defines: V1JTB52E8C
uses: [HM2HHE3J51, 77020CY5ZW, Z2CP530WDE]
sources:
  - url: https://en.wikipedia.org/wiki/Density_matrix
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] with inner product $\ip{\cdot}{\cdot}$.
A *density operator*, or *density matrix*, on $\mathcal{H}$ is a bounded operator $\rho$ on $\mathcal{H}$ such that:

1. $\rho$ is [[positive|77020CY5ZW]]: $\ip{\psi}{\rho\psi} \ge 0$ for all $\psi \in \mathcal{H}$;
2. $\rho$ is a [[trace class operator|Z2CP530WDE]];
3. $\operatorname{tr} \rho = 1$.

## Remarks

On a complex Hilbert space, clause 1 implies that $\rho$ is self-adjoint.
When $\mathcal{H} = \C^n$, a density matrix is a Hermitian positive semidefinite $n \times n$ matrix with trace $1$.
In general $\rho = \sum_k p_k \lvert e_k \rangle\langle e_k \rvert$ for an orthonormal family $(e_k)$ of eigenvectors and eigenvalues $p_k \ge 0$ with $\sum_k p_k = 1$.

Example: $\rho = \begin{pmatrix} 2/3 & 1/3 \\ 1/3 & 1/3 \end{pmatrix}$ is Hermitian with trace $1$.
Its diagonal entries are positive and its determinant is $2/9 - 1/9 = 1/9 > 0$, so both eigenvalues are positive and $\rho$ is a density matrix.

Non-example: $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ is Hermitian with trace $1$, but its determinant is $-1 < 0$.
So one eigenvalue is negative, and clause 1 fails.
