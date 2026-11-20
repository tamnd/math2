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

We use $\ip{x}{y} = y^*x$ throughout.

**The equivalent conditions.**

1. Assume condition 1. Then $\overline{\det U}\det U = \det(U^*)\det U = \det(U^*U) = 1$, by steps 11 and 12 below and [[multiplicativity of the determinant|04CPJ6AF00]]. So $\det U \neq 0$, and $U$ is invertible.
2. Multiply $U^*U = I_n$ on the right by $U^{-1}$. This gives $U^* = U^{-1}$, which is condition 3.
3. Condition 3 gives $UU^* = UU^{-1} = I_n$, which is condition 2. In the same way, condition 2 gives that $U^*$ is a right inverse, so $U^* = U^{-1}$ and condition 1 holds.
4. The $(j, k)$ entry of $U^*U$ is $\sum_m \overline{u_{mj}}u_{mk} = \ip{c_k}{c_j}$, where $c_j$ is column $j$. So condition 1 says $\ip{c_k}{c_j} = 1$ for $j = k$ and $0$ for $j \neq k$, which is condition 4. Here $n$ orthonormal vectors in $\C^n$ are a basis, because they are linearly independent.
5. The $(j, k)$ entry of $UU^*$ is $\sum_m u_{jm}\overline{u_{km}} = \ip{r_j}{r_k}$, where $r_j$ is row $j$. So condition 2 is condition 5, in the same way.
6. Assume condition 1. Then $\ip{Ux}{Uy} = (Uy)^*(Ux) = y^*U^*Ux = y^*x = \ip{x}{y}$. This is condition 6.
7. Condition 6 with $y = x$ gives $\norm{Ux}^2 = \norm{x}^2$, which is condition 7.
8. Condition 7 implies condition 6, by [[the equivalent conditions for a linear isometry|95ST99SEW7]] applied to the map $x \mapsto Ux$. That proof uses the complex polarization identity.
9. Assume condition 6. For all $x$ and $y$, $\ip{(U^*U - I_n)x}{y} = y^*U^*Ux - y^*x = \ip{Ux}{Uy} - \ip{x}{y} = 0$.
10. Take $y = (U^*U - I_n)x$. Then $\norm{y}^2 = 0$, so $y = 0$. This holds for all $x$, so $U^*U = I_n$, which is condition 1.

**The determinant.**

11. The determinant is a polynomial in the entries with integer coefficients. So the determinant of the entrywise conjugate $\overline{U}$ is $\overline{\det U}$.
12. The [[determinant of the transpose|0ZZQ2E1MTE]] is the same determinant. So $\det(U^*) = \det(\overline{U}^T) = \overline{\det U}$.
13. Now let $U$ be unitary. By steps 11 and 12, $\abs{\det U}^2 = \overline{\det U}\det U = \det(U^*U) = \det I_n = 1$. So $\abs{\det U} = 1$.

**The eigenvalues and eigenvectors.**

14. Let $Uv = \lambda v$ with $v \neq 0$. By condition 7, $\norm{v} = \norm{Uv} = \abs{\lambda}\norm{v}$.
15. $\norm{v} \neq 0$, so $\abs{\lambda} = 1$. In particular, $\overline{\lambda} = \lambda^{-1}$.
16. Let $Uw = \mu w$ with $w \neq 0$ and $\mu \neq \lambda$. By condition 6, $\ip{v}{w} = \ip{Uv}{Uw} = \lambda\overline{\mu}\ip{v}{w}$.
17. By step 15, $\lambda\overline{\mu} = \lambda/\mu \neq 1$. So $(1 - \lambda/\mu)\ip{v}{w} = 0$ gives $\ip{v}{w} = 0$.

**The spectral form and the converse.**

18. By conditions 1 and 2, $U^*U = I_n = UU^*$. So $U$ is normal.
19. By the [[complex spectral theorem|04CW1P44VD]], $\C^n$ has an [[orthonormal basis|0FWJ0VW561]] $v_1, \dots, v_n$ of eigenvectors of $U$, with $Uv_k = \lambda_kv_k$.
20. Let $V$ be the matrix with columns $v_1, \dots, v_n$, and let $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. Then $V$ is unitary, by condition 4, and $UV = VD$.
21. So $U = VDV^{-1} = VDV^*$, and $\abs{\lambda_k} = 1$ by step 15.
22. For the converse, let $V$ be unitary and $D = \operatorname{diag}(d_1, \dots, d_n)$ with $\abs{d_k} = 1$. Then $D^*D = \operatorname{diag}(\abs{d_1}^2, \dots, \abs{d_n}^2) = I_n$.
23. So $(VDV^*)^*(VDV^*) = VD^*V^*VDV^* = VD^*DV^* = VV^* = I_n$, and $VDV^*$ is unitary. $\blacksquare$

## Idea

The entries of $U^*U$ and $UU^*$ are the inner products of the columns and of the rows.
The eigenvalue facts come from the fact that $U$ keeps lengths, and the spectral form comes from normality.

## Variants

- Step 8 can avoid the general theorem: the complex polarization identity writes $\ip{x}{y}$ with the four lengths $\norm{x + i^ky}$, and $U$ keeps them.
- Steps 14 and 15 also follow from a bound: all powers $U^k$ have columns of length $1$, so $\abs{\lambda}^k\norm{v} = \norm{U^kv} = \norm{v}$ for all $k \in \Z$.
