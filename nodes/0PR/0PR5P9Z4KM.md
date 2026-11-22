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

Every real quadratic form becomes a sum of squares with no cross terms after a rotation of the coordinate axes, and the coefficients of the squares are the eigenvalues of its matrix.

Let $A$ be a real [[symmetric|0N28QN4CYA]] $n \times n$ matrix, and let $Q(x) = x^{\mathsf{T}} A x$ for $x \in \mathbb{R}^n$.
Then there are an [[orthogonal matrix|0W02QESPJQ]] $P$ and real numbers $\lambda_1, \dots, \lambda_n$ such that, for every $y \in \mathbb{R}^n$ and $x = Py$,
$$Q(x) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \dots + \lambda_n y_n^2.$$
The numbers $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, repeated by multiplicity, and the columns of $P$ are orthonormal eigenvectors of $A$, with column $i$ belonging to $\lambda_i$.
The matrix $P$ can be chosen with $\det P = 1$, so that the change of variables $x = Py$ is a rotation.

## Remarks

### A first case in the plane

Take $Q = 3x^2 + 2xy + 3y^2$, with matrix $A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$.
The vector $(1, 1)$ is an eigenvector for $4$ and $(-1, 1)$ is an eigenvector for $2$, since $A(1, 1)^{\mathsf{T}} = (4, 4)^{\mathsf{T}}$ and $A(-1, 1)^{\mathsf{T}} = (-2, 2)^{\mathsf{T}}$.
Their unit multiples are the columns of the rotation by $45^\circ$:
$$P = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}, \qquad P^{\mathsf{T}} A P = \begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}.$$
Check: $AP = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 4 & -2 \\ 4 & 2 \end{pmatrix}$, and multiplying by $P^{\mathsf{T}}$ gives $\tfrac{1}{2} \begin{pmatrix} 8 & 0 \\ 0 & 4 \end{pmatrix}$.
So with $x = (u - v)/\sqrt{2}$ and $y = (u + v)/\sqrt{2}$, the form is $4u^2 + 2v^2$.
The lines along $(1, 1)$ and $(-1, 1)$ are the *principal axes* of $Q$.

### Why each hypothesis is needed

The matrix must be symmetric.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the single eigenvalue $1$, but its form $x_1^2 + x_1 x_2 + x_2^2$ is $\tfrac{1}{2}$ at the unit vector $(1, -1)/\sqrt{2}$, so it is not $y_1^2 + y_2^2$ in any orthonormal coordinates.
Every form has a symmetric matrix, so always replace $A$ by $\tfrac{1}{2}(A + A^{\mathsf{T}})$ before you look for eigenvalues.

The entries must be real.
The complex symmetric matrix $\begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ has square $0$, so its only eigenvalue is $0$, and since it is not $0$ it is not diagonalizable at all.

The change of variables must be orthogonal for the coefficients to be eigenvalues.
The next subsection shows what goes wrong with a general invertible matrix.

### Rotation keeps eigenvalues, congruence keeps only signs

