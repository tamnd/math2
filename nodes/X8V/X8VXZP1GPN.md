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

We write each entry of $G c$ as one inner product with a single vector $w$, and then every part follows from positive definiteness.
Let $V$, $v_1, \dots, v_k$ and $G$ be as in the statement, and for $c \in \mathbb{K}^k$ put
$$w = \sum_{j=1}^k \overline{c_j}\, v_j.$$

1. Part 1. Conjugate symmetry of the [[inner product|0VGSYBWHV2]] gives $G_{ji} = \ip{v_j}{v_i} = \overline{\ip{v_i}{v_j}} = \overline{G_{ij}}$.
2. By the [[definition of the Gram matrix|0HX8HZ1WTQ]], the $i$-th entry of $G c$ is $(G c)_i = \sum_j \ip{v_i}{v_j}\, c_j$.
3. The inner product is conjugate-linear in the second slot, so $c_j \ip{v_i}{v_j} = \ip{v_i}{\overline{c_j}\, v_j}$, and additivity in the second slot gives $(G c)_i = \ip{v_i}{w}$.
4. Part 2. By step 3 and linearity in the first slot, $c^* G c = \sum_i \overline{c_i} \ip{v_i}{w} = \ip{w}{w} = \norm{w}^2 \ge 0$.
5. Part 3, one direction. If $w = 0$, then step 3 gives $(G c)_i = \ip{v_i}{0} = 0$ for every $i$, so $G c = 0$.
6. Part 3, other direction. If $G c = 0$, then step 4 gives $\norm{w}^2 = c^* G c = 0$, and positive definiteness gives $w = 0$.
7. Part 4, one direction. Let $G$ be invertible and let $\sum_j a_j v_j = 0$. Put $c_j = \overline{a_j}$, so that $w = \sum_j a_j v_j = 0$.
8. Part 3 then gives $G c = 0$, and invertibility of $G$ gives $c = 0$. So every $a_j = 0$, and the $v_j$ are [[linearly independent|0EVHJFTG9Z]].
9. Part 4, other direction. Let the $v_j$ be independent and let $G c = 0$. Part 3 gives $\sum_j \overline{c_j}\, v_j = 0$.
10. Independence gives $\overline{c_j} = 0$ for every $j$, so $c = 0$. So the null space of $G$ is $\{0\}$.
11. A square matrix with null space $\{0\}$ is invertible, by the [[invertible matrix theorem|ACDFDABVQK]]. So $G$ is invertible.
12. Part 5. Let $L \colon \mathbb{K}^k \to V$ be the linear map $L(a) = \sum_j a_j v_j$. Its image is the span $S$ of the $v_j$.
13. The [[rank-nullity theorem|0W4FSW1TVB]] gives $\dim \ker L = k - \dim S$.
14. Write $\overline{c}$ for the column with the entries $\overline{c_j}$. By part 3, $c \in \ker G$ exactly when $\overline{c} \in \ker L$.
15. The map $c \mapsto \overline{c}$ is additive, turns a scalar $\lambda$ into $\overline{\lambda}$, and is its own inverse. So it maps a basis of $\ker L$ to a basis of $\ker G$, and $\dim \ker G = \dim \ker L = k - \dim S$.
16. Rank-nullity for $G$ gives $\operatorname{rank} G = k - \dim \ker G = \dim S$.

This proves parts 1 to 5.

## Idea

The $i$-th entry of $G c$ is the inner product of $v_i$ with one combination $w$ of the vectors.
Pairing $G c$ with $c$ then collects these entries into $\norm{w}^2$.
So $G c = 0$ forces $\norm{w} = 0$, and positive definiteness turns that into the linear relation $w = 0$.
The null space of $G$ is therefore the space of linear relations among the $v_j$, read with conjugate coefficients.

## Variants

For real column vectors there is a short matrix version.
The Gram matrix is $A^{\mathsf{T}} A$, and $A^{\mathsf{T}} A c = 0$ gives $c^{\mathsf{T}} A^{\mathsf{T}} A c = \norm{A c}^2 = 0$, so $A c = 0$; this shows $\ker(A^{\mathsf{T}} A) = \ker A$, and parts 4 and 5 follow.

Part 4 also follows from determinants.
The [[squared volume theorem|FWA0AKJA2R]] computes $\det G$ as a product of positive numbers for an independent family, so $G$ is invertible.
For the other direction, a relation $\sum_j a_j v_j = 0$ with some $a_j \ne 0$ gives $G \overline{a} = 0$ by step 5, so $G$ is singular.
