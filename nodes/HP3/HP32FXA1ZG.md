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

We take the inner product of a vanishing combination with each vector of the family, which isolates one coefficient at a time.
Let $V$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.

*Part 1.*

1. Let $(v_i)_{i \in I}$ be nonzero and pairwise [[orthogonal|0TS7VZJBWD]].
   By the definition of [[linear independence|0EVHJFTG9Z]] for a family, it is enough to test finite subfamilies.
2. Let $i_1, \dots, i_k \in I$ be distinct, and let $a_1, \dots, a_k \in \mathbb{K}$ satisfy
$$a_1 v_{i_1} + \dots + a_k v_{i_k} = 0.$$
3. Fix $m$ with $1 \le m \le k$.
   The inner product of the zero vector with any vector is $0$, because linearity in the first argument gives $\ip{0}{w} = \ip{0 \cdot 0}{w} = 0 \cdot \ip{0}{w}$.
4. Take the inner product of both sides of step 2 with $v_{i_m}$.
   Linearity in the first argument and step 3 give
$$\sum_{l=1}^{k} a_l \ip{v_{i_l}}{v_{i_m}} = 0.$$
5. The indices are distinct, so $\ip{v_{i_l}}{v_{i_m}} = 0$ for $l \neq m$ by orthogonality.
   The sum in step 4 is therefore $a_m \ip{v_{i_m}}{v_{i_m}}$, so $a_m \ip{v_{i_m}}{v_{i_m}} = 0$.
6. Since $v_{i_m} \neq 0$, positive definiteness gives $\ip{v_{i_m}}{v_{i_m}} > 0$, and we can cancel this factor.
   Hence $a_m = 0$.
7. This holds for each $m$, so only the trivial combination vanishes, and the family is independent.

*Part 2.*

8. Let $(e_i)_{i \in I}$ be [[orthonormal|09VYHEF2VT]].
   Then $\ip{e_i}{e_i} = 1 \neq 0$, so each $e_i$ is nonzero, and $\ip{e_i}{e_j} = 0$ for $i \neq j$.
9. So part 1 applies, and the family is independent.

*Part 3.*

10. Let $\dim V = n$, so a basis $w_1, \dots, w_n$ spans $V$, by the definition of [[dimension|05G2G0P224]].
11. Let $e_1, \dots, e_m$ be distinct members of an orthonormal family.
    By part 2 they are independent.
12. The [[Steinitz exchange lemma|08ZDRN6H41]] says that an independent family in a space spanned by $n$ vectors has at most $n$ members, so $m \le n$.
13. Every finite subfamily has at most $n$ members, so the family itself has at most $n$ members.

## Idea

Take a combination that gives zero and pair it with one vector $v_m$ of the family.
Orthogonality kills every term except the one with $v_m$, and that term is the coefficient of $v_m$ times $\norm{v_m}^2$.
Since $\norm{v_m}^2$ is not zero, the coefficient must be zero.
Doing this for each $m$ shows that every coefficient is zero.

## Variants

For an orthonormal family, step 5 gives $a_m = 0$ at once, since $\ip{e_m}{e_m} = 1$.
A second proof uses the [[Pythagorean theorem|0BVTDM872V]]: if $\sum_l a_l e_l = 0$, then
$$0 = \norm{\textstyle\sum_l a_l e_l}^2 = \sum_l \abs{a_l}^2,$$
and a sum of nonnegative terms is zero only when each term is zero.
In matrix form, for $V = \mathbb{K}^n$, let $Q$ have the orthonormal columns, so that $Q^* Q = I_k$.
If $Q a = 0$, then $a = Q^* Q a = Q^* 0 = 0$.
