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

Over the real numbers a normal operator need not have an orthonormal eigenbasis, but it always becomes block diagonal, with blocks of size $1$ and rotation-and-scaling blocks of size $2$, in a suitable orthonormal basis.

1. Matrix form. Let $A$ be a real $n \times n$ [[normal matrix|0XYKE8BE7X]], so $A A^{\mathsf{T}} = A^{\mathsf{T}} A$. Then there is a real [[orthogonal matrix|0QRBVFJ50X]] $Q$ such that $Q^{\mathsf{T}} A Q$ is [[block diagonal|0M0SNKZ482]], and each diagonal block is either a real $1 \times 1$ block $(c)$ or a $2 \times 2$ block
$$\begin{pmatrix} a & -b \\ b & a \end{pmatrix} \qquad \text{with } a, b \in \mathbb{R} \text{ and } b > 0.$$
2. Operator form. Let $V$ be a finite-dimensional real inner product space, and let $T \colon V \to V$ be [[normal|0ENZN5G4CV]]. Then $V$ has an [[orthonormal basis|0FWJ0VW561]] in which the matrix of $T$ has the form of part 1.
3. Skew-symmetric case. If $A$ is [[skew-symmetric|03RNVFDEAN]], so $A^{\mathsf{T}} = -A$, then every $1 \times 1$ block is $(0)$, and every $2 \times 2$ block is $\begin{pmatrix} 0 & -b \\ b & 0 \end{pmatrix}$ with $b > 0$.

The $1 \times 1$ blocks are the real eigenvalues of $A$, and each $2 \times 2$ block carries one pair of non-real eigenvalues $a + ib$ and $a - ib$.

## Remarks

### A first example

The cyclic permutation matrix $A$ with $A e_1 = e_2$, $A e_2 = e_3$ and $A e_3 = e_1$ is orthogonal, so it is normal.
It fixes $u_3 = \tfrac{1}{\sqrt{3}}(1, 1, 1)$, which gives a $1 \times 1$ block $(1)$.
On the plane orthogonal to $u_3$, take the orthonormal basis $u_1 = \tfrac{1}{\sqrt{2}}(1, -1, 0)$ and $u_2 = \tfrac{1}{\sqrt{6}}(1, 1, -2)$.
Expanding $A u_1$ and $A u_2$ in this basis gives
$$A u_1 = -\tfrac{1}{2} u_1 + \tfrac{\sqrt{3}}{2} u_2, \qquad A u_2 = -\tfrac{\sqrt{3}}{2} u_1 - \tfrac{1}{2} u_2.$$
So with $Q = (u_1, u_2, u_3)$ we get one block with $a = -\tfrac{1}{2}$ and $b = \tfrac{\sqrt{3}}{2}$, a rotation by $120$ degrees, and the block $(1)$.
Check: the eigenvalues $1$ and $-\tfrac{1}{2} \pm \tfrac{\sqrt{3}}{2} i$ are the three cube roots of $1$, as they must be, since $A^3 = I$.

### Why each hypothesis is needed

Normality is needed.
The [[shear|BF9MKKHH4Z]] with rows $(1, 1)$ and $(0, 1)$ has the single eigenvalue $1$, so its normal form could only be the identity matrix, and the shear is not the identity.
The $2 \times 2$ blocks are needed because the field is $\mathbb{R}$.
The [[rotation by a right angle|1CF483TZZA]] is normal and has no real eigenvalue, so no real orthonormal basis makes it diagonal; it is already one block with $a = 0$ and $b = 1$.

### What it gives you

A real orthogonal matrix has the same form with $1 \times 1$ blocks $\pm 1$ and $2 \times 2$ blocks with $a^2 + b^2 = 1$, because each block of an orthogonal block diagonal matrix is orthogonal.
These blocks are the rotations $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ with $0 < \theta < \pi$.
A real skew-symmetric matrix has even rank, because its rank is twice the number of its $2 \times 2$ blocks.
So a skew-symmetric matrix of odd size has at least one block $(0)$ and determinant $0$.
A real normal matrix whose eigenvalues are all real has no $2 \times 2$ blocks, so it is orthogonally similar to a diagonal matrix and is symmetric.

