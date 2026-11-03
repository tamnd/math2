---
tag: 2ZVG43GSKA
kind: statement
role: theorem
name: Euler's rotation theorem
msc: [70B10, 15B10, 51F25]
uses: [0CGYNDCWRR, 0XNZWJ96HK, 0BQAA2BK3Q, 0N6960W0BV, 00KDZRW4C0, 0XC1RDBY7A]
about: [0CGYNDCWRR, 0HFREYRSZP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem
same_as:
  wikidata: Q681406
  wikipedia: Euler's rotation theorem
---

## Statement

Let $R$ be a real $3 \times 3$ matrix in the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$, that is, $R^T R = I$ and $\det R = 1$.
Then there is a unit vector $u \in \R^3$ with $R u = u$.
Moreover, there is an angle $\theta \in [0, \pi]$ such that $R$ is the [[rotation|0XNZWJ96HK]] by $\theta$ about the axis $\R u$, and
$$\tr R = 1 + 2 \cos\theta.$$

## Remarks

Proof idea: since $R^T R = I$ and $\det R = 1$, one gets $\det(R - I) = \det(R^T)\det(R - I) = \det(I - R^T) = \det(I - R) = -\det(R - I)$, because the size $3$ is odd.
So $\det(R - I) = 0$, and $1$ is an [[eigenvalue|0BQAA2BK3Q]] with an [[eigenvector|0N6960W0BV]] $u$.
The plane orthogonal to $u$ is mapped to itself, and there $R$ acts as an element of $SO(2)$, that is, a plane rotation.
The [[trace|0XC1RDBY7A]] formula follows by computing $\tr R$ in an orthonormal basis that starts with $u$.

Example: the cyclic permutation matrix $R$ with $R e_1 = e_2$, $R e_2 = e_3$, $R e_3 = e_1$ lies in $SO(3)$.
It fixes $u = (1, 1, 1)/\sqrt{3}$, and $\tr R = 0$ gives $\cos\theta = -1/2$, so it is the rotation by $2\pi/3$ about the line through $(1, 1, 1)$.

The hypothesis $\det R = 1$ is needed: the matrix $-I$ is orthogonal with $\det(-I) = -1$, and it fixes no nonzero vector.
The odd dimension is also needed.
In $\R^4$, take the rotations by $\pi/2$ in the plane of $e_1, e_2$ and in the plane of $e_3, e_4$.
Their block matrix has determinant $1$ and fixes no nonzero vector.

## Explanations

### L1 human

However you turn a ball about its centre, the end result is a single turn about one fixed axis.
Two points of the ball's surface, the ends of the axis, end up exactly where they started.
So any sequence of turns, however complicated, can be replaced by one turn about a well chosen axis by a well chosen angle.

### L2 human

The theorem says that $SO(3)$ is the set of rotations about axes through the origin, which justifies calling its elements rotations.
It gives the axis-angle description of orientations, which [[Rodrigues' rotation formula|WS52X8SGC4]] turns into an explicit matrix and [[unit quaternions|EAK8KT5AMD]] turn into an algebra.
Its counterpart for rigid motions that also translate is [[Chasles' theorem|X4R728TVZE]].
In rigid body kinematics it leads to the existence of an instantaneous axis of rotation and of the [[angular velocity|2FTZ7D8Z0F]] vector.
