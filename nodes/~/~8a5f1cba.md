---
tag: ~8a5f1cba
kind: statement
role: theorem
name: Existence of the LU decomposition and leading principal minors
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug2
about: [0RKG5YW66Y]
uses: [0RKG5YW66Y, 00J3KZP8Y0, 0N4XY7Z3NN, 00KDZRW4C0, 0EB9N0S33C, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: Existence and uniqueness
  - book: isbn:9780521548236
    locator: Section 3.5
---

## Statement

Let $F$ be a [[field|0QA8CHH8MG]] and let $A$ be an $n \times n$ matrix over $F$.
For $k = 1, \dots, n$, let $A_k$ be the upper left $k \times k$ submatrix of $A$, and let $\Delta_k = \det A_k$ be its [[determinant|00KDZRW4C0]]; set $\Delta_0 = 1$.

1. If $\Delta_1, \dots, \Delta_{n-1}$ are nonzero, then $A = LU$ for a unit [[lower triangular|00J3KZP8Y0]] $L$ and an [[upper triangular|0N4XY7Z3NN]] $U$.
2. If $A = LU$ with $L$ unit lower triangular and $U$ upper triangular, then $\Delta_k = u_{11} u_{22} \cdots u_{kk}$ for each $k$.
3. Let $A$ be [[invertible|0EB9N0S33C]]. Then $A$ has an [[LU decomposition|0RKG5YW66Y]] $A = LU$, with $L$ unit lower triangular and $U$ upper triangular, if and only if $\Delta_1, \dots, \Delta_n$ are all nonzero. In that case the pivots are $u_{kk} = \Delta_k / \Delta_{k-1}$.

## Remarks

### Why each hypothesis is needed

- Invertibility is needed for the "only if" in part 3. The singular matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ equals $I_2$ times itself, so it has an LU decomposition, but $\Delta_1 = 0$.
- In part 1 the last minor $\Delta_n$ does not matter: $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ has $\Delta_2 = 0$.
- The minors $\Delta_k$ with $k < n$ matter: the [[exchange matrix|~a3b4cee2]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is invertible with $\Delta_1 = 0$, and it has no LU decomposition.

### Consequences

- Elimination without row exchanges succeeds on $A$ exactly when the pivots $\Delta_k/\Delta_{k-1}$ are nonzero.
- Each [[positive definite|0KX66CZMBB]] matrix has all $\Delta_k > 0$, so it has an LU decomposition with positive pivots.
- A strictly diagonally dominant matrix also has all $\Delta_k \ne 0$, so elimination needs no row exchanges.
- The entry $u_{nn}$ equals $a_{nn} - c^{\mathsf{T}} A_{n-1}^{-1} b$ in the notation of the proof, which is the [[Schur complement|6HWFBXYPZP]] of $A_{n-1}$.

### Converse

The converse of part 1 fails: $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has an LU decomposition and $\Delta_1 = 0$.
Part 3 is the correct biconditional for invertible matrices.

### Generalizations

- With a [[permutation matrix|08SP3DF8NB]] $P$, each square matrix over a field has $PA = LU$. This is shown in the [[worked $PA = LU$ example|~595614c8]] and in the concept of [[LU decomposition|0RKG5YW66Y]].
- The same block proof works for matrices over a commutative ring if each $\Delta_k$ with $k < n$ is a unit.

## Explanations

### L1 human

Elimination without row swaps works if each pivot is nonzero.
The theorem gives a test that you can check before you start: the determinants of the upper left corners must be nonzero.
Each pivot is the quotient of two such determinants.

### L2 human

Take $A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$.

1. $\Delta_1 = 2$.
2. $\Delta_2 = 2 \cdot 3 - 1 \cdot 4 = 2$.
3. $\Delta_3 = \det A = 2(27 - 21) - 1(36 - 24) + 1(28 - 24) = 12 - 12 + 4 = 4$.
4. So the pivots are $\Delta_1/\Delta_0 = 2$, $\Delta_2/\Delta_1 = 1$ and $\Delta_3/\Delta_2 = 2$.
5. The [[worked LU example|~3fa7f06e]] finds $U$ with diagonal $2, 1, 2$, as predicted.

### L3 human

Part 2 holds over each commutative ring, because $A_k = L_k U_k$ for the leading blocks.
The quotients $\Delta_k/\Delta_{k-1}$ show that the pivots are rational functions of the entries.
This matters for elimination over $\mathbb{Z}$ with exact division, as in the Bareiss algorithm.
