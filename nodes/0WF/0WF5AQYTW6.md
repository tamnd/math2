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

A matrix over a field is in reduced row echelon form when it is in [[row echelon form|0VYCDGMJJJ]], each leading entry is $1$, and each leading entry is the only nonzero entry in its column.
The exact definition is in [[the definition node|0NNR68BFRY]].
Every matrix is row equivalent to exactly one matrix in reduced row echelon form, see [[the existence theorem|~d9e684c6]] and [[the uniqueness theorem|BF9SMZMJZE]]; it is called the RREF of the matrix.
The RREF matters because the solutions of a system can be read from the RREF of its augmented matrix without further computation, see [[the lemma on systems in RREF|~e45eea91]].

## Motivation

A row echelon form still needs [[back substitution|0ATFVE08MW]] before we see the solutions, and it is not unique.
If we also clear the entries above each pivot and scale each pivot to $1$, each equation contains exactly one basic variable.
Then each basic variable is given directly in terms of the free variables.
This form is unique, so it is a fingerprint of the matrix up to row operations.

## Notation

1. Common notations are $\operatorname{rref}(A)$ and $\operatorname{RREF}(A)$.
2. Lay calls it the "reduced echelon form".
3. Computer algebra systems compute it: MATLAB and Octave have `rref(A)`, SymPy has `Matrix.rref()`, and Sage has `A.rref()`.
4. The RREF of the [[augmented matrix|0T6MWGZSXA]] $[A \mid b]$ is written $\operatorname{rref}[A \mid b]$; it is not $\operatorname{rref}(A)$ with a column added.

## Remarks

### Examples

1. $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ is in RREF, with pivot columns $1$ and $3$.
2. The identity matrix $I_n$ is in RREF, and it is the RREF of every invertible $n \times n$ matrix.
3. $\left[\begin{array}{rrr|r} 1 & 0 & 2 & 2 \\ 0 & 1 & -1 & 1 \end{array}\right]$ is in RREF, and it gives the line of solutions in [[the line example|~f4f0e07b]].
4. The three cases "unique", "none" and "infinitely many" are read off three RREFs in [[the reading example|~e19ce05e]].
5. The RREFs of $A$ and of $[A \mid b]$ can have different numbers of pivots, see [[the trap example|~7ea020f3]].

### Non-examples

1. $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \end{bmatrix}$ is in row echelon form but not in RREF, because a leading entry is $3$, see [[the non-examples|~c5f4bde3]].
2. $\begin{bmatrix} 1 & 2 & 5 \\ 0 & 1 & 3 \end{bmatrix}$ is not in RREF, because the entry $2$ lies above the leading $1$ of row 2.
3. $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ is not in RREF, because it is not in row echelon form.

### Basic properties

1. Every matrix has an RREF, see [[the existence theorem|~d9e684c6]], and it is unique, see [[the uniqueness theorem|BF9SMZMJZE]].
2. Two matrices of the same size are row equivalent if and only if they have the same RREF.
3. The pivot columns of the RREF are the unit vectors $e_1, \dots, e_r$, where $r$ is the number of pivots.
4. The number $r$ of nonzero rows of the RREF is the [[rank|0ZC9YTXZRY]] of the matrix, and the nonzero rows are a basis of its row space.
5. The RREF of $[A \mid B]$ begins with the RREF of $A$, see [[the augmentation principle|BE3NZP35HY]].
6. A square matrix is invertible if and only if its RREF is the identity matrix.

### History

Wilhelm Jordan described elimination to this form in 1888 in a handbook of geodesy, and the method is now called [[Gauss-Jordan elimination|098D6FQN3N]].
The name "reduced row echelon form" and the abbreviation RREF are standard in English textbooks such as Lay.

### Common errors

1. Forgetting to clear the entries above the pivots.
2. Computing $\operatorname{rref}(A)$ when the question is about $Ax = b$.
3. Reading the values of the basic variables from the last column while ignoring the free variables in the same row.

## Explanations

### L1 human

Reduced row echelon form is the simplest form that row operations can reach.
Each staircase step starts with a $1$, and that $1$ has zeros above it and below it.
For example, the rows $(1, 0 \mid 2)$ and $(0, 1 \mid 1)$ say directly $x = 2$ and $y = 1$.
From this form we can read the solutions of the system without more work.

### L2 human

We read the solutions of the system whose augmented matrix has the RREF $\left[\begin{array}{rrrr|r} 1 & 0 & 2 & 0 & 3 \\ 0 & 1 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1 & -2 \end{array}\right]$.

1. The last column has no pivot, so the system is consistent.
2. The pivot columns are $1$, $2$ and $4$; so $x_1, x_2, x_4$ are basic, and $x_3$ is free.
3. Put $x_3 = t$. The rows say $x_1 + 2t = 3$, $x_2 - t = 1$ and $x_4 = -2$.
4. So $x = (3, 1, 0, -2) + t(-2, 1, 1, 0)$.
5. Check $t = 1$, the point $(1, 2, 1, -2)$: $1 + 2 = 3$, $2 - 1 = 1$ and $x_4 = -2$.

The typical use is the final step of solving a system by hand or by computer.
A trap: a zero row $(0, \dots, 0 \mid 0)$ is harmless, but a row $(0, \dots, 0 \mid 1)$ means there is no solution.

### L3 human

The RREF is a canonical form for the action of $\mathrm{GL}_m(F)$ on $m \times n$ matrices by left multiplication.
Its nonzero rows are the unique basis of the row space that is in reduced echelon form, so the RREF gives coordinates on the Grassmannian, cell by cell.
The RREF computes the [[null space|0PHDYNR24D]], the rank and the pivot basis of the [[column space|03AJKXH1AV]] in one pass.
For exact arithmetic over $\mathbb{Q}$ the entries can grow, and fraction-free methods are used; over $\R$ in floating point, the RREF is sensitive to rounding, so numerical software prefers factorizations.
