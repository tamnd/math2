---
tag: 0RKG5YW66Y
kind: concept
name: LU decomposition
aliases: [lu-factorization]
msc: [15A23, 65F05]
topics: [P8J6QR66TJ]
audience: ug1
uses: [00J3KZP8Y0, 0N4XY7Z3NN, 0JVJ2WCXZH, 08SP3DF8NB, 0ATFVE08MW, 01REXW3WWE, 7X1B65CTG4]
sources:
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 2.5
  - book: isbn:9781733146678
same_as:
  wikidata: Q833089
  wikipedia: LU decomposition
---

## Summary

The LU decomposition is Gaussian elimination written as a matrix product: $A = LU$, where $U$ is the echelon form that elimination reaches and $L$ records the multipliers it used.
Here $A$ is a square matrix over a field, $L$ is a unit [[lower triangular matrix|00J3KZP8Y0]], with diagonal entries $1$, and $U$ is an [[upper triangular matrix|0N4XY7Z3NN]].
[[Gaussian elimination|0JVJ2WCXZH]] without row exchanges produces such a factorization whenever it runs without meeting a zero pivot.
With row exchanges, one gets $PA = LU$ for a [[permutation matrix|08SP3DF8NB]] $P$, and every square matrix over a field has a factorization of this kind.
Once $A = LU$ is known, every system $Ax = b$ reduces to two triangular systems.

## Motivation

Elimination on $A$ does the same work whatever the right side $b$ of $Ax = b$ is.
The LU decomposition does that work once and stores it.
Then $Ax = b$ splits into $Ly = b$, solved from the top by forward substitution, and $Ux = y$, solved from the bottom by [[back substitution|0ATFVE08MW]].
For an $n \times n$ matrix the factorization costs about $n^3/3$ multiplications, and each new right side costs only about $n^2$.
That is the same cost per right side as multiplying by $A^{-1}$, at a third of the cost of computing $A^{-1}$.

## Notation

In this node, $L$ is always unit lower triangular; some books, for example in the Crout method, put the $1$s on the diagonal of $U$ instead.
The leading principal minor $\Delta_k$ of $A$ is the [[determinant|00KDZRW4C0]] of the upper left $k \times k$ submatrix $A_k$, for $k = 1, \dots, n$, and $\Delta_0 = 1$.
An LDU decomposition is $A = LDV$ with $L$ unit lower triangular, $D$ diagonal and $V$ unit upper triangular.

Warning on names: some books, especially in numerical analysis, use "LU decomposition" for $PA = LU$, which allows row exchanges, while others reserve the name for $A = LU$ with no exchanges.
The two conventions give different existence theorems, so check which one a theorem uses before you apply it.

## Remarks

### A first factorization

Take $A = \begin{pmatrix} 2 & 1 \\ 6 & 4 \end{pmatrix}$.
One step $R_2 \to R_2 - 3R_1$ gives $U$, and the multiplier $3$ goes into position $(2, 1)$ of $L$:
$$A = \begin{pmatrix} 2 & 1 \\ 6 & 4 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} = LU.$$
Check: $LU = \begin{pmatrix} 2 & 1 \\ 6 & 3 + 1 \end{pmatrix} = A$.
Now solve $Ax = (3, 10)^{\mathsf{T}}$.
Forward substitution in $Ly = b$ gives $y_1 = 3$ and $y_2 = 10 - 3 \cdot 3 = 1$.
Back substitution in $Ux = y$ gives $x_2 = 1$ and then $2x_1 + 1 = 3$, so $x_1 = 1$.
Check: $A(1, 1)^{\mathsf{T}} = (3, 10)^{\mathsf{T}}$.

### Why the multipliers land in $L$

