---
tag: GZ7NG7J3J8
kind: statement
role: theorem
name: Properties of a unitary matrix
aliases: [equivalent-conditions-for-a-unitary-matrix, eigenvalues-of-unitary-matrix-on-unit-circle]
msc: ["15B57", "15A18"]
topics: [AZS5BPF5H3]
audience: ug2
about: [0AR68JTMDT]
uses: [0D6RMJ10M9, 0EX045E2BP, 0C3CFHDN6R, 0ZND7NQ970, 0B5H4208Z9, 0XYKE8BE7X]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: Equivalent conditions
  - book: isbn:9780521839402
    locator: Chapter 2
---

## Statement

Seven natural tests for a complex matrix to keep lengths all agree, and a matrix that passes them has its determinant and eigenvalues on the unit circle and can be diagonalized by a unitary matrix.
Let $U$ be a complex $n \times n$ matrix, and let $\langle x, y \rangle = \sum_k x_k \overline{y_k} = y^* x$ be the standard inner product on $\C^n$.
The following seven conditions are equivalent.

1. $U^* U = I_n$, where $U^*$ is the [[conjugate transpose|0EX045E2BP]].
2. $U U^* = I_n$.
3. $U$ is invertible and $U^{-1} = U^*$.
4. The columns of $U$ form an orthonormal basis of $\C^n$.
5. The rows of $U$ form an orthonormal basis of $\C^n$.
6. $\langle Ux, Uy \rangle = \langle x, y \rangle$ for all $x, y \in \C^n$.
7. $\lVert Ux \rVert = \lVert x \rVert$ for all $x \in \C^n$.

If $U$ satisfies these conditions, so that $U$ is [[unitary|0D6RMJ10M9]], then the following hold.

1. $\lvert \det U \rvert = 1$.
2. Every [[eigenvalue|0ZND7NQ970]] $\lambda$ of $U$ has $\lvert \lambda \rvert = 1$.
3. [[Eigenvectors|0B5H4208Z9]] of $U$ for different eigenvalues are orthogonal.
4. $U$ is [[normal|0XYKE8BE7X]], and $U = V D V^*$ for a unitary matrix $V$ and a diagonal matrix $D$ whose diagonal entries have absolute value $1$.

Conversely, every matrix $V D V^*$ with $V$ unitary and $D$ diagonal with diagonal entries of absolute value $1$ is unitary.

## Remarks

### Why each hypothesis is needed

The matrix must be square.
The $2 \times 1$ matrix $U = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ has $U^* U = (1)$, so its one column is orthonormal and it keeps lengths, but $U U^* = \operatorname{diag}(1, 0) \ne I_2$.
So conditions 1 and 2 split apart, and $U$ has no inverse.

The converse needs $V$ to be unitary, not only invertible.
With $V = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $D = \operatorname{diag}(1, -1)$ we get
$$V D V^* = \begin{pmatrix} 1 & -1 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & -1 \end{pmatrix},$$
and its second column has length $\sqrt{2}$, so it is not unitary.

### What it gives you

The theorem lets you choose the cheapest test.
For a matrix with numbers, condition 4 is usually fastest: check the lengths and inner products of the columns.
For a proof, condition 6 or 7 is usually the useful one, because it speaks about vectors and not entries.

Each unitary matrix is unitarily similar to $\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n})$, so in a suitable orthonormal basis it multiplies each axis by a point of the unit circle.
The real case gives [[the determinant theorem for orthogonal matrices|QDZJMFATRW]], because a real orthogonal matrix is unitary; there the determinant is real, so it is $1$ or $-1$.

### The converse of the eigenvalue property

Eigenvalues on the unit circle do not make a matrix unitary.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the single eigenvalue $1$, but its second column has length $\sqrt{2}$.
The last part of the statement gives the correct converse: a normal matrix with all eigenvalues on the unit circle is unitary, because the spectral theorem writes it as $V D V^*$ with $V$ unitary.

### Generalizations

For a linear map $T$ of a finite-dimensional complex inner product space, the same conditions with the [[adjoint|0ST8QF9T3T]] $T^*$ define a [[unitary operator|MM0EJ2GDE4]], and the proof is the same.
In an infinite-dimensional Hilbert space condition 1 alone gives only an isometry.
The shift $S(x_1, x_2, \dots) = (0, x_1, x_2, \dots)$ on square-summable sequences has $S^* S = I$, but $S S^* \ne I$, since $S S^*$ sends $(1, 0, 0, \dots)$ to $0$.

## Explanations

### L1 human

A unitary matrix keeps all lengths in complex space.
There are many ways to test this, with columns, with rows or with lengths, and the theorem says that they all agree.
The eigenvalues of such a matrix are complex numbers of size $1$, so they are points on the unit circle.
In a good choice of axes, the matrix only turns each axis by an angle in its own complex plane.

### L2 human

Here is a worked case: $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$, studied in [[this example|F3P6M0A78R]].
Its determinant is
$$\det U = \frac{1}{2}(1 \cdot 1 - i \cdot i) = \frac{1 + 1}{2} = 1,$$
so $\lvert \det U \rvert = 1$.
The vectors $(1, 1)$ and $(1, -1)$ are eigenvectors, with the eigenvalues $\frac{1 + i}{\sqrt{2}}$ and $\frac{1 - i}{\sqrt{2}}$.
Both eigenvalues have absolute value $\sqrt{\frac{1}{2} + \frac{1}{2}} = 1$, and the eigenvectors are orthogonal, since $\langle (1, 1), (1, -1) \rangle = 1 - 1 = 0$.
The case shows the typical use: to diagonalize a unitary matrix, find its eigenvalues and choose an orthonormal basis of eigenvectors.
Watch out: in $\langle x, y \rangle = \sum_k x_k \overline{y_k}$ the second vector is conjugated, and forgetting the conjugate gives wrong answers as soon as the entries are not real.

### L3 human

The theorem says that $U(n)$ is the full group of linear isometries of $\C^n$.
The spectral form $U = V D V^*$ shows that every element of $U(n)$ lies in a maximal torus, a conjugate of the diagonal group $\{ \operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n}) \}$.
So the exponential map from the skew-Hermitian matrices onto $U(n)$ is surjective: $V \operatorname{diag}(e^{i\theta_k}) V^* = \exp\big(V \operatorname{diag}(i\theta_k) V^*\big)$.
The path $t \mapsto V \operatorname{diag}(e^{it\theta_k}) V^*$ for $t$ from $0$ to $1$ joins $I_n$ to $U$, so $U(n)$ is connected, unlike $O(n)$.
