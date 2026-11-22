---
tag: 0R9R0Y1HDK
kind: object
name: Unitary group
msc: [15B57, 20G20]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [G5S1M9]
uses: [0D6RMJ10M9]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_group
    locator: lead section
same_as:
  wikidata: Q1500617
  wikipedia: Unitary group
---

## Description

The unitary group is the complex version of the orthogonal group: it collects the complex matrices that keep the length of every vector in $\mathbb{C}^n$.
It is the symmetry group of complex inner product geometry, and in quantum mechanics it is the group of all reversible changes of a finite system.

Let $n \ge 1$, and write $U^*$ for the conjugate transpose of a complex matrix $U$.
The *unitary group* is the set of complex $n \times n$ [[unitary matrices|0AR68JTMDT]],
$$U(n) = \{ U \in M_n(\mathbb{C}) : U^* U = I_n \},$$
with matrix multiplication.
It is a subgroup of $GL_n(\mathbb{C})$, by the same four checks as for the [[orthogonal group|0TKYAEJ8N7]], with $U^*$ in place of $Q^{\mathsf{T}}$.
The inverse of $U$ is $U^*$, the product of two unitary matrices is unitary because $(UV)^* (UV) = V^* U^* U V = V^* V = I_n$, and $(U^*)^* U^* = U U^* = I_n$.
With the inner product $\langle x, y \rangle = \overline{x_1} y_1 + \dots + \overline{x_n} y_n$, the elements of $U(n)$ are exactly the matrices with $\langle Ux, Uy \rangle = \langle x, y \rangle$ for all $x, y \in \mathbb{C}^n$.

## Remarks

### The smallest case: a circle

For $n = 1$, a $1 \times 1$ matrix $(z)$ is unitary when $\overline{z} z = \lvert z \rvert^2 = 1$.
So $U(1)$ is the set of complex numbers of absolute value $1$, the [[circle group|04EAFVFTF7]], and the [[unitary group of degree one|1Y63SY7537]] is a circle.
Multiplication by $e^{i\theta}$ turns the complex plane by the angle $\theta$, so $U(1)$ is the group of rotations of $\mathbb{C} = \mathbb{R}^2$, the same group as $SO(2)$.

### An element of U(2)

Take
$$V = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}, \qquad V^* = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}.$$
Multiply, using $i^2 = -1$:
$$V^* V = \frac{1}{2} \begin{pmatrix} 1 - i^2 & i - i \\ -i + i & -i^2 + 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I_2.$$
So $V \in U(2)$.
Its determinant is $\tfrac{1}{2}(1 - i^2) = 1$, so $V$ also lies in the [[special unitary group|CZCWFPNS4N]].
Its characteristic polynomial is $t^2 - \sqrt{2}\, t + 1$, with roots $\tfrac{\sqrt{2}}{2}(1 \pm i) = e^{\pm i\pi/4}$, two numbers of absolute value $1$.

### Determinants and eigenvalues on the circle

Every $U \in U(n)$ has $\lvert \det U \rvert = 1$.
The reason is that $\det U^* = \overline{\det U}$, so
$$1 = \det(U^* U) = \overline{\det U} \, \det U = \lvert \det U \rvert^2.$$
Every value on the circle occurs, because $\det \operatorname{diag}(z, 1, \dots, 1) = z$ for each $z$ with $\lvert z \rvert = 1$.
So $\det \colon U(n) \to U(1)$ is a surjective homomorphism, and its kernel is $SU(n)$.
In the same way, every eigenvalue $\lambda$ has $\lvert \lambda \rvert = 1$: if $Uv = \lambda v$ with $v \ne 0$, then $\lVert v \rVert = \lVert Uv \rVert = \lvert \lambda \rvert \lVert v \rVert$.

### One piece, not two

Unlike $O(n)$, the group $U(n)$ is connected.
A unitary matrix is normal, so by the [[complex spectral theorem|04CW1P44VD]] it has the form $U = W \operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n}) W^*$ with $W$ unitary.
The path $t \mapsto W \operatorname{diag}(e^{it\theta_1}, \dots, e^{it\theta_n}) W^*$ for $t$ from $0$ to $1$ stays in $U(n)$ and joins $I_n$ to $U$.
In $O(n)$ no such path exists from $I_n$ to a reflection, because the determinant would have to jump from $1$ to $-1$; in $U(n)$ the determinant can move along the circle.
The group is also compact, and as a real manifold it has dimension $n^2$.

