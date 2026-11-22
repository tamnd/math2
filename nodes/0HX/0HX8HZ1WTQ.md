---
tag: 0HX8HZ1WTQ
kind: definition
name: Gram matrix
msc: ["15A63", "15B57"]
topics: [1D4JTZ9VS3]
audience: ug1
defines: 00SPJSDT3Z
uses: [0VGSYBWHV2, 01EK923SKP, 0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Definition

The Gram matrix of finitely many vectors is the square matrix of their pairwise inner products.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with an [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ that is linear in the first slot.
Let $k \ge 1$ and let $v_1, \dots, v_k \in V$.
The *Gram matrix* of $v_1, \dots, v_k$ is the $k \times k$ [[matrix|0JXZKX526R]] $G = G(v_1, \dots, v_k)$ over $\mathbb{K}$ with the entries
$$G_{ij} = \ip{v_i}{v_j} \qquad (1 \le i, j \le k).$$
The *Gram determinant* of $v_1, \dots, v_k$ is $\det G(v_1, \dots, v_k)$.

## Notation

For column vectors in $\mathbb{R}^n$ with the dot product, $G = A^{\mathsf{T}} A$, where $A$ is the $n \times k$ matrix with the columns $v_1, \dots, v_k$.
For column vectors in $\mathbb{C}^n$ with the standard inner product, $G_{ij} = v_j^* v_i$, so $G = A^{\mathsf{T}} \overline{A}$.
With an inner product that is linear in the second slot, as in Mathlib and in physics, the same formula $\ip{v_i}{v_j}$ gives the transpose of our matrix, which is $A^* A$ on $\mathbb{C}^n$.

## Remarks

The definition asks for a list, not a set, so a vector may appear twice and the order counts.
A repeated vector gives two equal rows, so the Gram determinant is $0$, as it should be for a dependent list.
Reordering the list replaces $G$ by $P^{\mathsf{T}} G P$ for a permutation matrix $P$, and the determinant does not change.

The inner product must be positive definite for the matrix to carry geometry.
Then $G_{ii} = \norm{v_i}^2 \ge 0$, the matrix is Hermitian and [[positive semidefinite|01MMVW8CKC]], it is invertible exactly when the list is [[linearly independent|EM1QNRGWQ8]], and its determinant is the squared [[volume of the parallelepiped|FWA0AKJA2R]] that the list spans.
With the Minkowski form $x_1 y_1 - x_2 y_2$ in place of an inner product, the same recipe applied to $(0, 1)$ gives the table $(-1)$, which no list of vectors has as a Gram matrix.

A small example: for $v_1 = (1, 0)$ and $v_2 = (3, 4)$ in $\mathbb{R}^2$, the entries are $1$, $3$, $3$ and $25$, so $\det G = 25 - 9 = 16$.
The parallelogram with sides $v_1$ and $v_2$ has base $1$ and height $4$, and $16 = 4^2$.
The concept page on the [[Gram matrix|00SPJSDT3Z]] gives more examples and the uses.

## Explanations

### L1 human

The Gram matrix is a table of all inner products of a list of vectors.
The diagonal holds the squared lengths, and the other entries record the angles.
Two lists with the same table have the same shape: one list can be turned into the other by a rigid motion that fixes the origin.

### L2 human

Over $\mathbb{C}$ the table is not symmetric.
For $v_1 = (1, i)$ and $v_2 = (0, 1)$ in $\mathbb{C}^2$, the entry $G_{12} = \ip{v_1}{v_2} = 1 \cdot \overline{0} + i \cdot \overline{1} = i$, but $G_{21} = \overline{G_{12}} = -i$.
The diagonal entries are $G_{11} = 1 + \abs{i}^2 = 2$ and $G_{22} = 1$, so
$$G = \begin{pmatrix} 2 & i \\ -i & 1 \end{pmatrix}, \qquad \det G = 2 - (i)(-i) = 2 - 1 = 1.$$
Watch out: if you forget the conjugate, you get $G_{11} = 1 + i^2 = 0$, which cannot be a squared length.