### The converse and the complex picture

Every matrix $Q M Q^{\mathsf{T}}$ with $Q$ orthogonal and $M$ of the form of part 1 is normal.
The reason is that each block $B = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ satisfies $B B^{\mathsf{T}} = (a^2 + b^2) I = B^{\mathsf{T}} B$, and conjugation by $Q$ keeps the identity $M M^{\mathsf{T}} = M^{\mathsf{T}} M$.

Over $\mathbb{C}$, the block $B$ is diagonal in the basis $(1, -i)$, $(1, i)$, with the eigenvalues $a + ib$ and $a - ib$.
Check: $B (1, -i) = (a + ib, b - ia) = (a + ib)(1, -i)$.
So part 1 is the real shadow of the [[complex spectral theorem|04CW1P44VD]], and its [[proof|7QN4QQGW33]] starts from the real Schur form.

### Watch out

The sign of $b$ depends on the order and the orientation of the two basis vectors of each plane.
Swapping $u_1$ and $u_2$, or replacing $u_2$ by $-u_2$, turns $b$ into $-b$, which is why the statement can demand $b > 0$.
Do not read the blocks as eigenvalues either: the block with $a = 0$ and $b = 1$ has eigenvalues $\pm i$, not $0$ and $1$.

### Try it

Find the normal form of $A = \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}$.
It is normal, since $A A^{\mathsf{T}} = 5I = A^{\mathsf{T}} A$, and it is already one block with $a = 1$ and $b = 2$, carrying the eigenvalues $1 \pm 2i$.

## Explanations

### L1 human

A real normal matrix splits space into perpendicular lines and perpendicular planes that it maps to themselves.
On each line it stretches by a real number.
On each plane it turns every vector by the same angle and stretches it by the same factor.
A skew-symmetric matrix does no stretching on the lines, and on each plane it only turns by a right angle and scales.

### L2 human

Here is a typical use: the cross product with $\omega = (1, 2, 3)$, which has the skew-symmetric matrix $K = \begin{pmatrix} 0 & -3 & 2 \\ 3 & 0 & -1 \\ -2 & 1 & 0 \end{pmatrix}$.
First, $K \omega = \omega \times \omega = 0$, so $u_3 = \tfrac{1}{\sqrt{14}}(1, 2, 3)$ gives the block $(0)$.
Next take $u_1 = \tfrac{1}{\sqrt{5}}(2, -1, 0)$, which is orthogonal to $\omega$, and compute $\omega \times (2, -1, 0) = (3, 6, -5)$, of length $\sqrt{70}$.
So $u_2 = \tfrac{1}{\sqrt{70}}(3, 6, -5)$ and $K u_1 = \sqrt{70 / 5}\, u_2 = \sqrt{14}\, u_2$.
The rule $\omega \times (\omega \times x) = -\norm{\omega}^2 x$ for $x \perp \omega$ gives $K u_2 = -\sqrt{14}\, u_1$.
With $Q = (u_1, u_2, u_3)$,
$$Q^{\mathsf{T}} K Q = \begin{pmatrix} 0 & -\sqrt{14} & 0 \\ \sqrt{14} & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
So the [[cross product|0N5N15HWZ7]] with $\omega$ is a turn by a right angle in the plane orthogonal to $\omega$, followed by scaling by $\norm{\omega} = \sqrt{14}$.

### L3 human

The theorem classifies real normal operators up to orthogonal similarity: the list of blocks, with $b > 0$, is unique up to order.
For skew-symmetric matrices, it is the normal form of an element of the Lie algebra $\mathfrak{so}(n)$ under conjugation by $O(n)$.
For a rotation in $SO(n)$, the form says that it is conjugate to an element of the standard [[maximal torus|Z2AJFZQTWT]] of block rotations.
The theory of isometries uses this form to describe the orthogonal matrices, and the complex version is the unitary diagonalization of the [[complex spectral theorem|04CW1P44VD]].
