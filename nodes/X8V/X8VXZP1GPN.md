---
tag: X8VXZP1GPN
kind: proof
name: Proof that a Gram matrix is invertible if and only if the family is independent
msc: ["15A63", "15B57"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: EM1QNRGWQ8
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [0HX8HZ1WTQ, 0VGSYBWHV2, 0EVHJFTG9Z, ACDFDABVQK, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Positive-semidefiniteness
---

## Proof

Let $V$, $v_1, \dots, v_k$ and $G$ be as in the statement.
For $c \in \mathbb{K}^k$ put $w = \sum_{j=1}^k \overline{c_j}\, v_j$.

1. Part 1. By conjugate symmetry of the [[inner product|0VGSYBWHV2]], $G_{ji} = \ip{v_j}{v_i} = \overline{\ip{v_i}{v_j}} = \overline{G_{ij}}$.
2. Let $c \in \mathbb{K}^k$. By the [[definition of $G$|0HX8HZ1WTQ]], $(Gc)_i = \sum_j \ip{v_i}{v_j}\, c_j$ for each $i$.
3. Conjugate-linearity in the second slot gives $c_j \ip{v_i}{v_j} = \ip{v_i}{\overline{c_j}\, v_j}$. Additivity then gives $(Gc)_i = \ip{v_i}{w}$.
4. Part 2. By step 3 and linearity in the first slot, $c^* G c = \sum_i \overline{c_i} \ip{v_i}{w} = \ip{w}{w} = \norm{w}^2 \geq 0$.
5. Part 3, first direction. If $w = 0$, then step 3 gives $(Gc)_i = \ip{v_i}{0} = 0$ for every $i$.
6. Part 3, second direction. If $Gc = 0$, then step 4 gives $\norm{w}^2 = c^* G c = 0$. So $w = 0$, by positive definiteness.
7. Part 4, first direction. Let $G$ be invertible, and let $\sum_j a_j v_j = 0$. Put $c_j = \overline{a_j}$, so that $w = \sum_j a_j v_j = 0$.
8. Part 3 gives $Gc = 0$. Since $G$ is invertible, $c = 0$, so every $a_j = 0$. So the $v_j$ are [[independent|0EVHJFTG9Z]].
9. Part 4, second direction. Let the $v_j$ be independent, and let $Gc = 0$. Part 3 gives $\sum_j \overline{c_j}\, v_j = 0$.
10. Independence gives $\overline{c_j} = 0$ for every $j$, so $c = 0$.
11. So the null space of $G$ is $\set{0}$. The [[invertible matrix theorem|ACDFDABVQK]], conditions 17 and 1, shows that $G$ is invertible.
12. Part 5. Let $L \colon \mathbb{K}^k \to V$ be the linear map $L(a) = \sum_j a_j v_j$. Its image is the span $S$ of the $v_j$.
13. The [[rank-nullity theorem|0W4FSW1TVB]] gives $\dim \ker L = k - \dim S$.
14. By part 3, $c \in \ker G$ exactly when $\overline{c} \in \ker L$, where $\overline{c}$ has the entries $\overline{c_j}$.
15. Conjugation of the entries maps a basis of $\ker L$ to a basis of $\ker G$. It preserves sums, and it turns each scalar $\lambda$ into $\overline{\lambda}$.
16. So $\dim \ker G = \dim \ker L = k - \dim S$.
17. Rank-nullity for $G$ gives $\operatorname{rank} G = k - \dim \ker G = \dim S$.

## Idea

The $i$-th entry of $Gc$ is the inner product of $v_i$ with the combination $w = \sum_j \overline{c_j} v_j$.
Then $c^* G c = \norm{w}^2$, so $Gc = 0$ forces $w = 0$.
So the null space of $G$ is the space of linear relations among the $v_j$, up to conjugation.

## Variants

- Over $\mathbb{R}$, for column vectors, $G = A^T A$, and $A^T A c = 0$ gives $c^T A^T A c = \norm{Ac}^2 = 0$. So $\ker(A^T A) = \ker A$.
- One can prove part 4 with determinants: the [[squared volume theorem|FWA0AKJA2R]] gives $\det G > 0$ for an independent family.
