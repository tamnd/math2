---
tag: 6WBVP2PB1Y
kind: concept
name: Special orthogonal group
aliases: [rotation-group, special-orthogonal-group-so-n]
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
uses: [WWK2E8BRGF, 0C3CFHDN6R, 0N0PXCTYA7, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Special orthogonal group
  - url: https://en.wikipedia.org/wiki/Circle_group
    locator: Special orthogonal group SO(2)
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
  - book: isbn:9780134860244
    locator: Section 6.11
---

## Summary

The special orthogonal group is the group of rotations: the rigid motions of $\R^n$ that fix the origin and never turn an object into its mirror image.
The determinant separates the rotations from the mirror images, since it is $1$ on the first kind and $-1$ on the second.
For $n \ge 1$, the *special orthogonal group* is
$$SO(n) = \{ Q \in O(n) : \det Q = 1 \},$$
the real orthogonal $n \times n$ matrices with [[determinant|0C3CFHDN6R]] $1$, with matrix multiplication; the [[formal definition|GPWRS6HSNR]] states it.
It is a [[normal subgroup|0W77CVBCHQ]] of index $2$ in the [[orthogonal group|WWK2E8BRGF]] $O(n)$, by [[the index theorem|XAVVA317M0]].
Its elements are called *rotations*.

## Motivation

A rigid body that turns about a fixed point never becomes its own mirror image during the motion.
So its possible positions form a smaller group than $O(n)$, and the determinant tells us which orthogonal matrices to keep.
This group describes a spinning top, the attitude of a satellite and the orientation of a camera in computer graphics.

In the plane the group is small and familiar: it is the group of turns $R(\theta)$, and it behaves like the unit circle.
In space it is much richer, and two rotations about different axes no longer commute.
Later pages describe it completely: [[Euler's rotation theorem|2ZVG43GSKA]] gives each rotation of space an axis and an angle, and the [[Cayley transform|HKQ5YY027B]] parametrizes most rotations by skew-symmetric matrices.

## Notation

Books write $SO(n)$, $SO_n(\R)$, $SO(n, \R)$ or $O^+(n)$.
Mathlib writes `Matrix.specialOrthogonalGroup (Fin n) ℝ`.
Some authors call only the elements of $SO(n)$ "orthogonal transformations"; here that name means any element of $O(n)$, and "rotation" means an element of $SO(n)$.
The [[rotation matrix|HNY4CPEEJA]] of the plane is
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$

## Remarks

### Rotations of the plane

Every element of $SO(2)$ is some $R(\theta)$, by [[the classification of O(2)|C97Z06HHB2]].
Check the determinant first:
$$\det R(\theta) = \cos^2\theta + \sin^2\theta = 1.$$
Multiplying two of them and using the addition formulas for sine and cosine gives
$$R(\theta) R(\varphi) = R(\theta + \varphi).$$
So turning by $\theta$ and then by $\varphi$ is turning by $\theta + \varphi$, and $SO(2)$ is commutative.
The map $R(\theta) \mapsto e^{i\theta}$ is an isomorphism onto the [[circle group|04EAFVFTF7]], because both sides multiply by adding angles.

### Rotations of space

In $\R^3$ the picture is different.
The [[rotation by sixty degrees about the diagonal|TFWTJ9K6K7]] and the [[cyclic permutation of the axes|E6SGA0X325]] are rotations about the line through $(1, 1, 1)$.
The [[half turn diag(-1, -1, 1)|EKK87GQF5W]] turns space by $\pi$ about the $z$-axis.
The $24$ signed permutation matrices of size $3$ with determinant $1$ form a subgroup, the rotation group of the cube.
By [[Euler's rotation theorem|2ZVG43GSKA]], every element of $SO(3)$ fixes an axis and turns about it by one angle.
But [[the basic rotations about two axes do not commute|F1KZ5GE4TC]], so $SO(n)$ is not commutative for $n \ge 3$.

### What it is not

The [[point reflection -I_3|X77QN4Y9VD]] is orthogonal, but its determinant is $(-1)^3 = -1$, so it is not in $SO(3)$.
A reflection in a line of the plane, such as $\operatorname{diag}(1, -1)$, has determinant $-1$, so it is not in $SO(2)$.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, but it is not orthogonal, so it is not a rotation either.

### The rules you can use

The group $SO(n)$ is the [[kernel|0Z424HK8CQ]] of the homomorphism $\det \colon O(n) \to \{1, -1\}$, so it is normal, and it has index $2$.
Every element of $O(n)$ with determinant $-1$ is $D R$ for a rotation $R$, where $D = \operatorname{diag}(-1, 1, \dots, 1)$.
For $n$ odd, $-I_n$ has determinant $-1$ and commutes with everything, so $O(n)$ is the direct product of $SO(n)$ and $\{ I_n, -I_n \}$.
The group $SO(n)$ is connected, and it is the component of $I_n$ in $O(n)$; it is compact, because it is a closed subset of the compact group $O(n)$.

### Watch out

Determinant $1$ alone does not make a rotation; the matrix must also be orthogonal, and the shear above shows the difference.
A second trap concerns $-I_n$.
It is a rotation when $n$ is even, since $-I_2 = R(\pi)$ is the half turn of the plane, and it is not a rotation when $n$ is odd.
In $\R^3$ the map $x \mapsto -x$ is a half turn followed by a reflection, as [[the classification of O(3)|2ZVG43GSKA]] explains.

### History

Cayley introduced in 1846 the transform that now carries his name, and it gives a rational parametrization of the rotations without the eigenvalue $-1$ by skew-symmetric matrices.

### Try it

First, is $Q = \frac{1}{5}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ a rotation?
Its columns are orthonormal, since $\frac{9 + 16}{25} = 1$ and $\frac{-12 + 12}{25} = 0$, and $\det Q = \frac{9 + 16}{25} = 1$, so yes; it is $R(\theta)$ with $\cos\theta = \frac{3}{5}$ and $\sin\theta = \frac{4}{5}$.

Second, is the permutation matrix that swaps $e_1$ and $e_2$ in $\R^3$ a rotation?
No: it is orthogonal, but a single swap of two rows of $I_3$ changes the determinant to $-1$.

## Explanations

### L1 human

A rotation turns space about a fixed point and never makes a mirror image.
In the plane it turns everything about the origin by one angle.
In space it turns everything about one fixed line, the axis.
Two rotations done one after the other give another rotation, and each rotation can be undone by turning back.
The special orthogonal group is the collection of all these rotations.

### L2 human

Here is a typical problem: show that
$$Q = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$
is a rotation of space, and find its axis.
The columns of $Q$ are $e_2$, $e_3$ and $e_1$, so they are orthonormal, and $Q$ is orthogonal.
Expand the determinant along the first row; only the entry in position $(1, 3)$ is nonzero, and its sign is $(-1)^{1+3} = 1$:
$$\det Q = 1 \cdot \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 1.$$
So $Q \in SO(3)$.
It sends $e_1 \mapsto e_2 \mapsto e_3 \mapsto e_1$, so it fixes $(1, 1, 1)$, and the axis is the line through $(1, 1, 1)$.
Three applications give $Q^3 = I_3$ while $Q \ne I_3$, so the angle $\theta$ in $[0, \pi]$ has $3\theta$ a multiple of $2\pi$ and $\theta \ne 0$, which leaves $\theta = \frac{2\pi}{3}$, as [[the axis and angle example|E6SGA0X325]] confirms with the trace.
The problem shows the usual two-step test for a rotation: check orthogonality, then check the determinant.

### L3 human

The group $SO(n)$ is a compact connected [[Lie group|7JBRGCVJRB]] of dimension $\frac{n(n-1)}{2}$, and its Lie algebra is the space of real skew-symmetric matrices.
The exponential map from this Lie algebra onto $SO(n)$ is surjective, by the [[normal form|QTY3VMFGY1]]: each block $R(\theta)$ is the exponential of $\begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$.
For $n \ge 3$ the fundamental group of $SO(n)$ is $\Z/2\Z$, and its double cover is the [[spin group|JJSXXJQGEH]].
For $n = 3$ this cover is $SU(2) \to SO(3)$, which the page on [[quaternions and spatial rotation|EAK8KT5AMD]] describes.
The area on Lie groups studies this structure.
