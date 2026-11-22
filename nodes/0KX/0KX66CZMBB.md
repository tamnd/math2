---
tag: 0KX66CZMBB
kind: concept
name: Positive definite matrix
msc: [15B57, 15A63]
topics: [SS4EVPKT3A]
audience: ug1
specializes: [01MMVW8CKC]
uses: [0QQCG3JWJ4, 0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Extension for non-Hermitian square matrices
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780321982384
inventory: [2Z8JQJ3GJZ]
---

## Summary

A positive definite matrix is the matrix version of a positive number.
Put the same nonzero vector on both sides of it, and the result is always a positive number.
Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]], so that $A^* = A$, where $A^*$ is the [[conjugate transpose|0DXKE10PHF]].
Then $A$ is *positive definite* when
$$x^* A x > 0 \qquad \text{for every } x \in \C^n \text{ with } x \ne 0.$$
For a real matrix, the condition is that $A$ is [[symmetric|0VR671PHE5]] and $x^{\mathsf{T}} A x > 0$ for every nonzero $x \in \R^n$.
The [[formal definition|0QQCG3JWJ4]] states both cases.
On a finite-dimensional inner product space $V$, a [[self-adjoint operator|0NEGN5CRSC]] $T$ is positive definite when $\ip{Tv}{v} > 0$ for every $v \ne 0$, and its matrix in an orthonormal basis is a positive definite matrix.

## Motivation

For a number $a > 0$, the function $x \mapsto a x^2$ is positive at every $x \ne 0$, and its graph is a parabola that opens upward.
In several variables, the function $x \mapsto x^{\mathsf{T}} A x = \sum_{i, j} a_{ij} x_i x_j$ takes its place, and we want to know when it is positive at every nonzero vector.
The answer decides many questions at once.
A formula $\ip{x}{y} = y^{\mathsf{T}} A x$ is an [[inner product|0NB0AWGJBW]] on $\R^n$ exactly when $A$ is symmetric and positive definite.
At a critical point of a smooth function, a positive definite [[Hessian matrix|0693Y2METT]] gives a strict local minimum.
In least squares, the matrix $A^{\mathsf{T}} A$ of the [[normal equations|4D7MRG4D91]] is positive definite when the columns of $A$ are independent, and so the normal equations have exactly one solution.

The idea returns throughout the rest of linear algebra.
Positive definite matrices have positive square roots, they factor as $LL^*$ by Cholesky, and the matrix $A^* A$ behind the singular value decomposition is positive definite when $A$ has independent columns.
In statistics, the [[covariance matrix|0V7G6WMFK0]] of a random vector is positive definite when no linear combination of its entries is constant.

## Notation

Books write $A \succ 0$ or $A > 0$.
Watch the second form: some books use $A > 0$ for a matrix with positive entries, which is a different idea.
We write $A \succ B$ when $A - B \succ 0$, and this is the strict part of the [[Loewner order|9G9S92T1VJ]].
In Lean's Mathlib the predicate is `Matrix.PosDef A`, and its definition includes the condition that $A$ is Hermitian.
Books also differ about symmetry.
Most books ask a positive definite matrix to be Hermitian, or real symmetric in the real case, and so do we.
Some books call a real matrix positive definite as soon as $x^{\mathsf{T}} A x > 0$ for all $x \ne 0$, with no symmetry, so check the convention before you use a theorem from a book.

## Remarks

### A first test by completing the square

Take $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, which is real and symmetric.
For $x = (x_1, x_2)$, multiply out the form:
$$x^{\mathsf{T}} A x = 2x_1^2 - 2x_1 x_2 + 2x_2^2 = x_1^2 + x_2^2 + (x_1 - x_2)^2.$$
Check: at $x = (1, 1)$ the left side is $2 - 2 + 2 = 2$ and the right side is $1 + 1 + 0 = 2$.
A sum of three squares is never negative, and it is zero only when $x_1 = 0$, $x_2 = 0$ and $x_1 = x_2$, that is, only at $x = 0$.
So $A$ is positive definite.
[[The tridiagonal 3 by 3 matrix|RSQW92W4PD]] with $2$ on the diagonal and $-1$ beside it is the next size of the same matrix, and the same trick works there.

