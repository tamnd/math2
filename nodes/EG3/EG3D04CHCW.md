---
tag: EG3D04CHCW
kind: proof
name: Proof that the Gram–Schmidt vectors are orthogonal
msc: [15A63, 65F25]
proves: 0WXBGBTA3D
uses: [0VGSYBWHV2, 0VT6P0GNQR, 0TS7VZJBWD, 0EVHJFTG9Z, 0HR573CHNM]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.32
---

## Proof

We argue by induction on $j$.

1. Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $v_1, \dots, v_k \in V$ be [[linearly independent|0EVHJFTG9Z]].
2. The [[Gram–Schmidt process|0VT6P0GNQR]] sets $u_1 = v_1$ and $u_j = v_j - \sum_{i=1}^{j-1} c_{ji} u_i$ for $j \ge 2$, where $c_{ji} = \ip{v_j}{u_i} / \ip{u_i}{u_i}$.
3. The formula for $u_j$ makes sense only if $u_1, \dots, u_{j-1}$ are nonzero. So we prove, for $1 \le j \le k$, the claim $P(j)$ below.
4. $P(j)$ says: the vectors $u_1, \dots, u_j$ are defined and nonzero, they are pairwise [[orthogonal|0TS7VZJBWD]], and $\operatorname{span}(u_1, \dots, u_j) = \operatorname{span}(v_1, \dots, v_j)$. Here span is the [[linear span|0HR573CHNM]].
5. Base case $j = 1$. We have $u_1 = v_1$. A linearly independent family has no zero vector, since $1 \cdot 0 = 0$ is a nontrivial vanishing combination. So $u_1 \ne 0$.
6. Also $\operatorname{span}(u_1) = \operatorname{span}(v_1)$, and there is no pair to check. So $P(1)$ holds.
7. Induction step. Let $2 \le j \le k$ and assume $P(j-1)$. Write $S = \operatorname{span}(u_1, \dots, u_{j-1}) = \operatorname{span}(v_1, \dots, v_{j-1})$.
8. Each $u_i$ with $i < j$ is nonzero, so $\ip{u_i}{u_i} > 0$. Hence the numbers $c_{ji}$ and the vector $u_j$ are defined.
9. Fix $m < j$. Linearity in the first argument gives $\ip{u_j}{u_m} = \ip{v_j}{u_m} - \sum_{i=1}^{j-1} c_{ji} \ip{u_i}{u_m}$.
10. By $P(j-1)$, $\ip{u_i}{u_m} = 0$ for $i \ne m$ with $i, m < j$. So the sum in step 9 is $c_{jm} \ip{u_m}{u_m} = \ip{v_j}{u_m}$.
11. Hence $\ip{u_j}{u_m} = 0$. By conjugate symmetry, also $\ip{u_m}{u_j} = \overline{0} = 0$. With $P(j-1)$, the vectors $u_1, \dots, u_j$ are pairwise orthogonal.
12. By step 2, $u_j = v_j - s$ with $s = \sum_{i < j} c_{ji} u_i \in S$. Since $S \subseteq \operatorname{span}(v_1, \dots, v_j)$, we get $u_j \in \operatorname{span}(v_1, \dots, v_j)$.
13. Also $u_1, \dots, u_{j-1} \in S \subseteq \operatorname{span}(v_1, \dots, v_j)$. So $\operatorname{span}(u_1, \dots, u_j) \subseteq \operatorname{span}(v_1, \dots, v_j)$, because the span is the smallest subspace that contains the vectors.
14. Conversely, $v_j = u_j + s$ with $s \in S \subseteq \operatorname{span}(u_1, \dots, u_j)$. With $v_1, \dots, v_{j-1} \in S$, this gives the reverse inclusion. So the two spans are equal.
15. Suppose that $u_j = 0$. Then $v_j = s \in S = \operatorname{span}(v_1, \dots, v_{j-1})$.
16. Write $v_j = \sum_{i < j} b_i v_i$. Then $\sum_{i<j} b_i v_i - v_j = 0$ is a vanishing combination with coefficient $-1$ at $v_j$. This contradicts linear independence.
17. Hence $u_j \ne 0$, and $P(j)$ holds.
18. By induction, $P(k)$ holds, and $P(j)$ holds for every $j \le k$. So $u_1, \dots, u_k$ are nonzero and pairwise orthogonal, with the stated spans.

## Idea

Each new vector $u_j$ is $v_j$ minus its components along the earlier $u_i$. Because the earlier vectors are already orthogonal, subtracting the component along $u_m$ kills exactly the inner product with $u_m$. The vector $u_j$ cannot be zero, since then $v_j$ would be a combination of the earlier $v_i$.
