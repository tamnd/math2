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

Let $F$ be a field and let $A$ be an [[invertible|0EB9N0S33C]] $n \times n$ matrix over $F$.

1. For each $b \in F^n$, the [[system of linear equations|0JTRMBQ1SA]] $Ax = b$ has exactly one solution, namely $x = A^{-1} b$.
2. More generally, for each $n \times p$ matrix $B$ over $F$, the matrix equation $AX = B$ has exactly one solution, namely $X = A^{-1} B$.

## Remarks

### Why each hypothesis is needed

If $A$ is singular, the system can have no solution or many solutions.
For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the right-hand side $(3, 6)^{\mathsf{T}}$ gives infinitely many solutions and $(3, 7)^{\mathsf{T}}$ gives none, as the [[singular example|~872a66f4]] shows.

### Consequences

- The columns of $A^{-1}$ are the solutions of $Ax = e_j$, where $e_j$ are the standard basis vectors.
- The equation $XA = B$ has the unique solution $X = BA^{-1}$; note the order of the factors.

### Converse

If $Ax = b$ has a solution for each $b \in F^n$, then $A$ is invertible, by the [[invertible matrix theorem|~9b681771]].
If $Ax = 0$ has only the solution $x = 0$, then $A$ is invertible, by [[invertibility and row reduction|1ZK55FS2BF]].

### Generalizations

The statement holds over each commutative ring, with the same proof.

## Explanations

### L1 human

If we know the inverse of $A$, then we solve $Ax = b$ by one multiplication: $x = A^{-1}b$.
There is no other solution.

### L2 human

The method is in the concept [[solving linear systems by matrix inversion|~83a4c6b6]], with the examples there.
A trap: $x = bA^{-1}$ is wrong; the inverse must stand on the left of $b$.

### L3 human

The statement says that left multiplication by $A$ is a bijection of $F^n$, and its inverse map is left multiplication by $A^{-1}$.
Part 2 is the same fact for the space of $n \times p$ matrices, applied column by column.
In numerical practice one solves $Ax = b$ by an [[LU decomposition|0RKG5YW66Y]] and does not form $A^{-1}$, because this is cheaper and more accurate.
