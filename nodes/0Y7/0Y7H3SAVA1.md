---
tag: 0Y7H3SAVA1
kind: concept
name: Matrix addition
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
specializes: [0M418FE7BB]
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_addition
    locator: Entrywise sum
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Basic operations
  - book: isbn:9780321982384
    locator: Section 2.1
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Three, Section IV
same_as:
  wikidata: Q2264115
  wikipedia: Matrix addition
inventory: [NAYXFHVVCR]
---

## Summary

Matrix addition adds two [[matrices|0VD9ZSWWJG]] of the same size entry by entry: $(A + B)_{ij} = a_{ij} + b_{ij}$.
[[Scalar multiplication|09V6DDACXR]] multiplies every entry by one number: $(cA)_{ij} = c\, a_{ij}$.
The [[formal definition of addition|0BVXADM10P]] and the [[formal definition of scalar multiplication|0K28YXMS7Q]] state the rules.
With these two operations, the $m \times n$ matrices over a field form a [[vector space|0RE6X3BGPN]] of dimension $mn$.
This page treats both operations, because they are almost always used together.

## Motivation

If $A$ and $B$ are the matrices of two linear maps $f, g : F^n \to F^m$, the map $x \mapsto f(x) + g(x)$ has the matrix $A + B$.
If $c$ is a scalar, the map $x \mapsto c f(x)$ has the matrix $cA$.
So the entrywise rules are the rules that match the addition and the scaling of linear maps.
For tables of data, such as the sales of two weeks, the entrywise sum is the natural total.

## Notation

- The difference is $A - B = A + (-1)B$, with entries $a_{ij} - b_{ij}$.
- A scalar multiple is written $cA$; the notation $Ac$ means the same over a commutative ring.
- Over a noncommutative ring $R$, $cA$ and $Ac$ can differ, so books state on which side the scalar acts.
- In Mathlib, `A + B` and `c • A` are the pointwise operations on functions `m → n → α`.

## Remarks

### Examples

- The [[combination 2A − 3B|R3SH1T0KYW]] of two $2 \times 2$ matrices, computed entry by entry.
- The [[space of matrices|0RE6X3BGPN]] $M_{m \times n}(F)$ is a vector space with these operations.
- $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = I_2$.

### Non-examples

- [[Matrices of different sizes cannot be added|VRD3P83FH7]]: a $2 \times 2$ matrix plus a $2 \times 3$ matrix is not defined.
- Adding a number to a matrix, as in $A + 1$, is not matrix addition. Software often reads it as adding $1$ to each entry, and algebra books read it as $A + I$.

### Basic properties

For matrices $A, B, C$ of one size and scalars $c, d$ in a field:

- $A + B = B + A$ and $(A + B) + C = A + (B + C)$, because these laws hold for each entry.
- $A + 0 = A$ for the [[zero matrix|0ZTKJJDGR7]], and $A + (-A) = 0$.
- $c(A + B) = cA + cB$, $(c + d)A = cA + dA$, $c(dA) = (cd)A$ and $1A = A$.
- Every $m \times n$ matrix is the combination $\sum_{i,j} a_{ij} E_{ij}$ of the [[matrix units|A4HTT7JFD1]].
- Addition and scalar multiplication are compatible with the product: $A(B + C) = AB + AC$ by the [[distributive law|0RXD6EZYBK]], and $A(cB) = c(AB)$ over a commutative ring.

### Common errors

- Adding matrices of different sizes after padding them with zeros.
- Multiplying only one row or one column by $c$ when computing $cA$; this is a row operation, not a scalar multiple.
- Assuming $\det(A + B) = \det A + \det B$ or $\det(cA) = c \det A$; in fact $\det(cA) = c^n \det A$ for an $n \times n$ matrix.

## Explanations

### L1 human

To add two matrices of the same size, add the numbers in the same positions.
To multiply a matrix by a number, multiply every entry by that number.
For example, $3 \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -3 \\ 0 & 6 \end{pmatrix}$.

### L2 human

The two operations make the matrices of one size into a vector space, with the entries as coordinates.
The matrix units $E_{ij}$ form its standard basis, so $\dim M_{m \times n}(F) = mn$.
The size must agree, because a matrix is a function on a fixed set of positions.

### L3 human

The vector space $M_{m \times n}(F)$ is isomorphic to the [[space of linear maps|0X9MBPP2Z3]] $\operatorname{Hom}(F^n, F^m)$, and the isomorphism respects both operations.
Over a ring $R$, $M_{m \times n}(R)$ is a free left $R$-module with basis $(E_{ij})$, and also a right module.
These module structures belong to [[ring theory|0B1261B5ED]], and this area does not treat them further.
