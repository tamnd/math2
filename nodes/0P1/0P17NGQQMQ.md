---
tag: 0P17NGQQMQ
kind: concept
name: Hermitian matrix
aliases: [self-adjoint-matrix]
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0MR0BYF0K2]
uses: [0DXKE10PHF, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Skew-Hermitian_matrix
    locator: lead section
same_as:
  wikidata: Q652941
  wikipedia: Hermitian matrix
inventory: [C1N93YZJGX]
---

## Summary

A Hermitian matrix is a complex square matrix that does not change when you take its [[conjugate transpose|0DXKE10PHF]].
Among complex matrices, Hermitian matrices play the part that real numbers play among complex numbers.
An $n \times n$ complex matrix $A = (a_{ij})$ is *Hermitian* when
$$A^* = A, \qquad \text{that is,} \qquad a_{ij} = \overline{a_{ji}} \text{ for all } i, j,$$
and it is *skew-Hermitian* when $A^* = -A$, that is, $a_{ij} = -\overline{a_{ji}}$ for all $i, j$.
The [[formal definition|0EKZCX4K3P]] states both conditions.
Every complex square matrix splits in exactly one way as $H + iK$ with $H$ and $K$ Hermitian, by the [[Cartesian decomposition|E2MNC3W2DM]].

## Motivation

A complex number $z$ is real exactly when $\overline{z} = z$, and purely imaginary exactly when $\overline{z} = -z$.
The conjugate transpose is the matrix version of the bar, so the equations $A^* = A$ and $A^* = -A$ are the matrix versions of "real" and "purely imaginary".
The analogy goes further than the names.
A Hermitian matrix has only real eigenvalues, by [[the theorem on self-adjoint operators|0C4NT4GT3X]], and the number $x^* A x$ is real for every vector $x$.

These facts are why Hermitian matrices appear wherever a complex model must produce real measurements.
In quantum mechanics, a quantity that can be measured is represented by a Hermitian matrix or operator, and the possible results are its eigenvalues.
In signal processing, the covariance matrix of a complex signal is Hermitian.
Over the real numbers, the Hermitian matrices are the [[symmetric matrices|0VR671PHE5]], so every fact on this page also covers that case.
The [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], in a later sub-area, shows that every Hermitian matrix is diagonal in a suitable orthonormal basis.

## Notation

There is no special symbol: one writes $A^* = A$, or $A^{\mathsf{H}} = A$, or $A^\dagger = A$, following the notation for the conjugate transpose.
Another name is *self-adjoint matrix*, and skew-Hermitian matrices are also called *anti-Hermitian*.
In Mathlib, `Matrix.IsHermitian A` means `Aᴴ = A`.
Mathlib has no separate name for skew-Hermitian matrices, and one writes the condition `Aᴴ = -A`.

## Remarks

### Reading the condition entry by entry

The condition $a_{ij} = \overline{a_{ji}}$ pairs each entry with its mirror image across the main diagonal.
On the diagonal, $i = j$ gives $a_{ii} = \overline{a_{ii}}$, so every diagonal entry is real.
Off the diagonal, each entry is the conjugate of its mirror entry.
For example,
$$A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$$
has real diagonal $2, 3$, and the entries $1 - i$ and $1 + i$ are conjugates, so $A$ is Hermitian.
[[The eigenvalue example|GGFA8S4NZ2]] shows that its eigenvalues are $1$ and $4$, both real.

For a skew-Hermitian matrix, $a_{ii} = -\overline{a_{ii}}$ says that each diagonal entry is purely imaginary.
The matrix $\begin{pmatrix} i & 1 \\ -1 & 0 \end{pmatrix}$ is skew-Hermitian: its conjugate transpose is $\begin{pmatrix} -i & -1 \\ 1 & 0 \end{pmatrix}$, which is minus the matrix.

### What it is not

A complex symmetric matrix need not be Hermitian.
[[The matrix with rows (1, i) and (i, 1)|DAZBNZXZK7]] equals its transpose, but its conjugate transpose has $-i$ off the diagonal, and its eigenvalues $1 \pm i$ are not real.
The scalar matrix $iI$ is not Hermitian either, since $(iI)^* = -iI$; it is skew-Hermitian.
A matrix that is not square is never Hermitian, because $A^*$ has the transposed size.

### The rules you can use

Let $A$ and $B$ be Hermitian of the same size.
Then $A + B$ is Hermitian, and so is $cA$ for every real $c$, because $(cA)^* = \overline{c} A^* = cA$.
For non-real $c$ this fails, so the Hermitian matrices form a real vector space of dimension $n^2$, not a complex one.
Multiplying by $i$ moves between the two kinds: $A$ is Hermitian if and only if $iA$ is skew-Hermitian.
The product $AB$ is Hermitian exactly when $AB = BA$, since $(AB)^* = B^* A^* = BA$; the proof is the one for [[symmetric matrices|YX9Z3E9SGN]].
For every complex matrix $C$, of any size, the products $C^* C$ and $C C^*$ are Hermitian, because $(C^* C)^* = C^* (C^*)^* = C^* C$.
Finally, $x^* A x$ is real, because it is a $1 \times 1$ matrix equal to its own conjugate:
$$\overline{x^* A x} = (x^* A x)^* = x^* A^* x = x^* A x.$$

### The Cartesian decomposition

Every complex number is $z = a + ib$ with $a = (z + \overline{z})/2$ and $b = (z - \overline{z})/(2i)$.
The same formulas with $A^*$ in place of $\overline{z}$ give
$$H = \tfrac12 (A + A^*), \qquad K = \tfrac{1}{2i} (A - A^*),$$
two Hermitian matrices with $A = H + iK$.
[[The 2 × 2 example|NQBXQ87CXZ]] carries this out for $\begin{pmatrix} 1 & 2 \\ 0 & i \end{pmatrix}$.
The matrix $A$ is Hermitian when $K = 0$, skew-Hermitian when $H = 0$, and [[normal|0MR0BYF0K2]] exactly when $HK = KH$.

### Watch out

The usual error is to test only the transpose.
The matrix $\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ equals its transpose, but its conjugate transpose is $\begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}$, so it is skew-Hermitian, not Hermitian.
Always conjugate as well as transpose.
A second error is to treat the Hermitian matrices as a complex subspace: $I$ is Hermitian, and $iI$ is not.

