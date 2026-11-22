---
tag: X29QSF7VVR
kind: proof
name: Proof that the special unitary group of degree two is the group of unit quaternions
msc: ["15B57", "20G20", "11R52"]
topics: [AZS5BPF5H3]
audience: ug2
proves: A763JSEVW8
uses: [AM07TESJED, 04CPJ6AF00, GZ7NG7J3J8]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
    locator: Isomorphism with group of versors and relation to spatial rotations
---

## Proof

We check that the images of $i$, $j$ and $k$ obey the quaternion rules, compute the conjugate transpose and the determinant of $\phi(q)$, and then read off the shape of a matrix in $SU(2)$ from its inverse.
Write $I = \phi(i)$, $J = \phi(j)$ and $K = \phi(k)$, so that
$$I = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}, \qquad J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad K = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}.$$

**Part 1.**

1. The formula for $\phi$ splits by the four real coordinates as $\phi(a + bi + cj + dk) = aI_2 + bI + cJ + dK$. So $\phi$ is $\R$-linear, and $\phi(1) = I_2$.
2. If $\phi(q) = 0$, then the first row gives $a + bi = 0$ and $c + di = 0$. Since $a, b, c, d$ are real, all four are $0$, so $\phi$ is injective.
3. Multiplication of the matrices gives $I^2 = J^2 = K^2 = -I_2$. For example, $J^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot (-1) & 0 \\ 0 & (-1) \cdot 1 + 0 \end{pmatrix} = -I_2$.
4. Multiplication also gives $IJ = K$, $JK = I$ and $KI = J$. For example,
$$JK = \begin{pmatrix} 0 \cdot 0 + 1 \cdot i & 0 \cdot i + 1 \cdot 0 \\ (-1) \cdot 0 + 0 \cdot i & (-1) \cdot i + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = I.$$
5. The reversed products follow from steps 3 and 4. For example, $JI = J(JK) = J^2 K = -K$, and in the same way $KJ = -I$ and $IK = -J$.
6. So $I$, $J$ and $K$ multiply exactly like $i$, $j$ and $k$, and in particular $IJK = K \cdot K = -I_2$.
7. The product of $\mathbb{H}$ is the $\R$-bilinear map that is fixed by the products of the basis elements $1, i, j, k$. By steps 1 and 6, $\phi$ sends each such product to the product of the images.
8. Matrix multiplication is $\R$-bilinear as well, and $\phi$ is $\R$-linear. So the two bilinear maps $(p, q) \mapsto \phi(pq)$ and $(p, q) \mapsto \phi(p)\phi(q)$ agree on pairs of basis elements, and hence $\phi(pq) = \phi(p)\phi(q)$ for all $p, q$.

**Part 2.**

9. The conjugate $\overline{q} = a - bi - cj - dk$ has the image $\phi(\overline{q}) = \begin{pmatrix} a - bi & -c - di \\ c - di & a + bi \end{pmatrix}$, by the formula with $b, c, d$ replaced by $-b, -c, -d$.
10. The transpose of $\phi(q)$ is $\begin{pmatrix} a + bi & -c + di \\ c + di & a - bi \end{pmatrix}$, and conjugating every entry gives $\begin{pmatrix} a - bi & -c - di \\ c - di & a + bi \end{pmatrix}$. So $\phi(q)^* = \phi(\overline{q})$.
11. The determinant is
$$\det \phi(q) = (a + bi)(a - bi) - (c + di)(-c + di) = (a^2 + b^2) - (-c^2 - d^2) = \abs{q}^2.$$

**Part 3.**

12. Multiplying out gives $\overline{q} q = a^2 + b^2 + c^2 + d^2 = \abs{q}^2$, a real number, because the mixed terms cancel in pairs. By steps 8 and 10, $\phi(q)^* \phi(q) = \phi(\overline{q} q) = \abs{q}^2 I_2$.
13. Let $\abs{q} = 1$. Then $\phi(q)^* \phi(q) = I_2$ by step 12, and $\det \phi(q) = 1$ by step 11. So $\phi(q) \in SU(2)$.
14. The unit quaternions form a group under multiplication. For unit $p$ and $q$, steps 8 and 11 and the [[multiplicativity of the determinant|04CPJ6AF00]] give $\abs{pq}^2 = \det \phi(p) \det \phi(q) = 1$, and the inverse of $q$ is $\overline{q}$ by step 12.
15. By steps 2, 8 and 13, $\phi$ is an injective group homomorphism from the unit quaternions into $SU(2)$.
16. For surjectivity, let $U = \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} \in SU(2)$.
17. Since $\det U = 1$, the formula for the inverse of a $2 \times 2$ matrix gives $U^{-1} = \begin{pmatrix} \delta & -\beta \\ -\gamma & \alpha \end{pmatrix}$.
18. Since $U$ is unitary, $U^{-1} = U^* = \begin{pmatrix} \overline{\alpha} & \overline{\gamma} \\ \overline{\beta} & \overline{\delta} \end{pmatrix}$, by [[the properties of unitary matrices|GZ7NG7J3J8]].
19. Comparing the entries of steps 17 and 18 gives $\delta = \overline{\alpha}$ and $-\beta = \overline{\gamma}$, so $\gamma = -\overline{\beta}$.
20. Write $\alpha = a + bi$ and $\beta = c + di$ with $a, b, c, d \in \R$. Then $U = \begin{pmatrix} a + bi & c + di \\ -c + di & a - bi \end{pmatrix} = \phi(a + bi + cj + dk)$.
21. By step 11, $\abs{a + bi + cj + dk}^2 = \det U = 1$. So $U$ is the image of a unit quaternion, and $\phi$ maps the unit quaternions onto $SU(2)$.

**Part 4.**

22. Steps 19 to 21 show that each $U \in SU(2)$ has the form $\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$ with $\abs{\alpha}^2 + \abs{\beta}^2 = \det U = 1$.
23. Conversely, such a matrix is $\phi(q)$ for the quaternion $q$ of step 20, and $\abs{q}^2 = \abs{\alpha}^2 + \abs{\beta}^2 = 1$, so it lies in $SU(2)$ by step 13. $\blacksquare$

## Idea

The three matrices $I$, $J$ and $K$ obey the same multiplication table as $i$, $j$ and $k$, so $\phi$ respects products.
Under $\phi$ the quaternion conjugate becomes the conjugate transpose, and the squared length becomes the determinant, so unit quaternions go to unitary matrices of determinant $1$.
For the way back, a $2 \times 2$ matrix of determinant $1$ has its inverse given by swapping and negating entries, and a unitary matrix has its inverse given by the conjugate transpose.
Setting the two inverses equal forces the shape $\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$.

## Variants

One can start from $SU(2)$ instead.
Steps 16 to 20 give the shape of its elements, and the real span of these matrices is closed under products, so it can serve as a definition of the quaternions.

Other books choose other signs, for example $\phi(j) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, or they put $\overline{\alpha}$ in the upper left corner.
Each choice gives an isomorphism onto $SU(2)$, but the formulas for $\alpha$ and $\beta$ change with it.
