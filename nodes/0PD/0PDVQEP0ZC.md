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

The product of an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ and a column vector $x$ with $n$ entries is the column vector $Ax$ with $m$ entries.
Its entry $i$ is $(Ax)_i = a_{i1} x_1 + \dots + a_{in} x_n$, the [[dot product|0S52TNNTH9]] of row $i$ of $A$ with $x$.
Equivalently, $Ax = x_1 a_1 + \dots + x_n a_n$ is the [[linear combination|0V8F3E48E6]] of the columns $a_1, \dots, a_n$ of $A$ with the weights $x_j$.
The [[formal definition|0CCQV3884B]] uses the first form.
The product turns a [[system of linear equations|0GT4WWGWH2]] into one equation $Ax = b$, and a matrix into a [[linear map|094V2VBJXJ]].

## Motivation

The system $a_{11}x_1 + \dots + a_{1n}x_n = b_1, \ \dots, \ a_{m1}x_1 + \dots + a_{mn}x_n = b_m$ has $m$ left sides.
If we define $Ax$ as the column of these left sides, the whole system is $Ax = b$.
The column view answers a second question: which vectors $b$ are combinations of the columns of $A$?
These are exactly the vectors $b$ for which $Ax = b$ has a solution.
So one product connects equations with combinations of vectors.

## Notation

- The vector $x$ is a column, an $n \times 1$ matrix, and $Ax$ is the matrix product of an $m \times n$ and an $n \times 1$ matrix.
- A row vector $y^{\mathsf{T}}$ with $m$ entries gives the product $y^{\mathsf{T}} A$ on the left, a row with $n$ entries.
- In Mathlib, `A.mulVec x` or `A *ᵥ x` is the product with a function `x : n → α`, and `x ᵥ* A` is the product on the left.

## Remarks

### Examples

- The [[product of a 2 × 3 matrix with a vector|~32cc287b]] computed by rows and by columns.
- The [[system x + 2y = 5, 3x − y = 1|~39155860]] written as $Ax = b$.
- $Ae_j$ is column $j$ of $A$, for the [[standard basis vector|0V7ZD6P7RK]] $e_j$, by [[this statement|PFEYWQJDK1]].
- $I_n x = x$ for the [[identity matrix|06DW9BAWB1]].

### Non-examples

- A [[2 × 2 matrix times a vector with 3 entries|~1daa7e3f]] is not defined.
- The entrywise product of a column of $A$ with $x$ is not $Ax$.

### Basic properties

- $A(x + y) = Ax + Ay$ and $A(cx) = c(Ax)$; this is the [[linearity of the product|ZE36VEAY80]].
- $(A + B)x = Ax + Bx$ and $(cA)x = c(Ax)$, entry by entry.
- $A(Bx) = (AB)x$ for an $n \times p$ matrix $B$; this is the [[composition rule|MH8YBQPZ7H]], and it leads to [[associativity|073E4XC016]].
- $Ax = 0$ for all $x$ only when $A = 0$, because $Ae_j$ is column $j$.

### Common errors

- Multiplying columns of $A$ by rows of $x$, or using the rows of $A$ as the weights.
- Writing $xA$ for a column $x$: the sizes $n \times 1$ and $m \times n$ do not fit unless $m = 1$.
- Forgetting that $Ax$ has as many entries as $A$ has rows, not columns.

## Explanations

### L1 human

To multiply a matrix by a vector, take each row of the matrix in turn.
Multiply its entries by the entries of the vector, position by position, and add the results.
Each row gives one entry of the answer.

### L2 human

The column view is often more useful: $Ax$ mixes the columns of $A$, and $x$ gives the amounts.
So the system $Ax = b$ asks whether $b$ is a mix of the columns of $A$.
The set of all such $b$ is the [[column space|03AJKXH1AV]] of $A$.

### L3 human

The matrix $A \in M_{m \times n}(R)$ defines the $R$-linear map $R^n \to R^m$, $x \mapsto Ax$, on column vectors.
Every linear map $F^n \to F^m$ over a field arises in this way from exactly one matrix, namely the matrix with columns $f(e_1), \dots, f(e_n)$.
For a noncommutative ring $R$, the map $x \mapsto Ax$ is linear for the right module structure on columns, since $A(xc) = (Ax)c$.
