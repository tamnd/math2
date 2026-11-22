---
tag: 09V6DDACXR
kind: concept
name: Scalar multiplication of matrices
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Scalar_multiplication
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Basic operations
---

## Summary

To multiply a [[matrix|0VD9ZSWWJG]] by a number, multiply every entry by that number.
The scalar multiple $cA$ of a matrix $A = (a_{ij})$ by a scalar $c$ is the matrix of the same size with entries $c\, a_{ij}$.
For example,
$$3 \begin{pmatrix} 1 & -2 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 3 & -6 \\ 0 & 12 \end{pmatrix}.$$
The [[formal definition|0K28YXMS7Q]] states the rule, and the page on [[matrix addition|0Y7H3SAVA1]] treats it together with addition.

## Motivation

A scalar multiple changes the size of every entry by the same factor, which is what a change of units does.
If a table lists prices in dollars and one dollar is $100$ cents, the same table in cents is $100A$.

For a linear map the scalar multiple has a geometric meaning.
If $f(x) = Ax$, then $(cA)x = c(Ax)$, so $cA$ is the matrix of the map that first applies $f$ and then stretches the result by $c$.
For instance, $2 I_2$ doubles every vector in the plane, and $-I_2$ turns every vector to point the opposite way.

## Notation

Books write $cA$, $c \cdot A$ or $c\,A$, with the scalar on the left.
Over a commutative ring $Ac = cA$, and the order does not matter.
In Mathlib the scalar multiple is `c • A`, and its entry `(c • A) i j` is `c * A i j`.

## Remarks

### Scaling is multiplying by a scalar matrix

For an $n \times n$ matrix $A$, the scalar multiple equals a matrix product with the [[scalar matrix|067NKSBEWT]] $cI_n$:
$$cA = (cI_n) A = A (cI_n).$$
For example,
$$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & 3 \\ 5 & 7 \end{pmatrix} = \begin{pmatrix} 2 & 6 \\ 10 & 14 \end{pmatrix} = 2 \begin{pmatrix} 1 & 3 \\ 5 & 7 \end{pmatrix}.$$
So the scalar multiple of a square matrix is a special matrix product.
For an $m \times n$ matrix the same holds with $cI_m$ on the left and $cI_n$ on the right.

### Scaling and the product

A scalar can move through a matrix product: $c(AB) = (cA)B = A(cB)$ over a commutative ring.
So in a product of several factors the scalars can be collected in front, as in $(2A)(3B) = 6AB$.

### Watch out

The determinant of a scalar multiple is not the scalar times the determinant.
For an $n \times n$ matrix, every one of the $n$ rows is multiplied by $c$, so
$$\det(cA) = c^n \det A.$$
Check with $A = I_2$ and $c = 3$: $\det(3 I_2) = 3 \cdot 3 - 0 = 9 = 3^2$.

A scalar multiple also differs from a row operation.
Multiplying only the first row of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ by $2$ gives $\begin{pmatrix} 2 & 4 \\ 3 & 4 \end{pmatrix}$, an [[elementary row operation|04XWH28452]], while $2A$ doubles both rows.

### Left and right multiples

Over a noncommutative ring the side matters.
In the quaternions $ij = k$ and $ji = -k$, so the $1 \times 1$ matrix $(j)$ has $i(j) = (k)$ but $(j)i = (-k)$.
For this reason the matrices over a ring $R$ form a left $R$-module under $cA$ and a right $R$-module under $Ac$, and the two structures need not agree.

### Try it

Find $c$ with $c \begin{pmatrix} 2 & -4 \end{pmatrix} = \begin{pmatrix} -3 & 6 \end{pmatrix}$.
The first entries give $2c = -3$, so $c = -\tfrac{3}{2}$, and then $-\tfrac{3}{2} \cdot (-4) = 6$ matches the second entry.

Compute $\det(2A)$ for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
Here $\det A = 4 - 6 = -2$, so $\det(2A) = 2^2 \cdot (-2) = -8$, and directly $2 \cdot 8 - 4 \cdot 6 = -8$.

## Explanations

### L1 human

To multiply a matrix by a number, multiply every entry by that number.
For example, $2 \begin{pmatrix} 1 & -3 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 2 & -6 \\ 0 & 8 \end{pmatrix}$.
If a table lists the prices of some items, doubling every price doubles the whole table.

### L2 human

The scalar multiple $cA$ is the matrix of the linear map $x \mapsto c\,Ax$, so it stretches the output of $x \mapsto Ax$ by the factor $c$.
For a square matrix it is the product $(cI)A$ with a scalar matrix, and for that reason scalars commute with every square matrix over a field.
The typical use is in a linear combination such as $2A - 3B$, where scaling is done first and adding second.
The trap is to scale one row only, which is a row operation and not $cA$.

### L3 human

Scalar multiplication makes $M_{m \times n}(R)$ a module over $R$, and over a field a [[vector space|0RE6X3BGPN]] of dimension $mn$.
For square matrices with $n \ge 1$ the map $c \mapsto cI_n$ embeds $R$ into the center of the [[matrix ring|AB2MD5CD13]] $M_n(R)$ when $R$ is commutative, and this makes $M_n(R)$ an $R$-algebra.
