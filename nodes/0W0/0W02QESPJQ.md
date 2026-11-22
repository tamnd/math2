---
tag: 0W02QESPJQ
kind: concept
name: Orthogonal matrix
aliases: [real-orthogonal-matrix]
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: ug1
specializes: [0EB9N0S33C, 0MR0BYF0K2]
uses: [0QRBVFJ50X, 0W809K6AW0, 0FWJ0VW561]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L1829
    locator: src/section6-3.xml:1829
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
  - book: isbn:9780134860244
    locator: Section 6.5
same_as:
  wikidata: Q333871
  wikipedia: Orthogonal matrix
inventory: [8KHAEVF7HH]
---

## Summary

An orthogonal matrix is a square matrix that turns or mirrors space without changing any length, and its inverse is simply its transpose.
Its columns are perpendicular unit vectors, so they form a ready-made orthonormal coordinate system.
A real $n \times n$ matrix $Q$ is *orthogonal* when
$$Q^TQ = I_n,$$
where $Q^T$ is the [[transpose|09DXWYRD43]] and $I_n$ is the identity matrix.
The [[formal definition|0QRBVFJ50X]] states this.
[[Equivalently|F7M8ZXB4P7]], $Q$ is invertible with $Q^{-1} = Q^T$, its columns form an [[orthonormal basis|0S9GGTR0EX]] of $\R^n$, and so do its rows.
The map $x \mapsto Qx$ is a [[linear isometry|07SJXTWVQW]] of $\R^n$ exactly when $Q$ is orthogonal.

## Motivation

A change of basis in $\R^n$ is an invertible matrix $P$, and in general its inverse takes real work to compute.
When the new basis is orthonormal, the coordinates of a vector are just its dot products with the basis vectors.
So the inverse of $P$ is $P^T$, and no elimination is needed.

The same matrices describe the rigid motions of $\R^n$ that fix the origin, such as the rotations of a body about its center of mass and the reflections in a mirror.
In computing, the QR decomposition, Householder reflections and Givens rotations all rest on orthogonal matrices, because multiplying by them does not enlarge rounding errors.
Later pages sort the orthogonal matrices into [[rotations|HNY4CPEEJA]] and [[reflections|06BRDF3F0E]], and the [[normal form|QTY3VMFGY1]] shows that every orthogonal matrix is built from these two kinds of blocks.

## Notation

The set of real orthogonal $n \times n$ matrices is the [[orthogonal group|WWK2E8BRGF]] $O(n)$, also written $O_n(\R)$ or $O(n, \R)$.
Mathlib writes `Matrix.orthogonalGroup n ℝ`.
It defines this set for any ring with an involution, as the matrices with `star A * A = 1`, so over $\C$ the same name gives the unitary matrices.
Some books say "orthonormal matrix", which describes the columns better.
Some authors use "orthogonal transformation" for rotations only, that is, for $\det Q = 1$.
Here an orthogonal transformation is any linear isometry of a real inner product space, with $\det Q = \pm 1$.
A complex matrix with $Q^TQ = I$ is a *complex orthogonal matrix*, and it is not the same as a [[unitary matrix|0AR68JTMDT]].

## Remarks

### A first check

Take $Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
The columns are $\frac{1}{\sqrt 2}(1, 1)$ and $\frac{1}{\sqrt 2}(1, -1)$, and we compute their lengths and their dot product:
$$\tfrac{1}{2}(1 + 1) = 1, \qquad \tfrac{1}{2}(1 + 1) = 1, \qquad \tfrac{1}{2}(1 - 1) = 0.$$
The entries of $Q^TQ$ are exactly these three numbers, so $Q^TQ = I$ and $Q^{-1} = Q^T = Q$.
The determinant is $\frac{1}{2}(-1 - 1) = -1$, so $Q$ is a reflection and not a rotation.
It fixes the line at angle $\pi/8$ to the $x$-axis, the line through $(1, \sqrt 2 - 1)$.

### More examples

