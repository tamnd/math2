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

An *LU decomposition* of a square matrix $A$ over a field is a factorization $A = LU$.
Here $L$ is a unit [[lower triangular matrix|00J3KZP8Y0]], with diagonal entries $1$, and $U$ is an [[upper triangular matrix|0N4XY7Z3NN]].
[[Gaussian elimination|0JVJ2WCXZH]] without row exchanges produces such a factorization: $U$ is the echelon form, and $L$ stores the multipliers of the row operations.
With row exchanges, one gets $PA = LU$ for a [[permutation matrix|08SP3DF8NB]] $P$, and each square matrix over a field has such a factorization.

## Motivation

Elimination on $A$ does the same work for each right-hand side $b$ of $Ax = b$.
The LU decomposition records this work once.
Then each system $Ax = b$ splits into two triangular systems: $Ly = b$, solved by forward substitution, and $Ux = y$, solved by [[back substitution|0ATFVE08MW]].
For an $n \times n$ matrix, the factorization costs about $n^3/3$ multiplications, and each new right-hand side costs only about $n^2$.

## Notation

- In this node, $L$ is always *unit* lower triangular. Some books, for example in the Crout method, put the $1$s on the diagonal of $U$ instead.
- The *leading principal minor* $\Delta_k$ of $A$ is the [[determinant|00KDZRW4C0]] of the upper left $k \times k$ submatrix $A_k$, for $k = 1, \dots, n$. We set $\Delta_0 = 1$.
- An *LDU decomposition* is $A = LDV$ with $L$ unit lower triangular, $D$ diagonal and $V$ unit upper triangular.
- A warning on names: some books, for example in numerical analysis, use "LU decomposition" for $PA = LU$, which allows row exchanges. Others reserve the name for $A = LU$. Check the convention before you use a theorem.

## Remarks

### Examples

- The [[worked $3 \times 3$ LU decomposition|~3fa7f06e]] factors $\begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$, solves a system with it, and gives the LDU form.
- The [[worked $PA = LU$ example|~595614c8]] needs one row exchange first.
- For an invertible upper triangular $A$, the decomposition is $A = I_n A$.
- For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a \ne 0$, one step $R_2 \to R_2 - (c/a) R_1$ gives $A = \begin{pmatrix} 1 & 0 \\ c/a & 1 \end{pmatrix} \begin{pmatrix} a & b \\ 0 & d - bc/a \end{pmatrix}$.

### Non-examples

- The [[exchange matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$|~a3b4cee2]] is invertible but has no LU decomposition, because its entry $(1, 1)$ is $0$.
- A factorization $A = UL$ with the triangular factors in the other order is a different factorization, and it exists under different conditions.

### Basic properties

- The theorem on [[existence of the LU decomposition|~8a5f1cba]]: an invertible $A$ has an LU decomposition if and only if $\Delta_1, \dots, \Delta_n$ are all nonzero. Then the pivots are $u_{kk} = \Delta_k / \Delta_{k-1}$.
- The theorem on [[uniqueness of the LDU decomposition|~abf13bad]]. For invertible $A$ the LU and the LDU decompositions are unique, and a symmetric $A$ has $A = LDL^{\mathsf{T}}$.
- Entry $(i, j)$ of $L$ below the diagonal is the multiplier $\ell_{ij}$ in the row operation $R_i \to R_i - \ell_{ij} R_j$. The reason is that $L = E_1^{-1} \cdots E_k^{-1}$ for the [[elementary matrices|01REXW3WWE]] $E_l$ of these operations.
- $\det A = \det U = u_{11} \cdots u_{nn}$, because $\det L = 1$.
- For a [[positive definite|0KX66CZMBB]] matrix, all $\Delta_k$ are positive, and the symmetric form leads to the [[Cholesky decomposition|0WKG8CYY6A]].

### History

Banachiewicz introduced the decomposition in 1938, in his work on the solution of linear systems.
Turing analysed it in his 1948 paper on rounding-off errors in matrix processes.
Crout published his variant in 1941.

### Common errors

- Students put the multiplier with the wrong sign in $L$. For $R_i \to R_i - \ell R_j$, the entry of $L$ is $+\ell$.
- Students forget that an exchange can be needed. If a pivot is $0$, the matrix may have no $A = LU$, but it has $PA = LU$.
- Students assume that a singular matrix has no LU decomposition. The matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ equals $I_2$ times itself, so it is already of the form $LU$.

## Explanations

### L1 human

An LU decomposition writes a matrix as a product of two triangular matrices.
Triangular systems are easy to solve, so we solve $Ax = b$ in two easy steps.
It is useful when we solve many systems with the same $A$ and different right sides.

### L2 human

Do elimination from the top down, and only subtract multiples of higher rows from lower rows.
Keep each multiplier: in $R_i \to R_i - \ell R_j$, write $\ell$ in position $(i, j)$ of a unit lower triangular matrix $L$.
The final echelon matrix is $U$, and $A = LU$.
For $A = \begin{pmatrix} 2 & 1 \\ 6 & 4 \end{pmatrix}$, the step $R_2 \to R_2 - 3R_1$ gives $U = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$ and $L = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$.
Check: $LU = \begin{pmatrix} 2 & 1 \\ 6 & 3 + 1 \end{pmatrix} = A$.

### L3 human

In terms of groups, the invertible matrices with an LU decomposition form the product $B^- B^+$ of the lower and upper triangular subgroups of $\mathrm{GL}_n(F)$.
With permutation matrices, $\mathrm{GL}_n(F)$ is the union of the double cosets $B^- P B^+$, which is a form of the Bruhat decomposition.
Pivoting strategies, stability and the cost in floating point belong to numerical analysis.
