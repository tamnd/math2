---
tag: 0HQFZAP3ND
kind: concept
name: Coefficient matrix
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
specializes: [0VD9ZSWWJG]
uses: [0GT4WWGWH2, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Coefficient_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.1
same_as:
  wikidata: Q5140577
  wikipedia: Coefficient matrix
---

## Summary

The coefficient matrix keeps the numbers of a linear system and drops the names of the unknowns.
It turns a list of equations into one object, and the whole system becomes the single equation $Ax = b$.
For a [[system of linear equations|0GT4WWGWH2]] with $m$ equations in $n$ unknowns, the coefficient matrix is the $m \times n$ [[matrix|0VD9ZSWWJG]]
$$A = (a_{ij}), \qquad a_{ij} = \text{the coefficient of } x_j \text{ in equation } i.$$
The [[formal definition|0P7A2MJD24]] states this with the convention for missing unknowns.

## Motivation

Writing every unknown in every row is slow, and the names of the unknowns never change during elimination.
Only the numbers change, so we keep only the numbers, in a table with one row for each equation and one column for each unknown.
This is what the Chinese counting boards of the *Nine Chapters* did two thousand years ago, and it is what a computer stores today.

The table is more than shorthand.
Questions about the system become questions about the matrix: whether a solution is unique depends only on $A$, and the homogeneous system $Ax = 0$ is given by $A$ alone.
Later sub-areas read $A$ as a linear map, and the sub-area on matrix algebra studies the [[matrix|0VD9ZSWWJG]] as an object of its own.

## Notation

We write $A = (a_{ij})$ or $[a_{ij}]$, with the row index first.
With $x = (x_1, \dots, x_n)^{\mathsf{T}}$ and $b = (b_1, \dots, b_m)^{\mathsf{T}}$, the system is $Ax = b$, where $Ax$ is the [[matrix-vector product|0PDVQEP0ZC]].
Some books write $(a_{ij})_{1 \le i \le m,\, 1 \le j \le n}$ to show the sizes.

## Remarks

### Reading the matrix off a system

The system $2x + y = 5$, $x - 3y = 0$ has the coefficient matrix
$$A = \begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}.$$
Row 1 holds the coefficients of the first equation, and column 2 holds the coefficients of $y$.

When an unknown is missing from an equation, its coefficient is $0$, and the matrix must show that $0$.
The system $2y + x = 5$, $3z - y = 1$, $x = 4z$ first needs its unknowns in the order $x, y, z$ on the left, and then
$$A = \begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 3 \\ 1 & 0 & -4 \end{bmatrix},$$
as [[a coefficient matrix with missing unknowns|2E4TZ2ZV57]] works out.
The same rule gives the $1 \times 3$ matrix $\begin{bmatrix} 1 & 0 & -1 \end{bmatrix}$ for the single equation $x_1 - x_3 = 7$ in $x_1, x_2, x_3$.

### Two ways to read $Ax$

Each entry of $Ax$ is the left side of one equation:
$$(Ax)_i = a_{i1} x_1 + \cdots + a_{in} x_n.$$
Read by columns instead, $Ax$ is the [[linear combination|0V8F3E48E6]] of the columns $a_1, \dots, a_n$ of $A$ with the weights $x_1, \dots, x_n$:
$$Ax = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n.$$
For the $2 \times 2$ matrix above and $x = (3, 1)$, both readings give $(7, 0)$: by rows $2 \cdot 3 + 1 = 7$ and $3 - 3 = 0$, and by columns $3(2, 1) + 1(1, -3) = (7, 0)$.
The second reading is the theorem on [[linear systems as vector equations|E7SAHXQEVC]].

### What the matrix decides

Some answers depend only on $A$, and not on $b$.
The homogeneous system $Ax = 0$ is given by $A$, and its solution set is the [[null space|0PHDYNR24D]] of $A$.
When $Ax = b$ is consistent, its solution is unique exactly when every column of $A$ has a pivot, by the theorem on [[existence and uniqueness of solutions|BKA191KD1S]].
If $A$ is square and [[invertible|0EB9N0S33C]], the system has exactly one solution, $x = A^{-1} b$, for every $b$.
Reordering the equations permutes the rows of $A$ and keeps the solution set, while reordering the unknowns permutes the columns.

### What it is not

The [[augmented matrix|0T6MWGZSXA]] $[A \mid b]$ has the extra column $b$, so for $2x + y = 5$, $x - 3y = 0$ it is $\begin{bmatrix} 2 & 1 & 5 \\ 1 & -3 & 0 \end{bmatrix}$, and that is not the coefficient matrix.
Nor is the array that you read off before moving all unknowns to the left.
For $x + y = 2x + 1$, $3y = x - 2$, the left sides suggest $\begin{bmatrix} 1 & 1 \\ 0 & 3 \end{bmatrix}$, but the true matrix is $\begin{bmatrix} -1 & 1 \\ -1 & 3 \end{bmatrix}$, as [[unknowns on both sides|PE7H79RRY9]] shows.

### Watch out

The most common slip is a missing zero.
In $x_1 - 2x_3 = 4$, $3x_2 + x_1 = 0$, the first row must be $(1, 0, -2)$, with a $0$ for the absent $x_2$.
The second slip is a change of order: the second equation lists $x_2$ first, but its row is still $(1, 3, 0)$ in the order $x_1, x_2, x_3$.

### History

Arrays of coefficients on a counting board appear in the *Nine Chapters on the Mathematical Art*, where each column of rods held one equation.
Sylvester introduced the word "matrix" in 1850.

### Try it

First, write the coefficient matrix of $x + z = 1$, $y = 2$, $x - y + 4z = 0$.
It is $\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & -1 & 4 \end{bmatrix}$.

Second, with $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$, compute $Ax$ for $x = (1, -1)$ as a combination of columns.
It is $1 \cdot (1, 3) - 1 \cdot (2, 4) = (-1, -1)$.

## Explanations

### L1 human

The coefficient matrix is the table of numbers in front of the unknowns.
Each row is one equation and each column is one unknown.
For $2x + y = 5$ and $x - 3y = 0$, the table has the rows $2, 1$ and $1, -3$.
When an unknown is missing from an equation, we write $0$ in its place.

### L2 human

Here is the typical first step of a computation: write $x_1 - 2x_3 = 4$, $3x_2 + x_1 = 0$ as $Ax = b$.
First write both equations with the unknowns in the order $x_1, x_2, x_3$:
$$x_1 + 0x_2 - 2x_3 = 4, \qquad x_1 + 3x_2 + 0x_3 = 0.$$
Then read the rows:
$$A = \begin{bmatrix} 1 & 0 & -2 \\ 1 & 3 & 0 \end{bmatrix}, \qquad b = \begin{pmatrix} 4 \\ 0 \end{pmatrix}.$$
Check with $x = (4, -\tfrac43, 0)$: $Ax = (4 + 0 - 0, 4 - 4 + 0) = (4, 0) = b$.
Once the system is in this form, a computer can row reduce it, and the names of the unknowns no longer matter.

### L3 human

The coefficient matrix is the matrix of the [[linear map|0NRYHJPQG2]] $F^n \to F^m$, $x \mapsto Ax$, in the standard bases.
So existence of solutions is a question about the image of this map, and uniqueness is a question about its kernel.
Row operations replace $A$ by $EA$ with $E$ invertible, which changes coordinates in the target $F^m$ and keeps the kernel.
