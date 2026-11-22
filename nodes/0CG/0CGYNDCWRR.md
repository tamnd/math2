---
tag: 0CGYNDCWRR
kind: object
name: Special orthogonal group
msc: [15B10, 20G20]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [G5S1M9]
uses: [0TKYAEJ8N7, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Special orthogonal group
---

## Description

The special orthogonal group is the group of rotations of $\mathbb{R}^n$ about the origin: the length-preserving linear maps that do not turn space into its mirror image.
It is the half of the orthogonal group that contains the identity, and it describes every position of a rigid body with one fixed point.

Let $n \ge 1$.
The *special orthogonal group* is the set
$$SO(n) = \{ Q \in O(n) : \det Q = 1 \}$$
of real orthogonal $n \times n$ matrices with [[determinant|00KDZRW4C0]] $1$, with matrix multiplication.
We check that it is a [[normal subgroup|0CB0DX5BVV]] of index $2$ in the [[orthogonal group|0TKYAEJ8N7]] $O(n)$.

1. The map $\det \colon O(n) \to \{1, -1\}$ is a homomorphism, because $\det(PQ) = \det P \det Q$.
2. Its kernel is $SO(n)$ by definition, and the kernel of a homomorphism is a normal subgroup.
3. The map is onto, because $\operatorname{diag}(-1, 1, \dots, 1)$ is orthogonal with determinant $-1$.
4. So $O(n) / SO(n) \cong \{1, -1\}$, and $SO(n)$ has [[index two|XAVVA317M0]] in $O(n)$.

The elements of $SO(n)$ are called *rotations*, and the elements of the other coset are sometimes called improper rotations.

## Remarks

### Rotations of the plane

Every element of $SO(2)$ is a [[rotation matrix|0B9QNFGTHM]].
The first column of $Q \in SO(2)$ is a unit vector, so it is $(\cos\theta, \sin\theta)$ for some angle $\theta$.
The second column is a unit vector perpendicular to it, so it is $(-\sin\theta, \cos\theta)$ or $(\sin\theta, -\cos\theta)$.
The determinant is $1$ only for the first choice, so
$$Q = R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
Since $R(\alpha) R(\beta) = R(\alpha + \beta)$, the map $R(\theta) \mapsto e^{i\theta}$ is an isomorphism from $SO(2)$ onto the [[circle group|04EAFVFTF7]] of complex numbers of absolute value $1$.
In particular $SO(2)$ is commutative.

### Rotations of space

By [[Euler's rotation theorem|2ZVG43GSKA]], every element of $SO(3)$ is a rotation about an axis through the origin.
Take the cyclic permutation matrix
$$P = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},$$
which sends $e_1 \mapsto e_2 \mapsto e_3 \mapsto e_1$.
Its columns are the standard basis vectors in another order, so $P \in O(3)$, and its determinant is $1$, since the cyclic permutation of three objects is even.
It fixes $(1, 1, 1)$, so that is the axis.
For a rotation by the angle $\theta$, the trace is $1 + 2\cos\theta$, and here the trace is $0$, so $\cos\theta = -\tfrac{1}{2}$ and $\theta = 120$ degrees; the [[axis and angle of this matrix|E6SGA0X325]] are worked out in full.
Unlike $SO(2)$, the group $SO(3)$ is not commutative, as the [[basic rotations of space|F1KZ5GE4TC]] show.

### One piece

The group $SO(n)$ is connected.
In the plane, the path $t \mapsto R(t\theta)$ for $t$ from $0$ to $1$ joins $I_2$ to $R(\theta)$ inside $SO(2)$.
In general, the [[normal form of an orthogonal matrix|QTY3VMFGY1]] writes a rotation in a suitable orthonormal basis as blocks $R(\theta_k)$ and entries $1$, with an even number of entries $-1$ that pair into blocks $R(\pi)$.
Turning every angle down to $0$ at the same time joins the rotation to $I_n$.
So $SO(n)$ is the connected component of $I_n$ in $O(n)$, and $O(n)$ has exactly two components.
The group is also compact, as a closed subset of the compact group $O(n)$.

### What it is not

A reflection has determinant $-1$, so it is never in $SO(n)$.
For example, the [[coordinate swap of the plane|27TY1G77KM]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is orthogonal but not a rotation.
The map $x \mapsto -x$ depends on the dimension, since $\det(-I_n) = (-1)^n$.
In the plane $-I_2 = R(\pi)$ is the half turn, but in space the [[point reflection|X77QN4Y9VD]] $-I_3$ has determinant $-1$ and is not a rotation.

### Watch out

Determinant $1$ alone does not make a rotation.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, but it is not orthogonal, because its second column $(1, 1)$ has length $\sqrt{2}$.
Both conditions are needed: $Q^{\mathsf{T}} Q = I_n$ and $\det Q = 1$.
A second trap is the word itself: some books call every element of $O(n)$ a rotation, so check the definition in use.

### Try it

First, is $\frac{1}{5} \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ in $SO(2)$, and what is its angle?
Its columns are orthonormal and its determinant is $\tfrac{9 + 16}{25} = 1$, so it is $R(\theta)$ with $\cos\theta = \tfrac{3}{5}$ and $\sin\theta = \tfrac{4}{5}$, about $53.1$ degrees.

Second, show that $\operatorname{diag}(-1, -1, 1)$ is in $SO(3)$ and find its axis and angle.
Its determinant is $(-1)(-1)(1) = 1$, it fixes $e_3$, and it sends $e_1, e_2$ to $-e_1, -e_2$, so it is the half turn about the $z$-axis.

## Explanations

### L1 human

A rotation turns space about the origin without stretching anything and without flipping it over.
A turn of a clock hand is a rotation of the plane, and a spinning top turns about its axis in space.
Two rotations done one after the other give another rotation, and a rotation can be undone by turning back.
A mirror image is not a rotation: you cannot turn a left hand into a right hand.

### L2 human

Here is a typical problem: show that every element of $SO(3)$ has the eigenvalue $1$, so that it fixes an axis.
Let $Q \in SO(3)$ and compute $\det(Q - I)$, using $Q^{\mathsf{T}} Q = I$ and $\det Q = 1$:
$$\det(Q - I) = \det\big(Q (I - Q^{\mathsf{T}})\big) = \det Q \cdot \det\big((I - Q)^{\mathsf{T}}\big) = \det(I - Q).$$
For a $3 \times 3$ matrix, $\det(I - Q) = (-1)^3 \det(Q - I) = -\det(Q - I)$.
So $\det(Q - I) = -\det(Q - I)$, which gives $\det(Q - I) = 0$.
Hence $Q - I$ is singular, and some nonzero vector $v$ has $Qv = v$.
The argument uses that $3$ is odd; in $SO(2)$ the rotation $R(\pi/2)$ fixes no nonzero vector.
This is the heart of Euler's rotation theorem, and it is the typical way that the determinant condition is used.

### L3 human

The group $SO(n)$ is a connected compact [[Lie group|7JBRGCVJRB]] of dimension $\tfrac{n(n-1)}{2}$, with the same Lie algebra of skew-symmetric matrices as $O(n)$.
For $n \ge 3$ it is not simply connected: its universal cover is the spin group, a double cover, and for $n = 3$ this cover is the group $SU(2)$ of unit quaternions.
The [[Cayley transform|HKQ5YY027B]] parametrizes the rotations without the eigenvalue $-1$ by skew-symmetric matrices.
For odd $n$, $O(n)$ is the direct product $SO(n) \times \{I_n, -I_n\}$, because $-I_n$ is central with determinant $-1$; for even $n$ this fails, since $-I_n$ lies in $SO(n)$.