### History

The name honors the French mathematician Charles Hermite, who studied forms of this type.

### Try it

First, for which real $a$ and complex $b$ is $\begin{pmatrix} a & b \\ 2 + 3i & 1 \end{pmatrix}$ Hermitian?
The diagonal $a$ and $1$ is already real, and you need $b = \overline{2 + 3i} = 2 - 3i$, so every real $a$ works with $b = 2 - 3i$.

Second, show that the diagonal of $C^* C$ is real and nonnegative for $C = \begin{pmatrix} 1 & i \\ 2 & 0 \end{pmatrix}$.
Entry $(j, j)$ of $C^* C$ is $\sum_k |c_{kj}|^2$, which gives $1 + 4 = 5$ and $1 + 0 = 1$.

## Explanations

### L1 human

A Hermitian matrix is the complex version of a symmetric matrix.
Fold the matrix along its main diagonal: each entry must land on its complex conjugate.
So $1 + i$ in one corner must meet $1 - i$ in the other corner.
A number on the fold must meet itself, and a number equal to its own conjugate is real, so the diagonal is real.

### L2 human

Here is why the eigenvalues of a Hermitian matrix $A$ are real.
Suppose $Ax = \lambda x$ with $x \neq 0$.
Multiply on the left by $x^*$:
$$x^* A x = \lambda\, x^* x.$$
The left side is real by the rule above, and $x^* x = |x_1|^2 + \dots + |x_n|^2$ is a positive real number.
So $\lambda = (x^* A x)/(x^* x)$ is real.
For $A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$ and the eigenvector $x = (1 - i, 2)^{\mathsf{T}}$, we get $x^* x = 2 + 4 = 6$ and $x^* A x = 24$, so $\lambda = 4$.
This argument is the typical use of the condition $A^* = A$: move $A$ across a product without changing it.

### L3 human

The equation $A^* = A$ says that the map $x \mapsto Ax$ is self-adjoint for the standard inner product on $\mathbb{C}^n$, $\langle Ax, y \rangle = \langle x, Ay \rangle$.
In the sub-area on [[operators on inner product spaces|3YM9EK6VMB]] this becomes the definition of a self-adjoint operator, and the spectral theorem diagonalizes it with a [[unitary matrix|0AR68JTMDT]].
The Cartesian decomposition identifies $M_n(\mathbb{C})$ with the complexification of the real space of Hermitian matrices.
The skew-Hermitian matrices form the Lie algebra $\mathfrak{u}(n)$ of the unitary group, and $e^{tK}$ is unitary for every skew-Hermitian $K$.
In any $*$-algebra, such as the bounded operators on a Hilbert space, the elements with $a^* = a$ are called self-adjoint, and they carry the same theory.
