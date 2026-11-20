---
tag: 0B8KZRT28M
kind: concept
name: Orthogonal projection
msc: [15A04, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
specializes: [033DA1WE8Y]
uses: [0XJXTBCB2T, 033DA1WE8Y, 0QVNCJXRY3]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Orthogonal projections
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L749
    locator: src/section6-3.xml:749
  - book: isbn:9780321982384
    locator: Section 6.3
  - book: isbn:9783031410253
    locator: Section 6C
---

## Summary

Let $V$ be an [[inner product space|0QVNCJXRY3]] over $\R$ or $\C$, and let $U$ be a finite-dimensional subspace of $V$.
Each $v \in V$ is $v = u + u'$ for exactly one $u \in U$ and one $u'$ in the [[orthogonal complement|0XJXTBCB2T]] $U^\perp$.
The *orthogonal projection* onto $U$ is the map $P_U \colon V \to V$ with $P_U(v) = u$.
So $P_U$ is the [[projection|033DA1WE8Y]] onto $U$ along $U^\perp$, and the precise statement is in the [[definition|0Q8HZTJC7G]].
Orthogonal projection is the tool behind best approximation, least squares and Fourier coefficients: in each case the answer is the projection of a vector onto a subspace.

## Motivation

To drop a perpendicular from a point onto a plane is a basic act of geometry.
The foot of the perpendicular is the point of the plane closest to the given point.
In linear algebra this becomes a linear map, and it has a matrix.
Many problems with no exact solution, such as an overdetermined system $Ax = b$, have a best answer: replace $b$ by its projection onto the column space and solve again.

## Notation

We write $P_U$, or $\operatorname{proj}_U$ as in Lay, for the projection onto $U$.
For a line $U = \mathbb{K} a$ with $a \ne 0$, the [[vector projection|0JW13B48YP]] is $\operatorname{proj}_a(v) = \frac{\ip{v}{a}}{\ip{a}{a}} a$.
Mathlib has `Submodule.orthogonalProjection U`, whose values lie in `U` and not in `V`.

## Remarks

### Examples

1. [[The projection onto a line in R3|~69c2d599]]: for $a = (1, 2, 2)$, $P = \frac{1}{9} a a^{\mathsf{T}}$, a symmetric idempotent matrix of rank $1$.
2. [[The projection onto a plane in R3|~33fbc74c]]: for the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$, $P = A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} = I - \frac{1}{3} n n^{\mathsf{T}}$ with $n = (1, -1, 1)$.
3. [[The projection onto the line spanned by (1, 1)|MAP4F54GJW]] in $\R^2$ has the matrix $\frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
4. In $\R^3$, the projection onto the $xy$-plane is $(x, y, z) \mapsto (x, y, 0)$, because the complement of the plane is the $z$-axis.
5. [[Best mean-square approximation by polynomials|~5c06ec2d]]: the best polynomial of degree at most $2$ for $\abs{x}$ on $[-1, 1]$ is a projection in a space of functions.

### Non-examples

1. [[An oblique projection|DZXTTHGFQD]]: the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ is idempotent, but it is not symmetric, so it projects along a line that is not orthogonal to its image.
2. [[A complement that is not orthogonal|~08979893]]: the projection onto the $x$-axis along the line $\R(1, 1)$ is a projection, but not an orthogonal one.
3. The map $v \mapsto 2v$ is symmetric, but $2 \cdot 2 v \ne 2v$ for $v \ne 0$, so it is not a projection.

### Basic properties

The [[formulas for the orthogonal projection|~680b213e]] give the following:

- $P_U$ is linear, $P_U^2 = P_U$, its image is $U$ and its kernel is $U^\perp$.
- For an orthonormal basis $e_1, \dots, e_k$ of $U$, $P_U v = \sum_i \ip{v}{e_i} e_i$. For an orthogonal basis $u_1, \dots, u_k$, $P_U v = \sum_i \frac{\ip{v}{u_i}}{\ip{u_i}{u_i}} u_i$.
- If the columns of a real matrix $A$ form a basis of $U \subseteq \R^n$, then $P_U = A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$. If the columns of $Q$ are orthonormal, then $P_U = Q Q^{\mathsf{T}}$, as in [[the matrix from an orthonormal basis|MHGFJ5GM2K]].

By the [[characterization by self-adjoint idempotents|~b5bacc85]], the orthogonal projections of a finite-dimensional space are exactly the linear maps with $P^2 = P$ and $\ip{Pv}{w} = \ip{v}{Pw}$ for all $v, w$.
The [[best approximation theorem|0MCDDSCB9Z]] says that $P_U v$ is the unique point of $U$ closest to $v$.

### Common errors

- Using the formula $\sum_i \ip{v}{u_i} u_i$ for a basis that is not orthonormal. For an orthogonal basis, divide by $\ip{u_i}{u_i}$; for a general basis, use the matrix formula.
- Thinking that every idempotent matrix is an orthogonal projection. It must also be symmetric, or Hermitian over $\C$.
- Writing $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} = A A^{-1} (A^{\mathsf{T}})^{-1} A^{\mathsf{T}} = I$. This step is wrong for a non-square $A$, which has no inverse.

## Explanations

### L1 human

Shine a light straight down onto a table.
The shadow of a pencil on the table is its orthogonal projection onto the table.
The shadow of a point on the table is the point itself.
Doing the projection twice gives the same shadow as doing it once.

### L2 human

We project $v = (1, 2, 3)$ onto the plane $U$ spanned by $a_1 = (1, 1, 0)$ and $a_2 = (0, 1, 1)$.

1. A normal vector of $U$ is $n = (1, -1, 1)$, by [[the plane example|~f9f46f63]].
2. The part of $v$ along $n$ is $\frac{v \cdot n}{n \cdot n} n = \frac{2}{3} (1, -1, 1)$.
3. So $P_U v = v - \frac{2}{3} n = (1/3, 8/3, 7/3)$.
4. Check: $(1/3, 8/3, 7/3) \cdot n = 1/3 - 8/3 + 7/3 = 0$, so the result lies in $U$.

The typical use is to project onto the complement when the complement is smaller.
The trap is to forget that $a_1$ and $a_2$ are not orthogonal: $a_1 \cdot a_2 = 1$, so the sum of the two line projections is not $P_U v$.

### L3 human

In an inner product space, the orthogonal projections onto finite-dimensional subspaces correspond one to one with those subspaces.
In a Hilbert space the same holds for closed subspaces, and the projections are the bounded self-adjoint idempotents.
They are the building blocks of the [[spectral theorem|06J4PXRG22]]: a self-adjoint operator is $\sum_i \lambda_i P_i$ with orthogonal projections $P_i$ onto its eigenspaces.
In quantum mechanics, orthogonal projections represent yes-or-no measurements.
