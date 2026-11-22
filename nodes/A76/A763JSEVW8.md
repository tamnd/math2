---
tag: A763JSEVW8
kind: statement
role: theorem
name: The special unitary group of degree two is the group of unit quaternions
aliases: [su-2-is-the-unit-quaternions, su2-as-versors]
msc: ["15B57", "20G20", "11R52"]
topics: [AZS5BPF5H3]
audience: ug2
about: [ZRYYPHWESP]
uses: [8AJ8XQESFM, AM07TESJED, 0EX045E2BP, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
    locator: Isomorphism with group of versors and relation to spatial rotations
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
    locator: SU(2)
---

## Statement

Every quaternion can be written as a $2 \times 2$ complex matrix so that products match products, and the quaternions of length $1$ become exactly the matrices of $SU(2)$.

Let $\mathbb{H}$ be the [[quaternions|AM07TESJED]], with basis $1, i, j, k$ over $\R$ and $i^2 = j^2 = k^2 = ijk = -1$.
For $q = a + bi + cj + dk$, let $\overline{q} = a - bi - cj - dk$ and $\abs{q}^2 = a^2 + b^2 + c^2 + d^2$.
Define $\phi \colon \mathbb{H} \to M_2(\C)$ by
$$\phi(a + bi + cj + dk) = \begin{pmatrix} a + bi & c + di \\ -c + di & a - bi \end{pmatrix}.$$

1. The map $\phi$ is injective and $\R$-linear, $\phi(1) = I_2$, and $\phi(pq) = \phi(p)\phi(q)$ for all $p, q \in \mathbb{H}$.
2. For every $q$, $\phi(\overline{q}) = \phi(q)^*$, the [[conjugate transpose|0EX045E2BP]], and $\det \phi(q) = \abs{q}^2$.
3. The map $\phi$ restricts to a group isomorphism from the unit quaternions $\{ q \in \mathbb{H} : \abs{q} = 1 \}$ onto $SU(2)$.
4. Consequently,
$$SU(2) = \left\{ \begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix} : \alpha, \beta \in \C, \ \abs{\alpha}^2 + \abs{\beta}^2 = 1 \right\}.$$

## Remarks

### Why each hypothesis is needed

Part 3 needs $\abs{q} = 1$.
For $q = 2$ the image is $\phi(2) = 2I_2$, whose determinant is $4$ and whose columns have length $2$, so it is neither unitary nor of determinant $1$.
Every quaternion still maps to a matrix with lower row $(-\overline{\beta}, \overline{\alpha})$, but only the unit ones land in $SU(2)$.

Part 4 needs the determinant to be $1$, not just of absolute value $1$.
The unitary matrix $\operatorname{diag}(i, i)$ has determinant $-1$, and it does not have the shape of part 4, because its diagonal entries $i$ and $i$ are not complex conjugates of each other.
So the unitary matrices with other determinants fall outside the image of the unit quaternions.

### What it gives you

The first gain is a picture of $SU(2)$.
The map $(a, b, c, d) \mapsto \phi(a + bi + cj + dk)$ is a homeomorphism from the unit sphere $S^3 \subseteq \R^4$ onto $SU(2)$, so $SU(2)$ is compact, connected and simply connected.

The second gain is a fast way to multiply.
For example, $q = \frac{1}{2}(1 + i + j + k)$ has $\abs{q}^2 = 4 \cdot \frac{1}{4} = 1$, and its image is
$$\phi(q) = \tfrac{1}{2} \begin{pmatrix} 1 + i & 1 + i \\ -1 + i & 1 - i \end{pmatrix},$$
which [[the worked example|Z7AEM725B9]] checks to be in $SU(2)$ with $\phi(q)^3 = -I_2$.
Part 2 with the product rule for determinants also gives $\abs{pq} = \abs{p} \abs{q}$ for all quaternions.

### The converse

Each element of $SU(2)$ comes from exactly one unit quaternion, so the formulas run both ways.
Given $U \in SU(2)$, read $\alpha = a + bi$ and $\beta = c + di$ from its first row, and the quaternion is $a + bi + cj + dk$.
For example, $\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ has $\alpha = \frac{1}{\sqrt{2}}$ and $\beta = \frac{i}{\sqrt{2}}$, so it comes from $\frac{1}{\sqrt{2}}(1 + k)$.

### Generalizations

The unit quaternions act on the pure quaternions $bi + cj + dk$, a copy of $\R^3$, by $v \mapsto q v \overline{q}$.
This gives a surjective homomorphism $SU(2) \to SO(3)$ with kernel $\{ \pm I_2 \}$, as [[quaternions and spatial rotation|EAK8KT5AMD]] explains, so $SU(2)$ double covers $SO(3)$.
In the same way, the $n \times n$ quaternion matrices that keep the quaternionic inner product on $\mathbb{H}^n$ form the compact symplectic group $Sp(n)$, and $Sp(1) = SU(2)$.

## History

Hamilton described the quaternions in 1843, with the rules $i^2 = j^2 = k^2 = ijk = -1$.

## Explanations

### L1 human

Quaternions are numbers with four real parts, and the size of a product is the product of the sizes, just as for complex numbers.
Each quaternion can be written as a $2 \times 2$ table of complex numbers.
Then multiplication of quaternions becomes multiplication of these tables.
The quaternions of size $1$ become exactly the unitary tables with determinant $1$.

### L2 human

Here is the check on the three basic units.
The formula gives
$$\phi(i) = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}, \qquad \phi(j) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad \phi(k) = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}.$$
Multiply the first two:
$$\phi(i)\phi(j) = \begin{pmatrix} i \cdot 0 + 0 \cdot (-1) & i \cdot 1 + 0 \cdot 0 \\ 0 \cdot 0 + (-i)(-1) & 0 \cdot 1 + (-i) \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} = \phi(k),$$
as the rule $ij = k$ demands.
Square the third: $\phi(k)^2 = \operatorname{diag}(i \cdot i, i \cdot i) = -I_2$, as $k^2 = -1$ demands.
Each of the three matrices is unitary with determinant $1$, so $i$, $j$ and $k$ are unit quaternions.
Watch out: $\phi(i)$ is not the scalar matrix $iI_2$, because the complex unit $i$ inside the entries and the quaternion unit $i$ are different objects.

### L3 human

The theorem identifies the compact Lie group $SU(2)$ with the sphere $S^3$, which is one of only three spheres, $S^0$, $S^1$ and $S^3$, that carry a continuous group structure.
The Lie algebra $\mathfrak{su}(2)$ is the space of pure quaternions with the bracket $[p, q] = pq - qp$, and for pure quaternions this bracket is $2\, p \times q$, twice the cross product.
The homomorphism $SU(2) \to SO(3)$ is the universal cover of $SO(3)$, so $SU(2)$ is the [[spin group|JJSXXJQGEH]] $\operatorname{Spin}(3)$.
The real algebra $\phi(\mathbb{H})$ of the matrices $\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$ is a division algebra of dimension $4$ inside $M_2(\C)$.
