---
tag: XAVVA317M0
kind: statement
role: theorem
name: The special orthogonal group has index two
aliases: [so-n-is-normal-of-index-two, so-2-is-the-circle-group]
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
about: [6WBVP2PB1Y, WWK2E8BRGF]
uses: [GPWRS6HSNR, 0HV9Y7WG5R, 0Z424HK8CQ, 0W77CVBCHQ, 04QEBF8S49, 04EAFVFTF7]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Special orthogonal group
  - url: https://en.wikipedia.org/wiki/Circle_group
    locator: Special orthogonal group SO(2)
  - book: isbn:9780134860244
    locator: Section 6.11
---

## Statement

The rotations form exactly half of the orthogonal group, and in the plane they form a copy of the unit circle.
Let $n \ge 1$, and let $D = \operatorname{diag}(-1, 1, \dots, 1)$.

1. The map $\det \colon O(n) \to \{1, -1\}$ is a surjective [[group homomorphism|0HV9Y7WG5R]], and its [[kernel|0Z424HK8CQ]] is $SO(n)$.
2. So $SO(n)$ is a [[normal subgroup|0W77CVBCHQ]] of $O(n)$ of [[index|04QEBF8S49]] $2$, and its two cosets are $SO(n)$ and $D \cdot SO(n) = \{ Q \in O(n) : \det Q = -1 \}$.
3. The map
$$\phi(a + ic) = \begin{pmatrix} a & -c \\ c & a \end{pmatrix}$$
is a group isomorphism from the [[circle group|04EAFVFTF7]] $\{ z \in \C : \lvert z \rvert = 1 \}$ onto $SO(2)$.
So $SO(2) = \{ R(\theta) : \theta \in \R \}$, where $R(\theta) = \phi(e^{i\theta})$ is the rotation matrix with first column $(\cos\theta, \sin\theta)$.

## Remarks

### Why each hypothesis is needed

Part 1 needs the matrices to be orthogonal.
On all of $GL_n(\R)$ the determinant takes every nonzero real value, so its image is not $\{1, -1\}$, and its kernel $SL_n(\R)$ has infinitely many cosets.

Part 3 needs determinant $1$.
The matrix $\operatorname{diag}(1, -1)$ is orthogonal, but it is not of the form $\phi(z)$, because the two diagonal entries of $\phi(z)$ are equal.

### What it gives you

Every orthogonal matrix with determinant $-1$ is $D$ times a rotation.
Indeed $\det(DQ) = (-1)(-1) = 1$, so $DQ$ is a rotation, and $Q = D(DQ)$ because $D^2 = I_n$.
For example, the reflection $Q = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ in the line $y = x$ gives
$$DQ = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = R(\pi/2).$$
So $Q$ is a quarter turn followed by the reflection $D$ in the $y$-axis.

The product of two orthogonal matrices with determinant $-1$ has determinant $1$, so the product of two reflections is a rotation.
Part 3 shows that $SO(2)$ is commutative, because the circle group is: $R(\theta) R(\varphi) = R(\theta + \varphi) = R(\varphi) R(\theta)$.

### Is the index two subgroup unique in the plane?

Yes: $SO(2)$ is the only subgroup of index $2$ in $O(2)$.
A subgroup $H$ of index $2$ is [[normal|0V547YQRMV]], and the quotient $O(2)/H$ has order $2$, so it is commutative.
So $H$ contains every commutator $xyx^{-1}y^{-1}$.
With $S = \operatorname{diag}(1, -1)$ one computes $S R(\theta) S^{-1} = R(-\theta)$, and so
$$S R(\theta) S^{-1} R(\theta)^{-1} = R(-\theta) R(-\theta) = R(-2\theta).$$
Every rotation $R(\varphi)$ has this form with $\theta = -\varphi/2$, so $SO(2) \subseteq H$, and the two subgroups are equal because both have index $2$.

### Generalizations

Over $\C$ the same argument works with the unit circle in place of $\{1, -1\}$.
The determinant $\det \colon U(n) \to \{ z : \lvert z \rvert = 1 \}$ is a surjective homomorphism with kernel $SU(n)$, so $SU(n)$ is normal in the [[unitary group|VW5H9XFNJB]], but its index is infinite.
For a nondegenerate symmetric bilinear form $B$ over a field of characteristic not $2$, a reflection in an anisotropic vector has determinant $-1$, so $SO(B)$ again has index $2$ in $O(B)$.

## Explanations

### L1 human

Every orthogonal matrix is either a rotation or a mirror image of a rotation.
The determinant tells which: it is $1$ for rotations and $-1$ for the others.
Multiplying everything by one fixed mirror swaps the two kinds, so the two halves have the same size.
In the plane, each rotation matches exactly one point of the unit circle, the point where the rotation sends $(1, 0)$.

### L2 human

Here is a typical use: describe all of $O(2)$.
By part 3, the rotations are the matrices $R(\theta)$.
By part 2, the rest of $O(2)$ is the coset $D \cdot SO(2)$, and its elements are
$$D R(\theta) = \begin{pmatrix} -\cos\theta & \sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
Check: the determinant is $-\cos^2\theta - \sin^2\theta = -1$.
So two families with one angle each describe the whole group, and this is the start of [[the classification of O(2)|C97Z06HHB2]].
Watch out: the set of matrices with determinant $-1$ is a coset, not a subgroup, since it does not contain $I_n$.

### L3 human

The theorem says that $O(n)$ is an extension of $\Z/2\Z$ by $SO(n)$, and the extension splits because $D^2 = I_n$.
So $O(n)$ is a semidirect product $SO(n) \rtimes \Z/2\Z$, with $D$ acting by conjugation.
For $n$ odd the element $-I_n$ is central with determinant $-1$, so the product is direct: $O(n) \cong SO(n) \times \Z/2\Z$.
For $n$ even, $O(n)$ is not the internal direct product of $SO(n)$ and a subgroup of order $2$.
Such a subgroup would have to be central with determinant $-1$, but the center of $O(n)$ is $\{ I_n, -I_n \}$, and it lies in $SO(n)$.
