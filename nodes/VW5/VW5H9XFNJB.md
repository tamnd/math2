---
tag: VW5H9XFNJB
kind: concept
name: Unitary group
aliases: [unitary-group-u-n]
msc: ["15B57", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
uses: [0D6RMJ10M9, 0N0PXCTYA7, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Unitary_group
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Unitary_group
    locator: Topology
  - url: https://en.wikipedia.org/wiki/Circle_group
    locator: Unitary group U(1)
---

## Summary

The unitary group collects every way to move the complex space $\C^n$ without a change of any length or angle.
It plays for complex spaces the role that the [[orthogonal group|WWK2E8BRGF]] plays for real ones, and it describes the symmetries of quantum mechanics.
For $n \ge 1$, the *unitary group* $U(n)$ is the set of complex $n \times n$ [[unitary matrices|0AR68JTMDT]], with matrix multiplication as the operation:
$$U(n) = \{ U \in M_n(\C) : U^*U = I_n \}.$$
It is a [[subgroup|0X1JXT47GA]] of the [[general linear group|0FCHE902D7]] $GL_n(\C)$.
By [[the properties of unitary matrices|GZ7NG7J3J8]], it is also the group of [[linear isometries|07SJXTWVQW]] of $\C^n$ with the standard inner product.

## Motivation

A change from one orthonormal basis of $\C^n$ to another is given by a unitary matrix, and such changes keep every inner product.
So any question about a complex inner product space that does not depend on the choice of orthonormal basis is a question about the action of $U(n)$.
The spectral theorem is an example: a normal matrix is $V D V^*$ with $V$ in $U(n)$ and $D$ diagonal.

Physics gives a second reason.
In quantum mechanics a state is a unit vector in a complex inner product space, and a symmetry or a time step must keep the inner products of states, so it acts by a unitary operator.
The determinant then splits $U(n)$ into a phase and the [[special unitary group|ZRYYPHWESP]] $SU(n)$, which carries the rest of the structure.

## Notation

Books write $U(n)$, $U_n$, $U(n, \C)$ or $\mathrm{U}(n)$, and physicists often write $U(N)$.
For a complex inner product space $V$, the group of its unitary operators is $U(V)$, and a choice of orthonormal basis identifies $U(V)$ with $U(\dim V)$.
Mathlib writes `Matrix.unitaryGroup n ℂ` for an index type `n`, so the group above is `Matrix.unitaryGroup (Fin n) ℂ`.
It is a special case of `unitary A`, the submonoid of elements $a$ with $a^* a = a a^* = 1$ in a star monoid $A$.

## Remarks

### The smallest case: a circle

For $n = 1$, a matrix is one complex number $(z)$, and $U^*U = I_1$ says $\overline{z} z = \abs{z}^2 = 1$.
So $U(1)$ is the unit circle with complex multiplication, the [[circle group|1Y63SY7537]].
Each element is $e^{i\theta}$, and multiplication by $e^{i\theta}$ turns the complex plane by the angle $\theta$.
The case $n = 1$ already shows the main difference from the real case: the real numbers with $x^2 = 1$ are only $\pm 1$, but the unit complex numbers form a whole circle.

### Two elements of U(2)

Take $U = \begin{pmatrix} 0 & i \\ 1 & 0 \end{pmatrix}$.
Its conjugate transpose is $U^* = \begin{pmatrix} 0 & 1 \\ -i & 0 \end{pmatrix}$, and we multiply:
$$U^*U = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot i + 1 \cdot 0 \\ -i \cdot 0 + 0 \cdot 1 & (-i) \cdot i + 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
So $U \in U(2)$, and $\det U = 0 \cdot 0 - i \cdot 1 = -i$.
The [[factorization into a phase and an element of SU(2)|6NZCDBCSKQ]] writes $U = \operatorname{diag}(-i, 1) \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, where the second factor has determinant $1$.

The scalar matrix $iI_2$ is unitary too, since $\overline{i} \cdot i = 1$ on the diagonal.
Its determinant is $i \cdot i = -1$, so it lies in $U(2)$ but [[not in SU(2)|QWV60RE301]].
In general $\det(zI_n) = z^n$, so the scalar $zI_n$ with $\abs{z} = 1$ lies in $SU(n)$ exactly when $z^n = 1$.

### What it is not

The condition $\abs{\det A} = 1$ is not enough.
The [[triangular matrix with diagonal entries i and 1|RMXFKRW9WQ]] has $\det A = i$, but its second column $(1, 1)$ has length $\sqrt{2}$, so it is not unitary.
The condition $A^{\mathsf{T}} A = I$ with the plain transpose is not enough either.
The [[complex orthogonal matrix|JRPHE0FG7D]] $\begin{pmatrix} \sqrt{2} & i \\ -i & \sqrt{2} \end{pmatrix}$ satisfies it, but its first column $(\sqrt{2}, -i)$ has length $\sqrt{3}$.
Both failures come from the same rule: a unitary matrix needs orthonormal columns for the inner product $\ip{x}{y} = \sum_k x_k \overline{y_k}$, with the conjugate.

### The rules you can use

$U(n)$ is a group: $(UW)^*(UW) = W^* U^* U W = W^* W = I_n$, and $U^{-1} = U^*$ is unitary because $(U^*)^* U^* = U U^* = I_n$.
The determinant of a unitary matrix lies on the unit circle, because $\abs{\det U}^2 = \det U^* \det U = \det I_n = 1$.
Every point of the circle occurs, since $\det \operatorname{diag}(z, 1, \dots, 1) = z$.
So $\det \colon U(n) \to U(1)$ is a surjective homomorphism, and its kernel is $SU(n)$.
The center of $U(n)$ is the group of scalars $zI_n$ with $\abs{z} = 1$.
For $n \ge 2$ the group is not commutative, as the L2 explanation shows.
The real matrices in $U(n)$ are exactly the orthogonal matrices, so $O(n) = U(n) \cap GL_n(\R)$.

### One piece, not two

The orthogonal group $O(n)$ falls into two pieces, the matrices with determinant $1$ and those with determinant $-1$, and no continuous path joins them.
The unitary group has only one piece.
For example, the path
$$t \mapsto \begin{pmatrix} 1 & 0 \\ 0 & e^{i \pi t} \end{pmatrix}, \qquad 0 \le t \le 1,$$
stays in $U(2)$ and joins $I_2$ to $\operatorname{diag}(1, -1)$.
In general, the [[spectral form|GZ7NG7J3J8]] writes $U = V \operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n}) V^*$ with $V$ unitary.
Then $U_t = V \operatorname{diag}(e^{it\theta_1}, \dots, e^{it\theta_n}) V^*$ is unitary for each $t$, with $U_0 = I_n$ and $U_1 = U$.
So $U(n)$ is connected, and it is also compact, as a closed and bounded set of matrices.

