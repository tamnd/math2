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

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]], so $A^* = A$.
The matrix $A$ is *positive definite* when
$$x^* A x > 0 \qquad \text{for all } x \in \C^n \text{ with } x \ne 0.$$
A real [[symmetric matrix|0VR671PHE5]] $A$ is positive definite when $x^T A x > 0$ for all $x \in \R^n$ with $x \ne 0$.

## Notation

We write $A \succ 0$.
In Mathlib the predicate is `Matrix.PosDef A`, and it includes the condition that $A$ is Hermitian.

## Remarks

- For a Hermitian $A$, the number $x^* A x$ is real, because its conjugate is $(x^* A x)^* = x^* A^* x = x^* A x$.
- For a real symmetric $A$, the real and the complex definitions agree. For $x = a + ib$ with $a, b$ real, $x^* A x = a^T A a + b^T A b$, since the cross terms cancel by symmetry.
- Some books do not ask for symmetry. They call a real matrix positive definite when $x^T A x > 0$ for all $x \ne 0$. Then $A$ is positive definite if and only if its symmetric part $\tfrac12 (A + A^T)$ is, because $x^T A x = x^T \tfrac12 (A + A^T) x$. This page always asks for symmetry.
- $A$ is positive definite if and only if $\ip{x}{y} = y^* A x$ is an [[inner product|0NB0AWGJBW]] on $\C^n$. The symmetry of the inner product needs $A^* = A$, and positivity is the condition above.

## Explanations

### L1 human

A positive definite matrix gives a positive number $x^T A x$ for every nonzero vector $x$.
The matrix must also be symmetric, so that it equals its own transpose.
For example, $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ gives $2x_1^2 - 2x_1x_2 + 2x_2^2$, which is $x_1^2 + x_2^2 + (x_1 - x_2)^2$.
This is positive for every nonzero $x$.

### L2 human

To check the definition directly, write the form $x^T A x$ as a sum of squares with positive coefficients.
For $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, one sum is $2(x_1 - \tfrac12 x_2)^2 + \tfrac32 x_2^2$.
This method is slow for large matrices.
The usual tests are [[the eigenvalue test|0HYC2RHD3M]], [[Sylvester's criterion|0WKEF78PMV]] and the [[Cholesky decomposition|0WKG8CYY6A]].
A trap: a test that uses only some vectors, for example the standard basis vectors, cannot prove positive definiteness.

### L3 human

The definition says that the Hermitian form $(x, y) \mapsto y^* A x$ is positive definite.
So positive definite matrices are the Gram matrices of inner products on $\C^n$ in the standard basis.
Under a change of basis $x = Py$, the matrix changes to $P^* A P$, and positive definiteness is kept.
The Mathlib definition `Matrix.PosDef` works over any star-ordered ring, and its real and complex cases agree with this page.
