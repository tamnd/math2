---
tag: 00SPJSDT3Z
kind: concept
name: Gram matrix
msc: ["15A63", "15B57"]
topics: [1D4JTZ9VS3]
audience: ug1
specializes: [0JXZKX526R]
uses: [0NB0AWGJBW, 0EVHJFTG9Z, 0MFJJV97RJ]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Gram determinant
  - book: isbn:9783031410253
    locator: Chapter 6
same_as:
  wikidata: Q1409400
  wikipedia: Gram matrix
---

## Summary

Let $V$ be an inner product space over $\mathbb{R}$ or $\mathbb{C}$, and let $v_1, \dots, v_k \in V$.
The Gram matrix of $v_1, \dots, v_k$ is the $k \times k$ matrix $G$ with the entries $G_{ij} = \ip{v_i}{v_j}$.
The [[formal definition|0HX8HZ1WTQ]] states this.
The Gram matrix holds all the lengths and all the angles of the family, and nothing else.
It matters because it detects [[linear independence|0EVHJFTG9Z]], and its determinant is the squared volume that the vectors span.

## Motivation

Many questions about a finite family of vectors use only their inner products.
Examples are the lengths $\norm{v_i}$ and the angles between the vectors.
Other examples are the distance from $v_k$ to the span of the others, and the volume of the parallelepiped that the vectors span.
The Gram matrix collects these numbers in one square matrix.
Then matrix tools, like the determinant and the rank, answer the questions.
For column vectors in $\mathbb{R}^n$, the Gram matrix is $A^T A$, the matrix of the normal equations of least squares.

## Notation

- We write $G = G(v_1, \dots, v_k)$, and $\det G(v_1, \dots, v_k)$ for the Gram determinant.
- For the dot product on $\mathbb{R}^n$, with $A$ the $n \times k$ matrix with the columns $v_j$, we have $G = A^T A$.
- For the standard inner product on $\mathbb{C}^n$, we have $G_{ij} = v_j^* v_i$, so $G = A^T \overline{A}$. This is the transpose of $A^* A$.
- In Mathlib and in physics, the inner product is linear in the second slot. Then the matrix of $\ip{v_i}{v_j}$ is $A^* A$, which is the transpose of our $G$.

## Remarks

### Examples

- The Gram matrix of an [[orthonormal family|0RW9TNNT87]] is the identity matrix $I_k$. The Gram matrix of an orthogonal family is diagonal, with the entries $\norm{v_i}^2$.
- In $\mathbb{R}^3$, the vectors $(1, 1, 0)$ and $(1, 0, 1)$ have the [[Gram matrix with determinant 3|~d04ddcaf]]. The parallelogram that they span has area $\sqrt{3}$.
- For $1, x, x^2$ with $\ip{p}{q} = \int_0^1 pq$, the Gram matrix is the [[Hilbert matrix|~8b34fb11]] $H_3$, with the entries $\frac{1}{i + j - 1}$.
- For two vectors, $\det G(x, y) = \norm{x}^2\norm{y}^2 - |\ip{x}{y}|^2$. This is $\geq 0$ by the [[Cauchy-Schwarz inequality|0RFWW56Y22]].

### Non-examples

- The [[symmetric matrix with entries 1, 2, 2, 1|~a766ff9d]] is not a Gram matrix, since its determinant is $-3 < 0$.
- The matrix $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ is not a Gram matrix, since $G_{21}$ must be $\overline{G_{12}} = -i$.
- A matrix of values $\beta(v_i, v_j)$ for the [[Minkowski form|TFGECQ5C32]] $\beta(x, y) = x_1 y_1 - x_2 y_2$ is not a Gram matrix in general. For $(0, 1)$ alone it is $(-1)$, and a Gram matrix has $G_{11} = \norm{v_1}^2 \geq 0$.

### Basic properties

- $G$ is [[Hermitian|0P17NGQQMQ]]: $G_{ji} = \ip{v_j}{v_i} = \overline{\ip{v_i}{v_j}} = \overline{G_{ij}}$. Over $\mathbb{R}$, $G$ is symmetric.
- $G$ is [[positive semidefinite|01MMVW8CKC]]: for $c \in \mathbb{K}^k$, $\sum_{i,j} c_i \overline{c_j}\, G_{ij} = \norm{\sum_i c_i v_i}^2 \geq 0$.
- $G$ is invertible if and only if $v_1, \dots, v_k$ are linearly independent, by the [[Gram invertibility theorem|~271d272f]]. The rank of $G$ is the dimension of the span.
- For an independent family, $\det G = \norm{u_1}^2 \cdots \norm{u_k}^2$, with $u_j$ the Gram-Schmidt output. This is the [[squared volume theorem|~6efb00d4]].
- Two families have the same Gram matrix if and only if a linear isometry between their spans maps one family to the other.

### History

The Gram matrix is named after Jørgen Pedersen Gram, according to the Wikipedia article.
The same Gram also gave his name to the [[Gram-Schmidt process|0VT6P0GNQR]].

### Common errors

- Over $\mathbb{C}$, students write $G = A^T A$ without conjugates. For $v_1 = (1, i)$ this gives $G_{11} = 1 + i^2 = 0$, but $\norm{v_1}^2 = 2$.
- Students think that a matrix with a positive determinant is a Gram matrix. The matrix $-I_2$ has determinant $1$, but its diagonal entries are negative.
- Students mix the conventions. With linearity in the second slot, the matrix of $\ip{v_i}{v_j}$ is the transpose of ours. For real vectors the two agree.

## Explanations

### L1 human

Make a table of all inner products of a list of vectors.
The entry in row $i$ and column $j$ is the inner product of vector $i$ with vector $j$.
The diagonal holds the squared lengths, and the other entries hold the angles.
For $(1, 0)$ and $(1, 1)$ in the plane, the table is $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
Its determinant is $1$, the squared area of the parallelogram that the two vectors span.

### L2 human

Worked example: test the vectors $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 9)$ of $\mathbb{R}^3$ for independence.

1. The squared lengths are $14$, $77$ and $194$.
2. The dot products are $(1, 2, 3) \cdot (4, 5, 6) = 32$, $(1, 2, 3) \cdot (7, 8, 9) = 50$ and $(4, 5, 6) \cdot (7, 8, 9) = 122$.
3. So $G = \begin{pmatrix} 14 & 32 & 50 \\ 32 & 77 & 122 \\ 50 & 122 & 194 \end{pmatrix}$.
4. Row 1 minus twice row 2 plus row 3 is $(14 - 64 + 50, 32 - 154 + 122, 50 - 244 + 194) = (0, 0, 0)$.
5. So $\det G = 0$, and the vectors are dependent. In fact, $v_1 - 2v_2 + v_3 = 0$.

The typical use is to test independence, or to compute a volume, when only inner products are known.
A trap: the Gram matrix of $k$ vectors is $k \times k$, even when the vectors live in a space of larger dimension.

### L3 human

The Gram matrix is the matrix of the inner product, restricted to the span, in the spanning family.
Each positive semidefinite matrix is a Gram matrix, so Gram matrices are exactly the positive semidefinite matrices.
In statistics, the covariance matrix of random variables of mean zero is a Gram matrix.
In machine learning, a kernel matrix is a Gram matrix in a feature space.
The Gram determinant gives the volume of a parallelepiped of $k$ vectors in $\mathbb{R}^n$ for $k < n$, where the ordinary determinant is not defined.
By the [[Cauchy-Binet formula|08WE2W7DYS]], $\det A^T A$ is the sum of the squares of the $k \times k$ minors of $A$.
