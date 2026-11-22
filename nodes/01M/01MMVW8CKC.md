---
tag: 01MMVW8CKC
kind: concept
name: Positive semidefinite matrix
msc: [15B57, 15A63]
topics: [SS4EVPKT3A]
audience: ug1
specializes: [0P17NGQQMQ]
uses: [0880F9EQCP, 0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Decomposition
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780521839402
    locator: Chapter 7
inventory: [8XQP955FKQ]
---

## Summary

A positive semidefinite matrix is the matrix version of a number that is greater than or equal to zero.
The form $x^* A x$ is never negative, but it may be zero at a nonzero vector.
Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].
Then $A$ is *positive semidefinite* when
$$x^* A x \ge 0 \qquad \text{for every } x \in \C^n.$$
For a real matrix, the condition is that $A$ is [[symmetric|0VR671PHE5]] and $x^{\mathsf{T}} A x \ge 0$ for every $x \in \R^n$.
The [[formal definition|0880F9EQCP]] states both cases, and every [[positive definite matrix|0KX66CZMBB]] is positive semidefinite.

## Motivation

Many matrices that come from data are positive semidefinite without being positive definite, so we need a theory that allows the value $0$.
The [[Gram matrix|00SPJSDT3Z]] of a list of vectors is positive semidefinite, and it is definite only when the vectors are independent.
A [[covariance matrix|0V7G6WMFK0]] $C$ is positive semidefinite, because $v^{\mathsf{T}} C v$ is the variance of the combination $v_1 X_1 + \dots + v_n X_n$, and a variance is never negative.
The matrices $A^* A$ and $A A^*$ are positive semidefinite for every matrix $A$, and the [[singular values|09VMDSRXWJ]] of $A$ are the square roots of the eigenvalues of $A^* A$.
Later, the positive semidefinite square root gives the polar decomposition, and the same idea for operators on spaces of functions gives the positive operators of functional analysis.

## Notation

Books write $A \succeq 0$ or $A \ge 0$, and $A \succeq B$ means $A - B \succeq 0$, which is the [[Loewner order|9G9S92T1VJ]].
Mathlib writes `Matrix.PosSemidef A`, and its definition includes the condition that $A$ is Hermitian.
As for positive definite matrices, some books do not ask for symmetry in the real case, and we always ask for it.
Books on operators often say *positive operator* for the semidefinite case, so "positive" there means "$\ge 0$".

## Remarks

### First examples

The zero matrix is positive semidefinite, since its form is $0$ everywhere, and it is not positive definite.
[[The all-ones matrix|YAAQD2E1BZ]] $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has the form $(x_1 + x_2)^2 \ge 0$, and the form is $0$ at $(1, -1)$.
An [[orthogonal projection|0B8KZRT28M]] $P$ is positive semidefinite, because $P^* = P = P^2$ gives
$$x^* P x = x^* P^* P x = \norm{Px}^2 \ge 0.$$
For example, $\operatorname{diag}(1, 0)$ projects $\R^2$ onto the first axis, and its form is $x_1^2$.
Every positive definite matrix, such as [[the tridiagonal example|RSQW92W4PD]] or [[the matrix of the square root example|QTV6Y0710E]], is also positive semidefinite.

### Gram matrices and covariance matrices

For every $m \times n$ matrix $B$, the matrix $B^* B$ is positive semidefinite, since $x^* B^* B x = \norm{Bx}^2$.
This is the first part of [[the Gram matrix theorem|0AM050KCAW]], and its converse says that every positive semidefinite matrix has this form.

A covariance matrix shows where the zero values come from.
Let $X$ be a random variable with variance $1$, and let $Y = X$.
The covariance matrix of $(X, Y)$ is the all-ones matrix, and
$$v^{\mathsf{T}} C v = \operatorname{Var}(v_1 X + v_2 Y) = (v_1 + v_2)^2 \operatorname{Var}(X) = (v_1 + v_2)^2.$$
At $v = (1, -1)$ the combination is $X - Y = 0$, a constant with variance $0$.
So a covariance matrix is singular exactly when some nontrivial combination of the variables is constant.

### What it is not

[[The matrix diag(0, -1)|9ZQ1GV2F0G]] is symmetric, but its form is $-1$ at $e_2 = (0, 1)$.
[[The matrix with entries 1, 2, 2, 1|N9TX4J2W4R]] has only positive entries, and still its form is $-2$ at $(1, -1)$, so nonnegative entries do not give semidefiniteness.
The matrix $\operatorname{diag}(1, -1)$ is Hermitian with form $x_1^2 - x_2^2$, which takes both signs, and such a matrix is called *indefinite*.

