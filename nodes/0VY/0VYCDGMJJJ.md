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

A matrix in row echelon form has a staircase shape, and a system with that shape can be solved from the bottom up.
Call the first nonzero entry of a nonzero row its leading entry.
A [[matrix|0VD9ZSWWJG]] is in row echelon form when its zero rows are at the bottom and each leading entry lies strictly to the right of the leading entry in the row above.
Every matrix can be brought to this form by [[elementary row operations|04XWH28452]], by the [[existence theorem|FCM29NQ6DN]], although the form is not unique.
The positions of the leading entries show the rank and the free variables, and [[back substitution|0ATFVE08MW]] then finds the solutions.
The [[formal definition|0F27PBRWD7]] states the two conditions.

## Motivation

To solve a system by hand, we want each equation to involve fewer unknowns than the one above it.
Then the last equation has the fewest unknowns, we solve it first, and we work upwards.
For example, the system $x + 2y + 3z = 6$, $4z = 8$ is easy: the second equation gives $z = 2$, and the first then gives $x + 2y = 0$.

Row echelon form is the exact version of this staircase shape.
It is the target of the forward phase of [[Gaussian elimination|0JVJ2WCXZH]], which creates zeros below each leading entry, column by column.

## Notation

The names differ between books, and this causes confusion.
On this site and in Lay's textbook, "echelon form" or "row echelon form" does not require the leading entries to be $1$, and Lay uses "reduced echelon form" for the stronger form.
Some other books require each leading entry of a row echelon form to be $1$.
The abbreviation REF is common, and RREF is used for the [[reduced row echelon form|0WF5AQYTW6]].

## Remarks

### Reading a staircase

The matrix
$$\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$$
is in row echelon form.
Its leading entries are $1$ in column $1$ and $4$ in column $3$, and the zero row is at the bottom.
The step from row 1 to row 2 jumps two columns, because column $2$ has no leading entry.
In a system, the unknown of column $2$ would be a free variable.

Below each leading entry, all entries are zero.
This follows from the definition: every lower row starts further to the right.
Above a leading entry, the entries can be anything.

### More examples

Every upper triangular matrix with nonzero diagonal entries is in row echelon form.
The zero matrix is in row echelon form, with no leading entries at all.
[[The 4 by 5 example|TSZFS6VP5M]] is in row echelon form with pivot columns $1$, $3$ and $5$.

### Shapes that fail

The matrix $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 4 & 5 \end{bmatrix}$ fails, because a zero row lies above a nonzero row.
The matrix $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 6 & 7 \end{bmatrix}$ fails, because rows 2 and 3 have their leading entries in the same column.
The matrix $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ fails, because the leading entry of row 2 is left of that of row 1.
[[The non-examples|KEV3SBST22]] repair the first two with one row operation each, and a swap repairs the third.

### Not unique, but the pivots are

The matrix $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ has the echelon forms $\begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix}$ and $\begin{bmatrix} 3 & 4 \\ 0 & \tfrac23 \end{bmatrix}$, as [[two echelon forms|19FNDHJ181]] shows.
The numbers differ, but the positions of the leading entries do not.
They never do, because they are the pivot positions of the unique RREF, by the [[uniqueness theorem|BF9SMZMJZE]].
So every echelon form of $A$ has the same number of nonzero rows, and this number is the rank of $A$.
The nonzero rows of an echelon form are linearly independent and span the row space of $A$.

### Consistency at a glance

An augmented matrix $[A \mid b]$ in row echelon form belongs to an inconsistent system exactly when it has a leading entry in the last column.
Such a row reads $0 = c$ with $c \ne 0$.

### Watch out

Check which convention your book uses before you scale rows to get leading $1$s.
Two leading entries in the same column are never allowed, and zero rows must be at the bottom.

### History

The staircase arrangement goes back to the counting-board arrays of the "Fangcheng" chapter of the *Nine Chapters on the Mathematical Art*.
The word "echelon" is French for a rung of a ladder, and it was used for a staggered formation of troops.

### Try it

Is $\begin{bmatrix} 0 & 3 & 1 \\ 0 & 0 & 2 \end{bmatrix}$ in row echelon form, and what is its rank?
Yes, with leading entries in columns $2$ and $3$, so the rank is $2$.

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
4. So $M$ is in row echelon form in the convention of this site. In a book that requires leading $1$s, it is not, because the leading entries are $2$ and $5$.

The typical use is to read off the rank and to set up [[back substitution|0ATFVE08MW]].
Watch out: two people can reduce the same matrix to different echelon forms, and both can be right, but the pivot positions must agree.

### L3 human

Row echelon form is the matrix version of a triangular system, and for a square invertible matrix it is an upper triangular matrix with nonzero diagonal.
The pivot positions of an echelon form of $A$ describe the Schubert cell of the row space of $A$ in the Grassmannian.
Over a principal ideal domain, the analogous canonical form is the Hermite normal form.
In numerical work, the echelon form is obtained with partial pivoting, and the factorization $PA = LU$ records the steps, as the page on [[LU decomposition|0RKG5YW66Y]] explains.
