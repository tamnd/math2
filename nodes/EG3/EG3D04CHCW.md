---
tag: EG3D04CHCW
kind: proof
name: Proof that the Gram-Schmidt process gives an orthonormal family with the same spans
msc: ["15A63", "65F25"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 0WXBGBTA3D
methods: [0ASJVEFA9J, 0J0XBKG64S, 0NTF6DMVAP]
uses: [0VGSYBWHV2, A1Y41YZFB6, 0TS7VZJBWD, 0EVHJFTG9Z, 0HR573CHNM, 09VYHEF2VT, 0KG4D8AP6G]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.32
---

## Proof

We prove parts 1 and 2 for the $u_j$ by induction on $j$, and then we read off the claims about the $e_j$.
Let $V$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ linear in the first slot.
Let $v_1, \dots, v_k$ be [[linearly independent|0EVHJFTG9Z]], let $u_j$ and $e_j$ be as in the [[Gram-Schmidt process|A1Y41YZFB6]], and write $c_{ji} = \ip{v_j}{u_i} / \ip{u_i}{u_i}$.
For $1 \leq j \leq k$, let $P(j)$ be the claim that $u_1, \dots, u_j$ are defined, nonzero and pairwise [[orthogonal|0TS7VZJBWD]], and that $\operatorname{span}(u_1, \dots, u_j) = \operatorname{span}(v_1, \dots, v_j)$.

1. Base case: $u_1 = v_1$, and an independent family contains no zero vector, since $1 \cdot 0 = 0$ would be a nontrivial relation, so $u_1 \neq 0$.
2. Also $\operatorname{span}(u_1) = \operatorname{span}(v_1)$, and there is no pair to check, so $P(1)$ holds.
3. Inductive step: let $2 \leq j \leq k$, assume $P(j - 1)$, and put $S = \operatorname{span}(u_1, \dots, u_{j-1}) = \operatorname{span}(v_1, \dots, v_{j-1})$.
4. Each $u_i$ with $i < j$ is nonzero, so $\ip{u_i}{u_i} > 0$ by positive definiteness, and hence the $c_{ji}$ and $u_j$ are defined.
5. Fix $m < j$; linearity in the first slot gives $\ip{u_j}{u_m} = \ip{v_j}{u_m} - \sum_{i < j} c_{ji}\ip{u_i}{u_m}$.
6. By $P(j - 1)$, $\ip{u_i}{u_m} = 0$ for $i \neq m$, so the sum is $c_{jm}\ip{u_m}{u_m} = \ip{v_j}{u_m}$, and therefore $\ip{u_j}{u_m} = 0$.
7. By conjugate symmetry also $\ip{u_m}{u_j} = 0$, so $u_1, \dots, u_j$ are pairwise orthogonal.
8. Write $s = \sum_{i < j} c_{ji} u_i$, which lies in $S$, so that $u_j = v_j - s$ and $v_j = u_j + s$.
9. Since $S \subseteq \operatorname{span}(v_1, \dots, v_j)$, step 8 gives $u_j \in \operatorname{span}(v_1, \dots, v_j)$, and so $\operatorname{span}(u_1, \dots, u_j) \subseteq \operatorname{span}(v_1, \dots, v_j)$.
10. In the same way $v_j = u_j + s$ lies in $\operatorname{span}(u_1, \dots, u_j)$, so the two [[spans|0HR573CHNM]] are equal.
11. Suppose $u_j = 0$; then $v_j = s \in S = \operatorname{span}(v_1, \dots, v_{j-1})$, say $v_j = \sum_{i < j} b_i v_i$.
12. Then $\sum_{i < j} b_i v_i - v_j = 0$ is a relation with the coefficient $-1$ at $v_j$, which contradicts independence, so $u_j \neq 0$.
13. So $P(j)$ holds, and by induction $P(j)$ holds for all $j \leq k$, which proves part 1 and the second equality of part 2.
14. Part 3: the [[induced norm|0KG4D8AP6G]] is homogeneous, so $\norm{e_j} = \norm{u_j}/\norm{u_j} = 1$.
15. For $i \neq j$, $\ip{e_i}{e_j} = \ip{u_i}{u_j} / (\norm{u_i}\norm{u_j}) = 0$, because the norms are real and no conjugate appears, so $(e_j)$ is [[orthonormal|09VYHEF2VT]].
16. Part 2, first equality: each $e_i$ is a nonzero multiple of $u_i$, so the two lists span the same subspaces.
17. Part 4: with $s$ from step 8, $\ip{s}{u_j} = \sum_{i < j} c_{ji}\ip{u_i}{u_j} = 0$ by part 1.
18. So $\ip{v_j}{u_j} = \ip{u_j}{u_j} + \ip{s}{u_j} = \norm{u_j}^2$.
19. Since $1/\norm{u_j}$ is real, $\ip{v_j}{e_j} = \ip{v_j}{u_j}/\norm{u_j} = \norm{u_j}$, which is positive by part 1.
20. Part 5: let $v_1, \dots, v_m$ be orthonormal; we show $u_j = e_j = v_j$ for $j \leq m$ by induction on $j$.
21. For $j = 1$, $u_1 = v_1$ and $\norm{v_1} = 1$, so $e_1 = v_1$.
22. Let $2 \leq j \leq m$ with $u_i = v_i$ for $i < j$; then $\ip{v_j}{u_i} = \ip{v_j}{v_i} = 0$, so every $c_{ji}$ is $0$.
23. Hence $u_j = v_j$, and $\norm{v_j} = 1$ gives $e_j = v_j$.

This proves all five parts of the [[Gram-Schmidt theorem|0WXBGBTA3D]].

## Idea

Each new vector $u_j$ is $v_j$ minus its shadows on the earlier $u_i$.
Since the earlier vectors are already orthogonal to each other, removing the shadow on $u_m$ changes the inner product with $u_m$ and with nothing else, and it brings that inner product to $0$.
The vector $u_j$ cannot be zero, because then $v_j$ would be a combination of the earlier $v_i$.
Normalizing changes neither orthogonality nor spans, so the claims pass from the $u_j$ to the $e_j$.

## Variants

One can phrase the inductive step with the [[orthogonal projection|0B8KZRT28M]] $P$ onto $S$.
Then $u_j = v_j - P v_j$, and $v_j - P v_j$ is orthogonal to $S$ by the projection theorem, which replaces steps 5 to 7.

One cannot skip the induction by a direct computation of all $\ip{u_j}{u_m}$ at once.
The coefficients $c_{ji}$ are only defined when the earlier $u_i$ are known to be nonzero, and that is part of the inductive claim.