Each step $R_i \to R_i - \ell_{ij} R_j$ with $i > j$ is left multiplication by the [[elementary matrix|01REXW3WWE]] $T_{ij}(-\ell_{ij})$.
If elimination uses $E_1, \dots, E_k$, then $E_k \cdots E_1 A = U$ and $L = E_1^{-1} \cdots E_k^{-1}$.
Each inverse $T_{ij}(\ell_{ij})$ is unit lower triangular, and when the steps are taken column by column, their product has each multiplier $\ell_{ij}$ sitting in position $(i, j)$ with no interaction.
Since $\det L = 1$, also $\det A = \det U = u_{11} \cdots u_{nn}$.

### When it exists, and when it is unique

The theorem on [[existence of the LU decomposition|3PPBWG0B96]] says that an invertible $A$ has $A = LU$ exactly when $\Delta_1, \dots, \Delta_n$ are all nonzero, and then the pivots are $u_{kk} = \Delta_k / \Delta_{k-1}$.
The theorem on [[uniqueness of the LDU decomposition|R424G32KFA]] says that for invertible $A$ the factors are unique, and that a symmetric $A$ then has $A = LDL^{\mathsf{T}}$.
For a [[positive definite|0KX66CZMBB]] matrix all $\Delta_k$ are positive, and the symmetric form leads to the [[Cholesky decomposition|0WKG8CYY6A]].

### Examples and non-examples

The [[worked $3 \times 3$ LU decomposition|B61PAXBBHQ]] factors a $3 \times 3$ matrix, solves a system with it, and gives the LDU form.
The [[worked $PA = LU$ example|EYPH6X8N5G]] needs one row exchange first.
The [[exchange matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$|HZR79K1TZ6]] is invertible but has no LU decomposition, because its entry $(1, 1)$ is $0$ and $\Delta_1 = 0$.
A factorization $A = UL$, with the factors in the other order, is a different factorization with different conditions for existence.

### Watch out

The multiplier enters $L$ with a plus sign: the step $R_i \to R_i - \ell R_j$ puts $+\ell$ into position $(i, j)$, because $L$ undoes the elimination.
A zero pivot does not mean that $A$ is singular; it means that this $A$ may have no factorization $A = LU$, while $PA = LU$ still exists.
And a singular matrix can have an LU decomposition: $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is already upper triangular, so it equals $I_2$ times itself.

### History

Banachiewicz introduced the decomposition in 1938, in his work on the solution of linear systems.
Crout published his variant in 1941, and Turing analyzed the method in his 1948 paper on rounding-off errors in matrix processes.

### Try it

First, factor $\begin{pmatrix} 1 & 2 \\ 3 & 8 \end{pmatrix}$.
Answer: $R_2 \to R_2 - 3R_1$ gives $L = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$ and $U = \begin{pmatrix} 1 & 2 \\ 0 & 2 \end{pmatrix}$, and $LU = \begin{pmatrix} 1 & 2 \\ 3 & 6 + 2 \end{pmatrix}$.

Second, does $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ have a factorization $A = LU$, and what about $PA = LU$?
Answer: no, since $\Delta_1 = 0$ while $\Delta_2 = -1 \ne 0$; but exchanging the rows gives $P_{12}A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = I_2 \cdot U$.

## Explanations

### L1 human

An LU decomposition writes a matrix as a product of two triangular matrices.
Triangular systems are easy to solve, one unknown at a time, so we solve $Ax = b$ in two easy steps.
It is useful when we solve many systems with the same $A$ and different right sides.

### L2 human

Do elimination from the top down, and only subtract multiples of higher rows from lower rows.
Keep each multiplier: for $R_i \to R_i - \ell R_j$, write $\ell$ in position $(i, j)$ of a unit lower triangular matrix $L$.
The final echelon matrix is $U$, and $A = LU$.
If a zero pivot appears, exchange rows and record the exchange in $P$, and you get $PA = LU$ instead.

### L3 human

In terms of groups, the invertible matrices with an LU decomposition form the product $B^- B^+$ of the lower and upper triangular subgroups of $\mathrm{GL}_n(F)$.
With permutation matrices, $\mathrm{GL}_n(F)$ is the disjoint union of the double cosets $B^- P B^+$, which is a form of the Bruhat decomposition.
Pivoting strategies, stability and the cost in floating point belong to numerical analysis.
