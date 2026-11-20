---
tag: 0PR5P9Z4KM
kind: statement
role: theorem
name: Principal axis theorem
msc: [15A63, 15A18]
topics: [6TSCEW8QMK]
audience: ug1
about: [0RBQS1JJCR, 0VR671PHE5]
uses: [0HZNE5QZDJ, 0DGZBQWZWN, 0N28QN4CYA, 0W02QESPJQ, 0BQAA2BK3Q]
proofs: [1WYTQ45PXX]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_axis_theorem
    locator: Formal statement
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-2.xml#L1032
    locator: src/section7-2.xml:1032
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Real quadratic forms
  - book: isbn:9780321982384
same_as:
  wikidata: Q7245073
  wikipedia: Principal axis theorem
inventory: [3RHN4QR9M8]
---

## Statement

Let $A$ be a real [[symmetric|0N28QN4CYA]] $n \times n$ matrix, and let $Q(x) = x^T A x$ for $x \in \R^n$.
Then there are an [[orthogonal matrix|0W02QESPJQ]] $P$ and real numbers $\lambda_1, \dots, \lambda_n$ such that, for $x = P y$,
$$Q(x) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2.$$
The numbers $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, with multiplicity, and the columns of $P$ are orthonormal eigenvectors of $A$.
The matrix $P$ can be chosen with $\det P = 1$, so that $x = Py$ is a rotation.

## Remarks

### Why each hypothesis is needed

- $A$ symmetric: the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has only the eigenvalue $1$. But its form $x_1^2 + x_1 x_2 + x_2^2$ takes the value $\frac12$ at the unit vector $(1, -1)/\sqrt 2$. So it is not $y_1^2 + y_2^2$ in orthonormal coordinates. Always replace $A$ by its symmetric part first.
- Real entries: the complex symmetric matrix $\begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ has $A^2 = 0$, so its only eigenvalue is $0$, but $A \ne 0$. It is not diagonalizable at all.
- Orthogonal $P$: with an invertible $P$ that is not orthogonal, [[the diagonalization theorem|0Z3FEWZ8HA]] gives a diagonal form. But its coefficients are not the eigenvalues; see [[congruent matrices with different eigenvalues|57GZX8S4ES]].

### Consequences

- The lines spanned by the columns of $P$ are the *principal axes* of $Q$. They are orthogonal, so lengths and angles are kept.
- The level set $Q(x) = 1$ is classified by the signs of the eigenvalues: [[ellipses and hyperbolas in the plane|1DGT7X9E35]], and [[ellipsoids and hyperboloids in space|F42W4DQHBK]].
- [[The principal axes of $5x^2 + 4xy + 2y^2 = 1$|GP4XSY4FNH]] are the eigenvectors $(2, 1)$ and $(-1, 2)$, and the curve is $6u^2 + v^2 = 1$.
- The numbers $p$, $q$ and $r$ of [[the signature|07EZA80NEH]] are the numbers of positive, negative and zero eigenvalues.
- [[The extreme values of $Q$ on the unit sphere|YS4HT1EYE5]] are the largest and smallest eigenvalues.

### Converse

If $Q(Py) = \sum_i \lambda_i y_i^2$ with $P$ orthogonal, then $P^T A P = \operatorname{diag}(\lambda_i)$.
So the columns of $P$ are eigenvectors and the $\lambda_i$ are eigenvalues.
So the orthonormal bases that diagonalize $Q$ are exactly the orthonormal bases of eigenvectors.

### Generalizations

- For a Hermitian matrix and a unitary $P$, the same holds with $\abs{y_i}^2$, by [[the spectral theorem for Hermitian matrices|0DGZBQWZWN]].
- For a quadratic form on a real inner product space, the theorem gives an orthonormal basis that is also orthogonal for the form. This is a simultaneous diagonalization of two forms, one of them positive definite.

## History

The Wikipedia article on quadratic forms has a section on real quadratic forms.
It says that Jacobi proved that every real quadratic form has an orthogonal diagonalization.
It gives no date for this, so we give none.

## Explanations

### L1 human

Each real quadratic form becomes a sum of squares after a rotation of the axes.
The new axes are the principal axes of the form, and the coefficients are the eigenvalues.
This is how we find the shape of an ellipse or a hyperbola from its equation.

### L2 human

Worked example: the form $Q = 3x^2 + 2xy + 3y^2$.

1. The matrix is $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, with eigenvalues $4$ on $(1, 1)$ and $2$ on $(-1, 1)$.
2. With the unit vectors $\frac{1}{\sqrt 2}(1, 1)$ and $\frac{1}{\sqrt 2}(-1, 1)$, the rotation by $45^\circ$ is $x = \frac{u - v}{\sqrt 2}$, $y = \frac{u + v}{\sqrt 2}$.
3. Then $Q = 4u^2 + 2v^2$. Check at $(u, v) = (1, 0)$: $(x, y) = \frac{1}{\sqrt 2}(1, 1)$, and $Q = \frac12 (3 + 2 + 3) = 4$.

A trap: the eigenvectors must be normalized.
With $P$ of columns $(1, 1)$ and $(-1, 1)$, the coefficients become $8$ and $4$, not $4$ and $2$.

### L3 human

The theorem is the spectral theorem for self-adjoint operators, read for the form $\ip{Av}{v}$ in place of the operator $A$.
It says that a pair of real quadratic forms, one positive definite, can be diagonalized at the same time.
In mechanics, this gives the normal modes of small oscillations, with the kinetic energy as the positive definite form.
