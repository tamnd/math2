---
tag: RQ44FKS5QM
kind: concept
name: Dodgson condensation
msc: ["15A15", "65F40"]
topics: [DTBK11SR77]
audience: grad
sources:
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
    locator: Desnanot–Jacobi identity and proof of correctness of the condensation algorithm
same_as:
  wikidata: Q4230490
  wikipedia: Dodgson condensation
---

## Summary

Dodgson condensation computes a [[determinant|00KDZRW4C0]] by shrinking the matrix one size at a time, using nothing but $2 \times 2$ determinants and exact divisions.
Each step replaces the current matrix by the matrix of its connected $2 \times 2$ minors, the determinants of the blocks of four neighboring entries.
From the second step on, each of these minors is divided by the matching interior entry of the matrix from two steps before.
For an $n \times n$ matrix over a field, after $n - 1$ steps a single number is left, and it is the determinant, provided that no divisor was zero.
The [[definition|F7D849A4RZ]] gives the exact recursion, and the [[Desnanot-Jacobi identity|KWW7519E58]] is the reason it works.

## Motivation

Expansion by cofactors needs about $n!$ products, so it is hopeless beyond small sizes.
Gaussian elimination is fast, but on an integer matrix it brings in fractions at once.
Condensation is a middle way that a person can run by hand: every intermediate number is a determinant of a block of the original matrix, so on an integer matrix every number stays an integer.
The cost is about $n^3/3$ small determinants in all, the same order as elimination.

The idea rests on one fact.
The Desnanot-Jacobi identity writes a determinant through its four corner minors of one size smaller and its central minor of two sizes smaller.
Applied to all connected blocks at once, it turns the minors of size $k$ and $k - 1$ into the minors of size $k + 1$.
The same identity returns in [[Sylvester's determinant identity|7SSKBQYFW1]] and in the fraction-free [[Bareiss algorithm|ZDBW3AB587]].

## Notation

We write $A^{(0)} = A$ for the starting matrix and $A^{(k)}$ for the $(n - k) \times (n - k)$ matrix after step $k$.
Its entry $a^{(k)}_{ij}$ is the connected minor of $A$ of order $k + 1$ whose top left corner is at position $(i, j)$.
The interior of a matrix is the block that remains when its first and last rows and columns are deleted.

## Remarks

### A first condensation

Take
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}.$$
The first step takes the four connected $2 \times 2$ minors:
$$A^{(1)} = \begin{pmatrix} 1 \cdot 5 - 2 \cdot 4 & 2 \cdot 6 - 3 \cdot 5 \\ 4 \cdot 8 - 5 \cdot 7 & 5 \cdot 10 - 6 \cdot 8 \end{pmatrix} = \begin{pmatrix} -3 & -3 \\ -3 & 2 \end{pmatrix}.$$
The second step takes the $2 \times 2$ determinant of $A^{(1)}$ and divides it by the interior of $A$, which is the central entry $5$:
$$A^{(2)} = \frac{(-3) \cdot 2 - (-3)(-3)}{5} = \frac{-15}{5} = -3.$$
Check by expansion along the first row: $1 \cdot 2 - 2 \cdot (40 - 42) + 3 \cdot (32 - 35) = 2 + 4 - 9 = -3$.

### Two larger computations

The [[condensation of a 4 × 4 matrix|FZJMAYK2DN]] runs three steps, with divisors $2$, $1$, $1$, $2$ in the second step and $3$ in the third, and it ends with $21$.
It checks the result with the general Laplace expansion along two rows.
The [[condensation with a negative divisor|WHN8H0777X]] ends with a division by $-1$, and it gives $-14$.
In both, every division is exact, and a fraction in the middle of a computation is a sign of an arithmetic error.

### Why the divisions come out exact

By induction on $k$, each entry of $A^{(k)}$ is a connected minor of $A$ of order $k + 1$.
The step from $k - 1$ to $k$ is the Desnanot-Jacobi identity for the connected block of order $k + 1$: its four corner minors are entries of $A^{(k-1)}$, and its central minor is an entry of $A^{(k-2)}$.
So each quotient is a minor of $A$, and for an integer matrix it is an integer.

### When the method fails

A zero divisor stops the method.
For the matrix with rows $(1, 2, 3)$, $(4, 0, 5)$ and $(6, 7, 8)$, the second step must divide $0$ by $0$, although the determinant is $45$; the [[non-example|AD6GEXKCB1]] works this out and repairs it by a cyclic shift of the rows.
The numerator is always $0$ in this situation, because it equals the divisor times a minor.

Over a ring with zero divisors the method can also fail with nonzero divisors.
In $\mathbb{Z}/4\mathbb{Z}$, the equation $2x = 2$ has the two solutions $x = 1$ and $x = 3$, so "divide $2$ by $2$" has no single answer.

### Watch out

The divisor in step $k$ comes from the matrix two steps back, $A^{(k-2)}$, and not from the previous matrix $A^{(k-1)}$.
In the [[4 × 4 example|FZJMAYK2DN]], entry $(1, 1)$ of the second step is $-16/2 = -8$, with the interior entry $2$ of $A$ as divisor.
Dividing by the central entry $3$ of $A^{(1)}$ instead would give the fraction $-16/3$, and that fraction signals the error.
Also, a value $0/0$ is not the value $0$: it means that the method gave no answer.

### History

Charles Dodgson, the mathematician known as the author Lewis Carroll, published the method in 1866.
The identity behind it carries the names of Desnanot and Jacobi.

### Try it

First, condense $\begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$.
The first step gives the minors $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, and the second gives $(9 - 1)/2 = 4$, which is the determinant.

Second, condense $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 3 & 6 \end{pmatrix}$.
The first step gives $\begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}$, and the second gives $(3 - 1)/2 = 1$, which agrees with expansion along the first row, $3 - 3 + 1 = 1$.

## Explanations

### L1 human

Start with a square table of numbers.
For each little square of four neighbors, compute "top left times bottom right minus top right times bottom left".
The results form a table that is one row and one column smaller.
Repeat with the new table, but now divide each new number by the matching inner number of the table from two rounds before.
When one number is left, it is the determinant of the first table.

### L2 human

Here is a typical use: a hand computation of a $4 \times 4$ integer determinant.
Write the matrix, then the $3 \times 3$ table of its connected $2 \times 2$ minors.
Next write the $2 \times 2$ table of connected minors of that table, and divide each entry by the matching entry of the interior of the original matrix.
Finally take the $2 \times 2$ determinant of the last table and divide by the central entry of the $3 \times 3$ table.
The [[worked example|FZJMAYK2DN]] does this and finds $21$, and each division in it is exact.
Watch out for zeros in the interior: before you start, look at the interior of the matrix, and if it contains a $0$, permute rows or columns first and track the sign.

### L3 human

The recursion is a special case of the octahedron recurrence.
When the starting values of that recurrence are free variables, every quantity it produces is a Laurent polynomial in them, one of the first examples of the Laurent phenomenon of [[cluster algebras|TKK0TV2MYC]].
When the $2 \times 2$ rule $ad - bc$ is deformed to $ad + \lambda bc$, condensation defines the lambda-determinant of Robbins and Rumsey, and its expansion is a sum over alternating sign matrices.
In exact computer algebra the same idea, organized as elimination, is the [[Bareiss algorithm|ZDBW3AB587]].
