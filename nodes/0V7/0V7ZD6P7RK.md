---
tag: 0V7ZD6P7RK
kind: object
name: Standard basis
aliases: [canonical-basis]
msc: [15A03]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [0KCQ9Y3QKA]
uses: [0XM8BZD76G]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_basis
    locator: lead section
same_as:
  wikidata: Q2000912
  wikipedia: Standard basis
---

## Description

The standard basis of $F^n$ is the list of vectors with a single entry $1$ and all other entries $0$.
It is the basis in which the coordinates of a vector are its own entries, so every computation with columns uses it, often without saying so.

Let $F$ be a [[field|04C5ZBG1WT]] and let $n \ge 1$ be an integer.
For $i = 1, \dots, n$, let $e_i$ be the vector of the [[coordinate space|0XM8BZD76G]] $F^n$ with entry $1$ in position $i$ and entry $0$ in every other position.
The *standard basis* of $F^n$ is the ordered family $(e_1, \dots, e_n)$.
In $F^3$, for example,
$$e_1 = (1, 0, 0), \qquad e_2 = (0, 1, 0), \qquad e_3 = (0, 0, 1).$$
We check the two conditions of a [[basis|0KCQ9Y3QKA]].

1. The family spans $F^n$, because each $x = (x_1, \dots, x_n)$ satisfies $x = x_1 e_1 + x_2 e_2 + \dots + x_n e_n$; the right side has entry $x_i$ in position $i$, since only $e_i$ contributes there.
2. The family is [[linearly independent|0CRMGPAH83]], because $c_1 e_1 + \dots + c_n e_n = (c_1, \dots, c_n)$, and this is the zero vector only when every $c_i = 0$.

So $(e_1, \dots, e_n)$ is a basis of $F^n$, and $F^n$ has [[dimension|03GSZ8RTZJ]] $n$.

## Remarks

### A first computation

In $\mathbb{R}^3$ take $x = (3, -2, 4)$.
Its expansion in the standard basis reads its entries off directly:
$$x = 3 e_1 - 2 e_2 + 4 e_3 = (3, 0, 0) + (0, -2, 0) + (0, 0, 4).$$
So the [[coordinate vector|04CYQHN6MC]] of $x$ in the standard basis is $x$ itself.
In any other basis you must solve a linear system to find the coordinates, and that is what makes the standard basis special.

### Columns of a matrix

The product of a matrix with $e_j$ picks out one column.
For an $m \times n$ matrix $A$, the vector $A e_j$ is column $j$ of $A$, because only the entry in position $j$ of $e_j$ is nonzero.
For example,
$$\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}.$$
This gives the rule for writing down the matrix of a [[linear map|0NRYHJPQG2]] $T \colon F^n \to F^m$: column $j$ is $T(e_j)$.
For the rotation of the plane by a right angle, $T(e_1) = e_2$ and $T(e_2) = -e_1$, so its matrix has columns $(0, 1)$ and $(-1, 0)$.

### Standard bases of other spaces

Other common spaces have a basis that plays the same part.
The space of polynomials of degree at most $n$ has the monomial basis $1, x, x^2, \dots, x^n$, so its dimension is $n + 1$; see the [[space of polynomials|0JGZCDT5DN]].
The space of $m \times n$ matrices has the [[matrix units|A4HTT7JFD1]] $E_{ij}$, with entry $1$ in position $(i, j)$ and $0$ elsewhere, so its dimension is $mn$; see the [[space of matrices|0RE6X3BGPN]].
In both cases the coordinates of an element are the numbers you write down to describe it: the coefficients, or the entries.

### All the other bases of F^n

