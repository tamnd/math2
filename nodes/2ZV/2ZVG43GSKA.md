---
tag: 2ZVG43GSKA
kind: statement
role: theorem
name: Classification of O(3) and Euler's rotation theorem
aliases: [eulers-rotation-theorem, axis-angle-form-of-a-rotation, classification-of-o-3]
msc: ["70B10", "15B10", "51F25"]
topics: [AZS5BPF5H3]
audience: ug2
about: [0CGYNDCWRR, 0HFREYRSZP, ~5781ca68, ~dc22fe40]
uses: [~7e2db5c6, 0XNZWJ96HK, 0BQAA2BK3Q, 0N6960W0BV, 00KDZRW4C0, 0XC1RDBY7A, 0FWJ0VW561]
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

Let $R \in SO(3)$, so $R$ is a real $3 \times 3$ matrix with $R^TR = I_3$ and $\det R = 1$.

1. (Euler's rotation theorem.) There is a unit vector $u \in \R^3$ with $Ru = u$.
2. There are an [[orthonormal basis|0FWJ0VW561]] $u, v, w$ of $\R^3$ with $w = u \times v$ and an angle $\theta \in [0, \pi]$ such that $Ru = u$, $Rv = \cos\theta\,v + \sin\theta\,w$ and $Rw = -\sin\theta\,v + \cos\theta\,w$. So $R$ is the [[rotation|0XNZWJ96HK]] by $\theta$ about the axis $\R u$.
3. $\tr R = 1 + 2\cos\theta$.
4. $R - R^T = 2\sin\theta\,[u]_\times$, where $[u]_\times = \begin{pmatrix} 0 & -u_3 & u_2 \\ u_3 & 0 & -u_1 \\ -u_2 & u_1 & 0 \end{pmatrix}$ is the matrix of $x \mapsto u \times x$. So for $0 < \theta < \pi$, the axis is $u = \frac{1}{2\sin\theta}(r_{32} - r_{23}, \ r_{13} - r_{31}, \ r_{21} - r_{12})$.
5. (The other coset.) Let $Q \in O(3)$ with $\det Q = -1$. Then $-Q \in SO(3)$. In some orthonormal basis $u, v, w$ as in part 2, $Q$ has the matrix $\begin{pmatrix} -1 & 0 \\ 0 & R(\psi) \end{pmatrix}$ with $\psi \in [0, \pi]$. For $\psi = 0$, $Q$ is the reflection in $u^\perp$, and for $\psi = \pi$, $Q = -I_3$.

## Remarks

### Why each hypothesis is needed

- Part 1 needs $\det R = 1$. The matrix $-I_3$ is orthogonal with determinant $-1$, and it fixes no vector other than $0$.
- Part 1 needs an odd dimension. In $\R^4$, the block matrix $\operatorname{diag}(R(\pi/2), R(\pi/2))$ has determinant $1$, and it fixes no vector other than $0$.
- Part 4 gives the axis only for $0 < \theta < \pi$. For $\theta = \pi$, $R$ is symmetric and $R - R^T = 0$. Then $u$ is a unit vector in the kernel of $R - I_3$, and $R = 2uu^T - I_3$.

### Consequences

- Each element of $SO(3)$ is a rotation about an axis. So the name "rotation" for the elements of $SO(3)$ is justified.
- The angle of $R$ is $\theta = \arccos\frac{\tr R - 1}{2}$. Two elements of $SO(3)$ are conjugate in $SO(3)$ exactly when they have the same angle.
- The product of two rotations of space is a rotation about some axis, although the axes of the factors may differ.
- The element $Q$ of part 5 is a *rotary reflection*: a rotation by $\psi$ about $u$, followed by the reflection in $u^\perp$.

### Converse

For each unit vector $u$ and each angle $\theta$, the matrix of part 2 is in $SO(3)$.
So the pairs $(u, \theta)$ describe all of $SO(3)$, and [[Rodrigues' rotation formula|WS52X8SGC4]] gives the matrix in closed form.
The pair is unique for $0 < \theta < \pi$, while $(u, \pi)$ and $(-u, \pi)$ give the same rotation.

### Generalizations

- In $\R^n$, each orthogonal matrix has a block diagonal normal form with blocks $R(\theta_j)$, $1$ and $-1$, see [[the normal form|~ff85d703]].
- For $n$ odd, each element of $SO(n)$ fixes a nonzero vector, by the argument of part 1.
- For rigid motions with translations, the analogue is [[Chasles' theorem|X4R728TVZE]].

## History

The theorem is named after Euler, who proved it with spherical geometry.

## Explanations

### L1 human

However you turn a ball about its centre, the end result is a single turn about one fixed axis.
The two ends of this axis on the surface end where they started.
The trace of the matrix tells the angle of the turn.
A mirror image of space is a turn followed by one mirror.

### L2 human

Worked example: the cyclic matrix $R = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$, see [[this example|~942de4eb]].

1. $\tr R = 0 = 1 + 2\cos\theta$, so $\cos\theta = -\frac{1}{2}$ and $\theta = \frac{2\pi}{3}$.
2. $r_{32} - r_{23} = 1$, $r_{13} - r_{31} = 1$ and $r_{21} - r_{12} = 1$.
3. $2\sin\theta = \sqrt{3}$, so $u = \frac{1}{\sqrt{3}}(1, 1, 1)$.
4. Check: $Ru = u$, because $R$ permutes the coordinates.

The typical use: read the axis and the angle of a rotation from its matrix.
A trap: the trace gives $\cos\theta$ only, and the sign of $\theta$ depends on the direction of $u$.

### L3 human

The theorem shows that $SO(3)$ is the image of the closed ball of radius $\pi$ under $(u, \theta) \mapsto \theta u$, with antipodal points of the boundary sphere identified.
So $SO(3)$ is homeomorphic to the real projective space $\R P^3$, and its fundamental group is $\Z/2\Z$.
The axis-angle form also gives $R = \exp(\theta[u]_\times)$, so the exponential map onto $SO(3)$ is surjective.
In rigid body kinematics, the infinitesimal version gives the [[angular velocity|2FTZ7D8Z0F]] vector.
