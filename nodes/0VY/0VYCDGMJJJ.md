---
tag: 0VYCDGMJJJ
kind: concept
name: Row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [0VD9ZSWWJG, 04XWH28452]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.2
  - url: https://understandinglinearalgebra.org/
    locator: Chapter 1
same_as:
  wikidata: Q2091296
  wikipedia: Row echelon form
---

## Summary

Let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over a field, and call the first nonzero entry of a nonzero row its leading entry.
$A$ is in row echelon form when every zero row lies below every nonzero row, and the leading entry of each nonzero row is strictly to the right of the leading entry of the row above it.
The exact definition is in [[the definition node|0F27PBRWD7]].
Then all entries below a leading entry are zero, and the nonzero rows form a staircase.
Every matrix can be brought to row echelon form by [[elementary row operations|04XWH28452]], see [[the existence theorem|~d9e684c6]], but the form is not unique.
Row echelon form matters because a system in this form is solved from the bottom up by [[back substitution|0ATFVE08MW]], and its pivot positions show the rank and the free variables.

## Motivation

To solve a system, we want each equation to contain fewer unknowns than the one above it.
Then the last equation has the fewest unknowns, and we can solve upwards.
Row echelon form is the precise version of this staircase shape.
It is the target of the forward phase of [[Gaussian elimination|0JVJ2WCXZH]].

## Notation

1. The names differ between books, and this is a common source of confusion.
2. In this tree and in Lay, "echelon form" or "row echelon form" does not require leading entries to be $1$; Lay uses "reduced echelon form" for the stronger form.
3. Anton and some other books require each leading entry of a row echelon form to be $1$.
4. Wikipedia notes both conventions.
5. The abbreviation REF is common, and RREF is used for the [[reduced row echelon form|0WF5AQYTW6]].

## Remarks

### Examples

1. $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$ is in row echelon form, with leading entries in columns $1$ and $3$.
2. $\begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix}$ and $\begin{bmatrix} 3 & 4 \\ 0 & \tfrac23 \end{bmatrix}$ are two row echelon forms of the same matrix, see [[two echelon forms|~492b4f42]].
3. The $4 \times 5$ matrix in [[the 4 by 5 example|~57cb9856]] is in row echelon form with pivot columns $1$, $3$ and $5$.
4. Every upper triangular matrix with nonzero diagonal entries is in row echelon form.
5. The zero matrix is in row echelon form, with no leading entries.

### Non-examples

1. $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 4 & 5 \end{bmatrix}$ is not in row echelon form, because a zero row lies above a nonzero row, see [[the non-examples|~127031fb]].
2. $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 6 & 7 \end{bmatrix}$ is not in row echelon form, because rows 2 and 3 have their leading entries in the same column.
3. $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ is not in row echelon form, because the leading entry of row 2 is left of that of row 1.

### Basic properties

1. Every matrix over a field is row equivalent to a matrix in row echelon form, see [[the existence theorem|~d9e684c6]].
2. Row echelon forms of a matrix are not unique, see [[two echelon forms|~492b4f42]].
3. The positions of the leading entries do not depend on the echelon form chosen, since they are the pivot positions of the unique RREF, see [[the uniqueness theorem|BF9SMZMJZE]].
4. So the number of nonzero rows of any echelon form of $A$ is the same; it is the rank of $A$.
5. The nonzero rows of a row echelon form are linearly independent, and they span the row space of $A$.
6. A system $[A \mid b]$ in row echelon form is inconsistent exactly when it has a leading entry in the last column.

### History

The staircase arrangement goes back to the counting-board arrays of the "Fangcheng" chapter of the *Nine Chapters on the Mathematical Art*.
The word "echelon" is French for a rung of a ladder and was used for a staggered formation of troops.

### Common errors

1. Requiring leading $1$s, or not requiring them, without checking which convention the book uses.
2. Allowing two leading entries in the same column.
3. Forgetting that zero rows must be at the bottom.

## Explanations

### L1 human

Row echelon form looks like a staircase.
Each nonzero row starts further to the right than the row above it, and the zero rows sit at the bottom.
For example, the rows $(1, 2, 3)$, $(0, 0, 4)$, $(0, 0, 0)$ form a staircase with two steps.
A system in this form is easy to solve from the bottom row up.

### L2 human

We decide whether $M = \begin{bmatrix} 2 & 1 & 0 & 3 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$ is in row echelon form.

1. The leading entries are $2$ in column $1$ and $5$ in column $3$.
2. Column $3$ is right of column $1$, so the staircase condition holds.
3. The only zero row is row $3$, which is at the bottom.
4. So $M$ is in row echelon form, in the convention of Lay; in Anton's convention it is not, because the leading entries are not $1$.

The typical use is to read off the rank and to set up [[back substitution|0ATFVE08MW]].
A trap: two people can reduce the same matrix to different echelon forms, and both can be right; only the pivot positions must agree.

### L3 human

Row echelon form is the matrix version of a triangular system, and for a square invertible matrix it is an upper triangular matrix with nonzero diagonal.
The pivot positions of the echelon form of $A$ describe the Schubert cell of the row space of $A$ in the Grassmannian.
Over a principal ideal domain, the analogous canonical form is the Hermite normal form.
In numerical work, the echelon form is obtained with partial pivoting, and the factorization $PA = LU$ records the steps, see [[LU decomposition|0RKG5YW66Y]].
