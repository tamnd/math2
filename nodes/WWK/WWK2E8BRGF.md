---
tag: WWK2E8BRGF
kind: concept
name: Orthogonal group
aliases: [orthogonal-group-o-n, real-orthogonal-group]
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
uses: [0QRBVFJ50X, 0N0PXCTYA7, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Name
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Topology
  - book: isbn:9780134860244
    locator: Section 6.11
---

## Summary

The orthogonal group collects all the ways to move $\R^n$ rigidly while the origin stays fixed.
In the plane these moves are the turns about the origin and the mirror images in lines through the origin, and two of them done in a row give a third.
For $n \ge 1$, the *orthogonal group* is the set of real $n \times n$ [[orthogonal matrices|0W02QESPJQ]],
$$O(n) = \{ Q \in M_n(\R) : Q^{\mathsf{T}} Q = I_n \},$$
with matrix multiplication as the group operation.
It is a [[subgroup|0X1JXT47GA]] of the [[general linear group|0FCHE902D7]] $GL_n(\R)$.
By [[the equivalent conditions for an orthogonal matrix|F7M8ZXB4P7]], it is the group of [[linear isometries|07SJXTWVQW]] of $\R^n$ with the dot product.

## Motivation

The symmetries of a figure that keep its center fixed form a group, and we want one group that contains all of them at once.
For a square centered at $0$ the symmetries are four turns and four mirror images, and for a cube there are $48$.
Each of these moves keeps lengths and fixes $0$.
By [[the theorem on isometries and inner products|0R7VXTYHYZ]], a map of $\R^n$ that keeps distances and fixes $0$ is linear, so it is an orthogonal matrix.
So $O(n)$ is the largest such group, and the symmetry group of every figure centered at $0$ sits inside it.

The same group returns in many places.
A change from one orthonormal basis of $\R^n$ to another is an element of $O(n)$.
In mechanics, the positions of a rigid body with one fixed point are elements of the rotation subgroup, and the [[normal form|QTY3VMFGY1]] and the [[Cartan-Dieudonné theorem|0VMWGYY35Q]] later describe every element of $O(n)$ in simple pieces.

## Notation

Books write $O(n)$, $O_n(\R)$ or $O(n, \R)$, and for a real inner product space $V$ of finite dimension they write $O(V)$ for the group of its bijective linear isometries.
Mathlib writes `Matrix.orthogonalGroup (Fin n) ℝ`, the matrices `A` with `star A * A = 1` and `A * star A = 1`, where `star` is the transpose for real matrices.
Watch the words: some authors say "orthogonal transformation" only for rotations, the elements of the [[special orthogonal group|6WBVP2PB1Y]] $SO(n)$.
Here an orthogonal transformation is any element of $O(n)$.

## Remarks

### The smallest cases

For $n = 1$, a matrix $(a)$ is orthogonal when $a^2 = 1$, so [[O(1) has the two elements 1 and -1|D9VHRJRMAS]].
For $n = 2$, the [[classification of O(2)|C97Z06HHB2]] shows that every element is a rotation
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
or a reflection in a line through $0$, so $O(2)$ is already infinite.
Inside $O(2)$ sit [[the eight signed permutation matrices of size 2|HV3HWHW9RE]], the symmetry group of a square centered at $0$.
In the same way, $O(3)$ contains the $3! \cdot 2^3 = 48$ signed permutation matrices of size $3$: there are $6$ ways to permute the axes and $8$ ways to choose the signs.
They form the symmetry group of the cube with corners $(\pm 1, \pm 1, \pm 1)$.

### Why it is a group

The identity is orthogonal, and products and inverses stay orthogonal.
For $P, Q \in O(n)$ we compute
$$(PQ)^{\mathsf{T}} (PQ) = Q^{\mathsf{T}} P^{\mathsf{T}} P Q = Q^{\mathsf{T}} Q = I_n.$$
The inverse of $Q$ is $Q^{\mathsf{T}}$, and $(Q^{\mathsf{T}})^{\mathsf{T}} Q^{\mathsf{T}} = Q Q^{\mathsf{T}} = I_n$, because a one-sided inverse of a square matrix is two-sided.
So $O(n)$ is a subgroup of $GL_n(\R)$.
It is not commutative for $n \ge 2$, as the worked problem in the explanations below shows.

### Two halves

Every orthogonal matrix has [[determinant 1 or -1|QDZJMFATRW]], and the map $\det \colon O(n) \to \{1, -1\}$ is a surjective [[homomorphism|0JYTG5K9Y4]].
Its kernel is $SO(n)$, so [[SO(n) has index two|XAVVA317M0]], and the other coset is the set of orthogonal matrices with determinant $-1$.
With $D = \operatorname{diag}(-1, 1, \dots, 1)$, that coset is $D \cdot SO(n)$.

The two cosets are also the two connected components of $O(n)$.
The determinant is continuous and takes only the values $1$ and $-1$, so no path in $O(n)$ joins a rotation to a mirror image.
On the other side, $SO(n)$ is connected: by the normal form, a rotation is built from blocks $R(\theta_k)$, and the path $t \mapsto R(t\theta_k)$ for $t$ from $1$ to $0$ joins it to $I_n$.
The group $O(n)$ is also compact, because $Q^{\mathsf{T}} Q = I_n$ is a closed condition and it forces every entry into $[-1, 1]$.

### What it is not

The [[matrices with determinant 1 or -1|R304WJSMWX]] form a group that is larger than $O(2)$.
It contains the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, which keeps areas but sends $(0, 1)$ to $(1, 1)$, of length $\sqrt{2}$.
The set of reflections of the plane is not a subgroup either, because the product of two reflections is a rotation.
The set of $2 \times 2$ matrices with orthogonal columns is not a group, because it contains the zero matrix, which has no inverse.

### Built from reflections

Every element of $O(n)$ is a product of [[reflections|06BRDF3F0E]] in hyperplanes, by [[the theorem on reflections|FEER10D15S]].
The [[Cartan-Dieudonné theorem|0VMWGYY35Q]] makes this exact: at most $n$ reflections are needed.
The bound is reached, for example by [[a product of three reflections of space|YXTM3P2YV8]] that fixes no nonzero vector.
The parity of the number of reflections is fixed by the determinant: an even number gives a rotation, and an odd number gives determinant $-1$.

### Watch out

The matrices with determinant $-1$ do not form a subgroup, because they do not contain $I_n$, and the product of two of them has determinant $1$.
The map $x \mapsto -x$ is a rotation in even dimension and not in odd dimension, because $\det(-I_n) = (-1)^n$.
So [[the point reflection of space|X77QN4Y9VD]] is in $O(3)$ but not in $SO(3)$, while $-I_2 = R(\pi)$ is a half turn of the plane.

### History

The name comes from a property of the elements.
Up to a common scaling factor, the elements of $O(n)$ are exactly the linear maps of a Euclidean space that send orthogonal vectors to orthogonal vectors.

### Try it

First, is $Q = \frac{1}{3}\begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & -2 \\ 2 & -2 & 1 \end{pmatrix}$ in $O(3)$?
Yes: each column has squared length $\frac{1 + 4 + 4}{9} = 1$, and the dot products of columns are $\frac{2 + 2 - 4}{9} = 0$, $\frac{2 - 4 + 2}{9} = 0$ and $\frac{4 - 2 - 2}{9} = 0$.

Second, explain why $O(n)$ has no element $Q$ with $Q^2 = -I_n$ when $n$ is odd.
Taking determinants gives $(\det Q)^2 = (-1)^n = -1$, which is impossible for a real number.

## Explanations

### L1 human

The orthogonal group is the collection of all the ways to turn or mirror space while the origin stays fixed.
Two such moves done one after the other give another such move, and each move can be undone.
On the number line there are only two moves: do nothing, or send each number $x$ to $-x$.
In the plane there are infinitely many, one turn for each angle and one mirror for each line through the origin.

### L2 human

Here is a typical problem: do a rotation and a reflection of the plane commute?
Take the quarter turn $R = R(\pi/2)$ and the reflection $S$ in the $x$-axis:
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad S = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
Multiply in both orders:
$$RS = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad SR = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}.$$
The first product is the reflection in the line $y = x$, and the second is the reflection in the line $y = -x$.
Check: both have determinant $-1$, as $\det(RS) = \det R \det S = 1 \cdot (-1)$ requires.
So $RS \ne SR$, and $O(2)$ is not commutative.
The problem shows the typical use of the group: you name the symmetries as matrices, and then products of matrices answer questions about doing one symmetry after another.

### L3 human

The group $O(n)$ is a compact [[Lie group|7JBRGCVJRB]] of dimension $\frac{n(n-1)}{2}$, one of the [[classical groups|75H4HY10Z4]], and its Lie algebra is the space of real skew-symmetric matrices.
Its two components are detected by the determinant, so $\pi_0(O(n)) \cong \Z/2\Z$; the area on Lie groups studies this structure.
The [[Cayley transform|HKQ5YY027B]] gives a chart of $SO(n)$ near $I_n$ by skew-symmetric matrices.
For a nondegenerate symmetric bilinear form $B$ on a vector space over any field, the maps that keep $B$ form the orthogonal group $O(B)$.
Over $\R$ with the form of matrix $\operatorname{diag}(1, \dots, 1, -1, \dots, -1)$ this gives the [[indefinite orthogonal groups|M2900DMEW6]], among them the Lorentz group of special relativity.
