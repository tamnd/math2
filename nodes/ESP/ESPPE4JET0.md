---
tag: ESPPE4JET0
kind: proof
name: Proof of the properties of a unitary matrix
msc: ["15B57", "15A18"]
topics: [AZS5BPF5H3]
audience: ug2
proves: GZ7NG7J3J8
uses: [95ST99SEW7, 04CPJ6AF00, 0ZZQ2E1MTE, 04CW1P44VD, 0FWJ0VW561]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: Equivalent conditions
  - book: isbn:9780521839402
    locator: Chapter 2
---

## Proof

We read the entries of $U^* U$ and $U U^*$ as inner products of columns and rows, we use the determinant to get invertibility, and we use the complex spectral theorem for the diagonal form.
Throughout, $\langle x, y \rangle = y^* x$.

**The determinant of the conjugate transpose.**

1. The determinant is a polynomial in the entries with integer coefficients, and conjugation respects sums and products, so $\det \overline{U} = \overline{\det U}$.
2. The [[determinant of the transpose|0ZZQ2E1MTE]] equals the determinant, so $\det(U^*) = \det(\overline{U}^{\mathsf{T}}) = \overline{\det U}$.

**The equivalent conditions.**

3. Assume condition 1. By step 2 and [[multiplicativity of the determinant|04CPJ6AF00]], $\overline{\det U} \det U = \det(U^* U) = \det I_n = 1$, so $\det U \ne 0$ and $U$ is invertible.
4. Multiply $U^* U = I_n$ on the right by $U^{-1}$ to get $U^* = U^{-1}$, which is condition 3.
5. Condition 3 gives $U U^* = U U^{-1} = I_n$, which is condition 2. In the same way, condition 2 makes $U^*$ a right inverse of the square matrix $U$, so $U^* = U^{-1}$, and conditions 3 and 1 follow.
6. The entry in position $(j, k)$ of $U^* U$ is $\sum_m \overline{u_{mj}} u_{mk} = \langle c_k, c_j \rangle$, where $c_j$ is column $j$. So condition 1 says that the columns are orthonormal. Orthonormal vectors are linearly independent, so $n$ of them in $\C^n$ form a basis, and this is condition 4.
7. The entry in position $(j, k)$ of $U U^*$ is $\sum_m u_{jm} \overline{u_{km}} = \langle r_j, r_k \rangle$, where $r_j$ is row $j$. So condition 2 is condition 5 in the same way.
8. Assume condition 1. Then $\langle Ux, Uy \rangle = (Uy)^* (Ux) = y^* U^* U x = y^* x = \langle x, y \rangle$, which is condition 6.
9. Condition 6 with $y = x$ gives $\lVert Ux \rVert^2 = \lVert x \rVert^2$, which is condition 7.
10. Condition 7 implies condition 6, by [[the equivalent conditions for a linear isometry|95ST99SEW7]] applied to the complex-linear map $x \mapsto Ux$; that proof uses the complex polarization identity.
11. Assume condition 6. For all $x$ and $y$,
$$\langle (U^* U - I_n) x, y \rangle = y^* U^* U x - y^* x = \langle Ux, Uy \rangle - \langle x, y \rangle = 0.$$
12. Take $y = (U^* U - I_n) x$. Then $\lVert y \rVert^2 = 0$, so $y = 0$. This holds for every $x$, so $U^* U = I_n$, which is condition 1.

**The determinant and the eigenvalues.**

13. Let $U$ be unitary. Step 3 gives $\lvert \det U \rvert^2 = \overline{\det U} \det U = 1$, so $\lvert \det U \rvert = 1$.
14. Let $U v = \lambda v$ with $v \ne 0$. By condition 7, $\lVert v \rVert = \lVert U v \rVert = \lvert \lambda \rvert \lVert v \rVert$.
15. Since $\lVert v \rVert \ne 0$, we get $\lvert \lambda \rvert = 1$, and so $\overline{\lambda} = \lambda^{-1}$.
16. Let $U w = \mu w$ with $w \ne 0$ and $\mu \ne \lambda$. By condition 6, $\langle v, w \rangle = \langle U v, U w \rangle = \lambda \overline{\mu} \langle v, w \rangle$.
17. By step 15, $\lambda \overline{\mu} = \lambda / \mu \ne 1$, so $(1 - \lambda / \mu) \langle v, w \rangle = 0$ gives $\langle v, w \rangle = 0$.

**The spectral form and the converse.**

18. Conditions 1 and 2 give $U^* U = I_n = U U^*$, so $U$ is normal.
19. By the [[complex spectral theorem|04CW1P44VD]], $\C^n$ has an [[orthonormal basis|0FWJ0VW561]] $v_1, \dots, v_n$ of eigenvectors of $U$, with $U v_k = \lambda_k v_k$.
20. Let $V$ have columns $v_1, \dots, v_n$, and let $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. Then $V$ is unitary by condition 4, and $U V = V D$.
21. So $U = V D V^{-1} = V D V^*$, and $\lvert \lambda_k \rvert = 1$ by step 15.
22. For the converse, let $V$ be unitary and $D = \operatorname{diag}(d_1, \dots, d_n)$ with $\lvert d_k \rvert = 1$. Then $D^* D = \operatorname{diag}(\lvert d_1 \rvert^2, \dots, \lvert d_n \rvert^2) = I_n$.
23. So
$$(V D V^*)^* (V D V^*) = V D^* V^* V D V^* = V D^* D V^* = V V^* = I_n,$$
and $V D V^*$ is unitary.

## Idea

Every entry of $U^* U$ is an inner product of two columns, and every entry of $U U^*$ is an inner product of two rows.
So the matrix conditions are statements about orthonormal columns or rows, and the determinant shows that a one-sided inverse is two-sided.
The eigenvalue facts come from the fact that $U$ keeps lengths: an eigenvector cannot grow or shrink.
The diagonal form comes from normality and the spectral theorem.

## Variants

Step 10 can avoid the general theorem on isometries.
The complex polarization identity writes $4 \langle x, y \rangle$ as $\sum_{k=0}^{3} i^k \lVert x + i^k y \rVert^2$, and $U$ keeps each of the four lengths, because $U(x + i^k y) = Ux + i^k Uy$.
Steps 14 and 15 also follow from powers: every power $U^k$ with $k \in \Z$ is unitary, so $\lvert \lambda \rvert^k \lVert v \rVert = \lVert U^k v \rVert = \lVert v \rVert$, and a positive number whose powers stay equal to $1$ is $1$.
