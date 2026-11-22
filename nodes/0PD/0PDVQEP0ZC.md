---
tag: 0PDVQEP0ZC
kind: concept
name: Matrix–vector product
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
uses: [0VD9ZSWWJG, 0V8F3E48E6, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Definition
  - book: isbn:9780321982384
    locator: Section 1.4
  - url: https://understandinglinearalgebra.org/
    locator: Section 2.2
---

## Summary

A matrix acts on a vector, and the result can be read in two ways: row by row as a list of dot products, or column by column as a mix of the columns.
For an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ and a column vector $x$ with $n$ entries, the product $Ax$ is the column vector with $m$ entries
$$(Ax)_i = a_{i1} x_1 + \dots + a_{in} x_n,$$
the [[dot product|0S52TNNTH9]] of row $i$ of $A$ with $x$.
The same vector is the [[linear combination|0V8F3E48E6]] $Ax = x_1 a_1 + \dots + x_n a_n$ of the columns $a_1, \dots, a_n$ of $A$, with the entries of $x$ as weights.
The [[formal definition|0CCQV3884B]] uses the first form.
The product turns a [[system of linear equations|0GT4WWGWH2]] into one equation $Ax = b$, and a matrix into a [[linear map|094V2VBJXJ]].

## Motivation

Start with the system
$$x_1 + 2x_2 = 5, \qquad 3x_1 - x_2 = 1.$$
It has two left sides, and each one pairs the coefficients of one equation with the unknowns.
If we define $Ax$ as the column of these left sides, the whole system becomes a single equation:
$$\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} x_1 + 2x_2 \\ 3x_1 - x_2 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}.$$
The [[worked system|VBFC9PEMPF]] solves it.

The column view answers a second question: which vectors $b$ are combinations of the columns of $A$?
These are exactly the vectors $b$ for which $Ax = b$ has a solution.
So one product connects equations with combinations of vectors.

## Notation

The vector $x$ is a column, that is an $n \times 1$ matrix, and $Ax$ is the [[matrix product|076JGP6R3T]] of an $m \times n$ and an $n \times 1$ matrix.
A row vector $y^{\mathsf{T}}$ with $m$ entries gives the product $y^{\mathsf{T}} A$ on the left, a row with $n$ entries.
In Mathlib, `A.mulVec x` or `A *ᵥ x` is the product with a function `x : n → α`, and `x ᵥ* A` is the product on the left.

## Remarks

### Rows and columns give the same answer

Take $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ and $x = (1, 0, -1)^{\mathsf{T}}$.
Row by row, the entries are $1 + 0 - 3 = -2$ and $4 + 0 - 6 = -2$.
Column by column,
$$Ax = 1 \begin{pmatrix} 1 \\ 4 \end{pmatrix} + 0 \begin{pmatrix} 2 \\ 5 \end{pmatrix} - 1 \begin{pmatrix} 3 \\ 6 \end{pmatrix} = \begin{pmatrix} -2 \\ -2 \end{pmatrix}.$$
The two views add the same six terms $a_{ij} x_j$ in a different order, so they always agree; the [[2 × 3 example|1NYHYECE0A]] carries this out step by step.

### Columns are images of basis vectors

For the [[standard basis vector|0V7ZD6P7RK]] $e_j$, the column view gives $Ae_j = a_j$, the column $j$ of $A$; this is [[this statement|PFEYWQJDK1]].
For instance, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} e_2 = (2, 4)^{\mathsf{T}}$.
It follows that $Ax = 0$ for all $x$ only when $A = 0$, and that $I_n x = x$ for the [[identity matrix|06DW9BAWB1]].

### The rules of the product

The product is linear in $x$: $A(x + y) = Ax + Ay$ and $A(cx) = c(Ax)$, which is the [[linearity of the product|ZE36VEAY80]].
It is also linear in $A$: $(A + B)x = Ax + Bx$ and $(cA)x = c(Ax)$, entry by entry.
For an $n \times p$ matrix $B$ and $x$ with $p$ entries, $A(Bx) = (AB)x$; this is the [[composition rule|MH8YBQPZ7H]], and it leads to [[associativity|073E4XC016]].

### Watch out

The product needs the number of columns of $A$ to equal the number of entries of $x$, and then $Ax$ has as many entries as $A$ has rows.
So a [[2 × 2 matrix times a vector with 3 entries|VZN1T7QCWE]] is not defined.
Writing $xA$ for a column $x$ also fails, since the sizes $n \times 1$ and $m \times n$ do not fit unless $m = 1$.
The entrywise product of a column of $A$ with $x$ is a different thing and is not $Ax$.

### Try it

Compute $\begin{pmatrix} 2 & 0 & 1 \\ -1 & 3 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$.
The rows give $2 + 0 + 2 = 4$ and $-1 + 3 + 2 = 4$, so the answer is $(4, 4)^{\mathsf{T}}$.

Which $x$ gives $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} x = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$?
The right side is the second column, so $x = e_2 = (0, 1)^{\mathsf{T}}$ works.

## Explanations

### L1 human

To multiply a matrix by a vector, take each row of the matrix in turn.
Multiply its entries by the entries of the vector, position by position, and add the results.
Each row gives one entry of the answer.
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 7 \end{pmatrix}$.

### L2 human

The column view is often more useful: $Ax$ mixes the columns of $A$, and $x$ gives the amounts.
So the system $Ax = b$ asks whether $b$ is a mix of the columns of $A$, and the set of all such $b$ is the [[column space|03AJKXH1AV]] of $A$.
With $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, every $Ax = (x_1 + 2x_2)(1, 2)^{\mathsf{T}}$ lies on one line, so $Ax = (1, 0)^{\mathsf{T}}$ has no solution.
The trap is to use the rows of $A$ as the vectors being mixed, which gives the product with $A^{\mathsf{T}}$ instead.

### L3 human

The matrix $A \in M_{m \times n}(R)$ defines the $R$-linear map $R^n \to R^m$, $x \mapsto Ax$, on column vectors.
Every linear map $f \colon F^n \to F^m$ over a field arises in this way from exactly one matrix, namely the matrix with columns $f(e_1), \dots, f(e_n)$.
For a noncommutative ring $R$, the map $x \mapsto Ax$ is linear for the right module structure on columns, since $A(xc) = (Ax)c$.