### Watch out

The determinant of an orthogonal matrix is $1$ or $-1$, but the determinant of a unitary matrix can be any complex number of absolute value $1$.
For example, $\operatorname{diag}(e^{i\pi/3}, 1)$ is unitary with determinant $e^{i\pi/3}$, which is not real.
A second trap is the word *orthogonal* for complex matrices.
A complex matrix with $Q^{\mathsf{T}} Q = I$ is complex orthogonal, and it need not be unitary, as the non-example above shows.

### Try it

First, find the determinant of $\operatorname{diag}(e^{i\pi/3}, e^{i\pi/6})$, and say whether the matrix lies in $SU(2)$.
The matrix is unitary, and its determinant is $e^{i\pi/3 + i\pi/6} = e^{i\pi/2} = i$, so it is in $U(2)$ but not in $SU(2)$.

Second, show that $A_t = \begin{pmatrix} \cos t & i \sin t \\ i \sin t & \cos t \end{pmatrix}$ is unitary for every real $t$.
The columns have squared lengths $\cos^2 t + \sin^2 t = 1$, and their inner product is $\cos t \cdot \overline{i \sin t} + i \sin t \cdot \cos t = -i \cos t \sin t + i \sin t \cos t = 0$.

## Explanations

### L1 human

Think of the complex numbers as points of a plane.
Multiplication by a complex number of size $1$, such as $i$, turns the plane about $0$ and keeps every distance.
These turns are the unitary group of size $1$.
For larger sizes, a unitary matrix does the same thing to lists of complex numbers: it moves them around and keeps every length.
Two such moves, one after the other, give a third one, and each move can be undone, so they form a group.

### L2 human

Here is a typical check: is $U(2)$ commutative?
Take the swap $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and the phase $B = \operatorname{diag}(i, 1)$, which are both unitary.
Multiply them in both orders:
$$AB = \begin{pmatrix} 0 & 1 \\ i & 0 \end{pmatrix}, \qquad BA = \begin{pmatrix} 0 & i \\ 1 & 0 \end{pmatrix}.$$
The two products differ, so $U(2)$ is not commutative, and the same matrices placed in a corner show this for every $n \ge 2$.
Check: both products have determinant $0 - i = -i$, as they must, since the determinant is a homomorphism to the commutative group $U(1)$.
So the determinant forgets the order of the factors, and the rest of the matrix remembers it.

### L3 human

$U(n)$ is a compact connected [[Lie group|7JBRGCVJRB]] of real dimension $n^2$, and its Lie algebra is the space of skew-Hermitian matrices, $X^* = -X$.
It is a maximal compact subgroup of $GL_n(\C)$, and the [[polar decomposition|0J2C7BDJQA]] $A = UP$ shows that $GL_n(\C)$ deformation retracts onto it.
The multiplication map $U(1) \times SU(n) \to U(n)$, $(z, A) \mapsto zA$, is surjective, and its kernel is the cyclic group of the pairs $(\omega, \omega^{-1} I_n)$ with $\omega^n = 1$.
The determinant induces an isomorphism of fundamental groups $\pi_1(U(n)) \cong \pi_1(U(1)) \cong \Z$.
$U(n)$ is one of the [[classical groups|75H4HY10Z4]], and the sub-area on positive operators uses it again in the polar decomposition and the [[singular value decomposition|000NPTMX6J]].
