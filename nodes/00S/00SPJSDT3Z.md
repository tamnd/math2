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

The Gram matrix of a list of vectors is the table of all their inner products.
It keeps every length and every angle of the list and forgets everything else, so questions about shape become questions about one square matrix.
Let $V$ be an [[inner product space|0QVNCJXRY3]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the [[inner product|0NB0AWGJBW]] linear in the first slot, and let $v_1, \dots, v_k \in V$.
The Gram matrix of $v_1, \dots, v_k$ is the $k \times k$ matrix $G = G(v_1, \dots, v_k)$ with the entries
$$G_{ij} = \ip{v_i}{v_j} \qquad (1 \le i, j \le k).$$
The [[formal definition|0HX8HZ1WTQ]] states this, and $\det G$ is called the Gram determinant.
Two facts make the matrix useful: it is invertible exactly when the vectors are [[linearly independent|0EVHJFTG9Z]], and its determinant is the square of the volume that the vectors span.

## Motivation

Many questions about a few vectors need only their inner products.
How long is each vector, what are the angles between them, are they independent, and how large is the box that they span?
The vectors may live in $\mathbb{R}^{100}$, or in a space of polynomials, but these questions do not need coordinates.
The Gram matrix collects the $k^2$ numbers that the answers depend on, and then the rank and the determinant give the answers.

The same matrix appears in many places.
For column vectors in $\mathbb{R}^n$ it is $A^{\mathsf{T}} A$, the matrix of the [[normal equations|4D7MRG4D91]] of [[least squares|0BYTQ4X1HC]].
In statistics, the covariance matrix of random variables with mean zero is a Gram matrix, and in machine learning a kernel matrix is a Gram matrix in a space of features.
Later in the area, Gram matrices return as the positive semidefinite matrices of the sub-area on [[positive operators and singular values|SS4EVPKT3A]].

## Notation

We write $G(v_1, \dots, v_k)$, or just $G$, and $\det G(v_1, \dots, v_k)$ for the Gram determinant.
For the dot product on $\mathbb{R}^n$, let $A$ be the $n \times k$ matrix with the columns $v_1, \dots, v_k$; then $G = A^{\mathsf{T}} A$.
For the standard inner product on $\mathbb{C}^n$, the entry is $G_{ij} = \sum_l (v_i)_l \overline{(v_j)_l} = v_j^* v_i$, so $G = A^{\mathsf{T}} \overline{A}$, which is the transpose of $A^* A$.
Mathlib and physics books make the inner product linear in the second slot, and then the table of inner products is $A^* A$.
For real vectors the two conventions give the same matrix.

## Remarks

### A first computation

Take $v_1 = (1, 0)$ and $v_2 = (3, 4)$ in $\mathbb{R}^2$ with the dot product.
The three inner products are
$$\ip{v_1}{v_1} = 1, \qquad \ip{v_1}{v_2} = 3, \qquad \ip{v_2}{v_2} = 9 + 16 = 25.$$
So the Gram matrix and its determinant are
$$G = \begin{pmatrix} 1 & 3 \\ 3 & 25 \end{pmatrix}, \qquad \det G = 25 - 9 = 16.$$
The parallelogram with sides $v_1$ and $v_2$ has base $1$ and height $4$, so its area is $4$, and $16 = 4^2$.
The [[two vectors in $\mathbb{R}^3$|QG8VQCE4QC]] show the same thing in space, where no ordinary determinant of the two vectors exists: there $\det G = 3$ and the area is $\sqrt{3}$.

### What the entries record

The diagonal holds the squared lengths $G_{ii} = \norm{v_i}^2$, and each entry off the diagonal holds the angle information of one pair.
So the Gram matrix of an [[orthonormal family|0RW9TNNT87]] is the identity $I_k$, and the Gram matrix of an orthogonal family is diagonal with the entries $\norm{v_i}^2$.

Two rules hold for every Gram matrix.
It is [[Hermitian|0P17NGQQMQ]], since conjugate symmetry gives $G_{ji} = \ip{v_j}{v_i} = \overline{\ip{v_i}{v_j}} = \overline{G_{ij}}$; over $\mathbb{R}$ this says that $G$ is symmetric.
It is [[positive semidefinite|01MMVW8CKC]], since for every column $c \in \mathbb{K}^k$ the expansion of a squared norm gives
$$c^* G c = \sum_{i, j} \overline{c_i}\, G_{ij}\, c_j = \norm{\sum_{i} \overline{c_i}\, v_i}^2 \ge 0.$$
These two rules are also enough: every positive semidefinite matrix is the Gram matrix of some family.
Two families have the same Gram matrix exactly when a linear isometry between their spans carries one family to the other, so the Gram matrix records the shape of the family and nothing more.

### Independence and volume

A family is dependent exactly when some combination $\sum_i \overline{c_i}\, v_i$ with $c \ne 0$ is zero, and the display above turns this into $c^* G c = 0$.
The [[Gram invertibility theorem|EM1QNRGWQ8]] makes this precise: $G$ is invertible if and only if $v_1, \dots, v_k$ are independent, and the rank of $G$ is the dimension of their span.

The [[squared volume theorem|FWA0AKJA2R]] says more.
If $u_1, \dots, u_k$ are the orthogonal vectors that the [[Gram-Schmidt process|0VT6P0GNQR]] makes from an independent family, then
$$\det G = \norm{u_1}^2 \norm{u_2}^2 \cdots \norm{u_k}^2,$$
which is base times height, repeated, and squared.
For two vectors this reads $\det G(x, y) = \norm{x}^2 \norm{y}^2 - \abs{\ip{x}{y}}^2 \ge 0$, which is the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
For the polynomials $1, x, x^2$ with $\ip{p}{q} = \int_0^1 p q \, dx$, the Gram matrix is the [[Hilbert matrix|JNME2MD8GM]] with the entries $\frac{1}{i + j - 1}$ and determinant $\frac{1}{2160}$, so these three functions span a very thin box.

### What it is not

A symmetric real matrix need not be a Gram matrix.
The [[matrix with rows (1, 2) and (2, 1)|572X387N7F]] would describe two unit vectors with inner product $2$, which Cauchy-Schwarz forbids, and its determinant is $-3 < 0$.
Over $\mathbb{C}$ symmetry is the wrong condition: $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ is symmetric, but a Gram matrix needs $G_{21} = \overline{G_{12}} = -i$.
A table of values $\beta(v_i, v_j)$ of a form that is not positive definite is not a Gram matrix either.
For the [[Minkowski form|TFGECQ5C32]] $\beta(x, y) = x_1 y_1 - x_2 y_2$ and the single vector $(0, 1)$ the table is $(-1)$, while a Gram matrix has $G_{11} = \norm{v_1}^2 \ge 0$.

### Watch out

Over $\mathbb{C}$ the conjugate cannot be dropped.
For $v_1 = (1, i)$ the formula $A^{\mathsf{T}} A$ gives $1 + i^2 = 0$ in place of $G_{11}$, but $\norm{v_1}^2 = 1 + \abs{i}^2 = 2$.

A positive determinant does not make a Gram matrix.
The matrix $-I_2$ has determinant $1$, but its diagonal entries are $-1$, and a squared length is never negative.
The correct test is positive semidefiniteness, for example that all principal minors are $\ge 0$.

The size of $G$ is the number of vectors, not the dimension of the space.
Two vectors in $\mathbb{R}^3$ have a $2 \times 2$ Gram matrix, and two polynomials have one too.

### History

The matrix is named after the Danish mathematician Jørgen Pedersen Gram.
His name is also on the [[Gram-Schmidt process|0VT6P0GNQR]], which computes the factors $\norm{u_j}$ in the volume formula.

### Try it

First, find the Gram matrix of $(1, 1)$ and $(1, -1)$ in $\mathbb{R}^2$ and the area of their parallelogram.
The vectors are orthogonal with squared length $2$, so $G = \operatorname{diag}(2, 2)$, $\det G = 4$ and the area is $2$.

Second, is $\begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix}$ a Gram matrix?
Yes: it is the Gram matrix of $(2, 0)$ and $(3, 0)$, and its determinant $36 - 36 = 0$ says that these vectors are dependent.

