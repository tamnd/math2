---
tag: AK3JJ5HHG2
kind: statement
role: theorem
name: Formulas for the orthogonal projection
msc: [15A04, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
about: [0B8KZRT28M]
uses: [0Q8HZTJC7G, 079D68S3AW, 0FWJ0VW561, 0EX045E2BP, 0F0RPPJ2TT, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Formulas
  - book: isbn:9780321982384
    locator: Section 6.3
  - book: isbn:9781733146678
    locator: Chapter 4
---

## Statement

The orthogonal projection is a linear map, and it can be computed from an orthonormal basis, from an orthogonal basis or from any basis written as the columns of a matrix.

Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$, and let $U$ be a finite-dimensional subspace of $V$.
Let $P = P_U$ be the [[orthogonal projection|0Q8HZTJC7G]] onto $U$, and let $U^\perp$ be the [[orthogonal complement|079D68S3AW]] of $U$.
Then the following hold.

1. $P$ is linear, $P^2 = P$, the image of $P$ is $U$, and the kernel of $P$ is $U^\perp$.
2. If $e_1, \dots, e_k$ is an [[orthonormal basis|0FWJ0VW561]] of $U$, then $P v = \sum_{i=1}^{k} \ip{v}{e_i} e_i$ for all $v \in V$.
3. If $u_1, \dots, u_k$ is a basis of $U$ of nonzero, pairwise orthogonal vectors, then $P v = \sum_{i=1}^{k} \frac{\ip{v}{u_i}}{\ip{u_i}{u_i}} u_i$ for all $v \in V$.
4. Let $V = \mathbb{K}^n$ with $\ip{x}{y} = \sum_j x_j \overline{y_j}$. Let $A$ be an $n \times k$ matrix whose columns are [[linearly independent|0EVHJFTG9Z]] and span $U$, so that $U$ is the [[column space|0F0RPPJ2TT]] of $A$. Then $A^* A$ is invertible, and $P$ has the matrix $A (A^* A)^{-1} A^*$, where $A^*$ is the [[conjugate transpose|0EX045E2BP]]; over $\R$ this matrix is $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$.
5. In part 4, if the columns of $A = Q$ are orthonormal, then $Q^* Q = I$ and $P = Q Q^*$.

The [[proof|YT9XQ7NNJZ]] checks each formula against the unique splitting $v = Pv + (v - Pv)$.

## Remarks

### Why each hypothesis is needed

Part 2 needs the basis to be orthonormal.
Take the basis $(1, 1, 0)$, $(0, 1, 1)$ of a plane in $\R^3$ and $v = (1, 2, 3)$.
The sum in part 2 would give
$$3 (1, 1, 0) + 5 (0, 1, 1) = (3, 8, 5),$$
while the true projection is $\frac{1}{3}(1, 8, 7)$, as [[the projection onto a plane|8YDFZV8S5W]] shows.
Part 3 relaxes the condition to orthogonality, and the division by $\ip{u_i}{u_i}$ pays for the missing unit length.

Part 4 needs independent columns.
For $A = \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix}$ the second column is twice the first, and
$$A^{\mathsf{T}} A = \begin{pmatrix} 2 & 4 \\ 4 & 8 \end{pmatrix}, \qquad \det(A^{\mathsf{T}} A) = 16 - 16 = 0.$$
So $(A^{\mathsf{T}} A)^{-1}$ does not exist and the formula has no meaning.
The projection onto the column space still exists; we drop the dependent column and use $a = (1, 1)$, which gives $\frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
In fact $A^* A$ is invertible exactly when the columns of $A$ are independent.
One direction holds because $A^* A x = 0$ forces $\norm{Ax}^2 = x^* A^* A x = 0$, and the other because a dependence $Ax = 0$ with $x \ne 0$ also gives $A^* A x = 0$.

### What it gives you

For a line $\mathbb{K} a$ with $a \ne 0$, part 4 with $k = 1$ gives the matrix $\frac{a a^*}{a^* a}$, which is $\frac{a a^{\mathsf{T}}}{a^{\mathsf{T}} a}$ in $\R^n$.
The map $I - P$ is the orthogonal projection onto $U^\perp$, and the [[Pythagorean theorem|0BVTDM872V]] splits the length as $\norm{v}^2 = \norm{Pv}^2 + \norm{v - Pv}^2$.
When $V$ is finite-dimensional, the trace of $P$ is $\dim U$, because $\operatorname{tr}(Q Q^*) = \operatorname{tr}(Q^* Q) = \operatorname{tr}(I_k) = k$.

For $v \in U$ we have $Pv = v$, so part 3 becomes the [[expansion in an orthogonal set|Q6DE7QVZ24]].
Part 3 for a general $v$ is also recorded on its own as the [[projection formula for an orthogonal basis|6ARG1JYE34]].

### The matrix does not depend on the basis

Two bases of $U$ give matrices $A$ and $A' = A G$ with $G$ an invertible $k \times k$ matrix.
Then $A'^* A' = G^* (A^* A) G$, and
$$A' (A'^* A')^{-1} A'^* = A G \, G^{-1} (A^* A)^{-1} (G^*)^{-1} \, G^* A^* = A (A^* A)^{-1} A^*.$$
So the matrix depends only on $U$, as it must.
The factor $(A^* A)^{-1}$ is the inverse of the [[Gram matrix|00SPJSDT3Z]] of the columns, and it corrects for the angles and lengths of a basis that is not orthonormal.

### Generalizations

For a closed subspace $U$ of a Hilbert space with an orthonormal basis $(e_i)$, part 2 holds with an infinite sum that converges in norm.
The partial sum of degree $N$ of a [[Fourier series|G12KXDHPPS]] is the projection onto the trigonometric polynomials of degree at most $N$, and [[the polynomial and Fourier example|899D63WW04]] computes such projections.
With the [[Moore-Penrose pseudoinverse|0YY8VX28JR]] $A^+$, the projection onto the column space of any matrix $A$ is $A A^+$, with no condition on the columns.

## Explanations

### L1 human

To project onto a subspace whose axes are perpendicular and of unit length, project onto each axis and add the results.
If the axes are perpendicular but longer than one, divide each piece by the squared length of its axis.
If the axes are not perpendicular, this rule fails, and the matrix formula corrects for the angles between them.

### L2 human

We find the matrix of the projection onto the line through $a = (1, 2, 2)$ in $\R^3$.
Here $A = a$ is a $3 \times 1$ matrix, and its one column is independent because $a \ne 0$.
The factor in the middle is a number:
$$a^{\mathsf{T}} a = 1 + 4 + 4 = 9.$$
So part 4 gives
$$P = \frac{1}{9} a a^{\mathsf{T}} = \frac{1}{9} \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}.$$
For $v = (1, 1, 1)$ we get $a^{\mathsf{T}} v = 5$ and $P v = \frac{5}{9}(1, 2, 2)$, and [[the line example|VM9N7J68FW]] checks the error.
The same formula with more columns solves [[least squares|0BYTQ4X1HC]] problems: $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} b$ is the point of the column space closest to $b$.
Watch out: do not cancel the product to $I$, since $A$ is not square and has no inverse.

### L3 human

Part 1 says that $P$ is an idempotent with $\ker P = (\im P)^\perp$, and together with the [[self-adjoint characterization|ZJRJNWJ8V1]] this identifies orthogonal projections inside the algebra of operators.
Parts 2 to 5 are one formula seen in different coordinates: when $V$ is finite-dimensional, in an orthonormal basis of $U$ extended to one of $V$, the matrix of $P$ is diagonal with $k$ ones and the rest zeros.
In numerical work one never forms $(A^{\mathsf{T}} A)^{-1}$; one orthonormalizes the columns by a [[QR decomposition|0ERWG4NXQ9]] and uses part 5.
