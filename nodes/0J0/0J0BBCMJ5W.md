---
tag: 0J0BBCMJ5W
kind: concept
name: Pivots, basic variables and free variables
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [0VYCDGMJJJ, 0WF5AQYTW6, 0GT4WWGWH2]
aliases: [pivot, pivot-position, pivot-column, basic-variable]
sources:
  - url: https://en.wikipedia.org/wiki/Pivot_element
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.2
  - book: isbn:9781733146678
    locator: Chapter 2
same_as:
  wikidata: Q1425280
  wikipedia: Pivot element
---

## Summary

Let $A$ be a matrix over a field, and let $E$ be a matrix in [[row echelon form|0VYCDGMJJJ]] that is row equivalent to $A$.
The pivots of $E$ are the leading entries of its nonzero rows; their positions are the pivot positions of $A$, and the columns that contain them are the pivot columns of $A$.
These positions do not depend on the choice of $E$, because they are the positions of the leading $1$s of the unique [[reduced row echelon form|0WF5AQYTW6]] of $A$, see [[the uniqueness theorem|BF9SMZMJZE]].
In a [[system|0GT4WWGWH2]] $Ax = b$, the unknowns of the pivot columns of $A$ are the basic variables, and the others are the free variables.
The exact definition is in [[the definition node|0BCMGDHZGR]].
Pivots matter because their number is the rank, and the free variables give the parameters of the solution set.

## Motivation

In elimination, each step picks an entry and uses it to clear the other entries of its column.
That entry is the pivot of the step, and its column then belongs to one unknown that the equations determine.
The unknowns whose columns never receive a pivot are not determined: we can choose them freely, and the others follow.
So counting pivots counts the independent conditions, and the remaining columns count the free choices.

## Notation

1. The word "pivot" has two meanings in the literature, and this is a common source of confusion.
2. Strang and many numerical texts call the number itself the pivot: the nonzero entry by which we divide in elimination.
3. Lay uses "pivot position" for the place in $A$ of a leading $1$ of the RREF, and "pivot column" for a column that contains a pivot position; he calls the number used in elimination a pivot too.
4. In the first meaning, pivots depend on the elimination steps; in the second, pivot positions depend only on $A$.
5. Basic variables are also called leading variables or dependent variables; free variables are also called parameters.

## Remarks

### Examples

1. In $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$, the pivots are $1$ at $(1, 1)$ and $4$ at $(2, 3)$; the pivot columns are $1$ and $3$.
2. The matrix in [[the pivots example|~f5c146f8]] has pivot positions $(1, 2)$ and $(2, 4)$, basic variables $x_2, x_4$ and free variables $x_1, x_3, x_5$.
3. In the system $x + y + z = 3$, $x - y + 3z = 1$ of [[the line example|~f4f0e07b]], $x$ and $y$ are basic and $z$ is free.
4. An invertible $n \times n$ matrix has $n$ pivots, one in each row and each column, and no free variables.
5. In [[the 4 by 5 example|~57cb9856]], the pivot columns are $1$, $3$ and $5$.

### Non-examples

1. In $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, the leading entries of the rows are not pivots, because the matrix is not in echelon form; the pivot positions are $(1, 1)$ and $(2, 2)$, see [[the non-example|~fac38c23]].
2. A zero entry is never a pivot: elimination cannot divide by it, so a zero in a pivot place forces a row exchange.
3. A variable that is missing from one equation is not free for that reason; free means that its column has no pivot.

### Basic properties

1. Each row and each column contains at most one pivot.
2. So the number $r$ of pivots satisfies $r \le m$ and $r \le n$.
3. The number of pivots is the rank of $A$: the pivot columns of $A$ form a basis of its [[column space|03AJKXH1AV]], see [[the pivot basis|11CSKXQNG3]] and [[the second proof of Rouché-Capelli|~403d5028]].
4. The number of free variables of $Ax = 0$ is $n - r$, and it is the dimension of the [[null space|0PHDYNR24D]].
5. A consistent system has a unique solution exactly when it has no free variables, see [[the existence and uniqueness theorem|BKA191KD1S]].
6. $Ax = b$ is consistent for every $b$ exactly when every row of $A$ has a pivot, see [[the pivot criterion|HJTF7B36W9]].

### History

The use of "pivot" for the entry that drives an elimination step is standard in numerical analysis and in Strang's textbook.
The terms "basic variable" and "free variable" are standard in English textbooks such as Lay; "basic variable" is also used in linear programming, with a related meaning.

### Common errors

1. Reading pivots from a matrix that is not yet in echelon form.
2. Taking the columns of the echelon form, not of $A$, as a basis of the column space of $A$.
3. Counting a pivot in the last column of $[A \mid b]$ as a pivot of $A$; it means that the system is inconsistent.

## Explanations

### L1 human

When we simplify a system, each step uses one number to clear the numbers below it; that number is a pivot.
Each pivot pins down one unknown, which we call basic.
The unknowns without a pivot are free: we may give them any values.
For example, in the one equation $x + y = 3$, $x$ is basic and $y$ is free, so $y = 1$ gives $x = 2$ and $y = 5$ gives $x = -2$.

### L2 human

We find the pivots, basic and free variables of $x_1 + 2x_2 + x_3 = 4$, $2x_1 + 4x_2 + 3x_3 = 9$.

1. $R_2 \leftarrow R_2 - 2R_1$ gives $(0, 0, 1 \mid 1)$.
2. The echelon form $\left[\begin{array}{rrr|r} 1 & 2 & 1 & 4 \\ 0 & 0 & 1 & 1 \end{array}\right]$ has pivots at $(1, 1)$ and $(2, 3)$.
3. So $x_1, x_3$ are basic and $x_2$ is free.
4. Back substitution: $x_3 = 1$, and $x_1 = 4 - 2x_2 - x_3 = 3 - 2t$ with $x_2 = t$.
5. Check $t = 1$, the point $(1, 1, 1)$: $1 + 2 + 1 = 4$ and $2 + 4 + 3 = 9$.

The typical use is to count the parameters of the solution set before solving.
A trap: the choice of free variables comes from the pivot columns; choosing $x_1$ as free instead also describes the solutions, but it is not the standard form.

### L3 human

The pivot positions of $A$ form a set of $r$ positions with one in each of $r$ rows and $r$ columns, increasing to the right.
They depend only on the row space of $A$, and they index the Schubert cell of this space in the Grassmannian.
In numerical linear algebra, pivoting means choosing which entry to use as the pivot, for stability; partial and complete pivoting belong to numerical analysis and are outside this topic.
In the simplex method of linear programming, a pivot step is an elimination step around one entry, with the same algebra.
