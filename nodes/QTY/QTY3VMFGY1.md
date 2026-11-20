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

Let $Q$ be a real $n \times n$ [[orthogonal matrix|0QRBVFJ50X]], and let $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

1. There are an orthogonal matrix $P$, integers $k, q, p \ge 0$ with $2k + q + p = n$, and angles $0 < \theta_1 \le \dots \le \theta_k < \pi$ such that $P^TQP$ is the [[block diagonal matrix|0M0SNKZ482]]
$$P^TQP = \operatorname{diag}\left(R(\theta_1), \dots, R(\theta_k), -I_q, I_p\right).$$
2. The numbers $k$, $q$, $p$ and the angles $\theta_1, \dots, \theta_k$ are determined by $Q$. The non-real roots of the [[characteristic polynomial|039HF58KQ5]] of $Q$ are $e^{\pm i\theta_j}$, and $q$ and $p$ are the multiplicities of the roots $-1$ and $1$.
3. $\det Q = (-1)^q$. So $Q \in SO(n)$ exactly when $q$ is even.

## Remarks

### Why each hypothesis is needed

- Orthogonality is needed for the blocks $R(\theta)$ and $\pm 1$. The diagonal matrix $\operatorname{diag}(2, 1)$ is normal, and its block $(2)$ is not $\pm 1$.
- The $2 \times 2$ blocks are needed over $\R$. The rotation $R(\pi/2)$ has no real eigenvalue, so no real orthogonal $P$ makes $P^TR(\pi/2)P$ diagonal.

### Consequences

- For $Q \in SO(n)$, $q$ is even, and the pairs of entries $-1$ form blocks $R(\pi) = -I_2$. So each rotation is a product of commuting rotations in perpendicular planes.
- For $n = 2$, this gives [[the classification of O(2)|C97Z06HHB2]] up to a change of orthonormal basis. For $n = 3$, it gives [[Euler's rotation theorem|2ZVG43GSKA]].
- Each $Q \in SO(n)$ is $\exp(A)$ for a real skew-symmetric matrix $A$, because $R(\theta) = \exp\begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$.
- $SO(n)$ is connected: replacing each $\theta_j$ by $t\theta_j$, and each block $R(\pi)$ by $R(t\pi)$, for $t \in [0, 1]$, gives a path from $I_n$ to $Q$.

### Converse

Each matrix $P\operatorname{diag}(R(\theta_1), \dots, R(\theta_k), -I_q, I_p)P^T$ with $P$ orthogonal is orthogonal, because it is a product of orthogonal matrices.
So the normal forms describe exactly the orthogonal matrices.
Two orthogonal matrices are similar by an orthogonal matrix exactly when they have the same normal form.

### Generalizations

- The theorem is the orthogonal case of [[the normal form of a real normal operator|G6T1FNE3JC]].
- For a unitary matrix, the analogue is the diagonal form $\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n})$, by [[the properties of unitary matrices|GZ7NG7J3J8]].

## Explanations

### L1 human

Each map that keeps lengths and the origin splits space into perpendicular pieces.
Some pieces are planes, and on each plane the map is a turn.
Some pieces are lines, and on each line the map keeps or flips the direction.
The determinant counts the flips: it is $-1$ when the number of flips is odd.

### L2 human

Worked example: $Q = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$, see [[this example|TFWTJ9K6K7]].

1. $Q$ fixes $u_3 = \frac{1}{\sqrt{3}}(1, 1, 1)$, because each row of $3Q$ has sum $3$.
2. Take the orthonormal basis $u_1 = \frac{1}{\sqrt{2}}(1, -1, 0)$ and $u_2 = \frac{1}{\sqrt{6}}(1, 1, -2)$ of the plane $u_3^\perp$.
3. $Qu_1 = \frac{1}{\sqrt{2}}(1, 0, -1)$. Its dot products with $u_1$ and $u_2$ are $\frac{1}{2}$ and $\frac{3}{\sqrt{12}} = \frac{\sqrt{3}}{2}$.
4. So $Qu_1 = \frac{1}{2}u_1 + \frac{\sqrt{3}}{2}u_2$, and in the same way $Qu_2 = -\frac{\sqrt{3}}{2}u_1 + \frac{1}{2}u_2$.
5. With $P = (u_1, u_2, u_3)$, $P^TQP = \operatorname{diag}(R(\pi/3), 1)$. So $k = 1$, $q = 0$, $p = 1$ and $\theta_1 = \frac{\pi}{3}$.

The typical use: the normal form reduces a question about one orthogonal matrix to questions about $2 \times 2$ rotations.
A trap: the matrix $P$ is not unique, and the order of the blocks is a convention.

### L3 human

Let $n = 2m$ or $n = 2m + 1$, and let $T$ be the group of block matrices $\operatorname{diag}(R(\phi_1), \dots, R(\phi_m))$, with a last entry $1$ when $n$ is odd.
The theorem says that each element of $SO(n)$ is conjugate in $SO(n)$ to an element of the torus $T$.
The angles are the conjugacy invariants, so the conjugacy classes of $SO(n)$ are parametrized by the angles modulo the Weyl group.
This is the case of $SO(n)$ in the theory of maximal tori of compact Lie groups, which belongs to the area of Lie groups.
