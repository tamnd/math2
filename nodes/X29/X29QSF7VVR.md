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

Write $I = \phi(i)$, $J = \phi(j)$ and $K = \phi(k)$, so that $I = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}$, $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $K = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$.

**Part 1.**

1. By the formula, $\phi(a + bi + cj + dk) = aI_2 + bI + cJ + dK$. So $\phi$ is $\R$-linear, and $\phi(1) = I_2$.
2. If $\phi(q) = 0$, then the entries give $a + bi = 0$ and $c + di = 0$. So $a = b = c = d = 0$, and $\phi$ is injective.
3. Direct multiplication gives $I^2 = J^2 = K^2 = -I_2$.
4. Direct multiplication gives $IJ = K$, $JK = I$ and $KI = J$. For example, $IJ = \begin{pmatrix} 0 & i \\ -(-i) & 0 \end{pmatrix} = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} = K$.
5. Then $JI = -K$, $KJ = -I$ and $IK = -J$. For example, $JI = J(JK) = J^2K = -K$.
6. So $I$, $J$ and $K$ multiply like $i$, $j$ and $k$, and $IJK = K^2 = -I_2$.
7. The product in $\mathbb{H}$ is the $\R$-bilinear map fixed by the products of $1, i, j, k$. By steps 1 and 6, $\phi$ sends each of these products to the product of the images.
8. Matrix multiplication is also $\R$-bilinear. So $\phi(pq) = \phi(p)\phi(q)$ for all $p, q \in \mathbb{H}$.

**Part 2.**

9. $\phi(\overline{q}) = \begin{pmatrix} a - bi & -c - di \\ c - di & a + bi \end{pmatrix}$.
10. $\phi(q)^*$ is the conjugate of the transpose $\begin{pmatrix} a + bi & -c + di \\ c + di & a - bi \end{pmatrix}$, which is $\begin{pmatrix} a - bi & -c - di \\ c - di & a + bi \end{pmatrix}$. So $\phi(\overline{q}) = \phi(q)^*$.
11. $\det\phi(q) = (a + bi)(a - bi) - (c + di)(-c + di) = (a^2 + b^2) - (-c^2 - d^2) = \abs{q}^2$.

**Part 3.**

12. A direct computation gives $\overline{q}q = \abs{q}^2$, a real number. By step 8, $\phi(q)^*\phi(q) = \phi(\overline{q}q) = \abs{q}^2I_2$.
13. Let $\abs{q} = 1$. Then $\phi(q)^*\phi(q) = I_2$, and $\det\phi(q) = 1$ by step 11. So $\phi(q) \in SU(2)$.
14. The unit quaternions form a group under multiplication: $\abs{pq}^2 = \det\phi(pq) = \det\phi(p)\det\phi(q) = 1$, by steps 8 and 11 and [[multiplicativity of the determinant|04CPJ6AF00]]. The inverse of $q$ is $\overline{q}$.
15. By steps 2, 8 and 13, $\phi$ is an injective group homomorphism from the unit quaternions to $SU(2)$.
16. For surjectivity, let $U = \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} \in SU(2)$.
17. $\det U = 1$, so $U^{-1} = \begin{pmatrix} \delta & -\beta \\ -\gamma & \alpha \end{pmatrix}$, by the formula for the inverse of a $2 \times 2$ matrix.
18. $U$ is unitary, so $U^{-1} = U^* = \begin{pmatrix} \overline{\alpha} & \overline{\gamma} \\ \overline{\beta} & \overline{\delta} \end{pmatrix}$, by [[the properties of unitary matrices|GZ7NG7J3J8]].
19. Compare the entries of steps 17 and 18: $\delta = \overline{\alpha}$ and $-\beta = \overline{\gamma}$. So $\gamma = -\overline{\beta}$.
20. Write $\alpha = a + bi$ and $\beta = c + di$ with $a, b, c, d \in \R$. Then $U = \begin{pmatrix} a + bi & c + di \\ -c + di & a - bi \end{pmatrix} = \phi(a + bi + cj + dk)$.
21. By step 11, $\abs{a + bi + cj + dk}^2 = \det U = 1$. So $U$ is the image of a unit quaternion, and $\phi$ is an isomorphism onto $SU(2)$.

**Part 4.**

22. Steps 20 and 21 show that each $U \in SU(2)$ has the form $\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$ with $\abs{\alpha}^2 + \abs{\beta}^2 = 1$.
23. Conversely, each such matrix is $\phi(q)$ for a unit quaternion $q$, so it is in $SU(2)$ by step 13. $\blacksquare$

## Idea

The three matrices $I$, $J$ and $K$ satisfy the same rules as $i$, $j$ and $k$.
The quaternion conjugate becomes the conjugate transpose, and the norm squared becomes the determinant.
For the converse, the inverse of a matrix with determinant $1$ is its adjugate, and for a unitary matrix it is also the conjugate transpose.

## Variants

- One can start from $SU(2)$: steps 16 to 20 give the form of its elements, and then one defines the quaternions as the real span of these matrices.
- Other books use other signs, for example $\phi(j) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. Each choice gives an isomorphism, but the formulas differ.
