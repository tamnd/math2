---
tag: CZCWFPNS4N
kind: example
name: Special unitary group SU(n)
msc: ["22E15", "22C05", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [9TFC6ADC1C]
uses: [0R9R0Y1HDK, 00KDZRW4C0, 7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
same_as:
  wikidata: Q684363
  wikipedia: Special unitary group
---

## Example

The special unitary group is the part of the unitary group with determinant exactly $1$, and it is a standard example of a compact Lie group.
Its smallest interesting case, $SU(2)$, is the group of unit quaternions, a $3$-sphere.

Let $n \ge 1$ and write $U^*$ for the conjugate transpose of $U$.
The *special unitary group* is
$$SU(n) = \{ U \in M_n(\mathbb{C}) : U^* U = I_n, \ \det U = 1 \}.$$
It is the kernel of the [[determinant|00KDZRW4C0]] $\det \colon U(n) \to U(1)$ on the [[unitary group|0R9R0Y1HDK]], so it is a normal subgroup of $U(n)$.
We check that it is a [[compact Lie group|9TFC6ADC1C]].

1. It is closed in $M_n(\mathbb{C}) = \mathbb{R}^{2n^2}$, because $U^* U = I_n$ and $\det U = 1$ are polynomial equations in the real and imaginary parts of the entries.
2. It is bounded, because each column of a unitary matrix is a unit vector, so every entry has absolute value at most $1$.
3. So it is compact, as a closed and bounded subset of $\mathbb{R}^{2n^2}$.
4. It is a closed subgroup of the [[Lie group|7JBRGCVJRB]] $GL_n(\mathbb{C})$, so by the closed subgroup theorem it is a Lie group.

## Remarks

### The case n = 2 by hand

For $n = 1$ the group is trivial, since a $1 \times 1$ matrix with determinant $1$ is $(1)$.
For $n = 2$, let the first column of $U \in SU(2)$ be $(\alpha, \gamma)$, a unit vector in $\mathbb{C}^2$.
The unit vectors orthogonal to it are $c(-\overline{\gamma}, \overline{\alpha})$ with $\lvert c \rvert = 1$.
For this second column the determinant is $c(\alpha \overline{\alpha} + \gamma \overline{\gamma}) = c$, so the condition $\det U = 1$ forces $c = 1$.
Write $\beta = -\overline{\gamma}$; then every element of $SU(2)$ has the form
$$U = \begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}, \qquad \lvert \alpha \rvert^2 + \lvert \beta \rvert^2 = 1,$$
and every such matrix is in $SU(2)$.
Check: the matrix $V = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ has $\alpha = \tfrac{1}{\sqrt{2}}$ and $\beta = \tfrac{i}{\sqrt{2}}$, so $-\overline{\beta} = \tfrac{i}{\sqrt{2}}$ and $\lvert \alpha \rvert^2 + \lvert \beta \rvert^2 = 1$, as it must be.

### A 3-sphere of unit quaternions

The pair $(\alpha, \beta)$ is a unit vector in $\mathbb{C}^2 = \mathbb{R}^4$, so $SU(2)$ is the $3$-sphere $S^3$.
The group law also matches the [[quaternions|AM07TESJED]].
The map
$$a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k} \mapsto \begin{pmatrix} a + bi & c + di \\ -c + di & a - bi \end{pmatrix}$$
sends the quaternions of norm $1$ onto $SU(2)$ and turns quaternion products into matrix products, by the theorem that [[SU(2) is the group of unit quaternions|A763JSEVW8]].
For example, $\mathbf{i} \mapsto \operatorname{diag}(i, -i)$ and $\mathbf{j} \mapsto \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, and both matrices square to $-I_2$, as $\mathbf{i}^2 = \mathbf{j}^2 = -1$.
The [[unit quaternion example|Z7AEM725B9]] carries a general element through the map.

### Size, center and connectedness

The real dimension of $SU(n)$ is $n^2 - 1$.
The group $U(n)$ has dimension $n^2$, and for a unitary matrix the determinant already lies on the circle, so $\det U = 1$ is one real condition, not two.
For $n = 2$ this gives $3$, the dimension of $S^3$.

The center of $SU(n)$ is the set of scalar matrices $\omega I_n$ with $\omega^n = 1$, a cyclic group of order $n$, since $\det(\omega I_n) = \omega^n$.
For $SU(2)$ the center is $\{ I_2, -I_2 \}$.

