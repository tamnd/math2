---
tag: WCKDVAZMR2
kind: proof
name: Proof of the criteria for a nondegenerate bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
proves: 3ND2FNJ38Y
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [0KAN330PAH, ZVMJAF7D53, TR48YQGCCA, 0W4FSW1TVB, 0TZAG60ZYT, 00889YD15K, ACDFDABVQK, 059THXBRBB]
sources:
  - url: https://en.wikipedia.org/wiki/Degenerate_bilinear_form
    locator: Nondegenerate forms
---

## Proof

Let $(e_1, \dots, e_n)$ be the basis, and let $x$ be the coordinate vector of $u$.

Part 1.

1. The linear form $L_B(u)$ is zero exactly when it is zero on each $e_j$, because a linear form is fixed by its values on a basis.
2. By the [[correspondence theorem|ZVMJAF7D53]], $L_B(u)(e_j) = B(u, e_j) = \sum_i x_i A_{ij} = (A^T x)_j$.
3. So $u$ lies in the left radical exactly when $A^T x = 0$. The coordinate map is an [[isomorphism|059THXBRBB]] $V \to F^n$, so the left radical has the dimension of the null space of $A^T$.
4. By the [[rank-nullity theorem for matrices|TR48YQGCCA]], the null space of $A^T$ has dimension $n - \rank A^T$.
5. By [[row rank equals column rank|0TZAG60ZYT]], $\rank A^T = \rank A$. So the left radical has dimension $n - \rank A$.
6. In the same way, $v$ with coordinate vector $y$ lies in the right radical exactly when $B(e_i, v) = (Ay)_i = 0$ for all $i$, that is, when $Ay = 0$.
7. So the right radical has dimension $n - \rank A$ too.

Part 2.

8. (a) and (b) are equivalent: by part 1, each says $n - \rank A = 0$.
9. (a) and (c) are equivalent: $\rank A = n$ exactly when the square matrix $A$ is invertible, by the [[invertible matrix theorem|ACDFDABVQK]].
10. (d) implies (a): an isomorphism has kernel $\{0\}$, and the kernel of $L_B$ is the left radical.
11. (a) implies (d): $L_B$ is linear, by the correspondence theorem. Its kernel is $\{0\}$, so the [[rank-nullity theorem|0W4FSW1TVB]] gives $\dim \im L_B = n$.
12. By the [[dimension of the dual space|00889YD15K]], $\dim V^* = n$. A subspace of $V^*$ of dimension $n$ is all of $V^*$, so $L_B$ is surjective and an isomorphism.
13. Steps 10 to 12 with $R_B$ in place of $L_B$ show that (b) and (e) are equivalent.

Part 3.

14. Let $\lambda \colon V \to W^*$, $v \mapsto C(v, \cdot)$, and $\rho \colon W \to V^*$, $w \mapsto C(\cdot, w)$. Both are linear, by bilinearity of $C$.
15. $\lambda$ is injective, so rank-nullity gives $\dim V = \dim \im \lambda \le \dim W^* = \dim W$.
16. $\rho$ is injective, so in the same way $\dim W \le \dim V^* = \dim V$.
17. So $\dim V = \dim W$. Then $\lambda$ is an injective map into a space of the same dimension, and step 12 shows that it is surjective. The same holds for $\rho$.

This proves all three parts.

## Idea

Membership in the left radical is a system of linear equations with the matrix $A^T$, and membership in the right radical is one with the matrix $A$.
Since a matrix and its transpose have the same rank, the two radicals have the same dimension.
An injective linear map between spaces of the same finite dimension is bijective, and this gives the isomorphisms with the dual.

## Variants

The map $R_B$ is the dual map of $L_B$ after the identification of $V$ with $V^{**}$.
The [[kernel of a dual map|7FA499AW3T]] is the annihilator of the image, and this gives part 1 without matrices.