The [[rotation matrix|HNY4CPEEJA]] $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ is orthogonal, because its columns are unit vectors and their dot product is $-\cos\theta\sin\theta + \sin\theta\cos\theta = 0$.
Every [[permutation matrix|08SP3DF8NB]] is orthogonal, since its columns are the standard basis vectors in another order, and so is every diagonal matrix with entries $\pm 1$.
The [[signed permutation matrices of size two|HV3HWHW9RE]] are the eight symmetries of a square.
The [[coordinate swap|27TY1G77KM]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is orthogonal with determinant $-1$, so it is a reflection.
The [[Householder matrix|BE65CTF1HQ]] $I - 2vv^T$ of a unit vector $v$ is orthogonal and symmetric.
The matrix $\frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$ is a [[rotation by sixty degrees about the diagonal|TFWTJ9K6K7]] of $\R^3$.

### What it is not

The [[matrix $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$|B5SD0BTPZG]] has orthogonal columns, but each has length $\sqrt{2}$, so $Q^TQ = 2I$.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, but its second column $(1, 1)$ is not a unit vector.
A $3 \times 2$ matrix with orthonormal columns satisfies $Q^TQ = I_2$, but it is not square, so it is not an orthogonal matrix.
The [[complex matrix $\begin{pmatrix} \sqrt 2 & i \\ -i & \sqrt 2 \end{pmatrix}$|JRPHE0FG7D]] has $N^TN = I$, but it stretches its first column to length $\sqrt 3$, so the plain transpose is the wrong test over $\C$.

### The rules you can use

The [[equivalent conditions|F7M8ZXB4P7]] give six other forms of $Q^TQ = I$, among them $QQ^T = I$, orthonormal rows, and $\norm{Qx} = \norm{x}$ for all $x$.
By the [[determinant and eigenvalue theorem|QDZJMFATRW]], $\det Q = \pm 1$, and every complex eigenvalue of $Q$ lies on the unit circle, $\abs{\lambda} = 1$.
Products, inverses and transposes of orthogonal matrices are orthogonal, since $(AB)^T(AB) = B^TA^TAB = B^TB = I$.
So the orthogonal $n \times n$ matrices form a [[group|G5S1M9]], the group $O(n)$.
An orthogonal matrix is [[normal|0MR0BYF0K2]], because $QQ^T = I = Q^TQ$.

### Watch out

Orthogonal columns are not enough, because the columns must also be unit vectors.
The matrix $\operatorname{diag}(2, 1)$ has perpendicular columns, and it doubles the length of $(1, 0)$.
Determinant $\pm 1$ is not enough either: the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$ and is not orthogonal.
Over $\C$, the right condition is $U^*U = I$ with the conjugate transpose, not $U^TU = I$.

### History

Cayley described in 1846 a map that sends skew-symmetric matrices to special orthogonal matrices.
It is now called the [[Cayley transform|HKQ5YY027B]], and it describes the rotations without the eigenvalue $-1$ by rational formulas in the entries of a skew-symmetric matrix.

### Try it

First, is $\frac{1}{5}\begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix}$ orthogonal, and is it a rotation?
The columns have squared lengths $\frac{9 + 16}{25} = 1$ and dot product $\frac{12 - 12}{25} = 0$, so it is orthogonal, and its determinant $\frac{-9 - 16}{25} = -1$ makes it a reflection.

Second, solve $Qx = b$ for the $Q$ of the first check and $b = (\sqrt 2, 0)$.
Since $Q^{-1} = Q^T = Q$, we get $x = Qb = (1, 1)$.
Check: $Q(1, 1) = \frac{1}{\sqrt 2}(2, 0) = (\sqrt 2, 0)$.

## Explanations

### L1 human

An orthogonal matrix describes a turn or a mirror image of space that keeps the origin in place.
Its columns are arrows of length $1$ that are perpendicular to each other.
For example, the columns of $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ are $(0, 1)$ and $(-1, 0)$.
Both have length $1$, they meet at a right angle, and the matrix turns the plane by a quarter turn.

### L2 human

Here is a typical use: write $b = (2, 3, 1)$ in the orthonormal basis given by the columns $q_1, q_2, q_3$ of the rotation $Q = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$.
The coordinates are $Q^{-1}b = Q^Tb$, so each one is a dot product with a column:
$$q_1 \cdot b = \tfrac{4 + 6 - 1}{3} = 3, \qquad q_2 \cdot b = \tfrac{-2 + 6 + 2}{3} = 2, \qquad q_3 \cdot b = \tfrac{4 - 3 + 2}{3} = 1.$$
Check: $3q_1 + 2q_2 + q_3 = \frac{1}{3}(6 - 2 + 2,\ 6 + 4 - 1,\ -3 + 4 + 2) = (2, 3, 1)$.
Three dot products replaced the solution of a $3 \times 3$ system.
Watch out: this shortcut needs orthonormal columns, and with merely orthogonal columns each dot product must be divided by the squared length of the column.

### L3 human

The orthogonal matrices form the compact group $O(n)$, the symmetry group of the dot product.
Over any field, the matrices $Q$ with $Q^TBQ = B$ form the orthogonal group of the symmetric bilinear form with matrix $B$.
For $B = I$ over $\R$ this gives $O(n)$, and for $B = \operatorname{diag}(1, 1, 1, -1)$ it gives the Lorentz group of special relativity.
The [[Cartan-Dieudonné theorem|0VMWGYY35Q]] writes every element of $O(n)$ as a product of at most $n$ reflections, and the [[Cayley transform|HKQ5YY027B]] parametrizes the rotations without the eigenvalue $-1$ by skew-symmetric matrices.
