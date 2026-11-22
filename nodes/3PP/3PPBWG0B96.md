---
tag: 3PPBWG0B96
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

Elimination without row exchanges works exactly when the determinants of the upper left corners of the matrix are nonzero, and each pivot is a quotient of two of these determinants.
Let $F$ be a [[field|0QA8CHH8MG]] and let $A$ be an $n \times n$ matrix over $F$.
For $k = 1, \dots, n$, let $A_k$ be the upper left $k \times k$ submatrix of $A$, and let $\Delta_k = \det A_k$ be its [[determinant|00KDZRW4C0]]; set $\Delta_0 = 1$.

1. If $\Delta_1, \dots, \Delta_{n-1}$ are nonzero, then $A = LU$ for a unit [[lower triangular|00J3KZP8Y0]] $L$ and an [[upper triangular|0N4XY7Z3NN]] $U$.
2. If $A = LU$ with $L$ unit lower triangular and $U$ upper triangular, then $\Delta_k = u_{11} u_{22} \cdots u_{kk}$ for each $k$.
3. Let $A$ be [[invertible|0EB9N0S33C]]. Then $A$ has an [[LU decomposition|0RKG5YW66Y]] $A = LU$, with $L$ unit lower triangular and $U$ upper triangular, if and only if $\Delta_1, \dots, \Delta_n$ are all nonzero. In that case the pivots are $u_{kk} = \Delta_k / \Delta_{k-1}$.

## Remarks

### The theorem at work

Take $A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$ and compute the corner determinants:
$$\Delta_1 = 2, \qquad \Delta_2 = 2 \cdot 3 - 1 \cdot 4 = 2, \qquad \Delta_3 = 2(27 - 21) - 1(36 - 24) + 1(28 - 24) = 4.$$
All three are nonzero, so $A = LU$ exists, and the pivots will be
$$\frac{\Delta_1}{\Delta_0} = 2, \qquad \frac{\Delta_2}{\Delta_1} = 1, \qquad \frac{\Delta_3}{\Delta_2} = 2.$$
The [[worked LU example|B61PAXBBHQ]] finds $U$ with diagonal $2, 1, 2$, as predicted, before doing any elimination.

### Why the hypotheses are needed

The minors $\Delta_k$ with $k < n$ matter.
The [[exchange matrix|HZR79K1TZ6]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is invertible with $\Delta_1 = 0$, and it has no LU decomposition.
The last minor $\Delta_n$ does not matter for part 1:
$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$$
has $\Delta_2 = 0$.
Invertibility is needed for the "only if" in part 3: the singular matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ equals $I_2$ times itself, so it has an LU decomposition, but $\Delta_1 = 0$.
The same matrix shows that the converse of part 1 fails.

### What it gives you

For an invertible matrix, elimination without row exchanges succeeds exactly when $\Delta_1, \dots, \Delta_{n-1}$ are nonzero, and this can be tested before you start.
Each [[positive definite|0KX66CZMBB]] matrix has all $\Delta_k > 0$, so it has an LU decomposition with positive pivots.
A strictly diagonally dominant matrix has strictly diagonally dominant leading blocks, hence all $\Delta_k \ne 0$, so elimination on it needs no row exchanges either.
Write $A$ in blocks as $\begin{pmatrix} A' & b \\ c^{\mathsf{T}} & d \end{pmatrix}$ with $A' = A_{n-1}$; then the last pivot is $u_{nn} = d - c^{\mathsf{T}} A'^{-1} b$, the [[Schur complement|6HWFBXYPZP]] of $A'$.

### Generalizations

With a [[permutation matrix|08SP3DF8NB]] $P$, each square matrix over a field has $PA = LU$, as in the [[worked $PA = LU$ example|EYPH6X8N5G]].
The same block proof works over a commutative ring if each $\Delta_k$ with $k < n$ is a unit.
Part 2 holds over every commutative ring, because $A_k = L_k U_k$ for the leading blocks.

## Explanations

### L1 human

Elimination without row swaps works if each pivot is nonzero.
The theorem gives a test that you can check before you start: the determinants of the upper left corners must be nonzero.
Each pivot is the quotient of two such determinants.

### L2 human

Use the test when you want to know whether a given matrix needs row exchanges, without running elimination.
For a $2 \times 2$ matrix, it says that $A = LU$ with $A$ invertible exactly when $a_{11} \ne 0$, and then the pivots are $a_{11}$ and $\det A / a_{11}$.
A trap: the test is about the corner determinants, not the diagonal entries; $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ has $a_{22} = 0$ but $\Delta_1 = 1$ and $\Delta_2 = -1$, so it has an LU decomposition.

### L3 human

The quotients $\Delta_k/\Delta_{k-1}$ show that the pivots are rational functions of the entries of $A$.
This matters for exact elimination over $\mathbb{Z}$, where fraction-free methods such as the Bareiss algorithm keep every intermediate entry an integer minor of $A$.
