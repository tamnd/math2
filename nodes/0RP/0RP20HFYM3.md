---
tag: 0RP20HFYM3
kind: concept
name: Positive definite quadratic form
aliases: [positive-definite-quadratic-form]
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
specializes: [0RBQS1JJCR]
uses: [0RBQS1JJCR, 0KX66CZMBB, 0Z3FEWZ8HA, 0VGSYBWHV2]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
  - url: https://understandinglinearalgebra.org/sec-quadratic-forms.html
  - book: isbn:9780321982384
inventory: [R63EXRT7EA]
---

## Summary

A [[quadratic form|0RBQS1JJCR]] $Q$ on a finite-dimensional real vector space $V$ is *positive definite* when $Q(v) > 0$ for every $v \ne 0$; see [[the definition|00QN1N6MNT]].
For $Q(x) = x^T A x$ on $\R^n$ with $A$ symmetric, this says that $A$ is a [[positive definite matrix|0KX66CZMBB]].
The positive definite forms on $V$ are exactly the squared norms $\ip{v}{v}$ of the [[inner products|0VGSYBWHV2]] on $V$.
They are the forms of signature $(n, 0, 0)$, with $n = \dim V$.

## Motivation

The squared length $x_1^2 + \cdots + x_n^2$ is positive at every nonzero vector, and this property is what makes it a length.
Other forms with the same property give other notions of length, for example the energy $\frac12 m v^2$ summed over several masses.
In analysis, a positive definite Hessian at a critical point means a strict local minimum.
So it is useful to decide, from the coefficients, whether a given form is positive definite.

## Notation

- $Q > 0$, or $A \succ 0$ for the matrix, means positive definite.
- $Q \ge 0$, or $A \succeq 0$, means positive semidefinite: $Q(v) \ge 0$ for all $v$; see [[the five types|01RBSSGMY5]].
- Some older books write "definite" alone for "positive definite".

## Remarks

### Examples

- $x_1^2 + \cdots + x_n^2$ on $\R^n$: a sum of squares is $0$ only when every term is $0$.
- [[The form $x^2 + xy + y^2$|~513f51a9]]: it equals $(x + \frac y2)^2 + \frac34 y^2$, a sum of squares with positive coefficients.
- $Q(x) = x^T A x$ with $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$: its eigenvalues are $3$ and $1$, both positive.
- For any real matrix $M$ with independent columns, $Q(x) = \norm{Mx}^2 = x^T M^T M x$: it is $0$ only when $Mx = 0$, that is, when $x = 0$.

### Non-examples

- [[The form $2x^2 + 6xy + 4y^2$|~eda011e3]] has only positive coefficients, but $Q(3, -2) = -2$.
- $x^2$ on $\R^2$ is positive semidefinite but not positive definite: $Q(0, 1) = 0$.
- $x^2 - y^2$ is indefinite: $Q(0, 1) = -1$.

### Basic properties

For $Q(x) = x^T A x$ with $A$ symmetric $n \times n$, the following are equivalent; the tests are in the topic on positive definite matrices.

1. $Q$ is positive definite.
2. All eigenvalues of $A$ are positive, by [[the eigenvalue test|0HYC2RHD3M]].
3. All leading principal minors of $A$ are positive, by [[Sylvester's criterion|0WKEF78PMV]].
4. Completing squares, as in [[the diagonalization theorem|0Z3FEWZ8HA]], gives $n$ positive coefficients, by [[Sylvester's law of inertia|0WFED3K3DQ]].
5. $A = R^T R$ with $R$ upper triangular and with positive diagonal, by [[the Cholesky decomposition|0WKG8CYY6A]].

Also: the sum of two positive definite forms is positive definite, and so is the restriction of $Q$ to any subspace.
$Q$ is positive definite if and only if its associated symmetric bilinear form is an inner product.

### History

We found no source in the reading list of this topic for the first use of the term, so we give no date.

### Common errors

- Testing only the diagonal entries. Positive diagonal entries are necessary but not sufficient, as [[the form $2x^2 + 6xy + 4y^2$|~eda011e3]] shows.
- Using the minors test for semidefinite forms. The matrix $\operatorname{diag}(0, -1)$ has leading minors $0$ and $0$, but it is not positive semidefinite.
- Forgetting the factor $\frac12$: the matrix of $x^2 + xy + y^2$ has off-diagonal entries $\frac12$, not $1$.

## Explanations

### L1 human

A positive definite form is positive at every vector except $0$.
Its graph over the plane is a bowl with the lowest point at the origin.
The squared length $x^2 + y^2$ is the standard example.

### L2 human

To test a $2 \times 2$ form $a x^2 + b x y + c y^2$, check $a > 0$ and $ac - \frac{b^2}{4} > 0$.
These are the two leading minors of the matrix $\begin{pmatrix} a & b/2 \\ b/2 & c \end{pmatrix}$.
For $x^2 + xy + y^2$: $a = 1 > 0$ and $1 - \frac14 = \frac34 > 0$, so it is positive definite.
A trap: for semidefinite forms the minors test fails; use the eigenvalues or all principal minors.

### L3 human

The positive definite forms on $\R^n$ form an open convex cone in the space of quadratic forms.
Its closure is the cone of positive semidefinite forms.
Over $\Q$ or $\Z$, positive definite forms are the subject of the theory of lattices and of the representation of integers by forms.
That theory belongs to number theory.
