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

The orthogonal projection of a vector onto a subspace is the foot of the perpendicular that you drop from the vector to the subspace.
It is the closest point of the subspace, and it is the one linear map behind best approximation, least squares and Fourier coefficients.
To state it exactly, let $V$ be an [[inner product space|0QVNCJXRY3]] over $\R$ or $\C$, and let $U$ be a finite-dimensional subspace of $V$.
Each $v \in V$ splits as $v = u + u'$ for exactly one $u \in U$ and one $u'$ in the [[orthogonal complement|0XJXTBCB2T]] $U^\perp$.
The *orthogonal projection* onto $U$ is the map
$$P_U \colon V \to V, \qquad P_U(v) = u.$$
So $P_U$ is the [[projection|033DA1WE8Y]] onto $U$ along $U^\perp$, and the [[formal definition|0Q8HZTJC7G]] states it with all its conditions.

## Motivation

To drop a perpendicular from a point onto a line or a plane is one of the oldest acts of geometry.
The foot of the perpendicular is the point of the line or plane that is nearest to the given point.
Linear algebra turns this act into a linear map with a matrix, so that the same construction works in $\R^{100}$ and in spaces of functions.

Many problems have no exact answer but have a best one.
A system $Ax = b$ with more equations than unknowns is usually inconsistent, and the method of [[least squares|0BYTQ4X1HC]] replaces $b$ by its projection onto the column space of $A$.
A function on an interval is rarely a polynomial, and its best polynomial approximation in the mean-square sense is again a projection.
The [[best approximation theorem|0MCDDSCB9Z]] explains why the projection is always the right answer, and the [[QR decomposition|0ERWG4NXQ9]] computes it in practice.

## Notation

We write $P_U$, and Lay writes $\operatorname{proj}_U$.
For a line $U = \mathbb{K} a$ with $a \ne 0$, the projection is the [[vector projection|0JW13B48YP]] $\operatorname{proj}_a(v) = \frac{\ip{v}{a}}{\ip{a}{a}} a$.
In Mathlib, `Submodule.orthogonalProjection U` takes its values in `U` and not in `V`, so it must be composed with the inclusion to give a map from `V` to `V`.

## Remarks

### A first projection onto a line

Take $a = (1, 2, 2)$ in $\R^3$ and $v = (1, 1, 1)$.
The projection onto the line $\R a$ is the multiple of $a$ whose error is perpendicular to $a$, and the coefficient is $\frac{v \cdot a}{a \cdot a}$:
$$P_U v = \frac{1 + 2 + 2}{1 + 4 + 4} \, a = \frac{5}{9} (1, 2, 2).$$
Check: the error is $v - P_U v = \frac{1}{9}(4, -1, -1)$, and $(4, -1, -1) \cdot (1, 2, 2) = 4 - 2 - 2 = 0$.
Writing the same rule for every $v$ at once gives the matrix $P = \frac{1}{9} a a^{\mathsf{T}}$, a symmetric matrix of rank $1$.
[[The projection onto a line in R3|VM9N7J68FW]] checks this matrix in full, and [[the line spanned by (1, 1)|MAP4F54GJW]] gives the same rule in the plane, with matrix $\frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.

### Projecting onto a plane

Now let $U$ be the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$, and put these vectors into the columns of a $3 \times 2$ matrix $A$.
The columns are linearly independent, so $A^{\mathsf{T}} A$ is invertible and the matrix of $P_U$ is $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$.
[[The projection onto a plane in R3|8YDFZV8S5W]] works this out:
$$P = \frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}.$$
In $\R^3$ there is a shortcut, because the complement of a plane is a line.
The normal $n = (1, -1, 1)$ is orthogonal to both columns, so $P = I - \frac{1}{3} n n^{\mathsf{T}}$, and this gives the same matrix.
For $v = (1, 2, 3)$ we get $P v = \frac{1}{3}(1, 8, 7)$, and the error $v - P v = \frac{2}{3}(1, -1, 1)$ points along $n$, as it must.

### The formulas you can use

The [[formulas for the orthogonal projection|AK3JJ5HHG2]] collect the rules.
The map $P_U$ is linear and $P_U^2 = P_U$, because a vector of $U$ is its own projection.
Its image is $U$ and its kernel is $U^\perp$.
For an orthonormal basis $e_1, \dots, e_k$ of $U$ you project onto each axis and add, $P_U v = \sum_i \ip{v}{e_i} e_i$.
For an orthogonal basis $u_1, \dots, u_k$ you divide each term by $\ip{u_i}{u_i}$.
For a real matrix $A$ whose columns form a basis of $U$, the matrix is $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$, and the inverse exists exactly because the columns are independent.
When the columns of $Q$ are orthonormal, $Q^{\mathsf{T}} Q = I$ and the matrix shrinks to $Q Q^{\mathsf{T}}$, as in [[the matrix from an orthonormal basis|MHGFJ5GM2K]].

