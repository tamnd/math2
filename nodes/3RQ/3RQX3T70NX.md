---
tag: 3RQX3T70NX
kind: statement
role: proposition
name: Solving a linear system with an inverse matrix
msc: [15A09]
topics: [P8J6QR66TJ]
audience: school
uses: [0EB9N0S33C, 0JTRMBQ1SA]
about: [0EB9N0S33C]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-1.xml#L525
    locator: src/section3-1.xml:525
  - book: isbn:9780321982384
    locator: Section 2.2
---

## Statement

A system whose coefficient matrix is invertible has exactly one solution, and the inverse matrix produces it.
Let $F$ be a field and let $A$ be an [[invertible|0EB9N0S33C]] $n \times n$ matrix over $F$.

1. For each $b \in F^n$, the [[system of linear equations|0JTRMBQ1SA]] $Ax = b$ has exactly one solution, namely $x = A^{-1} b$.
2. More generally, for each $n \times p$ matrix $B$ over $F$, the matrix equation $AX = B$ has exactly one solution, namely $X = A^{-1} B$.

## Remarks

### The statement at work

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, whose inverse is $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, and solve $2x_1 + x_2 = 3$, $x_1 + x_2 = 2$.
One product gives the solution:
$$x = A^{-1} \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 - 2 \\ -3 + 4 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
Check: $2 + 1 = 3$ and $1 + 1 = 2$.
Part 1 also says that no other pair $(x_1, x_2)$ solves the system.

### Why the hypothesis is needed

If $A$ is singular, the system can have no solution or many.
For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the second equation is twice the first on the left side.
With right side $(3, 6)^{\mathsf{T}}$, every $(3 - 2t, t)$ is a solution, and with right side $(3, 7)^{\mathsf{T}}$ there is none, since $7 \ne 2 \cdot 3$.
The [[singular example|7XVJ4ZCXTV]] works this out.

### Order of the factors

Matrix products do not commute, so the side on which $A$ stands matters.
The equation $AX = B$ is solved by $X = A^{-1}B$, and the equation $XA = B$ by $X = BA^{-1}$.
The two answers differ in general.
For a column vector $b$, the expression $bA^{-1}$ is not even defined when $n \ge 2$.

### What it gives you

Taking $B = I_n$ in part 2 shows that the columns of $A^{-1}$ are the solutions of $Ax = e_j$, where $e_j$ is column $j$ of $I_n$.
This is the idea behind [[computing the inverse by row reduction|0Z83DHFMYM]].
Once $A^{-1}$ is known, each new right side costs only one matrix-vector product.

### The converse and generalizations

The converse holds in a strong form.
If $Ax = b$ has a solution for each $b \in F^n$, then $A$ is invertible, by the [[invertible matrix theorem|ACDFDABVQK]].
If $Ax = b$ has exactly one solution for even one $b$, then $Ax = 0$ has only the solution $0$, since the difference of two solutions solves $Ax = 0$, and $A$ is invertible by [[invertibility and row reduction|1ZK55FS2BF]].
The statement and its proof hold without change for an invertible matrix over any ring.

## Explanations

### L1 human

If we know the inverse of $A$, we solve $Ax = b$ by one multiplication: $x = A^{-1}b$.
There is no other solution, because the inverse undoes $A$.

### L2 human

The method, with more examples, is in the concept [[solving linear systems by matrix inversion|FBQCE3HVMP]].
Use it when the inverse is already known, or when many systems share the same matrix and the matrix is small.
A trap: $x = bA^{-1}$ is wrong; the inverse must stand to the left of $b$.

### L3 human

The statement says that left multiplication by $A$ is a bijection of $F^n$, whose inverse map is left multiplication by $A^{-1}$.
Part 2 is the same fact for the space of $n \times p$ matrices, applied column by column.
In numerical practice one solves $Ax = b$ with an [[LU decomposition|0RKG5YW66Y]] and does not form $A^{-1}$, because that is cheaper and more accurate.
