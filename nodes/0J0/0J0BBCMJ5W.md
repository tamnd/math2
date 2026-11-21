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

Pivots are the corners of the staircase, and they split the unknowns into those the equations fix and those we may choose.
The pivots of a matrix in [[row echelon form|0VYCDGMJJJ]] are the leading entries of its nonzero rows.
For any matrix $A$, the pivot positions are the places of the pivots in an echelon form of $A$, and the pivot columns of $A$ are the columns at those places.
In a [[system|0GT4WWGWH2]] $Ax = b$, the unknowns of the pivot columns are the basic variables, and the others are the free variables.
The positions do not depend on the echelon form chosen, because they are the leading $1$s of the unique [[reduced row echelon form|0WF5AQYTW6]], by the [[uniqueness theorem|BF9SMZMJZE]].
The number of pivots is the rank, and the free variables are the parameters of the solution set.
The [[formal definition|0BCMGDHZGR]] fixes these words.

## Motivation

In elimination, each step picks an entry and uses it to clear the other entries of its column.
That entry is the pivot of the step, and from then on its column belongs to an unknown that the equations determine.

Some columns never receive a pivot.
Their unknowns are not determined: we can choose them freely, and the others follow.
So counting pivots counts the independent conditions, and the other columns count the free choices.
For the single equation $x + y = 3$, the pivot sits in the column of $x$, so $y$ is free, and $y = 1$ gives $x = 2$ while $y = 5$ gives $x = -2$.

## Notation

The word "pivot" has two meanings in the literature.
Strang's textbook and many numerical texts call the number itself the pivot: the nonzero entry by which we divide in elimination.
Lay's textbook uses "pivot position" for the place in $A$ of a leading $1$ of the RREF, and "pivot column" for a column that contains a pivot position.
In the first meaning, the pivots depend on the elimination steps, while in the second, the pivot positions depend only on $A$.
Basic variables are also called leading or dependent variables, and free variables are also called parameters.

## Remarks

### Finding pivots in a system

Take $x_1 + 2x_2 + x_3 = 4$, $2x_1 + 4x_2 + 3x_3 = 9$.
The step $R_2 \leftarrow R_2 - 2R_1$ gives the echelon form
$$\left[\begin{array}{rrr|r} 1 & 2 & 1 & 4 \\ 0 & 0 & 1 & 1 \end{array}\right],$$
with pivots at $(1, 1)$ and $(2, 3)$.
So $x_1$ and $x_3$ are basic, and $x_2$ is free.
Back substitution gives $x_3 = 1$ and, with $x_2 = t$, $x_1 = 4 - 2t - 1 = 3 - 2t$.
Check $t = 1$, the point $(1, 1, 1)$: $1 + 2 + 1 = 4$ and $2 + 4 + 3 = 9$.

### More examples

In $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$ the pivots are $1$ at $(1, 1)$ and $4$ at $(2, 3)$, and the pivot columns are $1$ and $3$.
The matrix in [[the pivots example|HQVWQBHQSC]] has pivot positions $(1, 2)$ and $(2, 4)$, basic variables $x_2, x_4$ and free variables $x_1, x_3, x_5$.
In the system $x + y + z = 3$, $x - y + 3z = 1$ of [[the line example|PRB44DTZ1P]], $x$ and $y$ are basic and $z$ is free.
In [[the 4 by 5 example|TSZFS6VP5M]] the pivot columns are $1$, $3$ and $5$.
An invertible $n \times n$ matrix has $n$ pivots, one in each row and each column, and no free variables.

### What the count of pivots tells

Each row and each column contains at most one pivot, so the number $r$ of pivots satisfies $r \le m$ and $r \le n$.
This number is the rank of $A$, and the pivot columns of $A$ form a basis of its [[column space|03AJKXH1AV]], by [[the pivot basis|11CSKXQNG3]] and [[the second proof of Rouché-Capelli|N8HEMWKHZ0]].
The system $Ax = 0$ has $n - r$ free variables, and $n - r$ is the dimension of the [[null space|0PHDYNR24D]].
A consistent system has a unique solution exactly when it has no free variables, by the theorem on [[existence and uniqueness|BKA191KD1S]].
The system $Ax = b$ is consistent for every $b$ exactly when every row of $A$ has a pivot, by the [[pivot criterion|HJTF7B36W9]].

### What is not a pivot

In $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ the leading entries of the rows are not pivots, because the matrix is not in echelon form.
Its pivot positions are $(1, 1)$ and $(2, 2)$, where the entries are $0$, as [[the non-example|RY5BJ98F63]] shows.
A pivot in the sense of a number used in elimination is never $0$, since we divide by it, and a zero in a pivot place forces a row exchange.
A variable that is missing from one equation is not free for that reason, since free means that its column has no pivot.

### Watch out

Read pivots only from a matrix in echelon form.
For a basis of the column space of $A$, take the pivot columns of $A$ itself, not those of the echelon form.
A pivot in the last column of $[A \mid b]$ is not a pivot of $A$, and it means that the system is inconsistent.

### Try it

Find the basic and free variables of $\left[\begin{array}{rrrr|r} 1 & 3 & 0 & 2 & 1 \\ 0 & 0 & 1 & 4 & 5 \end{array}\right]$ in $x_1, \dots, x_4$.
The pivot columns are $1$ and $3$, so $x_1, x_3$ are basic and $x_2, x_4$ are free.

## Explanations

### L1 human

When we simplify a system, each step uses one number to clear the numbers below it, and that number is a pivot.
Each pivot pins down one unknown, which we call basic.
The unknowns without a pivot are free: we may give them any values.
For example, in the one equation $x + y = 3$, $x$ is basic and $y$ is free.

### L2 human

The typical use is to count the parameters of the solution set before solving.
Reduce to echelon form, mark the pivots, and give each free variable its own parameter.
Watch out: choosing $x_1$ as free instead of $x_2$ in the system above also describes the solutions, but it is not the standard form, which always takes the non-pivot columns.

### L3 human

The pivot positions of $A$ form a set of $r$ positions with one in each of $r$ rows and $r$ columns, increasing to the right.
They depend only on the row space of $A$, and they index the Schubert cell of this space in the Grassmannian.
In numerical linear algebra, pivoting means choosing which entry to use as the pivot, for stability, and partial and complete pivoting belong to numerical analysis.
In the simplex method of linear programming, a pivot step is an elimination step around one entry, with the same algebra, and "basic variable" has a related meaning there.