Which linear maps are orthogonal projections?
By the [[characterization by self-adjoint idempotents|ZJRJNWJ8V1]], on a finite-dimensional space they are exactly the maps with $P^2 = P$ and $\ip{Pv}{w} = \ip{v}{Pw}$; for a real matrix this means $P^2 = P$ and $P^{\mathsf{T}} = P$.

### What it is not

The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ satisfies $P^2 = P$, so it is a projection onto the $x$-axis.
It is not symmetric, and it projects along the line $\R(1, -1)$, which is not perpendicular to the $x$-axis; this is [[an oblique projection|DZXTTHGFQD]].
In the same way, [[the projection along the line R(1, 1)|NFHJSAH156]] onto the $x$-axis uses a complement that is not the orthogonal one.
The map $v \mapsto 2v$ is symmetric, but it fails $P^2 = P$, since $2 \cdot 2v \ne 2v$ for $v \ne 0$, so it is no projection at all.

### Watch out

The rule "project onto each basis vector and add" needs an orthogonal basis.
For the plane above and $v = (1, 2, 3)$, the sum $\sum_i (v \cdot a_i) a_i = 3(1, 1, 0) + 5(0, 1, 1) = (3, 8, 5)$ is not even close to $\frac{1}{3}(1, 8, 7)$.
Dividing by $a_i \cdot a_i$ does not repair it either, since $a_1 \cdot a_2 = 1 \ne 0$; use the matrix formula or orthogonalize first.

A second trap is to cancel in $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$.
Writing $(A^{\mathsf{T}} A)^{-1} = A^{-1} (A^{\mathsf{T}})^{-1}$ would give $I$, but a $3 \times 2$ matrix has no inverse, so the step is invalid.
Only a square invertible $A$ gives $I$, and then $U$ is the whole space.

### History

Orthogonal projections on Hilbert space became a basic tool of physics through von Neumann's book on the mathematical foundations of quantum mechanics, published in 1932.
There a measurement with a yes-or-no answer is described by an orthogonal projection.

### Try it

First, project $v = (3, 1)$ onto the line spanned by $(1, 1)$.
The coefficient is $\frac{3 + 1}{1 + 1} = 2$, so $P v = (2, 2)$, and the error $(1, -1)$ is perpendicular to $(1, 1)$.

Second, find the matrix of the projection onto the plane $x + y + z = 0$ in $\R^3$.
The normal is $n = (1, 1, 1)$ with $n \cdot n = 3$, so $P = I - \frac{1}{3} n n^{\mathsf{T}}$ has $\frac{2}{3}$ on the diagonal and $-\frac{1}{3}$ everywhere else.

## Explanations

### L1 human

Shine a lamp straight down onto a table and hold a pencil above it.
The shadow of the pencil on the table is its orthogonal projection onto the table.
A point that already lies on the table is its own shadow.
Taking the shadow of a shadow changes nothing, and the shadow of each point is the spot on the table nearest to it.

### L2 human

Here is a typical problem: how far is the point $v = (1, 2, 3)$ from the plane $U$ spanned by $a_1 = (1, 1, 0)$ and $a_2 = (0, 1, 1)$?
The [[plane example|38S0WYCSA3]] finds the normal $n = (1, -1, 1)$, and it is faster to project onto the line $\R n$ than onto the plane.
The part of $v$ along $n$ is
$$\frac{v \cdot n}{n \cdot n} \, n = \frac{1 - 2 + 3}{3} \, n = \frac{2}{3} (1, -1, 1).$$
Removing it gives the projection onto the plane:
$$P_U v = (1, 2, 3) - \frac{2}{3}(1, -1, 1) = \left( \frac{1}{3}, \frac{8}{3}, \frac{7}{3} \right).$$
Check: $\frac{1}{3} - \frac{8}{3} + \frac{7}{3} = 0$, so $P_U v$ is orthogonal to $n$ and lies in $U$.
The distance is the length of the removed part, $\frac{2}{3} \sqrt{3} = \frac{2}{\sqrt{3}}$.
The problem shows the general habit: project onto whichever of $U$ and $U^\perp$ is smaller, and subtract when you need the other one.

### L3 human

On an inner product space, the orthogonal projections onto finite-dimensional subspaces correspond one to one with those subspaces, and $P_{U^\perp} = I - P_U$.
In a Hilbert space the same holds for all closed subspaces, and the orthogonal projections are exactly the bounded self-adjoint idempotents.
They are the building blocks of the spectral theorems: a self-adjoint operator on a finite-dimensional space is $\sum_i \lambda_i P_i$, where the $P_i$ are the orthogonal projections onto its eigenspaces, as the [[real spectral theorem|06J4PXRG22]] shows.
In numerical work, the projection onto a column space is computed from a [[QR decomposition|0ERWG4NXQ9]] as $Q Q^{\mathsf{T}}$, and for a matrix with dependent columns from the [[Moore-Penrose inverse|0YY8VX28JR]] as $A A^{+}$.