Third, compute the Gram matrix of $v_1 = (1, i)$ and $v_2 = (0, 1)$ in $\mathbb{C}^2$.
You get $G_{11} = 2$, $G_{12} = 1 \cdot 0 + i \cdot \overline{1} = i$, $G_{21} = -i$ and $G_{22} = 1$, so $\det G = 2 - 1 = 1$, which is $\abs{\det A}^2$ for the matrix $A$ with these columns.

## Explanations

### L1 human

Write a list of arrows, and make a table of the dot product of each arrow with each arrow.
The entry in row $i$ and column $j$ is the dot product of arrow $i$ with arrow $j$.
The diagonal holds the squared lengths, and the other entries tell how the arrows lean toward each other.
For $(1, 0)$ and $(1, 1)$ in the plane, the table is $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
Its determinant is $2 - 1 = 1$, and the parallelogram of the two arrows has base $1$ and height $1$, so its area is $1$ as well.
The determinant of the table is always the square of the area, and it is zero when the arrows lie on one line.

### L2 human

Here is a typical use: are $v_1 = (1, 2, 3)$, $v_2 = (4, 5, 6)$ and $v_3 = (7, 8, 9)$ independent in $\mathbb{R}^3$?
The squared lengths are $14$, $77$ and $194$, and the other dot products are
$$v_1 \cdot v_2 = 32, \qquad v_1 \cdot v_3 = 50, \qquad v_2 \cdot v_3 = 122.$$
So the Gram matrix is
$$G = \begin{pmatrix} 14 & 32 & 50 \\ 32 & 77 & 122 \\ 50 & 122 & 194 \end{pmatrix}.$$
Row $1$ minus twice row $2$ plus row $3$ is $(14 - 64 + 50, \ 32 - 154 + 122, \ 50 - 244 + 194) = (0, 0, 0)$.
So $G c = 0$ for $c = (1, -2, 1)$, and $\det G = 0$.
The invertibility theorem then predicts the relation $v_1 - 2 v_2 + v_3 = 0$.
Check: $(1, 2, 3) - (8, 10, 12) + (7, 8, 9) = (0, 0, 0)$.
The same method works for functions or matrices, where you know the inner products but have no coordinates to row reduce.

### L3 human

For an independent family the Gram matrix is the matrix of the inner product on the span in the basis $v_1, \dots, v_k$: with our convention, $\ip{\sum_i a_i v_i}{\sum_j b_j v_j} = a^{\mathsf{T}} G\, \overline{b}$.
A change of basis $v_j' = \sum_i P_{ij} v_i$ changes it to $P^{\mathsf{T}} G \overline{P}$, a congruence and not a similarity, so $\det G$ changes by $\abs{\det P}^2$.
The Gram matrices of $k$ vectors are exactly the positive semidefinite $k \times k$ matrices, and the factorization $G = A^{\mathsf{T}} \overline{A}$ is the same thing as a choice of vectors.
The Gram determinant gives $k$-dimensional volume inside a space of any dimension, and by the [[Cauchy-Binet formula|08WE2W7DYS]] the real $\det(A^{\mathsf{T}} A)$ is the sum of the squares of the $k \times k$ minors of $A$.
In Riemannian geometry the metric tensor is a Gram matrix of tangent vectors at each point, and $\sqrt{\det g}$ is its volume density.
