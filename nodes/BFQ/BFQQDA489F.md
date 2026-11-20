---
tag: BFQQDA489F
kind: statement
role: theorem
name: Simultaneous unitary diagonalization of commuting normal operators
aliases: [simultaneous-unitary-diagonalization, commuting-normal-matrices-are-simultaneously-diagonalizable]
msc: ["15A21", "47B15"]
topics: [3YM9EK6VMB]
audience: ug2
about: [0C8BR8XRTR]
uses: [0ENZN5G4CV, 0MB8HQW495, 0FWJ0VW561, 0B5H4208Z9, 0D6RMJ10M9, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: Consequences
---

## Statement

1. Complex case. Let $V$ be a finite-dimensional complex inner product space, and let $\mathcal{F}$ be a set of [[normal|0ENZN5G4CV]] operators on $V$. Then $V$ has an [[orthonormal basis|0FWJ0VW561]] whose vectors are [[eigenvectors|0B5H4208Z9]] of every member of $\mathcal{F}$ if and only if $S T = T S$ for all $S, T \in \mathcal{F}$.
2. Real case. The same holds for a finite-dimensional real inner product space and a set $\mathcal{F}$ of [[self-adjoint|0MB8HQW495]] operators.
3. Matrix form. Let $A_1, \dots, A_k$ be complex normal $n \times n$ matrices. Then there is one [[unitary matrix|0D6RMJ10M9]] $U$ such that every $U^* A_j U$ is diagonal if and only if the $A_j$ commute pairwise. For real symmetric matrices, $U$ can be a real [[orthogonal matrix|0QRBVFJ50X]].

## Remarks

### Why each hypothesis is needed

- Commutation is needed. [[The matrices $\operatorname{diag}(1, -1)$ and $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$|2YEX40VH77]] are both symmetric, but they do not commute, and they have no common eigenvector.
- Normality is needed for an orthonormal basis. Two commuting diagonalizable matrices have a common basis of eigenvectors, but it need not be orthonormal. For example, $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ commutes with itself, and it has [[no orthonormal eigenbasis|5RQ7EC5RC6]].
- Over $\mathbb{R}$, normal operators are not enough: [[the rotation by a right angle|1CF483TZZA]] commutes with itself and has no real eigenvector.

### Consequences

- Commuting Hermitian matrices have a common unitary diagonalization with real diagonal matrices.
- If $T$ is normal, then $T$ and $T^*$ commute. So the case $\mathcal{F} = \set{T, T^*}$ gives back [[the complex spectral theorem|04CW1P44VD]] and the conjugate eigenvalues of $T^*$.
- If $S$ and $T$ are commuting normal operators, then $S + T$ and $S T$ are normal, because they are diagonal in the common basis.
- A normal $T = A + iB$, with $A$ and $B$ self-adjoint and $A B = B A$, is diagonalized by a common eigenbasis of $A$ and $B$. The eigenvalues of $T$ are then $\alpha_j + i \beta_j$.

### Converse

The direction "if" of each part is the easy one.
In a common orthonormal eigenbasis, all members of $\mathcal{F}$ have diagonal matrices, and diagonal matrices commute.

## Explanations

### L1 human

Two normal matrices that commute share a set of perpendicular special directions.
In these directions, both matrices act by multiplication with numbers.
So one change of coordinates makes both diagonal at the same time.
If the matrices do not commute, no such common directions exist.

### L2 human

Worked example: [[two commuting symmetric matrices|2YEX40VH77]].

1. Let $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. Then $A = 2I + B$, so $A B = B A$.
2. The vectors $(1, 1)$ and $(1, -1)$ are eigenvectors of both: $A$ has the eigenvalues $3$ and $1$, and $B$ has $1$ and $-1$.
3. With $Q = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, both $Q^T A Q = \operatorname{diag}(3, 1)$ and $Q^T B Q = \operatorname{diag}(1, -1)$.

The typical use is in quantum mechanics: commuting observables have a common basis of eigenstates.
A trap: a repeated eigenvalue of one matrix gives an eigenspace with many orthonormal bases.
Only some of them diagonalize the other matrix.

### L3 human

The members of $\mathcal{F}$, their adjoints and $I$ generate a commutative algebra of operators closed under ${}^*$.
The theorem says that this algebra is unitarily equivalent to an algebra of diagonal matrices.
In infinite dimension, a commutative von Neumann algebra plays this role, and the diagonal matrices become multiplication operators.
