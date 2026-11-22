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

We write membership in each radical as a system of linear equations, with matrix $A^{\mathsf{T}}$ for the left radical and $A$ for the right radical, and then we count dimensions.
Let $(e_1, \dots, e_n)$ be the basis, so that $A_{ij} = B(e_i, e_j)$.
For $u \in V$ let $x$ be its coordinate column, and for $v \in V$ let $y$ be its coordinate column.

Part 1.

1. The linear form $L_B(u)$ is zero exactly when it is zero on each $e_j$, because a linear form is fixed by its values on a basis.
2. By the [[correspondence of forms and matrices|ZVMJAF7D53]] and bilinearity, $L_B(u)(e_j) = B(u, e_j) = \sum_i x_i A_{ij}$, and this is entry $j$ of $A^{\mathsf{T}} x$.
3. So $u$ lies in the left radical exactly when $A^{\mathsf{T}} x = 0$. The coordinate map is an [[isomorphism|059THXBRBB]] $V \to F^n$, so the left radical has the dimension of the null space of $A^{\mathsf{T}}$.
4. By the [[rank-nullity theorem for matrices|TR48YQGCCA]], this null space has dimension $n - \operatorname{rank} A^{\mathsf{T}}$.
5. Since [[row rank equals column rank|0TZAG60ZYT]], $\operatorname{rank} A^{\mathsf{T}} = \operatorname{rank} A$. So the left radical has dimension $n - \operatorname{rank} A$.
6. In the same way, $B(e_i, v) = \sum_j A_{ij} y_j$ is entry $i$ of $A y$. So $v$ lies in the right radical exactly when $A y = 0$.
7. By rank-nullity again, the right radical has dimension $n - \operatorname{rank} A$.

Part 2.

8. Conditions (a) and (b) are equivalent, because by part 1 each one says $n - \operatorname{rank} A = 0$.
9. Conditions (a) and (c) are equivalent, because the square matrix $A$ has rank $n$ exactly when it is invertible, by the [[invertible matrix theorem|ACDFDABVQK]].
10. Condition (d) implies (a), because an isomorphism has kernel $\{0\}$ and the kernel of $L_B$ is the left radical.
11. Condition (a) implies (d). The map $L_B$ is linear, by the correspondence theorem, and its kernel is $\{0\}$. So the [[rank-nullity theorem|0W4FSW1TVB]] gives $\dim \operatorname{im} L_B = n$.
12. By the [[dimension of the dual space|00889YD15K]], $\dim V^* = n$. A subspace of $V^*$ of dimension $n$ is all of $V^*$, so $L_B$ is surjective, and so it is an isomorphism.
13. Steps 10 to 12 with $R_B$ in place of $L_B$ show that (b) and (e) are equivalent.

Part 3.

14. Let $\lambda \colon V \to W^*$ be $\lambda(v) = C(v, \cdot)$ and let $\rho \colon W \to V^*$ be $\rho(w) = C(\cdot, w)$. Both maps are linear, because $C$ is bilinear.
15. The map $\lambda$ is injective, so rank-nullity gives $\dim V = \dim \operatorname{im} \lambda \le \dim W^* = \dim W$.
16. The map $\rho$ is injective, so in the same way $\dim W \le \dim V^* = \dim V$.
17. So $\dim V = \dim W$. Then $\lambda$ is an injective linear map between spaces of the same finite dimension, and the argument of step 12 shows that it is surjective. The same holds for $\rho$.

This proves all three parts.

## Idea

A vector lies in the left radical when its coordinates solve the homogeneous system with matrix $A^{\mathsf{T}}$, and it lies in the right radical when its coordinates solve the system with matrix $A$.
A matrix and its transpose have the same rank, so the two solution spaces have the same dimension, even when they are different subspaces.
The rest is one fact used three times: an injective linear map between spaces of the same finite dimension is also surjective.
That fact is exactly where finite dimension enters.

## Variants

A proof without matrices uses duality.
After the identification of $V$ with $V^{**}$, the map $R_B$ is the dual map of $L_B$, because both send the pair $(u, v)$ to $B(u, v)$.
The [[kernel of the dual map|7FA499AW3T]] is the annihilator of the image, so $\dim \ker R_B = n - \dim \operatorname{im} L_B = \dim \ker L_B$, which is part 1.
