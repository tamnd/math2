---
tag: 0ZZQ2E1MTE
kind: statement
role: proposition
name: Determinant of the transpose
aliases: [determinant-of-a-transpose]
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 0W809K6AW0]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.det_transpose
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

Rows and columns play the same role in a determinant: turning a matrix on its diagonal does not change the value.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
Then
$$\det A^{\mathsf{T}} = \det A,$$
where $A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]] of $A$ and $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### A check in size three

Take
$$A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 2 \end{pmatrix}, \qquad A^{\mathsf{T}} = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 3 & 1 \\ 1 & 2 & 2 \end{pmatrix}.$$
Expand $A$ along its first row:
$$\det A = 2 (3 \cdot 2 - 2 \cdot 1) - 0 + 1 (1 \cdot 1 - 3 \cdot 1) = 8 - 2 = 6.$$
Expand $A^{\mathsf{T}}$ along its first row:
$$\det A^{\mathsf{T}} = 2 (3 \cdot 2 - 1 \cdot 2) - 1 (0 \cdot 2 - 1 \cdot 1) + 1 (0 \cdot 2 - 3 \cdot 1) = 8 + 1 - 3 = 6.$$
The two expansions use different numbers, but they give the same value.

### Why the ring must be commutative

The [[proof|CC5G952B5J]] reorders the factors of each product, and that needs $ab = ba$.
Over the quaternions the naive formula $a_{11} a_{22} - a_{12} a_{21}$ shows the failure.
For $A = \begin{pmatrix} i & j \\ i & j \end{pmatrix}$ it gives $ij - ji = k - (-k) = 2k$.
For $A^{\mathsf{T}} = \begin{pmatrix} i & i \\ j & j \end{pmatrix}$ it gives $ij - ij = 0$.

### Every row rule becomes a column rule

Since $\det$ is multilinear and alternating in the rows of $A^{\mathsf{T}}$, it is multilinear and alternating in the columns of $A$.
So the [[effects of row operations|09YB3WQG38]] hold for column operations, and two equal columns or a zero column give determinant $0$.
The [[Laplace expansion along a column|06AMCJMMVM]] follows from the expansion along a row.
In a computation you may therefore mix row and column operations freely.

### What it gives you

For a real orthogonal matrix $Q$ we have $Q^{\mathsf{T}} Q = I$.
With [[multiplicativity|04CPJ6AF00]] this gives $(\det Q)^2 = \det Q^{\mathsf{T}} \det Q = 1$, so $\det Q = \pm 1$.
In the same way, a real [[skew-symmetric matrix|0PBY4E9GQF]] $A$ of odd size satisfies $\det A = \det(-A) = -\det A$, so it is [[singular|55RX9C0ZTH]].
The statement also shows that the three properties of the definition, stated for columns, describe the same function; this is part of the [[equivalence of the three definitions|W3JN0WPZ10]].

### Watch out

$\det A^{\mathsf{T}} = \det A$ does not mean $A^{\mathsf{T}} = A$.
The matrices in the first example are different, and only their determinants agree.

### Try it

A $3 \times 3$ matrix $A$ has $\det A = 4$; what is $\det(2 A^{\mathsf{T}})$?
The transpose keeps the value $4$, and the factor $2$ in each of the three rows gives $2^3 \cdot 4 = 32$.

## Explanations

### L1 human

Turn a square table on its diagonal, so that the rows become the columns.
The determinant does not change.
For example, $\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 4 - 6 = -2$, and $\det \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} = 4 - 6 = -2$ as well.
So every rule about rows has a twin rule about columns.

### L2 human

Here is a typical use: compute
$$\det \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \\ 3 & 6 & 1 \end{pmatrix}.$$
Look at the columns: the second column is twice the first.
By the statement, the rule for dependent rows also holds for columns, so the determinant is $0$.
Check by the rule of Sarrus: $4 + 42 + 36 - 36 - 42 - 4 = 0$.
The problem shows the typical use: you may look for structure in the columns as well as in the rows, and pick whichever is simpler.

### L3 human

In invariant terms, the transpose is the matrix of the [[dual map|0AZ5ARP287]] in the dual bases, by the theorem on the [[matrix of the dual map|0ZPB3180AY]].
So the statement says that an endomorphism $f$ and its dual $f^{*}$ have the same [[determinant|0X0HQYSZ0K]].
Both act on a top exterior power, which is free of rank $1$, and both act by the same scalar.
Applied to square submatrices, the statement shows that $A$ and $A^{\mathsf{T}}$ have the same minors up to transposition, so they have the same [[rank by minors|HVHQ50TJB1]].
