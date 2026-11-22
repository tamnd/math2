---
tag: AZS5BPF5H3
kind: topic
name: Isometries and the orthogonal and unitary groups
msc: ["15B10", "15A04"]
topics: [GN8GYSDZFX]
---

## Summary

Some linear maps move space without stretching it: they keep every length, and so every angle.
These are the linear isometries, and in coordinates they are the orthogonal matrices over $\R$ and the unitary matrices over $\C$.
This part of [[linear algebra|GN8GYSDZFX]] starts from the single condition $\norm{Tv} = \norm{v}$ and shows that it is the same as keeping inner products, and the same as $Q^TQ = I$ or $U^*U = I$ for a matrix.
The isometries of $\R^n$ and $\C^n$ form the groups $O(n)$ and $U(n)$, and the determinant cuts out the subgroups $SO(n)$ and $SU(n)$.
In low dimension the groups have a concrete shape: $SO(2)$ is the circle of plane rotations, and every element of $O(2)$ is a rotation or a reflection.
Every rotation of space turns about an axis, and $SU(2)$ is the group of unit quaternions.
In every dimension, reflections build all of $O(n)$, and an orthogonal matrix splits into plane rotations and entries $\pm 1$.
The Cayley transform closes the story: it describes the rotations without the eigenvalue $-1$ by skew-symmetric matrices and rational formulas.

## Remarks

### Reading order

1. [[Linear isometry|07SJXTWVQW]]: the maps that keep lengths, and [[the equivalent conditions|95ST99SEW7]] that reduce the test to one orthonormal basis or to $T^*T = I$.
2. [[Isometries preserve inner products|0R7VXTYHYZ]]: keeping lengths means keeping angles, and a real distance-preserving map that fixes $0$ is linear.
3. [[Orthogonal matrix|0W02QESPJQ]]: the matrix test $Q^TQ = I$, [[seven equivalent forms of it|F7M8ZXB4P7]], and [[why $\det Q = \pm 1$ and the eigenvalues lie on the unit circle|QDZJMFATRW]].
4. [[Orthogonal group|WWK2E8BRGF]]: $O(n)$ as the group of linear isometries of $\R^n$, and its two pieces of determinant $1$ and $-1$.
5. [[Special orthogonal group|6WBVP2PB1Y]]: the rotations, a subgroup of [[index two|XAVVA317M0]], with $SO(2)$ the circle group.
6. [[Unitary matrix|0AR68JTMDT]]: the complex test $U^*U = I$ and [[what follows from it|GZ7NG7J3J8]].
7. [[Unitary group|VW5H9XFNJB]]: $U(n)$, whose determinants fill the unit circle, with $U(1)$ the circle group.
8. [[Special unitary group|ZRYYPHWESP]]: $SU(n)$ as the kernel of the determinant, and [[$SU(2)$ as the unit quaternions|A763JSEVW8]].
9. [[Rotation matrix|HNY4CPEEJA]]: the matrices $R(\theta)$ and the basic rotations of $\R^3$.
10. [[Reflection|06BRDF3F0E]]: the reflection in a hyperplane, the Householder matrix, and [[how reflections generate $O(n)$|FEER10D15S]].
11. [[Classification of O(2)|C97Z06HHB2]]: every isometry of the plane that fixes $0$ is a rotation or a reflection.
12. [[Classification of O(3) and Euler's rotation theorem|2ZVG43GSKA]]: every rotation of space has an axis.
13. [[Normal form of an orthogonal matrix|QTY3VMFGY1]]: a block form with rotations and $\pm 1$, obtained from the [[real normal form|G6T1FNE3JC]].
14. [[Cartan-Dieudonné theorem|0VMWGYY35Q]]: at most $n$ reflections suffice for each element of $O(n)$.
15. [[Cayley transform of matrices|HKQ5YY027B]]: skew-symmetric matrices and [[the rotations without the eigenvalue $-1$|R9Z3W1CFPP]].

### Where it leads

Two later topics use these groups.
The topic on [[canonical forms under similarity|GEBYZKYV3D]] gives normal forms for matrices that are not normal.
The topic on [[positive definite matrices and the singular value decomposition|SS4EVPKT3A]] uses unitary matrices in the [[polar decomposition|0J2C7BDJQA]] and the [[singular value decomposition|000NPTMX6J]].

### Prerequisites

- [[Inner product spaces|1D4JTZ9VS3]]: inner products, norms and orthonormal bases.
- [[Orthogonal complements, projections and least squares|8GQVME4SZZ]]: orthogonal complements and orthogonal projections.
- [[Adjoints, normal operators and the spectral theorems|3YM9EK6VMB]]: adjoints, normal matrices and the real normal form.
- [[Determinants|DTBK11SR77]]: the determinant and its product rule.
- [[Eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]]: eigenvalues and the characteristic polynomial.
- [[Diagonalization, triangularization and invariant subspaces|Z6S6PWMJPH]]: invariant subspaces.
- [[Groups and the group axioms|BAZT8JJ70S]]: groups and subgroups.
- [[Homomorphisms, normal subgroups and the isomorphism theorems|E1506A5A55]]: kernels, cosets and index.
