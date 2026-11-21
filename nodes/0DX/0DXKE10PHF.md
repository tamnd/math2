---
tag: 0DXKE10PHF
kind: concept
name: Conjugate transpose
aliases: [hermitian-transpose]
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
uses: [09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
same_as:
  wikidata: Q2051983
  wikipedia: Conjugate transpose
---

## Summary

The conjugate transpose is the version of the [[transpose|09DXWYRD43]] that works for complex matrices.
You flip the matrix over its main diagonal and replace each entry by its [[complex conjugate|0FTH2E9TAS]], and the result measures lengths and angles in $\mathbb{C}^n$ the way the transpose does in $\mathbb{R}^n$.
For a complex $m \times n$ matrix $A = (a_{ij})$, the conjugate transpose is the $n \times m$ matrix $A^*$ with
$$(A^*)_{ij} = \overline{a_{ji}}.$$
The [[formal definition|0EX045E2BP]] states this rule.
Equivalently, $A^* = \overline{A}^{\mathsf{T}} = \overline{A^{\mathsf{T}}}$, since conjugating the entries and moving them can be done in either order.

## Motivation

Over the real numbers, the length of a column $x$ comes from $x^{\mathsf{T}} x = x_1^2 + \dots + x_n^2$.
Over the complex numbers this formula breaks.
For $x = (1, i)$ it gives $1 + i^2 = 0$, although $x$ is not the zero vector.
The repair is to conjugate one factor: the squared size of a complex number $z$ is $\overline{z} z = |z|^2$, so the squared length of $x$ is $\overline{x_1} x_1 + \dots + \overline{x_n} x_n = x^* x$.

Once lengths use conjugates, every formula that moves a matrix across a product must use them too.
With the standard [[inner product|0NB0AWGJBW]] $\langle x, y \rangle = y^* x$ on $\mathbb{C}^n$, one has $\langle Ax, y \rangle = \langle x, A^* y \rangle$, so $A^*$ is the matrix of the adjoint map.
This is why quantum mechanics, signal processing and numerical linear algebra over $\mathbb{C}$ use $A^*$ wherever real linear algebra uses $A^{\mathsf{T}}$.
The next page, on [[Hermitian matrices|0P17NGQQMQ]], studies the matrices with $A^* = A$, and later sub-areas build [[unitary|0AR68JTMDT]] and [[normal|0MR0BYF0K2]] matrices from the same operation.

## Notation

Most mathematics books write $A^*$.
Numerical analysts often write $A^{\mathsf{H}}$ or $A^H$, and physicists write $A^\dagger$, read "A dagger".
Watch out for two clashes: a few books use $A^*$ for the entrywise conjugate $\overline{A}$, and some use it for the adjugate matrix.
In MATLAB, `A'` is the conjugate transpose and `A.'` is the plain transpose.
In Mathlib, `Matrix.conjTranspose A` is written `Aᴴ`, and it is defined over any ring with a `star` operation.

## Remarks

### A first computation

Take
$$A = \begin{pmatrix} 1 & i \\ 0 & 2 \end{pmatrix}.$$
The transpose moves the entry $i$ from position $(1, 2)$ to position $(2, 1)$, and the conjugate turns it into $-i$:
$$A^* = \begin{pmatrix} 1 & 0 \\ -i & 2 \end{pmatrix}.$$
For a column the operation gives a row: if $x = (1, i)^{\mathsf{T}}$, then $x^* = \begin{pmatrix} 1 & -i \end{pmatrix}$ and
$$x^* x = 1 \cdot 1 + (-i) \cdot i = 1 + 1 = 2.$$
That is $|1|^2 + |i|^2$, the squared length of $x$.
[[The vector example|THMQA9AQZK]] works this out for a second vector and for the inner product of two vectors.

### The rules you can use

The conjugate transpose obeys the rules of the transpose, with one change for scalars.
Applying it twice gives back $A$, so $(A^*)^* = A$, and it respects sums, $(A + B)^* = A^* + B^*$.
A scalar comes out conjugated, $(cA)^* = \overline{c}\, A^*$, so the map $A \mapsto A^*$ is conjugate-linear and not linear.
The product rule reverses the order, $(AB)^* = B^* A^*$, with the proof of the [[transpose of a product|09GK5PS824]] plus the identity $\overline{zw} = \overline{z}\, \overline{w}$.
For an [[invertible|0EB9N0S33C]] $A$, taking $*$ of $A A^{-1} = I$ gives $(A^{-1})^* A^* = I$, so $(A^{-1})^* = (A^*)^{-1}$.
The [[trace|0XC1RDBY7A]] and the [[determinant|00KDZRW4C0]] come out conjugated: $\operatorname{tr}(A^*) = \overline{\operatorname{tr} A}$ and $\det(A^*) = \overline{\det A}$.
Finally, $\operatorname{tr}(A^* A) = \sum_{i,j} |a_{ij}|^2$, which is $0$ only for $A = 0$.
[[The 2 × 2 example|NPKE6PDQQ8]] checks the product rule and the scalar rule with numbers.

### Real matrices

When every entry is real, conjugation does nothing, so $A^* = A^{\mathsf{T}}$.
For example, the conjugate transpose of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.
So every fact about $A^*$ contains the matching fact about the transpose of a real matrix.

### What it is not

The plain transpose of a complex matrix is not the conjugate transpose.
[[The isotropic vector example|5AG0M5GR5T]] shows the failure: for $x = (1, i)^{\mathsf{T}}$, the plain transpose gives $x^{\mathsf{T}} x = 0$ although $x \neq 0$.
The entrywise conjugate $\overline{A}$ is not $A^*$ either, unless $A$ is square and symmetric.
For $A$ above, $\overline{A} = \begin{pmatrix} 1 & -i \\ 0 & 2 \end{pmatrix}$, which differs from $A^*$ in positions $(1, 2)$ and $(2, 1)$.

### Watch out

The common slip is to drop the conjugate on a scalar.
With $A$ as above and $c = i$, the matrix $iA = \begin{pmatrix} i & -1 \\ 0 & 2i \end{pmatrix}$ has
$$(iA)^* = \begin{pmatrix} -i & 0 \\ -1 & -2i \end{pmatrix} = -i A^*,$$
not $i A^*$.
A second slip is to use $x^{\mathsf{T}} y$ as an inner product on $\mathbb{C}^n$; the correct form is $y^* x$ or $x^* y$, depending on the book.

### History

The other name, Hermitian transpose, honors Charles Hermite, after whom the [[Hermitian matrices|0P17NGQQMQ]] are named.

### Try it

First, find the conjugate transpose of $\begin{pmatrix} 2 & 1 - i & 3i \end{pmatrix}$.
The answer is the column $(2, 1 + i, -3i)^{\mathsf{T}}$.

Second, compute $x^* x$ for $x = (1 + i, 2)^{\mathsf{T}}$.
You get $(1 - i)(1 + i) + 2 \cdot 2 = 2 + 4 = 6$.

## Explanations

### L1 human

To find the conjugate transpose, write the rows of the matrix as columns, then change the sign of each imaginary part.
For the row $(1, i)$ you get the column with entries $1$ and $-i$.
Multiplying that by the original numbers and adding gives $1 \cdot 1 + (-i) \cdot i = 2$, a positive number, the squared length.
If the matrix has only real numbers, the sign change does nothing, and you get the ordinary transpose.

### L2 human

Here is a typical use: show that $A^* A$ has a real, nonnegative number $x^* A^* A x$ for every vector $x$.
Group the product with the rule $(AB)^* = B^* A^*$:
$$x^* A^* A x = (Ax)^* (Ax).$$
Put $y = Ax$.
Then $(Ax)^*(Ax) = y^* y = |y_1|^2 + \dots + |y_m|^2$, which is real and at least $0$.
For example, with $A = \begin{pmatrix} 1 & i \\ 0 & 2 \end{pmatrix}$ and $x = (1, 1)^{\mathsf{T}}$, we get $y = (1 + i, 2)^{\mathsf{T}}$ and $y^* y = 2 + 4 = 6$.
This one line is how one proves that the matrices $A^* A$ are positive semidefinite, which the Gram matrices and least squares problems of later sub-areas need.

### L3 human

The map $A \mapsto A^*$ is an involution of the ring $M_n(\mathbb{C})$ that reverses products and conjugates scalars, so it makes $M_n(\mathbb{C})$ a $*$-algebra, a [[ring with involution|7W52X4N3NJ]].
With the operator norm, $\|A^* A\| = \|A\|^2$ holds, and $M_n(\mathbb{C})$ becomes the basic example of a [[C*-algebra|M2WFY1D3SZ]].
Abstractly, $A^*$ is the adjoint of the map $x \mapsto Ax$ with respect to the standard inner products, and in an orthonormal basis the matrix of the adjoint of any operator is the conjugate transpose of its matrix.
Mathlib defines `conjTranspose` for any ring with a `star` operation, so the same notation covers matrices over the quaternions.
