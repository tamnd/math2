---
tag: 0T6MWGZSXA
kind: concept
name: Augmented matrix
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
specializes: [0VD9ZSWWJG]
uses: [0HQFZAP3ND, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.1
same_as:
  wikidata: Q2750301
  wikipedia: Augmented matrix
inventory: [7FF7WWJRZD]
---

## Summary

The augmented matrix is a whole linear system written as one table of numbers, right sides included.
It is the [[coefficient matrix|0HQFZAP3ND]] $A$ with the column $b$ of constants added on the right.
For a system $Ax = b$ with $m$ equations in $n$ unknowns, it is the $m \times (n + 1)$ [[matrix|0VD9ZSWWJG]] $[A \mid b]$.
Row reduction is done on this table, and the reduced table shows whether the system has a solution and what the solutions are.
The [[formal definition|0YCDZ7N8VD]] also allows several columns behind the bar.

## Motivation

When we eliminate an unknown, we replace one equation by itself minus a multiple of another.
The right side changes together with the left side, so the bookkeeping must carry the constants along.
The coefficient matrix alone cannot do this, because it has no place for the constants.

So we add one more column for the right sides.
Each row of the table is then a complete equation, and every row operation acts on a whole equation at once.
Nothing is lost: the table and the order of the unknowns together give back the system.

## Notation

We write $[A \mid b]$, with a vertical bar where the equals signs stood.
Row $i$ is $(a_{i1}, \dots, a_{in} \mid b_i)$.
Some books leave out the bar and write $[A \; b]$ or $(A, b)$.
With several right sides $b, c$ we write $[A \mid b \; c]$, and in general $[A \mid B]$ for a matrix $B$ with $m$ rows.

## Remarks

### From a system to its table and back

The system $2x + y = 5$, $x - 3y = 0$ has the augmented matrix
$$\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 1 & -3 & 0 \end{array}\right].$$
The first two columns are the coefficient matrix, and the last column holds the right sides $5$ and $0$.

The way back works as well, once the order of the unknowns is fixed.
In the unknowns $x, y, z$ the table
$$\left[\begin{array}{ccc|c} 1 & 0 & 2 & 3 \\ 0 & 1 & -1 & 1 \end{array}\right]$$
is the system $x + 2z = 3$, $y - z = 1$.

### Solving on the table

Here is the system $x + 2y = 5$, $3x + 4y = 6$, solved only on its table.
Start with $\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & 4 & 6 \end{array}\right]$.
The step $R_2 \leftarrow R_2 - 3R_1$ makes row 2 equal to $(0, -2 \mid -9)$, and dividing by $-2$ gives $(0, 1 \mid \tfrac92)$.
Then $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0 \mid -4)$.
The table now says $x = -4$ and $y = \tfrac92$, and indeed $-4 + 9 = 5$ and $-12 + 18 = 6$.
Each step is an [[elementary row operation|04XWH28452]], and such steps never change the solution set, by the [[theorem on row operations|K41GT10YM6]].

### Several right sides at once

The row operations are chosen by looking at $A$ only.
So two systems $Ax = b$ and $Ax = c$ with the same $A$ can share one reduction of $[A \mid b \; c]$, as [[the example with two right sides|KZ1G2TB2Q3]] shows.
Taking the columns of the identity as right sides, the reduction of $[A \mid I]$ to $[I \mid A^{-1}]$ computes the inverse of $A$.

### What the last column decides

A row $(0, \dots, 0 \mid c)$ with $c \ne 0$ says $0 = c$, which is impossible.
So the system is inconsistent exactly when an echelon form of $[A \mid b]$ has a pivot in the last column, by the theorem on [[existence and uniqueness|BKA191KD1S]].
In terms of rank, $\rank [A \mid b]$ is either $\rank A$ or $\rank A + 1$, and the system is consistent exactly when it equals $\rank A$.
This is the [[Rouché-Capelli theorem|0HV1SKWPMS]].

### What it is not

The coefficient matrix $\begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}$ of the first system is not its augmented matrix, because it lacks the column $b$.
An array of numbers read off a nonlinear system is not an augmented matrix either.
Treating $x^2$ as $x$ in $x^2 + y = 3$, $x - y = 1$ gives an array whose "solution" $(2, 1)$ fails the first equation, as [[the nonlinear array|VDC3D0JADY]] shows.

### Watch out

Reducing $A$ alone and forgetting $b$ is the most common slip.
For $x + 2y = 3$, $2x + 4y = 7$, the reduced form of $A$ has one pivot and looks harmless.
The reduced form of $[A \mid b]$ has a second pivot in the last column, and the system has no solution, as [[the trap example|HCYVBVXBF4]] shows.
A second slip is to read a pivot in the last column as a value of an unknown; it is the equation $0 = 1$.

### History

The counting boards of the Chinese *Nine Chapters on the Mathematical Art* held the constants in the same array of rods as the coefficients.
So the solver of that time already worked on the augmented matrix, one equation per column of rods.

### Try it

First, write the augmented matrix of $x - z = 2$, $y + z = 0$ in the unknowns $x, y, z$.
It is $\left[\begin{array}{ccc|c} 1 & 0 & -1 & 2 \\ 0 & 1 & 1 & 0 \end{array}\right]$, with a $0$ for each missing unknown.

Second, decide whether the table $\left[\begin{array}{cc|c} 1 & 3 & 1 \\ 0 & 0 & 4 \end{array}\right]$ comes from a consistent system.
It does not: the second row says $0 = 4$.

## Explanations

### L1 human

The augmented matrix is the whole system written as a table of numbers.
Each row is one equation, and the last column holds the numbers on the right of the equals signs.
A bar separates that column from the rest.
For $2x + y = 5$ and $x - 3y = 0$ the rows are $2, 1 \mid 5$ and $1, -3 \mid 0$.

### L2 human

In practice you build the table, row reduce it, and read off the answer.
For $x + 2y = 5$, $3x + 4y = 6$ the reduction ends with the rows $(1, 0 \mid -4)$ and $(0, 1 \mid \tfrac92)$, so $x = -4$ and $y = \tfrac92$.
Watch out: every operation acts on the full row, right side included.
A pivot in the last column is the equation $0 = 1$, not the value of an unknown.

### L3 human

The table $[A \mid b]$ is the coefficient matrix of the homogeneous system $Ax - bt = 0$ in the $n + 1$ unknowns $(x, t)$.
The solutions of $Ax = b$ are the solutions of this system with $t = 1$.
This is the projective view of an affine system, and it explains why consistency is a statement about the last column.
