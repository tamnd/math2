---
tag: 2ZVG43GSKA
kind: statement
role: theorem
name: Classification of O(3) and Euler's rotation theorem
aliases: [eulers-rotation-theorem, axis-angle-form-of-a-rotation, classification-of-o-3]
msc: ["70B10", "15B10", "51F25"]
topics: [AZS5BPF5H3]
audience: ug2
about: [0CGYNDCWRR, 0HFREYRSZP, 6WBVP2PB1Y, WWK2E8BRGF]
uses: [GPWRS6HSNR, 0XNZWJ96HK, 0BQAA2BK3Q, 0N6960W0BV, 00KDZRW4C0, 0XC1RDBY7A, 0FWJ0VW561]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem
    locator: Matrix proof
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Determining the angle
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Lower dimensions
same_as:
  wikidata: Q681406
  wikipedia: Euler's rotation theorem
---

## Statement

Every rotation of space about the origin turns space about one fixed axis, the trace of its matrix gives the angle, and every other element of $O(3)$ is such a rotation followed by a reflection.

Let $R \in SO(3)$, so $R$ is a real $3 \times 3$ matrix with $R^{\mathsf{T}}R = I_3$ and $\det R = 1$.

1. (Euler's rotation theorem.) There is a unit vector $u \in \R^3$ with $Ru = u$.
2. There are an [[orthonormal basis|0FWJ0VW561]] $u, v, w$ of $\R^3$ with $w = u \times v$ and an angle $\theta \in [0, \pi]$ such that $Ru = u$, $Rv = \cos\theta\,v + \sin\theta\,w$ and $Rw = -\sin\theta\,v + \cos\theta\,w$. So $R$ is the [[rotation|0XNZWJ96HK]] by $\theta$ about the axis $\R u$.
3. The trace is $\tr R = 1 + 2\cos\theta$.
4. We have $R - R^{\mathsf{T}} = 2\sin\theta\,[u]_\times$, where $[u]_\times = \begin{pmatrix} 0 & -u_3 & u_2 \\ u_3 & 0 & -u_1 \\ -u_2 & u_1 & 0 \end{pmatrix}$ is the matrix of $x \mapsto u \times x$. So for $0 < \theta < \pi$ the axis is $u = \frac{1}{2\sin\theta}(r_{32} - r_{23}, \ r_{13} - r_{31}, \ r_{21} - r_{12})$.
5. (The other coset.) Let $Q \in O(3)$ with $\det Q = -1$. Then $-Q \in SO(3)$, and in some orthonormal basis $u, v, w$ as in part 2 the matrix of $Q$ is $\begin{pmatrix} -1 & 0 \\ 0 & R(\psi) \end{pmatrix}$ with $\psi \in [0, \pi]$. For $\psi = 0$, $Q$ is the reflection in $u^\perp$, and for $\psi = \pi$, $Q = -I_3$.

## Remarks

### Why each hypothesis is needed

Part 1 needs $\det R = 1$.
The matrix $-I_3$ is orthogonal with determinant $-1$, and it fixes no vector other than $0$.
Part 1 also needs the odd dimension $3$.
In $\R^4$ the block matrix $\operatorname{diag}(R(\pi/2), R(\pi/2))$ is orthogonal with determinant $1$, but it fixes no vector other than $0$, because each block turns its own plane by a right angle.
Part 4 gives the axis only for $0 < \theta < \pi$.
For $\theta = \pi$ the matrix $R$ is symmetric and $R - R^{\mathsf{T}} = 0$, so we take instead a unit vector $u$ in the kernel of $R - I_3$, and then $R = 2uu^{\mathsf{T}} - I_3$.

### Reading the axis and the angle

Take the cyclic permutation matrix $R = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$ of [[the cyclic permutation example|E6SGA0X325]].
Its trace is $0$, so part 3 gives
$$1 + 2\cos\theta = 0, \qquad \cos\theta = -\tfrac{1}{2}, \qquad \theta = \tfrac{2\pi}{3}.$$
The three differences of part 4 are $r_{32} - r_{23} = 1 - 0$, $r_{13} - r_{31} = 1 - 0$ and $r_{21} - r_{12} = 1 - 0$, and $2\sin\theta = \sqrt{3}$.
So the axis is $u = \frac{1}{\sqrt{3}}(1, 1, 1)$.
Check: $R$ permutes the coordinates, so $R(1, 1, 1) = (1, 1, 1)$.
The [[rotation by sixty degrees about the diagonal|TFWTJ9K6K7]] works the same way with trace $2$.

### What it gives you

Each element of $SO(3)$ is a rotation about an axis, so the name "rotation group" for $SO(3)$ is justified.
The product of two rotations of space is again a rotation about some axis, even when the two axes differ.
The angle $\theta = \arccos\frac{\tr R - 1}{2}$ is a conjugacy invariant, and two elements of $SO(3)$ are conjugate in $SO(3)$ exactly when they have the same angle.
The element $Q$ of part 5 is an *improper rotation* or *rotary reflection*: a rotation by $\psi$ about $u$ followed by the reflection in $u^\perp$.
Since $\det Q = -1$ forces the eigenvalue $-1$ in the same way that part 1 forces the eigenvalue $1$, every improper rotation reverses some line.

### Euler angles

Euler's rotation theorem gives one axis and one angle.
A different description uses three angles about fixed coordinate axes: every $R \in SO(3)$ can be written as $R_z(\alpha) R_x(\beta) R_z(\gamma)$, where $R_x$ and $R_z$ are the [[basic rotations about the coordinate axes|F1KZ5GE4TC]].
The numbers $\alpha, \beta, \gamma$ are the [[Euler angles|7WGBNTRQ2S]] of $R$.
Watch out: the two descriptions are different, and the Euler angles depend on a convention for the order of the axes.

### The converse

For each unit vector $u$ and each angle $\theta$, the matrix described in part 2 lies in $SO(3)$, and [[Rodrigues' rotation formula|WS52X8SGC4]] gives it in closed form.
So the pairs $(u, \theta)$ describe all of $SO(3)$.
The pair is unique for $0 < \theta < \pi$, while $(u, \pi)$ and $(-u, \pi)$ give the same half turn, and every axis gives the identity for $\theta = 0$.

### Generalizations

In $\R^n$, each orthogonal matrix has a block diagonal [[normal form|QTY3VMFGY1]] with blocks $R(\theta_j)$, $1$ and $-1$, and part 2 is the case $n = 3$.
For every odd $n$, each element of $SO(n)$ fixes a nonzero vector, by the determinant argument of part 1.
For rigid motions that include translations, the analogue is [[Chasles' theorem|X4R728TVZE]].

## History

The theorem is named after Euler, who proved it with spherical geometry.

## Explanations

### L1 human

However you turn a ball about its center, the end result is a single turn about one fixed axis.
The two points where that axis meets the surface of the ball end where they started.
For example, the turn that sends the $x$-axis to the $y$-axis, the $y$-axis to the $z$-axis and the $z$-axis to the $x$-axis is one turn by a third of a full circle about the diagonal line through $(1, 1, 1)$.
A mirror image of space is such a turn followed by one mirror.

### L2 human

Here is a typical use: decide what the matrix $R = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$ does to space.
First check that $R \in SO(3)$: the columns are $e_1$, $e_3$ and $-e_2$, which are orthonormal, and the determinant is $1 \cdot (0 \cdot 0 - (-1) \cdot 1) = 1$.
The trace is $1$, so
$$1 + 2\cos\theta = 1, \qquad \theta = \tfrac{\pi}{2}.$$
Part 4 gives $(r_{32} - r_{23}, r_{13} - r_{31}, r_{21} - r_{12}) = (2, 0, 0)$, and dividing by $2\sin\theta = 2$ gives the axis $u = e_1$.
So $R$ is the quarter turn about the $x$-axis that sends $e_2$ to $e_3$.
Watch out: the trace gives only $\cos\theta$, and the direction of the turn is fixed by the sign chosen for $u$.

### L3 human

The theorem shows that $SO(3)$ is the image of the closed ball of radius $\pi$ in $\R^3$ under $\theta u \mapsto$ (rotation by $\theta$ about $u$), with antipodal points of the boundary sphere identified.
So $SO(3)$ is homeomorphic to the real projective space $\R P^3$, and its fundamental group is $\Z/2\Z$; the [[rotation group SO(3)|263GGJFA21]] treats this space.
The axis-angle form also gives $R = \exp(\theta[u]_\times)$, so the exponential map from the skew-symmetric matrices onto $SO(3)$ is surjective.
In rigid body kinematics, the infinitesimal version of the axis is the [[angular velocity|2FTZ7D8Z0F]] vector.
