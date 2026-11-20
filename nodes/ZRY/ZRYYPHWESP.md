---
tag: ZRYYPHWESP
kind: concept
name: Special unitary group
aliases: [special-unitary-group-su-n]
msc: ["15B57", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
uses: [VW5H9XFNJB, 0C3CFHDN6R, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
    locator: SU(2)
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
    locator: Isomorphism with group of versors and relation to spatial rotations
  - url: https://en.wikipedia.org/wiki/Quaternion
    locator: History
---

## Summary

Let $n \ge 1$.
The *special unitary group* $SU(n)$ is the set of complex unitary $n \times n$ matrices with [[determinant|0C3CFHDN6R]] $1$, $SU(n) = \set{U \in U(n) : \det U = 1}$.
It is the kernel of $\det \colon U(n) \to U(1)$, so it is a [[normal subgroup|0W77CVBCHQ]] of the [[unitary group|VW5H9XFNJB]].
The group $SU(2)$ consists of the matrices $\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$ with $\abs{\alpha}^2 + \abs{\beta}^2 = 1$, and it is isomorphic to the group of unit quaternions, by [[this theorem|A763JSEVW8]].

## Motivation

The unitary group has a large center, the scalar matrices $zI_n$ with $\abs{z} = 1$.
These scalars change only a common phase, which often has no effect, for example on quantum states.
The condition $\det U = 1$ removes most of this phase and leaves a group with a finite center.
For $n = 2$, the result is the group of unit quaternions, which describes rotations of space.

## Notation

- Books write $SU(n)$, $SU_n$ or $SU(n, \C)$.
- Mathlib writes `Matrix.specialUnitaryGroup (Fin n) ℂ`.
- A unit quaternion is also called a versor.

## Remarks

### Examples

- $SU(1) = \set{(1)}$, the trivial group.
- [[The unit quaternion (1 + i + j + k)/2|Z7AEM725B9]] gives the element $\frac{1}{2}\begin{pmatrix} 1 + i & 1 + i \\ -1 + i & 1 - i \end{pmatrix}$ of $SU(2)$.
- [[The matrix with rows (1, i) and (i, 1) divided by the square root of two|F3P6M0A78R]] is an element of $SU(2)$.
- The diagonal matrices $\operatorname{diag}(e^{i\theta}, e^{-i\theta})$ form a circle subgroup of $SU(2)$.
- $SO(n)$ is the subgroup of real matrices in $SU(n)$.

### Non-examples

- [[The matrix diag(i, i)|QWV60RE301]] is unitary, but its determinant is $i^2 = -1$, so it is not in $SU(2)$.
- [[A unitary matrix with determinant −i|6NZCDBCSKQ]] is in $U(2)$ but not in $SU(2)$.
- The matrix $\operatorname{diag}(2, \frac{1}{2})$ has determinant $1$, but it is not unitary, so it is not in $SU(2)$.

### Basic properties

- $SU(n)$ is a normal subgroup of $U(n)$, and $U(n)/SU(n) \cong U(1)$.
- The center of $SU(n)$ is $\set{\zeta I_n : \zeta^n = 1}$, a cyclic group of order $n$. For $SU(2)$, it is $\set{I_2, -I_2}$.
- $SU(2)$ is homeomorphic to the $3$-sphere $\set{(a, b, c, d) \in \R^4 : a^2 + b^2 + c^2 + d^2 = 1}$, by [[this theorem|A763JSEVW8]].
- The conjugation action of the unit quaternions on the pure quaternions gives a surjective homomorphism $SU(2) \to SO(3)$ with kernel $\set{\pm I_2}$, see [[quaternions and spatial rotation|EAK8KT5AMD]].
- $SU(n)$ is a compact connected [[Lie group|7JBRGCVJRB]] of real dimension $n^2 - 1$.

### History

Hamilton described the quaternions in 1843.
The unit quaternions give the modern description of $SU(2)$.

### Common errors

- $SU(2)$ is not $SO(3)$. The map $SU(2) \to SO(3)$ is two to one, because $U$ and $-U$ give the same rotation.
- In $SU(2)$, the lower row is $(-\overline{\beta}, \overline{\alpha})$, not $(\overline{\beta}, \overline{\alpha})$. The second form has determinant $\abs{\alpha}^2 - \abs{\beta}^2$.
- $-I_n \in SU(n)$ only for $n$ even, because $\det(-I_n) = (-1)^n$.

## Explanations

### L1 human

The special unitary group collects the unitary matrices with determinant $1$.
For size $2$, each such matrix is given by two complex numbers $\alpha$ and $\beta$ with $\abs{\alpha}^2 + \abs{\beta}^2 = 1$.
These are four real numbers on a sphere in four dimensions.
This sphere is also the set of unit quaternions, and they describe rotations of space.

### L2 human

Worked example: we check that $U = \frac{1}{2}\begin{pmatrix} 1 + i & 1 + i \\ -1 + i & 1 - i \end{pmatrix}$ is in $SU(2)$.

1. $U$ has the form $\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$ with $\alpha = \beta = \frac{1 + i}{2}$, because $-\overline{\beta} = \frac{-1 + i}{2}$ and $\overline{\alpha} = \frac{1 - i}{2}$.
2. $\abs{\alpha}^2 + \abs{\beta}^2 = \frac{2}{4} + \frac{2}{4} = 1$.
3. So $\det U = \alpha\overline{\alpha} + \beta\overline{\beta} = 1$, and the columns are orthonormal.
4. So $U \in SU(2)$.

The typical use: to test a $2 \times 2$ matrix, compare its lower row with $(-\overline{\beta}, \overline{\alpha})$.
A trap: the sign in $-\overline{\beta}$ is necessary.

### L3 human

$SU(n)$ is a compact, connected and simply connected Lie group of real dimension $n^2 - 1$, and its Lie algebra is the space of traceless skew-Hermitian matrices.
$SU(2)$ is the [[spin group|JJSXXJQGEH]] $\operatorname{Spin}(3)$, the universal cover of $SO(3)$.
The Lie theory and the representation theory of $SU(n)$ belong to the area of Lie groups.
