---
tag: HP32FXA1ZG
kind: proof
name: Proof that an orthonormal family is linearly independent
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 0JWM6GJNQW
methods: [0NTF6DMVAP]
uses: [0VGSYBWHV2, 09VYHEF2VT, 0TS7VZJBWD, 0EVHJFTG9Z, 08ZDRN6H41, 05G2G0P224]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Corollary 6.25
---

## Proof

Let $V$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.

1. Let $(v_i)_{i \in I}$ be nonzero and pairwise [[orthogonal|0TS7VZJBWD]]. By the definition of [[linear independence|0EVHJFTG9Z]], it is enough to test finite subfamilies.
2. Let $i_1, \dots, i_k \in I$ be distinct, and let $a_1, \dots, a_k \in \mathbb{K}$ with $a_1 v_{i_1} + \dots + a_k v_{i_k} = 0$.
3. Fix $m$ with $1 \leq m \leq k$. Linearity in the first argument gives $\ip{0}{v_{i_m}} = \ip{0 \cdot 0}{v_{i_m}} = 0 \cdot \ip{0}{v_{i_m}} = 0$.
4. Linearity in the first argument also gives $\ip{\sum_{l=1}^{k} a_l v_{i_l}}{v_{i_m}} = \sum_{l=1}^{k} a_l \ip{v_{i_l}}{v_{i_m}}$.
5. The indices are distinct, so $\ip{v_{i_l}}{v_{i_m}} = 0$ for $l \neq m$. The sum in step 4 equals $a_m \norm{v_{i_m}}^2$.
6. By steps 2 and 3, the same sum is $0$. So $a_m \norm{v_{i_m}}^2 = 0$.
7. Since $v_{i_m} \neq 0$, positive definiteness gives $\norm{v_{i_m}}^2 > 0$. Hence $a_m = 0$.
8. This holds for each $m$, so only the trivial combination vanishes. This proves part 1.
9. Part 2. Let $(e_i)_{i \in I}$ be [[orthonormal|09VYHEF2VT]]. Then $\norm{e_i}^2 = \ip{e_i}{e_i} = 1$, so each $e_i \neq 0$.
10. Also $\ip{e_i}{e_j} = 0$ for $i \neq j$. So part 1 applies, and the family is independent.
11. Part 3. Let $\dim V = n$, so a basis $w_1, \dots, w_n$ spans $V$, by the definition of [[dimension|05G2G0P224]].
12. Let $e_1, \dots, e_m$ be distinct members of an orthonormal family. By part 2 they are independent.
13. The [[Steinitz exchange lemma|08ZDRN6H41]] gives $m \leq n$. So the family has at most $n$ members.

## Idea

The inner product with $v_m$ picks out the coefficient of $v_m$ in a combination, times $\norm{v_m}^2$.
All other terms vanish by orthogonality.
If the combination is zero, each coefficient is zero, because $\norm{v_m}^2 \neq 0$.

## Variants

- For an orthonormal family, step 5 gives $a_m$ directly, since $\norm{e_m} = 1$.
- One can use the [[Pythagorean theorem|0BVTDM872V]]: if $\sum_l a_l e_l = 0$, then $0 = \norm{\sum_l a_l e_l}^2 = \sum_l |a_l|^2$, so every $a_l = 0$.
- In matrix form, for $V = \mathbb{K}^n$: if $Q^* Q = I_k$ and $Q a = 0$, then $a = Q^* Q a = 0$.