Any invertible $P$ turns the matrix $A$ into $P^{\mathsf{T}} A P$, and [[the diagonalization theorem|0Z3FEWZ8HA]] finds such a $P$ that gives a diagonal matrix.
When $P$ is orthogonal, $P^{\mathsf{T}} = P^{-1}$, so $P^{\mathsf{T}} A P$ is also similar to $A$ and has the same eigenvalues.
For a general $P$ this fails.
[[An example of congruent matrices|57GZX8S4ES]] takes $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$, with eigenvalues $3$ and $-1$, and an invertible $P$ with $P^{\mathsf{T}} A P = \operatorname{diag}(1, -3)$.
The diagonal entries changed, and only their signs, one positive and one negative, survived.
That is [[Sylvester's law of inertia|0WFED3K3DQ]]: a general change of variables keeps the signature, and only an orthogonal one keeps the eigenvalues, and with them lengths and angles.

### What it gives you

The theorem turns questions about $Q$ into questions about numbers.
The level set $Q(x) = 1$ has its shape read from the signs and sizes of the $\lambda_i$, which gives [[the types of conics|1DGT7X9E35]] in the plane and [[the types of quadric surfaces|F42W4DQHBK]] in space.
For example, [[the curve 5x² + 4xy + 2y² = 1|GP4XSY4FNH]] becomes $6u^2 + v^2 = 1$ in its principal axes, an ellipse with semi-axes $1/\sqrt{6}$ and $1$.
The numbers $p$, $q$ and $r$ of [[the signature|07EZA80NEH]] are the numbers of positive, negative and zero eigenvalues.
[[The extreme values of Q on unit vectors|YS4HT1EYE5]] are the largest and the smallest eigenvalue, because $Q = \sum_i \lambda_i y_i^2$ with $\sum_i y_i^2 = 1$.

### The converse

Suppose that $Q(Py) = \sum_i \lambda_i y_i^2$ for all $y$, with $P$ orthogonal.
Then the symmetric matrices of the two sides agree, so $P^{\mathsf{T}} A P = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ and $AP = P \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.
Column $i$ of this equation says $A p_i = \lambda_i p_i$.
So the orthonormal bases that remove all cross terms of $Q$ are exactly the orthonormal bases of eigenvectors of $A$.

### Generalizations

For a Hermitian matrix $A$ and a unitary $P$, the same holds with $\lvert y_i \rvert^2$ in place of $y_i^2$, by [[the spectral theorem for Hermitian matrices|0DGZBQWZWN]].
On a real inner product space $V$, the theorem gives an orthonormal basis that is also orthogonal for a second form $Q$.
So two forms, one of them positive definite, can be diagonalized at the same time, which is [[simultaneous diagonalization|K559AQ9H67]].

## History

Jacobi proved that every real quadratic form can be brought to a diagonal form by an orthogonal change of variables.

## Explanations

### L1 human

Take a tilted ellipse drawn on squared paper.
Its equation has an $xy$ term, because its axes do not line up with the grid.
Turn the paper until the axes of the ellipse line up with the grid, and the $xy$ term disappears.
The theorem says that this always works for every equation built from squares and products of the variables, and it tells you how far to turn.

### L2 human

Here is a typical problem: find the principal axes of $Q = x^2 + 4xy + y^2$ and the shape of $Q = 3$.
The matrix is $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$, with half of the coefficient $4$ in each off-diagonal place.
Its characteristic polynomial is $(1 - t)^2 - 4 = (t - 3)(t + 1)$, so the eigenvalues are $3$ and $-1$.
The eigenvectors are $(1, 1)$ for $3$ and $(-1, 1)$ for $-1$, and their unit multiples give the same rotation $P$ as in the first case above.
In the new coordinates $Q = 3u^2 - v^2$, so $Q = 3$ is the hyperbola $u^2 - v^2/3 = 1$.
Check at $(u, v) = (1, 0)$: then $(x, y) = (1, 1)/\sqrt{2}$ and $Q = \tfrac{1}{2}(1 + 4 + 1) = 3$.
Watch out: normalize the eigenvectors.
With the columns $(1, 1)$ and $(-1, 1)$ unnormalized, $P^{\mathsf{T}} A P$ is $\operatorname{diag}(6, -2)$, not $\operatorname{diag}(3, -1)$, because each column has squared length $2$.

### L3 human

The theorem is the [[real spectral theorem|06J4PXRG22]] read for the bilinear form $(x, y) \mapsto x^{\mathsf{T}} A y$ in place of the operator $x \mapsto Ax$.
On an inner product space the two readings agree, since the inner product identifies symmetric bilinear forms with self-adjoint operators.
In mechanics, the theorem applied to the kinetic and potential energy of small oscillations gives the normal modes, with the kinetic energy as the positive definite form.
In statistics, the principal axes of a covariance matrix are the directions of [[principal component analysis|ABXD13M340]].
Over a general field there is no preferred inner product to keep, so the classification of forms uses congruence alone, as in [[the classification over the complex numbers|0CEX9BRXRZ]].
