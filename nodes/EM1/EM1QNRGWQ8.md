---
tag: EM1QNRGWQ8
kind: statement
role: proposition
name: A Gram matrix is invertible if and only if the family is linearly independent
msc: ["15A63", "15B57"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [00SPJSDT3Z]
uses: [0HX8HZ1WTQ, 0EVHJFTG9Z, 0P17NGQQMQ, 01MMVW8CKC]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Positive-semidefiniteness
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Properties
---

## Statement

The null space of a Gram matrix is the space of linear relations among the vectors, so the matrix is invertible exactly when the vectors are independent.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot, and let $v_1, \dots, v_k \in V$.
Let $G$ be their [[Gram matrix|0HX8HZ1WTQ]], with $G_{ij} = \ip{v_i}{v_j}$.

1. $G$ is [[Hermitian|0P17NGQQMQ]]: $G_{ji} = \overline{G_{ij}}$ for all $i, j$.
2. For every column $c \in \mathbb{K}^k$, $c^* G c = \norm{\sum_{i=1}^k \overline{c_i}\, v_i}^2 \ge 0$, so $G$ is [[positive semidefinite|01MMVW8CKC]].
3. For every $c \in \mathbb{K}^k$, $G c = 0$ if and only if $\sum_{j=1}^k \overline{c_j}\, v_j = 0$.
4. $G$ is invertible if and only if $v_1, \dots, v_k$ are [[linearly independent|0EVHJFTG9Z]].
5. The rank of $G$ is the dimension of the span of $v_1, \dots, v_k$.

The [[proof|X8VXZP1GPN]] reads each entry of $G c$ as one inner product.

## Remarks

### Why each hypothesis is needed

The inner product must be definite, and not only semidefinite, for parts 3 and 4.
The form $\beta(x, y) = x_1 y_1$ on $\mathbb{R}^2$ is symmetric, bilinear and gives $\beta(x, x) \ge 0$, but on the independent pair $(1, 0)$, $(0, 1)$ its table of values is $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, which is singular.

Positivity is needed for part 2.
For the [[Minkowski form|TFGECQ5C32]] $\beta(x, y) = x_1 y_1 - x_2 y_2$ and the single vector $(0, 1)$, the table is $(-1)$, and $c = (1)$ gives $c^{\mathsf{T}} (-1) c = -1 < 0$.

Over $\mathbb{C}$ the conjugates in parts 2 and 3 are part of the statement.
Take $v_1 = (1, 0)$ and $v_2 = (i, 0)$ in $\mathbb{C}^2$, so that $G_{12} = 1 \cdot \overline{i} = -i$ and
$$G = \begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix}, \qquad c = \begin{pmatrix} 1 \\ -i \end{pmatrix}, \qquad G c = \begin{pmatrix} 1 + (-i)(-i) \\ i - i \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.$$
The relation with conjugate coefficients holds, $\overline{c_1}\, v_1 + \overline{c_2}\, v_2 = (1, 0) + i (i, 0) = (0, 0)$, but $c_1 v_1 + c_2 v_2 = (1, 0) - i (i, 0) = (2, 0)$ is not zero.

### What it gives you

The determinant of $G$ is a test for independence that uses only inner products, so it works for polynomials, functions and matrices as well as for columns.
The [[squared volume theorem|FWA0AKJA2R]] adds that $\det G \ge 0$ always, with $\det G > 0$ exactly for independent families.

For a real $n \times k$ matrix $A$, the Gram matrix of the columns is $A^{\mathsf{T}} A$.
So $A^{\mathsf{T}} A$ is invertible if and only if the columns of $A$ are independent, and then the [[normal equations|4D7MRG4D91]] $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$ of least squares have exactly one solution.
For $k = n$ this reads $\det(A^{\mathsf{T}} A) = (\det A)^2 \ne 0$, the usual test for a basis.

A vector in the null space of $G$ also hands you the relation itself, by part 3.
For $v_1 = (1, 2)$ and $v_2 = (2, 4)$ the Gram matrix is $\begin{pmatrix} 5 & 10 \\ 10 & 20 \end{pmatrix}$, the column $c = (2, -1)$ gives $G c = 0$, and indeed $2 v_1 - v_2 = 0$.

### The converse

Part 4 is already an equivalence, and so is part 3.
Part 2 has a converse too: every positive semidefinite Hermitian $k \times k$ matrix $M$ is a Gram matrix.
With our convention take the vectors to be the columns of a positive semidefinite square root $B$ of $\overline{M}$; then $B^{\mathsf{T}} \overline{B} = \overline{B^* B} = \overline{\overline{M}} = M$, since $B^* = B$.

### Generalizations

The proof uses only the $k$ vectors and the axioms, so the statement holds in every inner product space, also of infinite dimension.
For a positive semidefinite Hermitian form $\beta$ in place of an inner product, parts 1 and 2 still hold with $\beta(w, w)$ in place of $\norm{w}^2$.
Part 3 weakens to: $G c = 0$ if and only if $\beta(w, w) = 0$ for $w = \sum_j \overline{c_j}\, v_j$, and part 4 holds when $\beta$ is definite on the span.

## Explanations

### L1 human

Make the table of all dot products of a list of arrows.
The table can be inverted exactly when no arrow in the list is a combination of the others.
For $(1, 2)$ and $(2, 4)$ the table is $\begin{pmatrix} 5 & 10 \\ 10 & 20 \end{pmatrix}$, and its determinant is $100 - 100 = 0$.
That zero matches what you see: the second arrow is twice the first.

### L2 human

Here is a typical use with functions: are $1$, $x$ and $1 + 2x$ independent, with $\ip{p}{q} = \int_0^1 p q \, dx$?
The inner products are
$$\ip{1}{1} = 1, \quad \ip{1}{x} = \tfrac12, \quad \ip{1}{1 + 2x} = 2, \quad \ip{x}{x} = \tfrac13, \quad \ip{x}{1 + 2x} = \tfrac12 + \tfrac23 = \tfrac76, \quad \ip{1 + 2x}{1 + 2x} = 1 + 2 + \tfrac43 = \tfrac{13}{3}.$$
So the Gram matrix is
$$G = \begin{pmatrix} 1 & \frac12 & 2 \\ \frac12 & \frac13 & \frac76 \\ 2 & \frac76 & \frac{13}{3} \end{pmatrix}.$$
Its third column is the first column plus twice the second: $1 + 1 = 2$, $\tfrac12 + \tfrac23 = \tfrac76$ and $2 + \tfrac73 = \tfrac{13}{3}$.
So $G c = 0$ for $c = (1, 2, -1)$, and part 3 gives the relation $1 + 2x - (1 + 2x) = 0$, which is true.
The family is dependent, and you found the relation without writing a single coordinate.
Watch out: over $\mathbb{C}$ the relation has the conjugate coefficients $\overline{c_j}$, not $c_j$.

### L3 human

The map $L \colon \mathbb{K}^k \to V$, $L(a) = \sum_j a_j v_j$, has the span as its image and the linear relations as its kernel.
Part 3 says that the null space of $G$ is the conjugate of $\ker L$, so the rank of $G$ equals the rank of $L$.
Over $\mathbb{R}$ with columns, this is the identity $\ker(A^{\mathsf{T}} A) = \ker A$, which follows from $c^{\mathsf{T}} A^{\mathsf{T}} A c = \norm{A c}^2$.
The same idea gives the rank of a covariance matrix or of a kernel matrix, and it reappears in the sub-area on [[positive operators and singular values|SS4EVPKT3A]], where $A^* A$ has the same rank as $A$.
