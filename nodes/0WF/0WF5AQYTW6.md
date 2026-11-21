---
tag: 0WF5AQYTW6
kind: concept
name: Reduced row echelon form
aliases: [rref]
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
specializes: [0VYCDGMJJJ]
uses: [0VYCDGMJJJ, 04XWH28452]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: Reduced row echelon form
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-2.xml#L1072
    locator: src/section1-2.xml:1072
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Summary

The reduced row echelon form is the end point of row reduction, the form from which the solutions can be read with no more work.
A matrix is in reduced row echelon form when it is in [[row echelon form|0VYCDGMJJJ]], each leading entry is $1$, and each leading entry is the only nonzero entry in its column.
Every matrix is row equivalent to exactly one such matrix, its RREF, by the [[existence theorem|FCM29NQ6DN]] and the [[uniqueness theorem|BF9SMZMJZE]].
The solutions of a system can be read from the RREF of its augmented matrix, by the [[lemma on systems in RREF|P3HMRQN5KT]].
The [[formal definition|0NNR68BFRY]] lists the three conditions.

## Motivation

A row echelon form is a staircase, but it still needs [[back substitution|0ATFVE08MW]] before we see the solutions.
It is also not unique, so two people can reduce the same matrix and get different answers.

Both problems go away if we do a little more work, using only [[elementary row operations|04XWH28452]].
We scale each pivot to $1$ and clear the entries above each pivot as well as below.
Then each equation contains exactly one basic variable, and it gives that variable directly in terms of the free variables.
The resulting form is unique, so it is a fingerprint of the matrix up to row operations.

## Notation

Common notations are $\operatorname{rref}(A)$ and $\operatorname{RREF}(A)$.
Lay's textbook calls the form the "reduced echelon form".
Computer algebra systems compute it: MATLAB and Octave have `rref(A)`, SymPy has `Matrix.rref()`, and Sage has `A.rref()`.
The RREF of the [[augmented matrix|0T6MWGZSXA]] $[A \mid b]$ is written $\operatorname{rref}[A \mid b]$, and it is not $\operatorname{rref}(A)$ with a column added.

## Remarks

### Reading the solutions off

Suppose the augmented matrix of a system in $x_1, x_2, x_3, x_4$ has the RREF
$$\left[\begin{array}{rrrr|r} 1 & 0 & 2 & 0 & 3 \\ 0 & 1 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1 & -2 \end{array}\right].$$
The last column has no pivot, so the system is consistent.
The pivot columns are $1$, $2$ and $4$, so $x_1, x_2, x_4$ are basic and $x_3$ is free.
Put $x_3 = t$.
The rows say $x_1 + 2t = 3$, $x_2 - t = 1$ and $x_4 = -2$, so
$$x = (3, 1, 0, -2) + t(-2, 1, 1, 0), \qquad t \in \mathbb{R}.$$
Check $t = 1$, the point $(1, 2, 1, -2)$: $1 + 2 = 3$, $2 - 1 = 1$ and $x_4 = -2$.
[[The reading example|390YXGS32E]] shows the other two cases, a unique solution and no solution.
In three unknowns, the RREF $\left[\begin{array}{rrr|r} 1 & 0 & 2 & 2 \\ 0 & 1 & -1 & 1 \end{array}\right]$ gives a line of solutions, as in [[the line example|PRB44DTZ1P]].

### What the RREF tells you about a matrix

The pivot columns of the RREF are the unit vectors $e_1, \dots, e_r$, where $r$ is the number of pivots.
This number $r$ is the [[rank|0ZC9YTXZRY]] of the matrix, and the nonzero rows of the RREF are a basis of its row space.
Two matrices of the same size are row equivalent if and only if they have the same RREF.
A square matrix is invertible if and only if its RREF is the identity, so $I_n$ is the RREF of every invertible $n \times n$ matrix.

### Adding columns on the right

The RREF of $[A \mid B]$ begins with the RREF of $A$, by the [[augmentation principle|BE3NZP35HY]].
But the two RREFs can have different numbers of pivots.
For $x + 2y = 3$, $2x + 4y = 7$, the RREF of $A$ has one pivot and the RREF of $[A \mid b]$ has two, as [[the trap example|HCYVBVXBF4]] shows.

### Echelon but not reduced

The matrix $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \end{bmatrix}$ is in row echelon form but not in RREF, because a leading entry is $3$.
The matrix $\begin{bmatrix} 1 & 2 & 5 \\ 0 & 1 & 3 \end{bmatrix}$ is not in RREF, because the entry $2$ lies above the leading $1$ of row 2.
[[The non-examples|WCXMCF2T7S]] finish the reduction of both.
The matrix $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ is not in RREF, because it is not even in row echelon form.

### Watch out

Three slips are common.
The first is to forget the entries above the pivots.
The second is to compute $\operatorname{rref}(A)$ when the question is about $Ax = b$.
The third is to read $x_1 = 3$ from the first row of the matrix above, ignoring the free variable $x_3$ in the same row.
A zero row $(0, \dots, 0 \mid 0)$ is harmless, but a row $(0, \dots, 0 \mid 1)$ means there is no solution.

### History

Wilhelm Jordan described elimination to this form in 1888 in a handbook of geodesy, and the method is now called [[Gauss-Jordan elimination|098D6FQN3N]].

### Try it

Find the RREF of $\begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}$.
Scale row 1 by $\tfrac12$ to get $(1, 2)$, then $R_2 \leftarrow R_2 - R_1$ gives $(0, 1)$, and $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0)$.
The RREF is $I_2$, so the matrix is invertible.

## Explanations

### L1 human

Reduced row echelon form is the simplest form that row operations can reach.
Each staircase step starts with a $1$, and that $1$ has zeros above it and below it.
For example, the rows $(1, 0 \mid 2)$ and $(0, 1 \mid 1)$ say directly $x = 2$ and $y = 1$.
From this form we can read the solutions of the system without more work.

### L2 human

The typical use is the final step of solving a system by hand or by computer.
Reduce the augmented matrix, look at the last column for a pivot, list the free columns, and solve each row for its basic variable.
Each row of the RREF holds exactly one basic variable, so no back substitution is needed.

### L3 human

The RREF is a canonical form for the action of $\mathrm{GL}_m(F)$ on $m \times n$ matrices by left multiplication.
Its nonzero rows are the unique basis of the row space that is in reduced echelon form, so the RREF gives coordinates on the Grassmannian, cell by cell.
The RREF computes the [[null space|0PHDYNR24D]], the rank and the pivot basis of the [[column space|03AJKXH1AV]] in one pass.
For exact arithmetic over $\mathbb{Q}$ the entries can grow, and fraction-free methods are used.
In floating point over $\mathbb{R}$, the RREF is sensitive to rounding, so numerical software prefers factorizations.
