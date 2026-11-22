---
tag: 7JJE96MZQY
kind: concept
name: Computing eigenvalues and eigenvectors by hand
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
uses: [0BQAA2BK3Q, 0N6960W0BV, 0G0RFPG8HR, 0VSSPAFM2C]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenvalues and eigenvectors of a matrix
  - book: isbn:9780321982384
  - book: isbn:9781733146678
    locator: Chapter 6
  - url: https://understandinglinearalgebra.org/
    locator: Chapter 4
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: History
  - url: https://en.wikipedia.org/wiki/QR_algorithm
    locator: lead section
---

## Summary

For a small matrix you can find every eigenvalue and eigenvector with pencil and paper, by splitting the problem into a polynomial equation and a few linear systems.
Let $A$ be an $n \times n$ matrix over a field $F$.
First compute the [[characteristic polynomial|0VSSPAFM2C]] $p_A(t) = \det(tI - A)$, and find its roots in $F$; these are the [[eigenvalues|0BQAA2BK3Q]].
Then, for each eigenvalue $\lambda$, solve the homogeneous system
$$(A - \lambda I)\, x = 0$$
by row reduction.
Its nonzero solutions are the [[eigenvectors|0N6960W0BV]] for $\lambda$, and its solution space is the [[eigenspace|0G0RFPG8HR]].
Every answer can be checked by computing $Av$ and $\lambda v$.

## Motivation

The equation $Av = \lambda v$ has two unknowns, the number $\lambda$ and the vector $v$, and it is not linear in the two together.
The method separates them.
The determinant removes $v$ and leaves one polynomial equation in $\lambda$, by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
Once $\lambda$ is fixed, the equation for $v$ is linear, and row reduction solves it.

Hand computation is how you learn what eigenvalues are, and it is how exercises, examples in physics and symbolic problems with parameters are solved.
Later sub-areas use the same steps to diagonalize a matrix, to compute its powers and to solve systems of linear differential equations.

## Notation

We use $p_A(t) = \det(tI - A)$, which is monic.
With the convention $\det(A - tI)$ of some textbooks the roots are the same, and only the sign of the polynomial changes for odd $n$.
For the linear systems either $A - \lambda I$ or $\lambda I - A$ works, since the two have the same kernel.

## Remarks

### The method step by step

1. Compute $p_A(t) = \det(tI - A)$, by expanding along a row or a column with many zeros.
2. Check $p_A$: the coefficient of $t^{n-1}$ is $-\operatorname{tr} A$, the constant term is $(-1)^n \det A$, and for $n = 3$ the coefficient of $t$ is the sum of the three $2 \times 2$ principal minors, by the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
3. Find the roots of $p_A$ in $F$; for an integer polynomial, each integer root divides the constant term.
4. For each root $\lambda$, row reduce $A - \lambda I$ and write a basis of its kernel; the number of free variables is the [[geometric multiplicity|099TWVJ909]].
5. Check each basis vector $v$ by computing $Av = \lambda v$, and check that the eigenvalues add up to $\operatorname{tr} A$ when $p_A$ splits.

### A 2 by 2 example

Take $A = \begin{pmatrix} 5 & 4 \\ 1 & 2 \end{pmatrix}$.
The polynomial is
$$p_A(t) = (t - 5)(t - 2) - 4 = t^2 - 7t + 6 = (t - 1)(t - 6).$$
Check: $\operatorname{tr} A = 7$ and $\det A = 10 - 4 = 6$.
For $\lambda = 6$, the matrix $A - 6I$ has the rows $(-1, 4)$ and $(1, -4)$, so $x_1 = 4 x_2$ and $v = (4, 1)^{\mathsf{T}}$.
For $\lambda = 1$, the matrix $A - I$ has the rows $(4, 4)$ and $(1, 1)$, so $x_1 = -x_2$ and $w = (1, -1)^{\mathsf{T}}$.
Check: $Av = (24, 6)^{\mathsf{T}} = 6v$ and $Aw = (1, -1)^{\mathsf{T}} = w$.
The [[symmetric matrix with rows (2, 1) and (1, 2)|Z6K3QPP7DY]] is another case worked in full.

### A 3 by 3 example

Take
$$A = \begin{pmatrix} 4 & 0 & 1 \\ -2 & 1 & 0 \\ -2 & 0 & 1 \end{pmatrix}.$$
In $tI - A$ the second column has the single entry $t - 1$, so expand along it:
$$p_A(t) = (t - 1) \det \begin{pmatrix} t - 4 & -1 \\ 2 & t - 1 \end{pmatrix} = (t - 1)(t^2 - 5t + 6) = (t - 1)(t - 2)(t - 3).$$
Check: $1 + 2 + 3 = 6 = \operatorname{tr} A$, and $1 \cdot 2 \cdot 3 = 6 = \det A$.
For $\lambda = 1$, the second column of $A$ is $e_2$, so $v_1 = (0, 1, 0)$.
For $\lambda = 2$, the rows of $A - 2I$ give $2x_1 + x_3 = 0$ and $-2x_1 - x_2 = 0$, so $v_2 = (1, -2, -2)$.
For $\lambda = 3$, they give $x_1 + x_3 = 0$ and $-2x_1 - 2x_2 = 0$, so $v_3 = (1, -1, -1)$.
Check: $A v_2 = (4 - 2, -2 - 2, -2 - 2) = 2 v_2$ and $A v_3 = (4 - 1, -2 - 1, -2 - 1) = 3 v_3$.
A [[3 by 3 matrix with a defective eigenvalue|18XQY67HMS]] shows what happens when a double root has only a line of eigenvectors.

