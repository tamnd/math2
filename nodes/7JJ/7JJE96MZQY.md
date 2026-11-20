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

For a small square matrix $A$ over a field $F$, the eigenvalues and eigenvectors can be computed by hand in three stages.
First compute the [[characteristic polynomial|0VSSPAFM2C]] $p_A(t) = \det(tI - A)$.
Then find its roots in $F$; these are the [[eigenvalues|0BQAA2BK3Q]].
For each eigenvalue $\lambda$, solve the homogeneous system $(A - \lambda I)x = 0$; its nonzero solutions are the [[eigenvectors|0N6960W0BV]], and its solution space is the [[eigenspace|0G0RFPG8HR]].
Every result can be checked by computing $Av$ and $\lambda v$.

## Motivation

The definition of an eigenvalue has two unknowns, $\lambda$ and $v$, in the nonlinear equation $Av = \lambda v$.
The method separates them.
The determinant removes $v$ and leaves one polynomial equation for $\lambda$.
For a fixed $\lambda$, the equation for $v$ is linear and is solved by row reduction.

## Notation

The method uses $p_A(t) = \det(tI - A)$.
With the convention $\det(A - tI)$, the roots are the same, and only the sign of the polynomial changes for odd $n$.

## Remarks

### Examples

- [[The symmetric matrix with rows (2, 1) and (1, 2)|Z6K3QPP7DY]]: $p_A = (t - 1)(t - 3)$, with eigenvectors $(1, -1)^{\mathsf{T}}$ and $(1, 1)^{\mathsf{T}}$.
- [[A real matrix with complex eigenvalues|XGRN8RY29P]]: $p_A = t^2 - 2t + 5$ has the roots $1 \pm 2i$, and the eigenvectors are complex conjugates.
- [[A 3 by 3 matrix with a defective eigenvalue|18XQY67HMS]]: $p_A = (t - 1)(t - 2)^2$, and the eigenspace for $2$ is only a line.
- [[A triangular matrix|NHR1K0GPS1]]: the eigenvalues are the diagonal entries, but the eigenvectors still need the linear systems.

### Non-examples

- [[Row reduction changes the eigenvalues|M1XGWNT48M]]: the echelon form of $A$ is not similar to $A$ in general, so its diagonal does not give the eigenvalues of $A$.
- Computing the roots of $p_A$ by hand is not a practical method for large $n$. Numerical software uses the QR algorithm and never forms $p_A$.

### Basic properties

The method has these steps.

1. Compute $p_A(t) = \det(tI - A)$, for example by cofactor expansion along a row or column with many zeros.
2. Check $p_A$ by a second method: the coefficient of $t^{n-1}$ must be $-\operatorname{tr} A$ and the constant term must be $(-1)^n \det A$. For $n = 3$, the coefficient of $t$ is the sum of the three $2 \times 2$ principal minors, by the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
3. Find the roots of $p_A$ in $F$. Integer roots of an integer polynomial divide the constant term.
4. For each root $\lambda$, row reduce $A - \lambda I$. The number of free variables is the [[geometric multiplicity|099TWVJ909]].
5. Write a basis of the solution space. Each basis vector is an eigenvector.
6. Check each eigenvector $v$ by computing $Av$ and $\lambda v$.
7. Check the eigenvalues: their sum with multiplicity is $\operatorname{tr} A$ and their product is $\det A$, when $p_A$ splits.

For a triangular matrix, step 1 gives $p_A = \prod_i (t - a_{ii})$ at once, by the [[determinant of a triangular matrix|0K1KKMFHYH]].
For a real matrix, nonreal roots come in conjugate pairs, and so do their eigenvectors.
If $A - \lambda I$ row reduces to the identity, then $\lambda$ is not a root; this signals an error in step 1 or step 3.

### History

Von Mises published the power method in 1929, the first numerical algorithm for eigenvalues and eigenvectors.
Francis and Kublanovskaya found the QR algorithm independently, and it is now one of the most popular methods.

### Common errors

- Row reducing $A$ first and then computing the eigenvalues of the reduced matrix.
- Solving $(A - \lambda I)x = 0$ and finding only $x = 0$. Then $\lambda$ was not a root, and step 1 or step 3 has an error.
- Expanding $\det(tI - A)$ with a sign error in a cofactor. The check in step 2 finds most of these errors.
- Giving one eigenvector when the eigenspace has dimension $2$ or more.

## Explanations

### L1 human

We look for numbers $\lambda$ and nonzero vectors $v$ with $Av = \lambda v$.
First we find the numbers: they make $\det(\lambda I - A)$ equal to zero.
Then, for each number, we solve a linear system to find the vectors.
At the end we multiply $A$ by each vector to check the answer.

### L2 human

We compute the eigenvalues and eigenvectors of $A = \begin{pmatrix} 5 & 4 \\ 1 & 2 \end{pmatrix}$.

1. $p_A(t) = (t - 5)(t - 2) - 4 = t^2 - 7t + 6$.
2. Check: $\operatorname{tr} A = 7$ and $\det A = 10 - 4 = 6$.
3. $p_A(t) = (t - 1)(t - 6)$, so the eigenvalues are $1$ and $6$.
4. For $\lambda = 6$: $A - 6I$ has the rows $(-1, 4)$ and $(1, -4)$, so $x_1 = 4 x_2$, and $v = (4, 1)^{\mathsf{T}}$.
5. Check: $Av = (20 + 4, 4 + 2)^{\mathsf{T}} = (24, 6)^{\mathsf{T}} = 6v$.
6. For $\lambda = 1$: $A - I$ has the rows $(4, 4)$ and $(1, 1)$, so $x_1 = -x_2$, and $w = (1, -1)^{\mathsf{T}}$.
7. Check: $Aw = (5 - 4, 1 - 2)^{\mathsf{T}} = (1, -1)^{\mathsf{T}} = 1 \cdot w$.

The typical use is in exercises with $n \le 4$ and in symbolic work.
A trap: an eigenvalue found with a sign error gives a matrix $A - \lambda I$ of full rank, so the only solution is $0$.

### L3 human

The hand method reduces the eigenvalue problem to the roots of a polynomial, and by the Abel-Ruffini theorem these have no general formula for $n \ge 5$.
Every monic polynomial is the characteristic polynomial of its [[companion matrix|0ZCWPNZTQ3]], so eigenvalue problems are as hard as root finding.
Numerical methods therefore work with the matrix, by similarity transformations that converge to a triangular form.
For exact arithmetic over $\mathbb{Q}$, computer algebra systems factor $p_A$ and then solve the linear systems, as in the hand method.