### Real unitary matrices

A real matrix is unitary exactly when it is orthogonal, because for real $U$ the conjugate transpose is the transpose.
So $U(n) \cap M_n(\mathbb{R}) = O(n)$, and the reflection $\operatorname{diag}(-1, 1)$ is an element of $U(2)$ with determinant $-1$.
Inside $U(2)$ it can be joined to $I_2$ through $\operatorname{diag}(e^{it}, 1)$ for $t$ from $\pi$ to $0$, a path that leaves the real matrices.

### What it is not

A determinant on the unit circle does not make a matrix unitary: the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, but its second column has length $\sqrt{2}$, as in the [[matrix with determinant on the unit circle that is not unitary|RMXFKRW9WQ]].
A complex matrix with $Q^{\mathsf{T}} Q = I$ need not be unitary either.
The matrix $Q = \begin{pmatrix} \sqrt{2} & i \\ -i & \sqrt{2} \end{pmatrix}$ has $Q^{\mathsf{T}} Q = I_2$, but its first column has squared length $2 + 1 = 3$, the case of the [[complex orthogonal matrix that is not unitary|JRPHE0FG7D]].

### Watch out

The condition uses the conjugate transpose, not the transpose.
For $V$ above, $V^{\mathsf{T}} V = \tfrac{1}{2} \begin{pmatrix} 1 + i^2 & 2i \\ 2i & 1 + i^2 \end{pmatrix} = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$, which is not $I_2$, although $V$ is unitary.
Books also differ on which slot of $\langle x, y \rangle$ is conjugated, but the group $U(n)$ is the same with both conventions.

### Try it

First, is $W = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ i & -i \end{pmatrix}$ unitary, and what is its determinant?
The columns have length $1$ and $\langle w_1, w_2 \rangle = \tfrac{1}{2}(1 + \overline{i}(-i)) = \tfrac{1}{2}(1 - 1) = 0$, so it is unitary, and $\det W = \tfrac{1}{2}(-i - i) = -i$.

Second, which diagonal matrices $\operatorname{diag}(a, b)$ lie in $U(2)$?
Exactly those with $\lvert a \rvert = \lvert b \rvert = 1$, so they form a copy of $U(1) \times U(1)$, a torus.

## Explanations

### L1 human

In the plane, a rotation keeps every length.
The complex numbers give a second view of this: multiplying by a complex number of size $1$, such as $i$, turns the plane without stretching it.
The unitary group does the same in several complex dimensions at once.
Its elements turn complex space and keep the length of every vector.
Quantum computers act on their bits by such matrices, because the total probability, a squared length, must stay equal to $1$.

### L2 human

Here is a typical problem: write the matrix $W$ of the exercise as a phase times a matrix of determinant $1$.
We need a number $c$ with $\lvert c \rvert = 1$ and $\det(cW) = c^2 \det W = 1$.
Since $\det W = -i$, we need $c^2 = i$, and $c = e^{i\pi/4}$ works.
Then $S = e^{i\pi/4} W$ has
$$\det S = e^{i\pi/2} \cdot (-i) = i \cdot (-i) = 1,$$
so $S \in SU(2)$ and $W = e^{-i\pi/4} S$.
The [[phase times a special unitary matrix|6NZCDBCSKQ]] carries out the same steps for another matrix.
The phase is fixed only up to a sign here, since $c = -e^{i\pi/4}$ works too; in $U(n)$ it is fixed up to an $n$th root of unity.
This is the typical use: physical questions often ignore an overall phase, so they reduce from $U(n)$ to $SU(n)$.

### L3 human

The group $U(n)$ is a connected compact [[Lie group|7JBRGCVJRB]] of real dimension $n^2$, and its Lie algebra is the space of skew-Hermitian matrices.
The map $SU(n) \times U(1) \to U(n)$, $(S, z) \mapsto zS$, is a surjective homomorphism whose kernel consists of the pairs $(\omega^{-1} I_n, \omega)$ with $\omega^n = 1$, so $U(n)$ is a quotient of the product by a cyclic group of order $n$.
Viewed as real $2n \times 2n$ matrices, $U(n)$ is the intersection of $O(2n)$ with the matrices that commute with multiplication by $i$.
The [[polar decomposition|0J2C7BDJQA]] and the [[singular value decomposition|000NPTMX6J]] use unitary factors, and Mathlib writes `Matrix.unitaryGroup (Fin n) ℂ` for this group.