Every basis of $F^n$ arises from the standard one by an invertible matrix.
Put $n$ vectors of $F^n$ as the columns of an $n \times n$ matrix $P$, so that $P e_j$ is the $j$th vector.
By the [[column criterion|WFM1CX5PZT]], the vectors form a basis exactly when $P$ is invertible.
For example, $(1, 1)$ and $(1, -1)$ form a basis of $\mathbb{R}^2$, because
$$\det \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = -1 - 1 = -2 \ne 0.$$
So the bases of $F^n$ correspond one to one to the invertible $n \times n$ matrices, with the standard basis matched to the identity matrix.

### What it is not

The family $(1, 0), (1, 1)$ is a basis of $\mathbb{R}^2$, but it is not the standard basis, and in it the vector $(0, 1)$ has the coordinates $(-1, 1)$.
A plane through the origin in $\mathbb{R}^3$, such as $x + y + z = 0$, has no standard basis.
It has many bases, for example $(1, -1, 0), (0, 1, -1)$, but no basis is singled out, because the plane contains none of the vectors $e_1, e_2, e_3$.
The word "standard" refers to the coordinates of $F^n$, not to an abstract vector space.

### Watch out

The same two vectors in $\mathbb{F}_2^2$ behave differently, because there $-1 = 1$.
Over $\mathbb{F}_2$ the vectors $(1, 1)$ and $(1, -1)$ are equal, so they do not form a basis, and the determinant $-2$ above is $0$ in $\mathbb{F}_2$.
A second trap is infinite dimension.
In the space $F^{\mathbb{N}}$ of all sequences, the vectors $e_1, e_2, \dots$ are independent, but they do not span: a linear combination has finitely many terms, so it never gives the sequence $(1, 1, 1, \dots)$.
They form a basis only of the smaller space of sequences with finitely many nonzero entries.

### Try it

First, write $(5, 0, -7)$ in the standard basis of $\mathbb{R}^3$.
It is $5 e_1 + 0 e_2 - 7 e_3$, so its coordinates are $(5, 0, -7)$.

Second, find the matrix of the linear map $T(x, y) = (2x + y, x - y)$.
The columns are $T(e_1) = (2, 1)$ and $T(e_2) = (1, -1)$, so the matrix is $\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$.

## Explanations

### L1 human

In the plane, the standard basis is two arrows of length one: $e_1$ points along the $x$-axis and $e_2$ points along the $y$-axis.
Every point can be reached by walking some steps along $e_1$ and then some steps along $e_2$.
To reach $(3, 2)$, take $3$ steps along $e_1$ and $2$ steps along $e_2$.
The numbers of steps are just the coordinates of the point, so nothing needs to be computed.

### L2 human

Here is a typical use: find the matrix of the reflection $T$ of $\mathbb{R}^2$ in the line $y = x$.
The reflection swaps the two axes, so $T(e_1) = e_2$ and $T(e_2) = e_1$.
Put these images in the columns:
$$[T] = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
Check on a vector off the line: $[T] (3, 1)^{\mathsf{T}} = (1, 3)^{\mathsf{T}}$, and the reflection of $(3, 1)$ in $y = x$ is $(1, 3)$.
The method works for every linear map from $F^n$, because a linear map is fixed by its values on a basis.
The trap is to put the images in the rows instead of the columns, which gives the transpose of the correct matrix.

### L3 human

The standard basis of $\mathbb{R}^n$ is an [[orthonormal basis|0S9GGTR0EX]] for the dot product, since $e_i \cdot e_j$ is $1$ for $i = j$ and $0$ otherwise.
In $\mathbb{R}^3$ physics books write $\mathbf{i}, \mathbf{j}, \mathbf{k}$ for $e_1, e_2, e_3$, and the [[orientation|0QJJAQ6ZYZ]] of this ordered basis is the reference that defines right-handed bases.
For an arbitrary set $I$, the functions $\delta_i$ with value $1$ at $i$ and $0$ elsewhere form a basis of the space of finitely supported functions on $I$, and this is the free vector space on $I$.
The dual basis of the standard basis consists of the coordinate functions $x \mapsto x_i$, and the sub-area on [[dual spaces|9K7FFF26QR]] studies it.