### Complex eigenvalues of a real matrix

[[A real matrix with complex eigenvalues|XGRN8RY29P]] is $A = \begin{pmatrix} 3 & -2 \\ 4 & -1 \end{pmatrix}$, with $p_A(t) = t^2 - 2t + 5$.
The discriminant is $4 - 20 = -16$, so the roots are $1 \pm 2i$, and over $\mathbb{R}$ the matrix has no eigenvalue.
Over $\mathbb{C}$ the same steps work: the first row of $A - (1 + 2i)I$ is $(2 - 2i, -2)$, which gives $v = (1, 1 - i)$.
For a real matrix, the conjugate $\bar v$ is then an eigenvector for the conjugate eigenvalue, so one linear system gives both.

### Triangular matrices

When $A$ is triangular, $tI - A$ is triangular too, and the [[determinant of a triangular matrix|0K1KKMFHYH]] gives $p_A(t) = \prod_i (t - a_{ii})$.
So the eigenvalues are the diagonal entries, each counted as often as it appears.
The eigenvectors still need the linear systems, as [[a triangular matrix|NHR1K0GPS1]] shows: there the diagonal entry $2$ appears twice, but its eigenspace is only a line.

### Watch out

Row reduction does not keep eigenvalues, so never reduce $A$ first and then read off a diagonal.
For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $1$ and $-1$, but one row swap turns it into $I_2$, whose only eigenvalue is $1$; see [[row reduction changes the eigenvalues|M1XGWNT48M]].
The diagonal of a matrix that is not triangular does not give its eigenvalues either.

If $A - \lambda I$ row reduces to the identity, then the only solution is $x = 0$, and $\lambda$ was not a root.
That signals an arithmetic error in step 1 or step 3.
Also, when an eigenspace has dimension $2$ or more, give a basis of it, not one vector.

### History

Von Mises published the power method in 1929, the first numerical algorithm for eigenvalues and eigenvectors.
Francis and Kublanovskaya found the QR algorithm independently around 1961.
Numerical software uses methods of this kind and does not form $p_A$, since for $n \ge 5$ its roots have no general formula in radicals.

### Try it

First, find the eigenvalues and eigenvectors of $\begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix}$.
The trace is $4$ and the determinant is $-5$, so $p(t) = (t - 5)(t + 1)$; the eigenvectors are $(1, 1)$ for $5$ and $(2, -1)$ for $-1$.

Second, find an eigenvector of $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{C}$ for the eigenvalue $i$.
The first row of $A - iI$ gives $-i x_1 - x_2 = 0$, so $v = (1, -i)$, and indeed $Av = (i, 1) = i v$.

## Explanations

### L1 human

We look for numbers $\lambda$ and nonzero arrows $v$ with $Av = \lambda v$.
First we find the numbers: they are the values that make $\det(\lambda I - A)$ zero.
Then, for each number, we solve a small system of equations to find the arrows.
For the matrix with rows $(5, 4)$ and $(1, 2)$ this gives the number $6$ with the arrow $(4, 1)$, and the number $1$ with the arrow $(1, -1)$.
At the end we multiply $A$ by each arrow to check the answer.

### L2 human

Here is a problem with a trap: find all eigenvectors of $A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}$.
The trace is $4$ and the determinant is $3 + 1 = 4$, so
$$p_A(t) = t^2 - 4t + 4 = (t - 2)^2.$$
The only eigenvalue is $2$, as a double root.
Now solve $(A - 2I)x = 0$:
$$A - 2I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix},$$
and both rows say $x_1 + x_2 = 0$, so the eigenvectors are the nonzero multiples of $(1, -1)$.
Check: $A(1, -1)^{\mathsf{T}} = (2, -2)^{\mathsf{T}} = 2 (1, -1)^{\mathsf{T}}$.
The double root gives only one line of eigenvectors, so this matrix has no basis of eigenvectors.
The lesson is that the multiplicity of a root does not tell you how many independent eigenvectors there are; only the linear system does.

### L3 human

The hand method reduces the eigenvalue problem to the roots of a polynomial, and by the Abel-Ruffini theorem these have no general formula in radicals for $n \ge 5$.
The reduction also goes the other way: every monic polynomial is the characteristic polynomial of its [[companion matrix|0ZCWPNZTQ3]], so finding eigenvalues is exactly as hard as finding roots.
Numerical methods therefore work with the matrix itself, by similarity transformations that converge to a triangular form.
Computer algebra systems, which work with exact numbers, still follow the hand method: they factor $p_A$ and then solve the linear systems.
