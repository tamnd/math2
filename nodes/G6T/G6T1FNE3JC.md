---
tag: G6T1FNE3JC
kind: statement
role: theorem
name: Normal form of a real normal operator
aliases: [real-normal-form, block-diagonalization-of-real-normal-matrices]
msc: ["15A21", "47B15"]
topics: [3YM9EK6VMB]
audience: grad
about: [0C8BR8XRTR, 0PBY4E9GQF]
uses: [0ENZN5G4CV, 0XYKE8BE7X, 0QRBVFJ50X, 0FWJ0VW561, 0M0SNKZ482, 03RNVFDEAN]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Spectral theory
  - book: isbn:9783319110790
    locator: Section 9.B
---

## Statement

1. Matrix form. Let $A$ be a real $n \times n$ [[normal matrix|0XYKE8BE7X]], so $A A^T = A^T A$. Then there is a real [[orthogonal matrix|0QRBVFJ50X]] $Q$ such that $Q^T A Q$ is [[block diagonal|0M0SNKZ482]]. Each diagonal block is a real $1 \times 1$ block $(c)$ or a $2 \times 2$ block
$$\begin{pmatrix} a & -b \\ b & a \end{pmatrix} \quad \text{with } a, b \in \mathbb{R} \text{ and } b > 0.$$
2. Operator form. Let $V$ be a finite-dimensional real inner product space, and let $T \colon V \to V$ be [[normal|0ENZN5G4CV]]. Then $V$ has an [[orthonormal basis|0FWJ0VW561]] in which the matrix of $T$ has the form of part 1.
3. Skew-symmetric case. If $A$ is [[skew-symmetric|03RNVFDEAN]], so $A^T = -A$, then every $1 \times 1$ block is $(0)$, and every $2 \times 2$ block is $\begin{pmatrix} 0 & -b \\ b & 0 \end{pmatrix}$ with $b > 0$.

The $1 \times 1$ blocks are the real eigenvalues of $A$.
Each $2 \times 2$ block carries the pair of eigenvalues $a + ib$ and $a - ib$.

## Remarks

### Why each hypothesis is needed

- Normality is needed. [[The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$|BF9MKKHH4Z]] has the only eigenvalue $1$, so the form of part 1 would be the identity matrix. But the shear is not the identity.
- The $2 \times 2$ blocks are needed over $\mathbb{R}$. [[The rotation by a right angle|1CF483TZZA]] is normal and has no real eigenvalue, so no real orthonormal basis makes it diagonal. It is already one block with $a = 0$ and $b = 1$.

### Consequences

- A real orthogonal matrix has the same form with $1 \times 1$ blocks $\pm 1$ and $2 \times 2$ blocks with $a^2 + b^2 = 1$. These blocks are the rotations $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ with $0 < \theta < \pi$. The reason: each block of an orthogonal block diagonal matrix is orthogonal.
- A real skew-symmetric matrix has even rank, because its rank is twice the number of $2 \times 2$ blocks.
- A real skew-symmetric matrix of odd size has determinant $0$, because at least one block is $(0)$.
- A real normal matrix with only real eigenvalues is symmetric, because then no $2 \times 2$ block occurs.

### Converse

Every matrix $Q M Q^T$ with $Q$ orthogonal and $M$ of the form of part 1 is normal.
The block $B = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ satisfies $B B^T = (a^2 + b^2) I = B^T B$.
So $M M^T = M^T M$, and conjugation by $Q$ keeps this identity.

### Relation to the complex spectral theorem

Over $\mathbb{C}$, each $2 \times 2$ block is diagonal in the basis $(1, -i)$ and $(1, i)$, with the eigenvalues $a + ib$ and $a - ib$.
So part 1 is the real version of [[the complex spectral theorem|04CW1P44VD]].
The proof uses [[the real Schur form|V1JG4C7R7B]] and shows that a normal block triangular matrix is block diagonal.

## Explanations

### L1 human

A real normal matrix splits the space into perpendicular lines and perpendicular planes.
On each line it stretches by a real number.
On each plane it rotates and stretches by the same factor in all directions.
A skew-symmetric matrix does no stretching on the lines and only rotates the planes.

### L2 human

Worked example: the cross product with $\omega = (1, 2, 3)$.

1. The map $x \mapsto \omega \times x$ has the skew-symmetric matrix $K = \begin{pmatrix} 0 & -3 & 2 \\ 3 & 0 & -1 \\ -2 & 1 & 0 \end{pmatrix}$.
2. $K \omega = \omega \times \omega = 0$, so $u_3 = \tfrac{1}{\sqrt{14}}(1, 2, 3)$ spans the $1 \times 1$ block $(0)$.
3. Take $u_1 = \tfrac{1}{\sqrt{5}}(2, -1, 0)$, which is orthogonal to $\omega$. Then $\omega \times (2, -1, 0) = (3, 6, -5)$, and $u_2 = \tfrac{1}{\sqrt{70}}(3, 6, -5)$.
4. So $K u_1 = \sqrt{14}\, u_2$, because $\sqrt{70} / \sqrt{5} = \sqrt{14}$. Similarly $K u_2 = -\sqrt{14}\, u_1$.
5. With $Q = (u_1, u_2, u_3)$, we get $Q^T K Q = \begin{pmatrix} 0 & -\sqrt{14} & 0 \\ \sqrt{14} & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.

The block is a rotation by a right angle times $\sqrt{14} = \norm{\omega}$, in the plane orthogonal to $\omega$.
A trap: the sign of $b$ depends on the order of $u_1$ and $u_2$.
Swapping them, or changing the sign of one, changes $b$ to $-b$.

### L3 human

The theorem classifies real normal operators up to orthogonal equivalence: the list of blocks is unique up to order.
For skew-symmetric matrices, it is the normal form of an element of the Lie algebra $\mathfrak{so}(n)$ under the adjoint action of $O(n)$.
For a rotation in $SO(n)$, the form of the consequences says that it is conjugate under $O(n)$ to an element of the standard maximal torus.
