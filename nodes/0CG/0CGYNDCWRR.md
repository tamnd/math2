---
tag: 0CGYNDCWRR
kind: object
name: Special orthogonal group
msc: [15B10, 20G20]
instance_of: [G5S1M9]
uses: [0TKYAEJ8N7, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Special orthogonal group
---

## Description

Let $n \ge 1$.
The *special orthogonal group* is the set
$$SO(n) = \{Q \in O(n) : \det Q = 1\}$$
of real orthogonal $n \times n$ matrices with [[determinant|00KDZRW4C0]] $1$, with matrix multiplication.
It is a normal subgroup of index $2$ of the [[orthogonal group|0TKYAEJ8N7]] $O(n)$.

## Remarks

Its elements are the *rotations* of $\R^n$ about the origin.
$SO(2)$ consists of the [[rotation matrices|0B9QNFGTHM]] $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, and it is commutative.
Each element of $SO(3)$ is a rotation about an axis through the origin.
$SO(n)$ is a connected compact Lie group.

## Explanations

### L1 human

The special orthogonal group contains the orthogonal matrices that do not flip orientation.
These are the rotations.
Reflections have determinant $-1$, so they are not in this group.
