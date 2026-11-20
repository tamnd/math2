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

A real $n \times n$ matrix $Q$ is *orthogonal* when $Q^TQ = I_n$, where $Q^T$ is the [[transpose|09DXWYRD43]] and $I_n$ is the identity matrix.
[[Equivalently|F7M8ZXB4P7]], $Q$ is invertible with $Q^{-1} = Q^T$, and its columns form an [[orthonormal basis|0S9GGTR0EX]] of $\R^n$ for the dot product, and so do its rows.
Orthogonal matrices are the matrices of the [[linear isometries|07SJXTWVQW]] of $\R^n$: the map $x \mapsto Qx$ keeps all lengths and angles exactly when $Q$ is orthogonal.
They describe the changes between orthonormal bases, so they appear in every computation that must not distort lengths.

## Motivation

A change of basis in $\R^n$ is given by an invertible matrix $P$, and its inverse is usually hard to compute.
When the new basis is orthonormal, the coordinates of a vector are its dot products with the basis vectors.
So the inverse of $P$ is its transpose, and no computation is needed.
The same matrices describe the rigid motions of $\R^n$ that fix the origin, such as rotations and reflections.

## Notation

- The set of real orthogonal $n \times n$ matrices is the [[orthogonal group|~dc22fe40]] $O(n)$, also written $O_n(\R)$ or $O(n, \R)$.
- Mathlib writes `Matrix.orthogonalGroup n ℝ` for this set. It is defined for any ring with an involution as the matrices with $A^*A = 1$, so over $\C$ it gives the unitary matrices.
- Some books say "orthonormal matrix", because the columns are orthonormal, not only orthogonal.
- A warning on words: some authors call a map an "orthogonal transformation" only when it is a rotation, so only when $\det Q = 1$. Here an orthogonal transformation is any linear isometry, with $\det Q = \pm 1$.
- A complex matrix with $Q^TQ = I$ is a *complex orthogonal matrix*. It is not the same as a [[unitary matrix|0AR68JTMDT]], see [[this example|~83b36d34]].

## Remarks

### Examples

- The identity matrix $I_n$ is orthogonal.
- The [[rotation matrix|~8cba9603]] $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ is orthogonal, because its columns are unit vectors with dot product $0$.
- Each [[permutation matrix|08SP3DF8NB]] is orthogonal, because its columns are the standard basis vectors in another order.
- A diagonal matrix with entries $\pm 1$ is orthogonal.
- The [[Householder matrix|~c7e61f61]] $I - 2vv^T$ of a unit vector $v$ is orthogonal and symmetric.
- [[The matrix $\frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$|~129123c7]] is orthogonal, and it is a rotation of $\R^3$ about the axis through $(1, 1, 1)$.

### Non-examples

- [[The matrix $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$|~28937827]] has orthogonal columns, but they have length $\sqrt{2}$, so $Q^TQ = 2I$.
- The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, but its second column $(1, 1)$ is not a unit vector.
- A $3 \times 2$ matrix with orthonormal columns satisfies $Q^TQ = I_2$, but it is not square, so it is not an orthogonal matrix.

### Basic properties

- [[Equivalent conditions|F7M8ZXB4P7]]: $Q^TQ = I$, $QQ^T = I$, $Q^{-1} = Q^T$, orthonormal columns, orthonormal rows, and $\norm{Qx} = \norm{x}$ for all $x$.
- [[Determinant and eigenvalues|~d705bf24]]: $\det Q = \pm 1$, and every complex eigenvalue of $Q$ has absolute value $1$.
- Products, inverses and transposes of orthogonal matrices are orthogonal. So the orthogonal $n \times n$ matrices form the [[group|G5S1M9]] $O(n)$.
- An orthogonal matrix is [[normal|0MR0BYF0K2]], because $QQ^T = I = Q^TQ$.
- In a suitable orthonormal basis, an orthogonal matrix is block diagonal with blocks $\pm 1$ and $2 \times 2$ rotations, by the [[normal form|~ff85d703]].

### History

Cayley described in 1846 a map that sends skew-symmetric matrices to special orthogonal matrices.
This map is now called the [[Cayley transform|~be1c3d3e]], and it gives a rational description of orthogonal matrices.

### Common errors

- Orthogonal columns are not enough: the columns must also be unit vectors. The matrix $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$ is not orthogonal.
- Determinant $\pm 1$ is not enough: the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$ and is not orthogonal.
- Over $\C$, the right condition is $U^*U = I$ with the conjugate transpose, not $U^TU = I$.

## Explanations

### L1 human

An orthogonal matrix describes a turn or a mirror image of space that keeps the origin in place.
Its columns are arrows of length $1$ that are perpendicular to each other.
For example, the columns of $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ are $(0, 1)$ and $(-1, 0)$.
Both have length $1$, and they meet at a right angle.
This matrix turns the plane by a quarter turn.

### L2 human

Worked example: we test $Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.

1. The first column is $\frac{1}{\sqrt{2}}(1, 1)$, with squared length $\frac{1 + 1}{2} = 1$.
2. The second column is $\frac{1}{\sqrt{2}}(1, -1)$, with squared length $1$.
3. The dot product of the columns is $\frac{1}{2}(1 - 1) = 0$.
4. So $Q^TQ = I$, and $Q^{-1} = Q^T = Q$.
5. $\det Q = \frac{1}{2}(-1 - 1) = -1$, so $Q$ is not a rotation. It is the reflection in the line through $(1, \sqrt{2} - 1)$, at the angle $\pi/8$.

The typical use: to solve $Qx = b$, compute $x = Q^Tb$, which needs no elimination.
A trap: to check that a matrix is orthogonal, check both the dot products of the columns and their lengths.

### L3 human

The orthogonal matrices form the compact group $O(n)$, the group of symmetries of the dot product.
Over any field, the matrices $Q$ with $Q^TBQ = B$ form the orthogonal group of the symmetric bilinear form with matrix $B$.
For $B = I$ over $\R$, this gives $O(n)$, and for $B = \operatorname{diag}(1, 1, 1, -1)$ it gives the Lorentz group of special relativity.
Numerical linear algebra prefers orthogonal matrices, because multiplication by them does not change the size of errors.
This is the reason for the QR decomposition, Householder reflections and Givens rotations.
