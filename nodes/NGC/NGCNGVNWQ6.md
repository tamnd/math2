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

We write $v$ in the basis with unknown coefficients, find each coefficient by one inner product, and then get the norm from the Pythagorean theorem.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ linear in the first slot.
Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$, and let $v \in V$.

*Part 1.*

1. Since $(e_1, \dots, e_n)$ is a [[basis|0VTQTPQGAV]], there are scalars $a_1, \dots, a_n$ with
$$v = \sum_{j=1}^{n} a_j e_j.$$
2. Fix $i$, and take the inner product of both sides with $e_i$ in the second slot.
   Linearity in the first slot gives
$$\ip{v}{e_i} = \sum_{j=1}^{n} a_j \ip{e_j}{e_i}.$$
3. By [[orthonormality|09VYHEF2VT]], $\ip{e_j}{e_i} = 0$ for $j \neq i$ and $\ip{e_i}{e_i} = 1$.
   So the sum in step 2 has one term left, and $\ip{v}{e_i} = a_i$.
4. Put the values of step 3 into step 1 to get $v = \sum_{i=1}^{n} \ip{v}{e_i} e_i$.

*Part 2.*

5. The vectors $a_1 e_1, \dots, a_n e_n$ are pairwise orthogonal, since for $j \neq l$ linearity in the first slot and conjugate-linearity in the second give
$$\ip{a_j e_j}{a_l e_l} = a_j \overline{a_l} \ip{e_j}{e_l} = 0.$$
6. The [[Pythagorean theorem|0BVTDM872V]] for $n$ pairwise orthogonal vectors gives
$$\norm{v}^2 = \sum_{j=1}^{n} \norm{a_j e_j}^2.$$
7. By homogeneity of the norm, $\norm{a_j e_j}^2 = \abs{a_j}^2 \norm{e_j}^2 = \abs{a_j}^2$, since $\norm{e_j} = 1$.
8. With $a_j = \ip{v}{e_j}$ from step 3, this gives $\norm{v}^2 = \sum_{j=1}^{n} \abs{\ip{v}{e_j}}^2$.

## Idea

Write $v$ in the basis with unknown coefficients.
The inner product with $e_i$ removes every term except the one with $e_i$, and that term is exactly the coefficient $a_i$, because $e_i$ has length $1$.
The length then follows from the Pythagorean theorem, because the pieces $a_j e_j$ are pairwise orthogonal.

## Variants

Part 2 also follows by direct expansion, with no appeal to the Pythagorean theorem:
$$\ip{v}{v} = \sum_{j, l} a_j \overline{a_l} \ip{e_j}{e_l} = \sum_{j} a_j \overline{a_j} = \sum_j \abs{a_j}^2.$$
Part 1 can also be proved without naming the coefficients first.
Put $w = v - \sum_i \ip{v}{e_i} e_i$ and check that $\ip{w}{e_k} = \ip{v}{e_k} - \ip{v}{e_k} = 0$ for every $k$.
Then $w$ is orthogonal to a basis, hence to every vector, and in particular $\ip{w}{w} = 0$, so $w = 0$.