The group is connected.
By the [[complex spectral theorem|04CW1P44VD]], $U = W \operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n}) W^*$ with $W$ unitary, and since $\det U = 1$ we may choose the angles with $\theta_1 + \dots + \theta_n = 0$.
Then $t \mapsto W \operatorname{diag}(e^{it\theta_1}, \dots, e^{it\theta_n}) W^*$ has determinant $e^{it \cdot 0} = 1$ for every $t$, so it joins $I_n$ to $U$ inside $SU(n)$.
It is also simply connected, which for $SU(2)$ is the fact that the $3$-sphere is simply connected.

### What it is not

A unitary matrix need not have determinant $1$: $\operatorname{diag}(-1, 1)$ is unitary with determinant $-1$, as in the [[unitary matrix with determinant -1|QWV60RE301]].
A matrix with determinant $1$ need not be unitary: the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, but its second column has length $\sqrt{2}$.
Also, $U(n)$ is not the direct product $SU(n) \times U(1)$, because the scalar matrices $\omega I_n$ with $\omega^n = 1$ lie in both factors.

### Watch out

Multiplying by a phase $c$ changes the determinant by $c^n$, not by $c$.
So whether a scalar matrix lies in $SU(n)$ depends on $n$.
The matrix $i I_2$ has determinant $i^2 = -1$, so it is not in $SU(2)$, but $i I_4$ has determinant $i^4 = 1$, so it is in $SU(4)$.
The eigenvalues of an element of $SU(2)$ come as a pair $\lambda, \overline{\lambda}$ on the unit circle, because their product is $1$, as the [[eigenvalue example|F3P6M0A78R]] shows.

### Try it

First, is $\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ in $SU(2)$, and which quaternion does it come from?
Here $\alpha = 0$ and $\beta = i$, so $-\overline{\beta} = i$, and $\lvert \alpha \rvert^2 + \lvert \beta \rvert^2 = 1$; it is in $SU(2)$ and comes from $\mathbf{k}$.

Second, which diagonal matrices lie in $SU(2)$?
Exactly the matrices $\operatorname{diag}(e^{i\theta}, e^{-i\theta})$, a circle inside the $3$-sphere.

## Explanations

### L1 human

The unitary matrices turn complex space without stretching it.
Each of them has a determinant, a complex number of size $1$.
The special unitary group keeps only the turns whose determinant is exactly $1$.
For two complex dimensions these turns are the same as the unit quaternions, a number system that extends the complex numbers.
Physicists use $SU(2)$ to describe the spin of an electron and $SU(3)$ in the theory of quarks.

### L2 human

Here is a typical problem: find the inverse of $U = \begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$ in $SU(2)$, and check that it has the same form.
For a unitary matrix the inverse is the conjugate transpose, so
$$U^{-1} = U^* = \begin{pmatrix} \overline{\alpha} & -\beta \\ \overline{\beta} & \alpha \end{pmatrix}.$$
Check by multiplying:
$$U U^* = \begin{pmatrix} \alpha \overline{\alpha} + \beta \overline{\beta} & -\alpha \beta + \beta \alpha \\ -\overline{\beta} \overline{\alpha} + \overline{\alpha} \overline{\beta} & \overline{\beta} \beta + \overline{\alpha} \alpha \end{pmatrix} = I_2.$$
The inverse has the form of $U$ with $\overline{\alpha}$ in place of $\alpha$ and $-\beta$ in place of $\beta$.
In quaternion terms this is the conjugate $a - b\mathbf{i} - c\mathbf{j} - d\mathbf{k}$, which is the inverse of a unit quaternion.
This is the typical use of the $2 \times 2$ form: a question about the group becomes arithmetic with two complex numbers.

### L3 human

The Lie algebra $\mathfrak{su}(n)$ is the space of skew-Hermitian $n \times n$ matrices with trace $0$, of real dimension $n^2 - 1$, and for $n \ge 2$ it is simple.
The group $SU(n)$ is connected and simply connected, and $U(n)$ is the quotient of $SU(n) \times U(1)$ by a cyclic group of order $n$.
The conjugation action of $SU(2)$ on the $3$-dimensional space $\mathfrak{su}(2)$ gives a surjective homomorphism $SU(2) \to SO(3)$ with kernel $\{ I_2, -I_2 \}$, so $SU(2)$ is the double cover of the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$.
The real matrices in $SU(n)$ form $SO(n)$.
Every unitary matrix is a [[phase times a special unitary matrix|6NZCDBCSKQ]].
Mathlib writes `Matrix.specialUnitaryGroup (Fin n) ℂ` for this group.
