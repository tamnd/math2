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

Let $V$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.
Let $v_1, \dots, v_k$ be [[linearly independent|0EVHJFTG9Z]], and let $u_j$, $e_j$ be as in the [[Gram-Schmidt process|A1Y41YZFB6]], with $c_{ji} = \ip{v_j}{u_i} / \ip{u_i}{u_i}$.
For $1 \leq j \leq k$, let $P(j)$ be the claim: $u_1, \dots, u_j$ are defined, nonzero and pairwise [[orthogonal|0TS7VZJBWD]], and $\operatorname{span}(u_1, \dots, u_j) = \operatorname{span}(v_1, \dots, v_j)$.

1. Base case: $u_1 = v_1$. An independent family has no zero vector, since $1 \cdot 0 = 0$ is a nontrivial relation. So $u_1 \neq 0$.
2. Also $\operatorname{span}(u_1) = \operatorname{span}(v_1)$, and there is no pair to check. So $P(1)$ holds.
3. Inductive step. Let $2 \leq j \leq k$ and assume $P(j - 1)$. Put $S = \operatorname{span}(u_1, \dots, u_{j-1}) = \operatorname{span}(v_1, \dots, v_{j-1})$.
4. Each $u_i$ with $i < j$ is nonzero, so $\ip{u_i}{u_i} > 0$. Hence the $c_{ji}$ and $u_j$ are defined.
5. Fix $m < j$. Linearity in the first argument gives $\ip{u_j}{u_m} = \ip{v_j}{u_m} - \sum_{i < j} c_{ji}\ip{u_i}{u_m}$.
6. By $P(j - 1)$, $\ip{u_i}{u_m} = 0$ for $i \neq m$. So the sum is $c_{jm}\ip{u_m}{u_m} = \ip{v_j}{u_m}$, and $\ip{u_j}{u_m} = 0$.
7. By conjugate symmetry also $\ip{u_m}{u_j} = 0$. So $u_1, \dots, u_j$ are pairwise orthogonal.
8. Write $s = \sum_{i < j} c_{ji} u_i \in S$, so $u_j = v_j - s$ and $v_j = u_j + s$.
9. Since $S \subseteq \operatorname{span}(v_1, \dots, v_j)$, step 8 gives $u_j \in \operatorname{span}(v_1, \dots, v_j)$. So $\operatorname{span}(u_1, \dots, u_j) \subseteq \operatorname{span}(v_1, \dots, v_j)$.
10. In the same way, $v_j = u_j + s$ lies in $\operatorname{span}(u_1, \dots, u_j)$. So the two [[spans|0HR573CHNM]] are equal.
11. Suppose $u_j = 0$. Then $v_j = s \in S = \operatorname{span}(v_1, \dots, v_{j-1})$, say $v_j = \sum_{i < j} b_i v_i$.
12. Then $\sum_{i < j} b_i v_i - v_j = 0$ has the coefficient $-1$ at $v_j$. This contradicts independence, so $u_j \neq 0$.
13. So $P(j)$ holds, and by induction $P(j)$ holds for all $j \leq k$. This proves part 1 and the second equality of part 2.
14. Part 3. By homogeneity of the [[induced norm|0KG4D8AP6G]], $\norm{e_j} = \norm{u_j}/\norm{u_j} = 1$.
15. For $i \neq j$, $\ip{e_i}{e_j} = \ip{u_i}{u_j} / (\norm{u_i}\norm{u_j}) = 0$, since the norms are real. So $(e_j)$ is [[orthonormal|09VYHEF2VT]].
16. Part 2, first equality. Each $e_i$ is a nonzero multiple of $u_i$, so they span the same subspaces.
17. Part 4. With $s$ from step 8, $\ip{s}{u_j} = \sum_{i < j} c_{ji}\ip{u_i}{u_j} = 0$ by part 1.
18. So $\ip{v_j}{u_j} = \ip{u_j}{u_j} + \ip{s}{u_j} = \norm{u_j}^2$.
19. Since $1/\norm{u_j}$ is real, $\ip{v_j}{e_j} = \ip{v_j}{u_j}/\norm{u_j} = \norm{u_j} > 0$.
20. Part 5. Let $v_1, \dots, v_m$ be orthonormal. We show $u_j = e_j = v_j$ for $j \leq m$ by induction on $j$.
21. For $j = 1$, $u_1 = v_1$ and $\norm{v_1} = 1$, so $e_1 = v_1$.
22. Let $2 \leq j \leq m$ with $u_i = v_i$ for $i < j$. Then $\ip{v_j}{u_i} = \ip{v_j}{v_i} = 0$, so every $c_{ji} = 0$.
23. Hence $u_j = v_j$, and $\norm{v_j} = 1$ gives $e_j = v_j$.

## Idea

Each new vector $u_j$ is $v_j$ minus its components along the earlier $u_i$.
Since the earlier vectors are already orthogonal, subtracting the component along $u_m$ removes exactly the inner product with $u_m$.
The vector $u_j$ cannot be zero, since then $v_j$ would be a combination of the earlier $v_i$.
Normalizing does not change orthogonality or spans.

## Variants

- One can phrase the inductive step with the [[orthogonal projection|0B8KZRT28M]] $P$ onto $S$: $u_j = v_j - P v_j$, and $v_j - P v_j \perp S$ by the projection theorem.
- One can prove part 1 by a direct computation of all $\ip{u_j}{u_m}$, but the induction is needed to know that the coefficients $c_{ji}$ are defined.