### The rules you can use

A Hermitian matrix is positive semidefinite exactly when all its eigenvalues are nonnegative, by [[the eigenvalue test|0HYC2RHD3M]].
It is positive semidefinite exactly when all its principal minors are nonnegative, by part 2 of [[Sylvester's criterion|0WKEF78PMV]].
It has a unique positive semidefinite [[square root|EQ98KW1ZN4]].
A positive semidefinite matrix is positive definite exactly when it is invertible, since both say that $0$ is not an eigenvalue.

If $A \succeq 0$ and $P$ is any $n \times k$ matrix, then $P^* A P \succeq 0$, because $y^* P^* A P y = (Py)^* A (Py) \ge 0$.
Taking for $P$ a selection of columns of $I_n$ shows that every principal submatrix is positive semidefinite.
So each diagonal entry is nonnegative, and each $2 \times 2$ principal minor gives $\abs{a_{ij}}^2 \le a_{ii} a_{jj}$.
In particular, a zero diagonal entry $a_{ii} = 0$ forces the whole row $i$ and column $i$ to be zero.
Sums and nonnegative multiples of positive semidefinite matrices are positive semidefinite, so they form a closed convex cone.

### Watch out

The leading minors are not enough for semidefiniteness.
The matrix $\operatorname{diag}(0, -1)$ has leading minors $0$ and $0$, both nonnegative, but it is not semidefinite.
The principal minor $a_{22} = -1$ shows the failure, so check every principal minor, or use the eigenvalues.

Do not expect a positive semidefinite matrix to be invertible: the all-ones matrix has determinant $0$.
A zero value of the form does not force $x = 0$, but it does force $Ax = 0$.
Indeed, $x^* A x = \norm{A^{1/2} x}^2$, so $x^* A x = 0$ gives $A^{1/2} x = 0$ and then $Ax = A^{1/2} A^{1/2} x = 0$.

### History

In 1909 Mercer published his theorem on continuous kernels of positive type, the analogue of positive semidefinite matrices for integral operators.
For a continuous symmetric kernel $k(s, t)$, this condition is equivalent to asking that every matrix $\bigl( k(s_i, s_j) \bigr)$ built from finitely many points is positive semidefinite.

### Try it

First, decide whether $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ is positive semidefinite or positive definite.
The form is $x_1^2 + 4x_1 x_2 + 4x_2^2 = (x_1 + 2x_2)^2 \ge 0$, and it is $0$ at $(2, -1)$, so the matrix is semidefinite but not definite.

Second, find all real $t$ for which $\begin{pmatrix} t & 1 \\ 1 & t \end{pmatrix}$ is positive semidefinite.
The principal minors are $t$, $t$ and $t^2 - 1$, and all are nonnegative exactly when $t \ge 1$.

## Explanations

### L1 human

A positive semidefinite matrix never gives a negative number $x^{\mathsf{T}} A x$, but it may give $0$ for a nonzero vector.
For example, $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ gives $(x_1 + x_2)^2$.
This is never negative, and it is $0$ for $x = (1, -1)$.
The graph of such a function is a bowl or a valley with a flat floor, and never a saddle.

### L2 human

Here is a typical use: the least-squares function is convex.
For a matrix $A$ and a vector $b$, put $f(x) = \norm{Ax - b}^2$.
Expanding gives
$$f(x) = x^{\mathsf{T}} A^{\mathsf{T}} A x - 2 b^{\mathsf{T}} A x + b^{\mathsf{T}} b,$$
and the Hessian of $f$ is the constant matrix $2 A^{\mathsf{T}} A$.
That matrix is positive semidefinite for every $A$, so $f$ is convex, and every critical point of $f$ is a minimum.
If the columns of $A$ are dependent, $A^{\mathsf{T}} A$ is singular, and the minimum is reached along a whole affine subspace.
Watch out: to prove semidefiniteness from minors, you need every principal minor, not only the leading ones.

### L3 human

The positive semidefinite $n \times n$ matrices form a closed convex cone in the real space of Hermitian matrices.
The cone is self-dual for the trace inner product $\ip{A}{B} = \tr(AB)$: a Hermitian $B$ has $\tr(AB) \ge 0$ for every $A \succeq 0$ exactly when $B \succeq 0$.
Its interior is the cone of positive definite matrices, and its boundary is the set of singular positive semidefinite matrices.
A positive semidefinite matrix of rank $r$ is the Gram matrix of $n$ vectors that span an $r$-dimensional space.
In functional analysis the same notion gives positive operators and positive definite kernels, and in optimization it gives semidefinite programming.
