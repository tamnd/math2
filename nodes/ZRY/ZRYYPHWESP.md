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

The special unitary group keeps the unitary matrices whose determinant is exactly $1$, so it removes the overall phase from the [[unitary group|VW5H9XFNJB]].
For $n = 2$ the result is a copy of the unit quaternions, and it describes the rotations of space twice over.
For $n \ge 1$, the *special unitary group* is
$$SU(n) = \{ U \in U(n) : \det U = 1 \},$$
the set of complex unitary $n \times n$ matrices with [[determinant|0C3CFHDN6R]] $1$, with matrix multiplication.
It is the kernel of the homomorphism $\det \colon U(n) \to U(1)$, so it is a [[normal subgroup|0W77CVBCHQ]] of $U(n)$.
For $n = 2$ its elements are exactly the matrices
$$\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}, \qquad \alpha, \beta \in \C, \quad \abs{\alpha}^2 + \abs{\beta}^2 = 1,$$
by [[the theorem on unit quaternions|A763JSEVW8]].

## Motivation

The unitary group has a large center, the circle of scalar matrices $zI_n$ with $\abs{z} = 1$.
A common phase often has no effect, for example on a quantum state, where $v$ and $zv$ describe the same physical state.
The condition $\det U = 1$ removes all but finitely many of these scalars, and every unitary matrix is a phase times an element of $SU(n)$.

The case $n = 2$ is the most used.
Each element of $SU(2)$ is a unit quaternion, and each unit quaternion turns space by conjugation.
This gives a two-to-one map onto the rotation group $SO(3)$, which is how computer graphics stores rotations, and how physics describes the spin of an electron.
For $n \ge 2$ the groups $SU(n)$ return in the theory of Lie groups as basic examples of compact simple Lie groups.

## Notation

Books write $SU(n)$, $SU_n$, $SU(n, \C)$ or $\mathrm{SU}(n)$.
Mathlib writes `Matrix.specialUnitaryGroup n ℂ` for an index type `n`, defined from `Matrix.unitaryGroup n ℂ` by the condition on the determinant.
A unit quaternion is also called a *versor*.

## Remarks

### A first element of SU(2)

Take $U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$.
It has the shape above with $\alpha = \frac{1}{\sqrt{2}}$ and $\beta = \frac{i}{\sqrt{2}}$, since $-\overline{\beta} = \frac{i}{\sqrt{2}}$ and $\overline{\alpha} = \frac{1}{\sqrt{2}}$.
The condition holds, $\abs{\alpha}^2 + \abs{\beta}^2 = \frac{1}{2} + \frac{1}{2} = 1$, and the determinant is
$$\det U = \tfrac{1}{2}(1 \cdot 1 - i \cdot i) = \tfrac{1}{2}(1 + 1) = 1.$$
The [[eigenvalue example|F3P6M0A78R]] finds its eigenvalues $e^{\pm i\pi/4}$ and diagonalizes it.
A second example is the [[matrix of the quaternion (1 + i + j + k)/2|Z7AEM725B9]],
$$\tfrac{1}{2} \begin{pmatrix} 1 + i & 1 + i \\ -1 + i & 1 - i \end{pmatrix},$$
whose cube is $-I_2$.
The diagonal matrices $\operatorname{diag}(e^{i\theta}, e^{-i\theta})$ form a circle inside $SU(2)$, and their determinant is $e^{i\theta} e^{-i\theta} = 1$.

### What it is not

The scalar matrix [[iI_2|QWV60RE301]] is unitary, but its determinant is $i^2 = -1$, so it is not in $SU(2)$.
The [[matrix with rows (0, i) and (1, 0)|6NZCDBCSKQ]] is unitary with determinant $-i$, so it is not in $SU(2)$ either.
In the other direction, $\operatorname{diag}(2, \frac{1}{2})$ has determinant $1$, but its first column has length $2$, so it is not unitary.
So the two conditions are independent, and $SU(n)$ needs both.

### The rules you can use

$SU(n)$ is a normal subgroup of $U(n)$, and the determinant gives $U(n)/SU(n) \cong U(1)$.
Its center is $\{ \zeta I_n : \zeta^n = 1 \}$, a cyclic group of order $n$, because $\det(\zeta I_n) = \zeta^n$.
For $SU(2)$ the center is $\{ I_2, -I_2 \}$.
The real matrices in $SU(n)$ are exactly the rotation matrices, so $SO(n) = SU(n) \cap GL_n(\R)$.
$SU(n)$ is compact and connected, and $SU(2)$ is a $3$-sphere: the pairs $(\alpha, \beta)$ with $\abs{\alpha}^2 + \abs{\beta}^2 = 1$ are the unit vectors of $\C^2 = \R^4$.

