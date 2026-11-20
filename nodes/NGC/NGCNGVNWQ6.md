---
tag: NGCNGVNWQ6
kind: proof
name: Proof of the formula for coordinates in an orthonormal basis
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 09DZ8CD1AK
methods: [0NTF6DMVAP]
uses: [0VGSYBWHV2, 0FWJ0VW561, 09VYHEF2VT, 0VTQTPQGAV, 0BVTDM872V]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.30
---

## Proof

Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.
Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$, and let $v \in V$.

1. Since $(e_1, \dots, e_n)$ is a [[basis|0VTQTPQGAV]], there are scalars $a_1, \dots, a_n$ with $v = \sum_{j=1}^{n} a_j e_j$.
2. Fix $i$. Linearity in the first argument gives $\ip{v}{e_i} = \sum_{j=1}^{n} a_j \ip{e_j}{e_i}$.
3. By [[orthonormality|09VYHEF2VT]], $\ip{e_j}{e_i} = 0$ for $j \neq i$ and $\ip{e_i}{e_i} = 1$. So $\ip{v}{e_i} = a_i$.
4. Part 1. Put step 3 into step 1: $v = \sum_{i=1}^{n} \ip{v}{e_i} e_i$.
5. Part 2. The vectors $a_1 e_1, \dots, a_n e_n$ are pairwise orthogonal, since $\ip{a_j e_j}{a_l e_l} = a_j \overline{a_l}\ip{e_j}{e_l} = 0$ for $j \neq l$.
6. The [[Pythagorean theorem|0BVTDM872V]] for $n$ vectors gives $\norm{v}^2 = \sum_{j} \norm{a_j e_j}^2$.
7. By homogeneity of the norm, $\norm{a_j e_j}^2 = |a_j|^2 \norm{e_j}^2 = |a_j|^2$.
8. With step 3, $\norm{v}^2 = \sum_{j=1}^{n} |\ip{v}{e_j}|^2$.

## Idea

Write $v$ in the basis with unknown coefficients.
The inner product with $e_i$ removes every term except the one with $e_i$, and that term is the coefficient $a_i$.
The length then follows from Pythagoras, because the terms $a_j e_j$ are pairwise orthogonal.

## Variants

- One can prove part 2 by direct expansion: $\ip{v}{v} = \sum_{j, l} a_j \overline{a_l}\ip{e_j}{e_l} = \sum_j |a_j|^2$.
- One can avoid the existence of the coefficients in step 1. Put $w = v - \sum_i \ip{v}{e_i} e_i$, check $\ip{w}{e_i} = 0$ for all $i$, and conclude $w = 0$, since $w$ is orthogonal to a basis.
