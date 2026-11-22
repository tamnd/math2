---
tag: MP0MQDD34C
kind: proof
name: Proof of the equivalent conditions for a linear isometry
msc: ["15A04", "46C05"]
topics: [AZS5BPF5H3]
audience: ug1
proves: 95ST99SEW7
uses: [05FKHRT0B4, 09VYHEF2VT, 0Y85GYEGSF, 0FWJ0VW561, 0ST8QF9T3T, 0W4FSW1TVB]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Isometries
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

We prove the cycle of implications from 1 to 2, 2 to 3, 3 to 4, 4 to 5 and 5 to 1, and then we show that 5, 6 and 7 are equivalent when $\dim V = \dim W$.

**From 1 to 2.**

1. Assume condition 1, let $u, v \in V$, and first let $\mathbb{K} = \R$. The [[polarization identity|05FKHRT0B4]] in $W$ gives $\ip{Tu}{Tv} = \frac{1}{4}\left(\norm{Tu + Tv}^2 - \norm{Tu - Tv}^2\right)$.
2. Since $T$ is linear, $Tu + Tv = T(u + v)$ and $Tu - Tv = T(u - v)$. Condition 1 then gives $\norm{T(u \pm v)} = \norm{u \pm v}$.
3. So $\ip{Tu}{Tv} = \frac{1}{4}\left(\norm{u + v}^2 - \norm{u - v}^2\right)$, and the polarization identity in $V$ says that the right side is $\ip{u}{v}$.
4. Now let $\mathbb{K} = \C$, with the inner product linear in the first argument. The complex polarization identity is $\ip{x}{y} = \frac{1}{4}\sum_{k=0}^{3} i^k \norm{x + i^k y}^2$.
5. By linearity $Tu + i^k Tv = T(u + i^k v)$, and condition 1 gives $\norm{T(u + i^k v)} = \norm{u + i^k v}$ for $k = 0, 1, 2, 3$. So the identity for $\ip{Tu}{Tv}$ has the same four terms as the identity for $\ip{u}{v}$, and the two inner products are equal.

**From 2 to 3.**

6. Let $f_1, \dots, f_m$ be an [[orthonormal family|09VYHEF2VT]] of $V$, so $\ip{f_j}{f_k}$ is $1$ for $j = k$ and $0$ for $j \ne k$.
7. Condition 2 gives $\ip{Tf_j}{Tf_k} = \ip{f_j}{f_k}$ for all $j$ and $k$. So $Tf_1, \dots, Tf_m$ is an orthonormal family of $W$.

**From 3 to 4.**

8. The space $V$ is finite-dimensional, so it has an [[orthonormal basis|0FWJ0VW561]], by the [[existence theorem|0Y85GYEGSF]]. Condition 3 applied to this basis is condition 4.

**From 4 to 5.**

9. Let $e_1, \dots, e_n$ be as in condition 4, and write $u = \sum_j a_j e_j$ and $v = \sum_k b_k e_k$ with $a_j, b_k \in \mathbb{K}$.
10. The inner product is linear in the first argument and conjugate-linear in the second, and $T$ is linear. So $\ip{Tu}{Tv} = \sum_{j, k} a_j \overline{b_k} \ip{Te_j}{Te_k}$.
11. By condition 4, $\ip{Te_j}{Te_k}$ is $1$ for $j = k$ and $0$ otherwise, so $\ip{Tu}{Tv} = \sum_j a_j \overline{b_j}$. The same computation in $V$ gives $\ip{u}{v} = \sum_j a_j \overline{b_j}$, so $\ip{Tu}{Tv} = \ip{u}{v}$.
12. By the definition of the [[adjoint|0ST8QF9T3T]], $\ip{Tu}{Tv} = \ip{u}{T^*Tv}$. With step 11 this gives $\ip{u}{T^*Tv - v} = 0$ for all $u, v \in V$.
13. Fix $v$ and take $u = T^*Tv - v$. Then $\norm{T^*Tv - v}^2 = 0$, so $T^*Tv = v$. This holds for every $v$, so $T^*T = I_V$.

**From 5 to 1.**

14. Let $v \in V$. The definition of the adjoint and condition 5 give $\norm{Tv}^2 = \ip{Tv}{Tv} = \ip{v}{T^*Tv} = \ip{v}{v} = \norm{v}^2$.
15. Norms are nonnegative, so $\norm{Tv} = \norm{v}$.

**Equal dimensions.** Now let $\dim V = \dim W = n$.

16. Assume condition 5. If $Tv = 0$, then $v = T^*Tv = T^*0 = 0$, so $T$ is injective.
17. By the [[rank-nullity theorem|0W4FSW1TVB]], the range of $T$ has dimension $n - 0 = \dim W$. So $T$ is surjective, and hence invertible.
18. Then $T^* = T^*(TT^{-1}) = (T^*T)T^{-1} = T^{-1}$, by condition 5. This is condition 6.
19. Assume condition 6. Then $TT^* = TT^{-1} = I_W$, which is condition 7.
20. Assume condition 7. If $T^*w = 0$, then $w = TT^*w = 0$, so $T^* \colon W \to V$ is injective, and rank-nullity makes it invertible.
21. Then $T = T(T^*(T^*)^{-1}) = (TT^*)(T^*)^{-1} = (T^*)^{-1}$. So $T^*T = T^*(T^*)^{-1} = I_V$, which is condition 5.

So conditions 1 to 5 are equivalent, and they are equivalent to conditions 6 and 7 when $\dim V = \dim W$.

## Idea

The polarization identity writes an inner product in terms of norms, so a linear map that keeps norms keeps inner products.
An inner product is fixed by its values on an orthonormal basis, so a finite check on that basis is enough.
The adjoint turns "keeps inner products" into the single operator equation $T^*T = I$.
When the dimensions agree, rank-nullity turns this one-sided inverse into a two-sided inverse.

## Variants

One can go from 1 to 5 directly.
The operator $S = T^*T - I$ is self-adjoint, and $\ip{Sv}{v} = \norm{Tv}^2 - \norm{v}^2 = 0$ for all $v$.
A self-adjoint operator with $\ip{Sv}{v} = 0$ for all $v$ is $0$, so $T^*T = I$.

The step from 4 to 5 also has a matrix form.
The matrix $A$ of $T$ in orthonormal bases has the coordinate vectors of the $Te_j$ as its columns.
The entry $(j, k)$ of $A^*A$ is then $\ip{Te_k}{Te_j}$, so condition 4 says exactly that $A^*A = I$.