### Where positive definite matrices come from

Most positive definite matrices in practice have the form $B^{\mathsf{T}} B$.
For $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}$ we get
$$B^{\mathsf{T}} B = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad x^{\mathsf{T}} B^{\mathsf{T}} B x = \norm{Bx}^2 = x_1^2 + (x_1 + x_2)^2 + x_2^2.$$
The columns of $B$ are independent, so $Bx \ne 0$ for $x \ne 0$, and the form is positive.
This is the [[Gram matrix theorem|0AM050KCAW]]: $B^* B$ is positive definite exactly when the columns of $B$ are independent.
The [[Hilbert matrix|2DTWB6F5TA]] $\left( \frac{1}{i + j - 1} \right)$ is an example of the same kind, since its entry $(i, j)$ is $\int_0^1 t^{i-1} t^{j-1} \, dt$, the inner product of two independent functions.
For $n = 2$ it is $\begin{pmatrix} 1 & 1/2 \\ 1/2 & 1/3 \end{pmatrix}$, with determinant $\tfrac{1}{3} - \tfrac{1}{4} = \tfrac{1}{12} > 0$.
[[The 3 by 3 Cholesky example|M3YVJ6CFJ5]] is positive definite for the same reason, as $LL^{\mathsf{T}}$ with $L$ invertible.

### What it is not

[[The all-ones matrix|YAAQD2E1BZ]] $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has the form $(x_1 + x_2)^2$, which is $0$ at the nonzero vector $(1, -1)$.
It fails only the strict inequality, so it is [[positive semidefinite|01MMVW8CKC]] but not positive definite.
[[The matrix with entries 1, 2, 2, 1|N9TX4J2W4R]] has only positive entries, but its form is $1 - 4 + 1 = -2$ at $(1, -1)$, so positivity of the form fails badly.
[[The matrix with rows (1, -3) and (0, 1)|VB4AQ8TKVP]] is not symmetric, so it fails the first condition, and its form is also $-1$ at $(1, 1)$.
Finally, $-I_n$ is Hermitian, but its form is $-\norm{x}^2 < 0$.

### The rules you can use

