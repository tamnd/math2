---
tag: FBQCE3HVMP
kind: concept
name: Solving linear systems by matrix inversion
msc: ["15A09", "15A06"]
topics: [P8J6QR66TJ]
audience: school
uses: [0EB9N0S33C, 0JTRMBQ1SA, 3RQX3T70NX, 0Z83DHFMYM]
sources:
  - book: isbn:9780321982384
    locator: Section 2.2
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Applications
  - url: https://understandinglinearalgebra.org/
    locator: Section 3.1, Invertibility
---

## Summary

To solve a square [[system of linear equations|0JTRMBQ1SA]] $Ax = b$ with an [[invertible|0EB9N0S33C]] matrix $A$, compute $A^{-1}$ once and then form $x = A^{-1} b$.
The [[solution theorem|3RQX3T70NX]] says that this vector is the unique solution.
The method pays off when we must solve many systems with the same matrix $A$ and different right-hand sides.
For one system, elimination with back substitution is cheaper and more accurate.

## Motivation

A system $Ax = b$ with $n$ equations and $n$ unknowns is the matrix version of the equation $ax = b$ for numbers.
For numbers, we divide by $a$, or multiply by $a^{-1}$.
For matrices, we multiply on the left by $A^{-1}$, which we can compute by [[row reduction|0Z83DHFMYM]].
Once $A^{-1}$ is known, each new right-hand side costs only one matrix-vector product, about $n^2$ multiplications.

## Notation

- We write the system as $Ax = b$, with $x$ and $b$ as column vectors.
- For several right-hand sides $b_1, \dots, b_p$ we collect them as columns of a matrix $B$ and solve $AX = B$; then $X = A^{-1}B$.

## Remarks

### Examples

- The [[$2 \times 2$ system|FBFW5FE62Y]] $2x + y = 5$, $5x + 3y = 13$ has the solution $(2, 1)$.
- The [[$3 \times 3$ system with two right-hand sides|9NQH330E9G]] reuses one inverse for two systems.
- The [[formula for the inverse of a 2 × 2 matrix|8XWC7RKNN1]] solves $4x + 7y = 1$, $2x + 6y = 3$.

### Non-examples

- The method fails for a singular matrix, such as the coefficient matrix of $x + 2y = 3$, $2x + 4y = 6$; see the [[singular system|7XVJ4ZCXTV]].
- The method does not apply to non-square systems; there one uses elimination, or least squares in the sub-area on [[orthogonality and least squares|8GQVME4SZZ]].

### Basic properties

- The solution $x = A^{-1}b$ depends linearly on $b$: $A^{-1}(b + b') = A^{-1}b + A^{-1}b'$.
- Column $j$ of $A^{-1}$ is the solution for the right-hand side $e_j$.
- Computing $A^{-1}$ costs about $n^3$ multiplications, while elimination for one system costs about $n^3/3$. The [[LU decomposition|0RKG5YW66Y]] keeps the advantage of reuse at the lower cost.

### History

Cayley defined the inverse of a square matrix in his memoir on the theory of matrices of 1858.
He expressed the inverse with the cofactors divided by the determinant, which is Cramer's rule in matrix form.

### Common errors

- Students write $x = bA^{-1}$. The product $bA^{-1}$ is not even defined for a column vector $b$ and $n \ge 2$.
- Students apply the method before they check that $A$ is invertible.

## Explanations

### L1 human

If we have the inverse of the matrix of a system, we get the answer by one multiplication.
This is like solving $3x = 12$ by multiplying both sides by $\tfrac{1}{3}$.

### L2 human

Worked example: solve $2x + y = 3$, $x + y = 2$.

1. The matrix is $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, with $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
2. $x = A^{-1}(3, 2)^{\mathsf{T}} = (3 - 2, \; -3 + 4)^{\mathsf{T}} = (1, 1)^{\mathsf{T}}$.
3. Check: $2 + 1 = 3$ and $1 + 1 = 2$.

The typical use is a fixed matrix with many right-hand sides, for example the same circuit with different input voltages.
A trap: the inverse must be multiplied on the left of $b$.

### L3 human

In numerical linear algebra the inverse is rarely formed.
One stores a factorization $PA = LU$ and solves two triangular systems per right-hand side, at the same cost of about $n^2$ operations.
The accuracy of $A^{-1}b$ in floating point depends on the [[condition number|AB3S6MHJ8X]] of $A$, which belongs to numerical analysis.
