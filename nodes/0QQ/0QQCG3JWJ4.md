---
tag: 0QQCG3JWJ4
kind: definition
name: Positive definite matrix
msc: [15B57, 15A63]
topics: [SS4EVPKT3A]
audience: ug1
defines: 0KX66CZMBB
uses: [0EKZCX4K3P, 0N28QN4CYA, 0EX045E2BP]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.PosDef
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Definitions
  - book: isbn:9783031410253
    locator: Chapter 7
inventory: [2Z8JQJ3GJZ]
---

## Definition

A positive definite matrix is a Hermitian matrix that gives a positive number $x^* A x$ for every nonzero vector $x$.
Let $A$ be an $n \times n$ complex [[Hermitian matrix|0EKZCX4K3P]], so that $A^* = A$, where $A^*$ is the [[conjugate transpose|0EX045E2BP]].
The matrix $A$ is *positive definite* when
$$x^* A x > 0 \qquad \text{for all } x \in \C^n \text{ with } x \ne 0.$$
A real $n \times n$ matrix $A$ is *positive definite* when it is [[symmetric|0N28QN4CYA]], $A^{\mathsf{T}} = A$, and $x^{\mathsf{T}} A x > 0$ for all $x \in \R^n$ with $x \ne 0$.

## Notation

We write $A \succ 0$.
In Mathlib the predicate is `Matrix.PosDef A`, and it includes the condition that $A$ is Hermitian.

## Remarks

The definition has two conditions, and each one has a job.
The Hermitian condition makes the number $x^* A x$ real, so that the inequality has a meaning.
Indeed, the conjugate of the $1 \times 1$ matrix $x^* A x$ is $(x^* A x)^* = x^* A^* x = x^* A x$.
The strict inequality for every nonzero $x$ is the positivity itself, and it must hold for all vectors, not only for a basis.

Over $\R$ the symmetry condition is a real restriction, and it is not automatic.
The matrix $M = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$ has $x^{\mathsf{T}} M x = x_1^2 + x_2^2 > 0$ for $x \ne 0$, but it is not symmetric, so it is not positive definite in our sense.
Some books drop the symmetry condition for real matrices.
For them, $M$ is positive definite exactly when its symmetric part $\tfrac12 (M + M^{\mathsf{T}})$ is, since $x^{\mathsf{T}} M x = x^{\mathsf{T}} \tfrac12 (M + M^{\mathsf{T}}) x$ for every real $x$.

For a real symmetric $A$, the real and the complex definitions agree.
Write $x = a + ib$ with $a, b$ real; then $x^* A x = a^{\mathsf{T}} A a + b^{\mathsf{T}} A b$, because the two cross terms $i a^{\mathsf{T}} A b$ and $-i b^{\mathsf{T}} A a$ cancel by symmetry.

For a small example, $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ is symmetric, and
$$x^{\mathsf{T}} A x = 2x_1^2 - 2x_1 x_2 + 2x_2^2 = x_1^2 + x_2^2 + (x_1 - x_2)^2,$$
which is positive for $x \ne 0$.
The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ is symmetric but fails the inequality, since its form is $-2$ at $x = (1, -1)$.
The [[concept page|0KX66CZMBB]] gives more examples and the tests.

## Explanations

### L1 human

A positive definite matrix gives a positive number $x^{\mathsf{T}} A x$ for every nonzero vector $x$, and it must also equal its own transpose.
For example, $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ gives $2x_1^2 - 2x_1 x_2 + 2x_2^2$, which is $x_1^2 + x_2^2 + (x_1 - x_2)^2$.
This sum of squares is positive unless $x_1 = x_2 = 0$.

### L2 human

To check the definition directly, write the form $x^{\mathsf{T}} A x$ as a sum of squares with positive coefficients.
For $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, one such sum is $2\left( x_1 - \tfrac12 x_2 \right)^2 + \tfrac32 x_2^2$.
Check: the square expands to $2x_1^2 - 2x_1 x_2 + \tfrac12 x_2^2$, and $\tfrac12 + \tfrac32 = 2$.
For large matrices this is slow, and the usual tests are [[the eigenvalue test|0HYC2RHD3M]], [[Sylvester's criterion|0WKEF78PMV]] and the [[Cholesky decomposition|0WKG8CYY6A]].
Watch out: a test that uses only some vectors, for example the standard basis vectors, cannot prove positive definiteness.

### L3 human

The definition says that the Hermitian form $(x, y) \mapsto y^* A x$ is positive definite, so positive definite matrices are the Gram matrices of inner products on $\C^n$ in the standard basis.
Under a change of basis $x = Py$, the matrix changes to $P^* A P$, and positive definiteness is kept.
The Mathlib definition `Matrix.PosDef` works over any star-ordered ring, and its real and complex cases agree with the definition above.