The main tests are equivalent forms of the definition.
A Hermitian matrix is positive definite exactly when all its eigenvalues are positive, by the [[eigenvalue test|0HYC2RHD3M]], and exactly when all its leading principal minors are positive, by [[Sylvester's criterion|0WKEF78PMV]].
It is positive definite exactly when it has a [[Cholesky decomposition|0WKG8CYY6A]] $A = LL^*$ with $L$ lower triangular and with positive diagonal.

Several properties follow at once.
The determinant and the trace are positive, as the product and the sum of positive eigenvalues, so $A$ is invertible, and $A^{-1}$ is positive definite with eigenvalues $1/\lambda_i$.
Each diagonal entry is positive, because $a_{ii} = e_i^* A e_i$ for the standard basis vector $e_i$.
If $P$ is invertible, then $P^* A P$ is positive definite, because $x^* P^* A P x = (Px)^* A (Px)$ and $Px \ne 0$ for $x \ne 0$.
Sums and positive multiples of positive definite matrices are positive definite, so they form a convex cone.
Each positive definite matrix has a unique positive definite [[square root|EQ98KW1ZN4]].

### Watch out

A non-symmetric real matrix can make the form positive.
For $M = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$, the form is $x_1^2 + x_1 x_2 - x_1 x_2 + x_2^2 = x_1^2 + x_2^2$, which is positive for $x \ne 0$.
With the convention here, $M$ is still not positive definite, because it is not symmetric.
The form of any real $M$ equals the form of its symmetric part $\tfrac12 (M + M^{\mathsf{T}})$, which here is $I_2$.
Theorems such as Sylvester's criterion apply to that symmetric part, and not to $M$.

A second trap is to test the form at a few vectors only.
The values at $e_1, \dots, e_n$ are the diagonal entries, so positive values there say only that the diagonal is positive, and the matrix with entries $1, 2, 2, 1$ shows that this is not enough.

### Operators and the word "positive"

On a finite-dimensional inner product space, the definition is about a self-adjoint operator $T$ and the numbers $\ip{Tv}{v}$.
Watch the words here.
Axler and many books on operators call $T$ *positive* when $\ip{Tv}{v} \ge 0$, so a [[positive operator|77020CY5ZW]] matches a positive *semidefinite* matrix.
Such books call the strict condition, $\ip{Tv}{v} > 0$ for $v \ne 0$, positive definite or *strictly positive*.
So read "positive" as "$\ge 0$" in a book on operators unless it says otherwise.

### History

Gauss's Disquisitiones Arithmeticae of 1801 already sorted binary quadratic forms into definite and indefinite ones.
The test by leading minors carries the name of James Joseph Sylvester.

### Try it

First, decide whether $\begin{pmatrix} 3 & 2 \\ 2 & 2 \end{pmatrix}$ is positive definite.
Completing the square gives $3x_1^2 + 4x_1 x_2 + 2x_2^2 = 3 \left( x_1 + \tfrac23 x_2 \right)^2 + \tfrac23 x_2^2$, which is positive for $x \ne 0$, so the answer is yes.

Second, find all real $t$ for which $\begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}$ is positive definite.
Sylvester's criterion asks for $1 > 0$ and $1 - t^2 > 0$, so the answer is $-1 < t < 1$.

## Explanations

### L1 human

A positive definite matrix acts like a positive number.
For a positive number $a$, the value $a x^2$ is positive for every $x$ that is not zero.
For a matrix $A$, we put a vector $x$ on both sides and get one number, $x^{\mathsf{T}} A x$.
The matrix is positive definite when this number is positive for every nonzero vector.
For $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ the number is $2x_1^2 + 3x_2^2$, which is positive unless $x_1 = x_2 = 0$.
The graph of such a function is a bowl that opens upward.

### L2 human

Here is a typical use: find the minimum of $f(x, y) = x^2 + xy + y^2 - 3x$.
The gradient is zero when
$$2x + y - 3 = 0, \qquad x + 2y = 0,$$
so $x = -2y$, then $-3y = 3$, and the only critical point is $(2, -1)$.
Check: $2 \cdot 2 - 1 - 3 = 0$ and $2 - 2 = 0$.
The Hessian matrix is $H = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, and it is positive definite, since its leading minors are $2$ and $3$.
Because $f$ is quadratic, Taylor's formula is exact:
$$f(2 + h_1, -1 + h_2) = f(2, -1) + \tfrac12 h^{\mathsf{T}} H h = -3 + h_1^2 + h_1 h_2 + h_2^2.$$
So $f$ has its smallest value $-3$ at $(2, -1)$ and nowhere else.
This is the typical use: positive definiteness of a Hessian turns a critical point into a strict minimum.
Watch out: if the Hessian is only semidefinite, the second derivative test gives no answer.

### L3 human

The positive definite $n \times n$ matrices form an open convex cone in the real vector space of Hermitian matrices, and it is the interior of the closed cone of [[positive semidefinite matrices|01MMVW8CKC]].
The group $GL_n(\C)$ acts on the cone by $A \mapsto P^* A P$ with one orbit, since every positive definite $A$ is $LL^*$ by Cholesky.
The stabilizer of $I$ is the [[unitary group|0R9R0Y1HDK]] $U(n)$, so the cone is the homogeneous space $GL_n(\C) / U(n)$.
Positive definite matrices are the same as inner products on $\C^n$, and [[simultaneous diagonalization with a positive definite matrix|K559AQ9H67]] is the spectral theorem for a second inner product.
In functional analysis the same idea gives positive operators and positive definite kernels, and in probability it gives the covariance matrices of nondegenerate random vectors.
