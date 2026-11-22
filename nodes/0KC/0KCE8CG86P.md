---
tag: 0KCE8CG86P
kind: concept
name: Idempotent matrix
aliases: [projection-matrix]
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0JXZKX526R]
uses: [0JXZKX526R, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: Properties
same_as:
  wikidata: Q3751720
  wikipedia: Idempotent matrix
inventory: [DMB0JAP9ZR]
---

## Summary

An idempotent matrix is a matrix that changes nothing more when we apply it a second time.
It is the algebra of a projection: once a vector has been moved onto a line or a plane, moving it again leaves it where it is.
Exactly, a [[square matrix|0JXZKX526R]] $P$ is *idempotent* when
$$P^2 = P,$$
and the [[formal definition|0K7TD9BV2D]] states this over any ring.
Over a field, the idempotent matrices are exactly the matrices of [[projections|033DA1WE8Y]], their eigenvalues lie in $\{0, 1\}$, and their trace equals their rank in characteristic $0$.

## Motivation

Many problems ask us to split a vector into two parts: the part along a line and the part across it, the signal and the noise, the fitted values and the residuals.
A projection does this split, and its matrix $P$ satisfies $P^2 = P$, because a vector that is already in the image stays fixed.
The other part is given by $I - P$, which is idempotent as well.

Idempotent matrices appear wherever such splits appear.
In least squares, the fitted values are $P b$ for the idempotent "hat matrix" $P$, and the residuals are $(I - P) b$; the sub-area on [[orthogonality and least squares|8GQVME4SZZ]] builds this.
In the spectral theorem, a symmetric matrix is a sum of eigenvalues times idempotents.
In the [[matrix ring|AB2MD5CD13]], an idempotent $P$ and its partner $I - P$ split the identity, $I = P + (I - P)$ with $P (I - P) = 0$, in the way that $0$ and $1$ cannot do in a field.

## Notation

Many books call an idempotent matrix a *projection matrix*; others keep that name for the [[symmetric|0VR671PHE5]] idempotents, which are the orthogonal projections, so check the convention of the book.
In Mathlib the condition is `IsIdempotentElem P`, which means `P * P = P` in any semigroup.

## Remarks

### Three projections of the plane

The simplest idempotent is $E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, which keeps the first coordinate and erases the second; [[its powers are all equal to it|5VEW97EQR6]].

The orthogonal projection onto the line $y = x$ is $P = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
Square it:
$$P^2 = \tfrac14 \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = P.$$
It sends $(x, y)$ to the midpoint value $\bigl(\tfrac{x + y}{2}, \tfrac{x + y}{2}\bigr)$, as [[the orthogonal projection onto the line spanned by (1, 1)|MAP4F54GJW]] works out.

A projection need not be orthogonal.
The matrix $Q = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ sends $(x, y)$ to $(x + y, 0)$, and
$$Q^2 = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = Q.$$
It slides points onto the $x$-axis along the direction $(1, -1)$, which is [[an oblique projection of the plane onto a line|DZXTTHGFQD]].

### What it is not

The matrix $2I$ is not idempotent, since $(2I)^2 = 4I$; a scalar matrix $cI$ is idempotent only for $c^2 = c$, that is, $c = 0$ or $c = 1$.
Eigenvalues in $\{0, 1\}$ are not enough, as [[a matrix with eigenvalues in {0, 1} that is not idempotent|AVTQZC769M]] shows: the matrix $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ has eigenvalues $1, 0, 0$, but its square loses the entry $1$ in position $(2, 3)$.

### The rules you can use

Let $P$ be idempotent.
Then $I - P$ is idempotent, because $(I - P)^2 = I - 2P + P^2 = I - P$, and $P (I - P) = P - P^2 = 0$.
All powers agree, $P^k = P$ for $k \ge 1$, by induction from $P^{k+1} = P^k P = P P$.
The only [[invertible|0EB9N0S33C]] idempotent is $I$, since $P = P^{-1} P^2 = P^{-1} P = I$.

Over a field, each eigenvalue is $0$ or $1$: from $P v = \lambda v$ with $v \ne 0$ we get $\lambda v = P^2 v = \lambda^2 v$, so $\lambda^2 = \lambda$.
Each vector splits as $v = P v + (v - P v)$, with $P v$ in the image and $v - Pv$ in the kernel, so the space is the direct sum of the image and the kernel.
In a basis adapted to this split, $P = \operatorname{diag}(I_r, 0)$ with $r$ the [[rank|0ZC9YTXZRY]], and so $\operatorname{tr} P = r \cdot 1$.
Outside characteristic $2$, $P$ is idempotent if and only if $2P - I$ is [[involutory|NH2QE3671N]], since $(2P - I)^2 = I + 4(P^2 - P)$.

### Watch out

An idempotent matrix need not be symmetric: the oblique projection $Q$ above is idempotent and $Q^{\mathsf{T}} \ne Q$.
Only the orthogonal projections are symmetric.
Also, $P^2 = P$ does not allow us to cancel $P$ and conclude $P = I$, because $P$ is usually not invertible: $E_{11} E_{11} = E_{11} I$, but $E_{11} \ne I$.

### History

Benjamin Peirce introduced the words *idempotent* and *nilpotent* in his work on linear associative algebras around 1870.

### Try it

First, is $\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ idempotent?
Its square has rows $(1, 0)$ and $(1 \cdot 1 + 0 \cdot 1, 0) = (1, 0)$, so yes; its trace and its rank are both $1$.

Second, if $P$ is idempotent, what is $(I - 2P)^2$?
It is $I - 4P + 4P^2 = I$, so $I - 2P$ is a reflection.

## Explanations

### L1 human

Think of the shadow of a stick on the ground at noon.
The shadow of the shadow is the same shadow, because it already lies on the ground.
An idempotent matrix works like casting a shadow: doing it twice is the same as doing it once.
The matrix $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ sends $(3, 5)$ to $(3, 0)$, and sends $(3, 0)$ to $(3, 0)$ again.

### L2 human

Find the orthogonal projection onto the line through $u = (1, 2)$, and project $b = (3, 1)$.
The matrix is $P = u u^{\mathsf{T}} / (u^{\mathsf{T}} u)$, and $u^{\mathsf{T}} u = 5$:
$$P = \frac15 \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}^2 = \begin{pmatrix} 5 & 10 \\ 10 & 20 \end{pmatrix},$$
so $P^2 = \tfrac{1}{25} \cdot 5 \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = P$.
Then $P b = \tfrac15 (3 + 2, 6 + 4) = (1, 2)$, and the residual $b - Pb = (2, -1)$ is perpendicular to $u$, since $2 - 2 = 0$.
The trace is $\tfrac15 + \tfrac45 = 1$, the dimension of the line.
This is the typical use: an idempotent splits a vector into a kept part and a removed part.

### L3 human

Over a field, $P$ is idempotent if and only if its minimal polynomial divides $x^2 - x = x(x - 1)$, which has distinct roots, so every idempotent is diagonalizable and similar to $\operatorname{diag}(I_r, 0)$.
Thus idempotents of rank $r$ correspond to pairs of complementary subspaces of dimensions $r$ and $n - r$.
In ring theory, idempotents of the endomorphism ring of a module correspond to its decompositions into two direct summands, and the sub-area on [[direct sums and complements|QHKTJ89V6S]] returns to this.
For operators on inner product spaces, the self-adjoint idempotents are the orthogonal projections, and they are the building blocks of the spectral theorem.
