---
tag: HP32FXA1ZG
kind: proof
name: Proof that an orthonormal family is linearly independent
msc: [15A63, 46C05]
proves: 0JWM6GJNQW
uses: [0VGSYBWHV2, 09VYHEF2VT, 0EVHJFTG9Z]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Corollary 6.25
---

## Proof

We take the inner product of a vanishing combination with each vector of the family.

1. Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $(e_i)_{i \in I}$ be an [[orthonormal family|09VYHEF2VT]] in $V$, so $\ip{e_i}{e_j} = \delta_{ij}$ for all $i, j \in I$.
2. By the definition of [[linear independence|0EVHJFTG9Z]] of a family, it is enough to show that each finite subfamily is linearly independent.
3. Let $i_1, \dots, i_k$ be distinct indices in $I$. Let $a_1, \dots, a_k \in \mathbb{K}$ with $a_1 e_{i_1} + \cdots + a_k e_{i_k} = 0$.
4. Fix $m$ with $1 \le m \le k$. The inner product of $0$ with $e_{i_m}$ is $\ip{0}{e_{i_m}} = \ip{0 \cdot 0}{e_{i_m}} = 0 \cdot \ip{0}{e_{i_m}} = 0$, by linearity in the first argument.
5. Linearity in the first argument also gives $\ip{\sum_{l=1}^{k} a_l e_{i_l}}{e_{i_m}} = \sum_{l=1}^{k} a_l \ip{e_{i_l}}{e_{i_m}}$.
6. Since the indices are distinct, $\ip{e_{i_l}}{e_{i_m}} = \delta_{lm}$. So the sum in step 5 equals $a_m$.
7. By steps 3, 4 and 5, this sum is also $0$. Hence $a_m = 0$.
8. This holds for each $m$, so the only vanishing combination is the trivial one. Thus $(e_i)_{i \in I}$ is linearly independent.

## Idea

The inner product with $e_m$ picks out the coefficient of $e_m$ in a combination, because all the other vectors are orthogonal to $e_m$ and $e_m$ has length one. If the combination is zero, each picked coefficient is zero.