### SU(2) covers the rotations of space twice

Each unit quaternion $q$ turns the space of pure quaternions $bi + cj + dk$, a copy of $\R^3$, by $v \mapsto q v \overline{q}$.
For $q = i$ this sends $i \mapsto i$, $j \mapsto i j (-i) = -j$ and $k \mapsto i k (-i) = -k$, which is the half turn about the first axis.
The quaternion $-i$ gives the same half turn, because the two signs cancel in $q v \overline{q}$.
In general this gives a surjective homomorphism $SU(2) \to SO(3)$ with kernel $\{ \pm I_2 \}$, as [[quaternions and spatial rotation|EAK8KT5AMD]] explains.
So $SU(2)$ double covers $SO(3)$, and each rotation of space has exactly two preimages, $U$ and $-U$.

### Watch out

$SU(2)$ is not $SO(3)$.
The map between them is two to one, and the two groups are not isomorphic, since the center of $SU(2)$ has order $2$ and the center of $SO(3)$ is trivial.
A second trap is the sign in the lower row.
The matrix $\begin{pmatrix} \alpha & \beta \\ \overline{\beta} & \overline{\alpha} \end{pmatrix}$ has determinant $\abs{\alpha}^2 - \abs{\beta}^2$, so the minus sign in $-\overline{\beta}$ is needed.
A third trap: $-I_n$ lies in $SU(n)$ only for even $n$, because $\det(-I_n) = (-1)^n$.

### History

Hamilton described the quaternions in 1843.
The unit quaternions give the modern description of $SU(2)$, and the quaternion picture of rotations rests on the double cover above.

### Try it

First, decide whether $\operatorname{diag}(i, -i)$ lies in $SU(2)$.
It is unitary, since each diagonal entry has absolute value $1$, and its determinant is $i \cdot (-i) = 1$, so it does.

Second, find $\beta$ so that $\begin{pmatrix} \frac{3}{5} & \beta \\ \frac{4}{5} & \frac{3}{5} \end{pmatrix}$ lies in $SU(2)$.
The shape needs $-\overline{\beta} = \frac{4}{5}$, so $\beta = -\frac{4}{5}$, and then $\abs{\alpha}^2 + \abs{\beta}^2 = \frac{9}{25} + \frac{16}{25} = 1$.

## Explanations

### L1 human

The special unitary group collects the unitary matrices whose determinant is exactly $1$.
For size $2$, each such matrix is fixed by two complex numbers $\alpha$ and $\beta$ with $\abs{\alpha}^2 + \abs{\beta}^2 = 1$.
These are four real numbers whose squares add up to $1$, so they are a point on a sphere in four dimensions.
The same sphere is the set of unit quaternions, and each of them turns ordinary space.
Two opposite points of the sphere give the same turn.

### L2 human

Here is a typical test: is $U = \frac{1}{2} \begin{pmatrix} 1 + i & 1 + i \\ -1 + i & 1 - i \end{pmatrix}$ in $SU(2)$?
Read off $\alpha = \frac{1 + i}{2}$ and $\beta = \frac{1 + i}{2}$ from the first row.
The lower row should be $(-\overline{\beta}, \overline{\alpha}) = \left(\frac{-1 + i}{2}, \frac{1 - i}{2}\right)$, and it is.
Then the determinant is
$$\alpha \overline{\alpha} + \beta \overline{\beta} = \frac{2}{4} + \frac{2}{4} = 1,$$
and the columns are orthonormal, so $U \in SU(2)$.
So for $2 \times 2$ matrices the whole test is to compare the lower row with $(-\overline{\beta}, \overline{\alpha})$ and to add two squared absolute values.
Watch out: the shape alone is not enough, since $2I_2$ has the shape with $\alpha = 2$ and $\beta = 0$ but determinant $4$.

### L3 human

$SU(n)$ is a compact, connected and simply connected [[Lie group|7JBRGCVJRB]] of real dimension $n^2 - 1$.
Its Lie algebra $\mathfrak{su}(n)$ is the space of skew-Hermitian matrices with trace $0$.
For $n = 2$ the group is the [[spin group|JJSXXJQGEH]] $\operatorname{Spin}(3)$, the universal cover of $SO(3)$, and it is also the compact symplectic group $Sp(1)$.
The groups $SU(n)$ are among the [[classical groups|75H4HY10Z4]], and their representations are a central topic of the theory of Lie groups.
