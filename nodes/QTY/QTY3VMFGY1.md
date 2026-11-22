---
tag: QTY3VMFGY1
kind: statement
role: theorem
name: Normal form of an orthogonal matrix
aliases: [canonical-form-of-orthogonal-matrices, block-diagonal-form-of-orthogonal-matrices]
msc: ["15B10", "15A21"]
topics: [AZS5BPF5H3]
audience: grad
about: [0W02QESPJQ, WWK2E8BRGF]
uses: [0QRBVFJ50X, 0M0SNKZ482, 039HF58KQ5, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Canonical form
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Canonical form
---

## Statement

In a suitable orthonormal basis, every orthogonal matrix splits into rotations of perpendicular planes and entries $\pm 1$ on perpendicular lines.

Let $Q$ be a real $n \times n$ [[orthogonal matrix|0QRBVFJ50X]], and let $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

1. There are an orthogonal matrix $P$, integers $k, q, p \ge 0$ with $2k + q + p = n$, and angles $0 < \theta_1 \le \dots \le \theta_k < \pi$ such that $P^{\mathsf{T}}QP$ is the [[block diagonal matrix|0M0SNKZ482]]
$$P^{\mathsf{T}}QP = \operatorname{diag}\left(R(\theta_1), \dots, R(\theta_k), -I_q, I_p\right).$$
2. The numbers $k$, $q$, $p$ and the angles $\theta_1, \dots, \theta_k$ are determined by $Q$. The non-real roots of the [[characteristic polynomial|039HF58KQ5]] of $Q$ are the numbers $e^{\pm i\theta_j}$, and $q$ and $p$ are the multiplicities of the roots $-1$ and $1$.
3. We have $\det Q = (-1)^q$, so $Q \in SO(n)$ exactly when $q$ is even.

## Remarks

### A worked case

Take $Q = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$, the [[rotation by sixty degrees about the diagonal|TFWTJ9K6K7]].
Each row of $3Q$ has sum $3$, so $Q$ fixes $u_3 = \frac{1}{\sqrt{3}}(1, 1, 1)$.
For the plane $u_3^\perp$, take the orthonormal basis $u_1 = \frac{1}{\sqrt{2}}(1, -1, 0)$ and $u_2 = \frac{1}{\sqrt{6}}(1, 1, -2)$.
Multiplying out gives
$$Qu_1 = \tfrac{1}{\sqrt{2}}(1, 0, -1) = \tfrac{1}{2}u_1 + \tfrac{\sqrt{3}}{2}u_2, \qquad Qu_2 = \tfrac{1}{\sqrt{6}}(-1, 2, -1) = -\tfrac{\sqrt{3}}{2}u_1 + \tfrac{1}{2}u_2.$$
Check: $\ip{Qu_1}{u_2} = \frac{1 + 2}{\sqrt{12}} = \frac{\sqrt{3}}{2}$.
So with $P = (u_1, u_2, u_3)$ we get $P^{\mathsf{T}}QP = \operatorname{diag}(R(\pi/3), 1)$, with $k = 1$, $q = 0$, $p = 1$ and $\theta_1 = \frac{\pi}{3}$.

### Why each hypothesis is needed

Orthogonality is what makes the blocks rotations and signs.
The matrix $\operatorname{diag}(2, 1)$ is normal and already block diagonal, but its block $(2)$ is neither $1$ nor $-1$, because it does not keep lengths.
The $2 \times 2$ blocks are needed because we work over $\R$.
The rotation $R(\pi/2)$ has no real eigenvalue, so no real orthogonal $P$ makes $P^{\mathsf{T}}R(\pi/2)P$ diagonal.
Over $\C$ it is diagonalizable, with eigenvalues $i$ and $-i$, but the eigenvectors are not real.

### What it gives you

For $Q \in SO(n)$ the number $q$ is even, so the entries $-1$ pair up into blocks $R(\pi) = -I_2$.
So each rotation of $\R^n$ is a product of commuting rotations in perpendicular planes.
For $n = 3$ this gives [[Euler's rotation theorem|2ZVG43GSKA]], since $2k + q + p = 3$ forces $p \ge 1$ when $q$ is even.
Each $Q \in SO(n)$ is $\exp(A)$ for a real skew-symmetric matrix $A$, because $R(\theta) = \exp\begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$.
The group $SO(n)$ is connected: replacing each angle $\theta_j$ by $t\theta_j$, and each block $R(\pi)$ by $R(t\pi)$, for $t \in [0, 1]$, gives a path from $I_n$ to $Q$ inside $SO(n)$.

### The converse

Each matrix $P\operatorname{diag}(R(\theta_1), \dots, R(\theta_k), -I_q, I_p)P^{\mathsf{T}}$ with $P$ orthogonal is orthogonal, because it is a product of orthogonal matrices.
So the normal forms describe exactly the orthogonal matrices.
Two orthogonal matrices are similar exactly when they have the same normal form, and then they are similar by an orthogonal matrix.

### Generalizations

The theorem is the orthogonal case of [[the normal form of a real normal operator|G6T1FNE3JC]], in which the $2 \times 2$ blocks are $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with any $b > 0$.
For a unitary matrix the analogue is simpler: it is unitarily similar to $\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n})$, by [[the properties of unitary matrices|GZ7NG7J3J8]].

## Explanations

### L1 human

Every map that keeps lengths and keeps the origin fixed splits space into perpendicular pieces.
Some pieces are planes, and on each such plane the map is a turn by some angle.
The other pieces are lines, and on each line the map either keeps the direction or flips it.
The determinant counts the flips: it is $-1$ when the number of flipped lines is odd.

### L2 human

Here is a typical use: decide whether $Q = \operatorname{diag}(R(\pi/2), -1, -1)$ in $O(4)$ lies in $SO(4)$, and find its characteristic polynomial.
The normal form has $k = 1$, $q = 2$ and $p = 0$, so $\det Q = (-1)^2 = 1$ and $Q \in SO(4)$.
The block $R(\pi/2)$ contributes $t^2 - 2t\cos\frac{\pi}{2} + 1 = t^2 + 1$, and the two entries $-1$ contribute $(t + 1)^2$, so
$$\chi_Q(t) = (t^2 + 1)(t + 1)^2.$$
The two entries $-1$ form the block $R(\pi)$, so $Q$ is the product of a quarter turn in one plane and a half turn in the perpendicular plane.
Watch out: the matrix $P$ is not unique, and the order of the blocks is only a convention, but the angles and the numbers $k$, $q$, $p$ do not depend on these choices.

### L3 human

Let $n = 2m$ or $n = 2m + 1$, and let $T$ be the group of block matrices $\operatorname{diag}(R(\phi_1), \dots, R(\phi_m))$, with a last entry $1$ when $n$ is odd.
The theorem says that each element of $SO(n)$ is conjugate in $SO(n)$ to an element of the torus $T$.
The angles are the conjugacy invariants, so the conjugacy classes of $SO(n)$ correspond to the elements of $T$ up to the action of the Weyl group.
This is the case of $SO(n)$ of the theory of maximal tori in compact Lie groups, which belongs to the area of Lie groups.
