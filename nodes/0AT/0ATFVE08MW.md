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

A triangular system solves itself from the bottom up, one unknown per equation.
Back substitution is the method for a system $Ux = b$, where $U$ is an $n \times n$ [[upper triangular matrix|0N4XY7Z3NN]] with nonzero diagonal entries.
The last equation gives $x_n = b_n / u_{nn}$.
Then, for $i = n-1, \dots, 1$ in this order, equation $i$ gives
$$x_i = \frac{1}{u_{ii}} \left( b_i - \sum_{j = i+1}^{n} u_{ij} x_j \right),$$
which uses only the unknowns that are already known.
It is the second phase of solving a linear system, after [[Gaussian elimination|0JVJ2WCXZH]] has produced a triangular or [[echelon|0VYCDGMJJJ]] system.
It costs only about $n^2$ operations, much less than the elimination.

## Motivation

Take $x + y + z = 6$, $y - 2z = -4$, $-7z = -21$.
The last equation contains only $z$, so $z = 3$ at once.
Then the middle equation contains only one unknown that we do not know yet, and gives $y = -4 + 6 = 2$.
Then the first gives $x = 6 - 2 - 3 = 1$.
Elimination exists to bring every system into this shape, where each step solves one equation in one unknown.

## Notation

Forward substitution solves $Lx = b$ for a [[lower triangular matrix|00J3KZP8Y0]] $L$ in the same way, from the first equation down: $x_i = \frac{1}{\ell_{ii}} \bigl( b_i - \sum_{j < i} \ell_{ij} x_j \bigr)$.
For an echelon matrix that is not square, the free variables are given as parameters first, and then the [[pivot variables|0J0BBCMJ5W]] are found from the bottom up.

## Remarks

### Examples

[[A 3 by 3 upper triangular system|9G9Y9880MV]] gives $(1, 3, 2)$ in three steps.
[[A forward substitution example|ZN0DY3MZ5D]] solves a lower triangular system from the top.
[[A triangular matrix with a zero on the diagonal|39WWGKFHFV]] gives no solution or infinitely many, depending on the right side.
The last stage of [[the three planes example|YM0PB9F9HG]] is a back substitution, and the method itself is as old as elimination, see the History of [[Gaussian elimination|0JVJ2WCXZH]].

### When it does not apply

A full square system, such as $x + y = 3$, $x - y = 1$, cannot be solved by back substitution directly; it must first be made triangular.
Elimination above the pivots in [[Gauss-Jordan elimination|098D6FQN3N]] reaches the same answer by row operations on the matrix, not by substitution into equations.
If some $u_{ii} = 0$, the matrix is not invertible, since its determinant is the product of the diagonal entries, and the formula fails.

### What it costs

If every diagonal entry of $U$ is nonzero, back substitution gives the unique solution.
Row $i$ costs $n - i$ multiplications, $n - i$ subtractions and $1$ division.
The total is $\sum_{i=1}^{n} \bigl( 2(n - i) + 1 \bigr) = n(n - 1) + n = n^2$.
With an [[LU decomposition|0RKG5YW66Y]] $A = LU$, the system $Ax = b$ is solved by forward substitution for $Ly = b$ and then back substitution for $Ux = y$, at cost about $2n^2$ for each new $b$.

### Watch out

Start at the bottom of an upper triangular system, since the first equation still has $n$ unknowns.
Remember to divide by the diagonal entry $u_{ii}$.
On an echelon system with free variables, give the free variables as parameters before substituting.

### Try it

Solve $3x + y = 7$, $2y = 4$.
The second equation gives $y = 2$, and then $3x = 7 - 2 = 5$ gives $x = \tfrac53$.

## Explanations

### L1 human

In a triangular system, the last equation has only one unknown, so we solve it at once.
We put that value into the equation above it, which now has only one new unknown.
We continue upwards until we know all the unknowns.

### L2 human

The typical use is the last stage of solving a system after elimination, or the two triangular solves after an LU decomposition.
Check the answer in all equations, since an error in one step carries into every step above it.
Watch out: if a diagonal entry is $0$, the system has no solution or infinitely many, and the formula does not apply.

### L3 human

Back substitution is backward stable in floating point arithmetic, so its errors are small compared with those of the elimination.
For a sparse triangular matrix the cost is proportional to the number of nonzero entries.
In exact arithmetic over any [[field|04C5ZBG1WT]] the method works in the same way.
