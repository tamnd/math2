---
tag: 0ATFVE08MW
kind: concept
name: Back substitution
aliases: [forward-substitution]
msc: [15A06, 65F05]
topics: [DXSXFVDMXQ]
audience: school
uses: [0N4XY7Z3NN, 0VYCDGMJJJ, 0J0BBCMJ5W]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Forward and back substitution
  - book: isbn:9781733146678
    locator: Section 2.2
---

## Summary

Back substitution is a method to solve a system $Ux = b$, where $U$ is an $n \times n$ [[upper triangular matrix|0N4XY7Z3NN]] with nonzero diagonal entries.
The last equation gives $x_n = b_n / u_{nn}$.
Then, for $i = n-1, \dots, 1$ in this order, equation $i$ gives
$$x_i = \frac{1}{u_{ii}} \left( b_i - \sum_{j = i+1}^{n} u_{ij} x_j \right),$$
which uses only the unknowns that are already known.
It is the second phase of solving a linear system, after [[Gaussian elimination|0JVJ2WCXZH]] has produced a triangular or [[echelon|0VYCDGMJJJ]] system.
It matters because a triangular system costs only about $n^2$ operations, much less than the elimination.

## Motivation

Elimination makes the last equation contain only one unknown.
So we can solve the last equation at once and then work upwards.
Each step uses only values that we already know, and each step solves one equation in one unknown.

## Notation

1. Forward substitution solves $Lx = b$ for a [[lower triangular matrix|00J3KZP8Y0]] $L$ in the same way, from the first equation down: $x_i = \frac{1}{\ell_{ii}} \bigl( b_i - \sum_{j < i} \ell_{ij} x_j \bigr)$.
2. For an echelon matrix that is not square, the free variables are given as parameters first, and then the [[pivot variables|0J0BBCMJ5W]] are found from the bottom up.

## Remarks

### Examples

1. [[A 3 by 3 upper triangular system|~283a851a]] gives $(1, 3, 2)$ in three steps.
2. [[A forward substitution example|~9ebca448]] solves a lower triangular system from the top.
3. [[A triangular matrix with a zero on the diagonal|~2cf83436]] gives no solution or infinitely many, depending on the right-hand side.
4. The last stage of [[the three planes example|~382fc66c]] is a back substitution.

### Non-examples

1. A full square system, such as $x + y = 3$, $x - y = 1$, cannot be solved by back substitution directly; it must first be made triangular.
2. Elimination above the pivots in [[Gauss-Jordan elimination|098D6FQN3N]] reaches the same answer by row operations on the matrix, not by substitution into equations.

### Basic properties

1. If every diagonal entry of $U$ is nonzero, back substitution gives the unique solution.
2. If some $u_{ii} = 0$, the matrix is not invertible, and the formula fails.
3. Operation count: row $i$ costs $n - i$ multiplications, $n - i$ subtractions and $1$ division.
4. The total is $\sum_{i=1}^{n} \bigl( 2(n - i) + 1 \bigr) = n(n - 1) + n = n^2$.
5. With an [[LU decomposition|0RKG5YW66Y]] $A = LU$, the system $Ax = b$ is solved by forward substitution for $Ly = b$ and then back substitution for $Ux = y$, at cost about $2n^2$ for each new $b$.

### History

Substitution of known values into the remaining equations is as old as the solution of equations by elimination, see the History of [[Gaussian elimination|0JVJ2WCXZH]].
The words "forward substitution" and "back substitution" are standard in numerical linear algebra.

### Common errors

1. Starting at the top of an upper triangular system, where the first equation still has $n$ unknowns.
2. Forgetting to divide by the diagonal entry $u_{ii}$.
3. Using back substitution on an echelon system without first giving the free variables as parameters.

## Explanations

### L1 human

In a triangular system, the last equation has only one unknown, so we solve it at once.
We put that value into the equation above it, which now has only one new unknown.
We continue upwards until we know all the unknowns.

### L2 human

We solve $x + y + z = 6$, $y - 2z = -4$, $-7z = -21$.

1. The last equation gives $z = -21 / (-7) = 3$.
2. The second equation gives $y = -4 + 2 \cdot 3 = 2$.
3. The first equation gives $x = 6 - 2 - 3 = 1$.
4. Check: $1 + 2 + 3 = 6$, $2 - 6 = -4$ and $-21 = -21$.

The typical use is the last stage of solving a system after elimination, or the two triangular solves after an LU decomposition.
A trap: if a diagonal entry is $0$, the system has no solution or infinitely many, and the formula does not apply.

### L3 human

Back substitution is backward stable in floating point arithmetic, so its errors are small compared with those of the elimination.
For a sparse triangular matrix the cost is proportional to the number of nonzero entries.
In exact arithmetic over any [[field|04C5ZBG1WT]] the method works in the same way.
