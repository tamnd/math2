---
tag: VKGVCS860K
kind: definition
name: Observable
msc: ["81Q10", "47B25", "46N50"]
defines: DF5RN297GE
uses: [HM2HHE3J51, 0NEGN5CRSC, KRJX5RA0PW, BCJHNHKQFG, BMKATJ802A, 18KPYRRPZY, ATGT25E5FF]
sources:
  - url: https://en.wikipedia.org/wiki/Observable
---

## Definition

Let $\mathcal{H}$ be the complex [[Hilbert space|HM2HHE3J51]] of a quantum system.
An *observable* of the system is a [[self-adjoint operator|0NEGN5CRSC]] $A$ on $\mathcal{H}$.
Here $A$ may be [[unbounded|KRJX5RA0PW]]: it is a linear map $A \colon D(A) \to \mathcal{H}$ on a [[dense|BCJHNHKQFG]] subspace $D(A)$, and self-adjoint means $A = A^*$, with equal domains.

## Remarks

The [[spectrum|BMKATJ802A]] $\sigma(A)$ of an observable is a closed subset of $\R$; its points are the possible results of a measurement of $A$.
By the [[spectral theorem|18KPYRRPZY]], $A$ has a unique [[projection-valued measure|ATGT25E5FF]] $P^A$ on the Borel sets of $\R$ with $A = \int_\R \lambda \, dP^A(\lambda)$.
The eigenvectors of $A$ are the states in which a measurement of $A$ gives one value with certainty.

Example: the matrix $\sigma_z = \mathrm{diag}(1, -1)$ on $\C^2$ is self-adjoint, so it is an observable.
Its spectrum is $\set{1, -1}$, and $P^{\sigma_z}(\set{1}) = \mathrm{diag}(1, 0)$.

Non-example: $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ on $\C^2$ is not an observable, since $N^* = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \ne N$.
It has the single eigenvalue $0$ but no basis of eigenvectors, so it has no projection-valued measure.

For unbounded operators, being symmetric, $\ip{A\psi}{\varphi} = \ip{\psi}{A\varphi}$ on $D(A)$, is weaker than self-adjoint, and only self-adjoint operators have a spectral theorem.
Generalised measurements are described by positive operator-valued measures instead of single observables.
