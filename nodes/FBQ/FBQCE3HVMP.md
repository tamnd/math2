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

A square system $Ax = b$ with an [[invertible|0EB9N0S33C]] matrix $A$ is solved by one multiplication, $x = A^{-1}b$, in the same way that $3x = 12$ is solved by multiplying by $\tfrac{1}{3}$.
The [[solution theorem|3RQX3T70NX]] says that this vector is the only solution of the [[system|0JTRMBQ1SA]].
The method pays off when many systems share the same matrix, or when you want the solution as a formula in $b$.
For a single system with numbers, elimination with back substitution is cheaper.

## Motivation

Suppose you know the sum $s$ and the difference $d$ of two numbers, and want the numbers.
That is the system $x + y = s$, $x - y = d$, with matrix $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, and the right side changes every time you ask.
Instead of solving again for each pair $(s, d)$, invert $A$ once:
$$A^{-1} = \begin{pmatrix} \tfrac{1}{2} & \tfrac{1}{2} \\ \tfrac{1}{2} & -\tfrac{1}{2} \end{pmatrix}, \qquad \begin{pmatrix} x \\ y \end{pmatrix} = A^{-1} \begin{pmatrix} s \\ d \end{pmatrix} = \begin{pmatrix} \tfrac{1}{2}(s + d) \\ \tfrac{1}{2}(s - d) \end{pmatrix}.$$
Check: $x + y = s$ and $x - y = d$.
The inverse has turned a family of systems into one formula.

## Notation

We write the system as $Ax = b$ with $x$ and $b$ as column vectors.
Several right sides $b_1, \dots, b_p$ are collected as the columns of an $n \times p$ matrix $B$, and the systems become the single matrix equation $AX = B$, solved by $X = A^{-1}B$.

## Remarks

### The method in three steps

Write the system in matrix form, compute $A^{-1}$, and multiply.
For the [[$2 \times 2$ system|FBFW5FE62Y]] $2x + y = 5$, $5x + 3y = 13$, the [[$2 \times 2$ formula|8XWC7RKNN1]] gives the inverse and the product gives $(x, y) = (2, 1)$.
For larger matrices, the inverse comes from [[row reduction|0Z83DHFMYM]].
Always finish by substituting the answer back into the equations.

### Many right sides

The [[$3 \times 3$ example with two right sides|9NQH330E9G]] inverts one matrix and then solves two systems, each with one matrix-vector product.
Each new right side costs $n^2$ multiplications once $A^{-1}$ is known.
Taking $b = e_j$, column $j$ of $I_n$, gives column $j$ of $A^{-1}$ as the solution, so the inverse is itself the table of solutions for the simplest right sides.
The solution also depends linearly on the right side: $A^{-1}(b + b') = A^{-1}b + A^{-1}b'$.

### Cost

Computing $A^{-1}$ takes about $n^3$ multiplications, while elimination for one system takes about $n^3/3$.
So inverting to solve a single system triples the work.
The [[LU decomposition|0RKG5YW66Y]] keeps the advantage of reuse at the lower cost: it stores the elimination, and each later right side again costs about $n^2$ operations.

### When the method does not apply

The method needs a square invertible matrix.
For $x + 2y = 3$, $2x + 4y = 6$ the matrix is singular, and the system has infinitely many solutions, as the [[singular system|7XVJ4ZCXTV]] shows; with $7$ in place of $6$ it has none.
For non-square systems there is no inverse at all, and you use elimination, or least squares from the sub-area on [[orthogonality and least squares|8GQVME4SZZ]].

### Watch out

The inverse goes on the left: $x = A^{-1}b$.
The expression $bA^{-1}$ is not even defined for a column vector $b$ when $n \ge 2$.
For the equation $XA = B$, the solution is $X = BA^{-1}$, with the inverse on the right, and that is a different matrix from $A^{-1}B$ in general.
And check invertibility first: a calculator may print a "solution" for a matrix that is singular or nearly so, because of rounding.

### Try it

First, solve $x + y = 10$, $x - y = 4$ with the formula of the motivation.
Answer: $x = \tfrac{1}{2}(10 + 4) = 7$ and $y = \tfrac{1}{2}(10 - 4) = 3$.

Second, with $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$ and $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$, solve $Ax = (0, 1)^{\mathsf{T}}$.
Answer: the solution is column 2 of $A^{-1}$, namely $(-1, 2)$; check $2(-1) + 2 = 0$ and $5(-1) + 3 \cdot 2 = 1$.

## Explanations

### L1 human

If we have the inverse of the matrix of a system, we get the answer by one multiplication.
This is like solving $3x = 12$ by multiplying both sides by $\tfrac{1}{3}$.
The inverse matrix plays the role of the fraction $\tfrac{1}{3}$.

### L2 human

Here is a worked case: solve $2x + y = 3$, $x + y = 2$.
The matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ has inverse $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, so
$$x = A^{-1} \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 - 2 \\ -3 + 4 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
Check: $2 + 1 = 3$ and $1 + 1 = 2$.
The typical use is a fixed matrix with many right sides, for example the same electrical circuit fed with different input voltages.

### L3 human

In numerical linear algebra the inverse is rarely formed.
One stores a factorization $PA = LU$ and solves two triangular systems for each right side, at a cost of about $n^2$ operations, the same as one product with $A^{-1}$.
The accuracy of a computed solution depends on the [[condition number|AB3S6MHJ8X]] of $A$, which belongs to numerical analysis.
