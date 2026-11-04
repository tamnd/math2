---
tag: NGCNGVNWQ6
kind: proof
name: Proof of the formula for coordinates in an orthonormal basis
msc: [15A63, 46C05]
proves: 09DZ8CD1AK
uses: [0VGSYBWHV2, 0FWJ0VW561, 09VYHEF2VT, 0VTQTPQGAV]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.30
---

## Proof

We compute the inner product of $v$ with each basis vector.

1. Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$, so $\ip{e_j}{e_i} = \delta_{ji}$.
2. Let $v \in V$. Since $(e_1, \dots, e_n)$ is a [[basis|0VTQTPQGAV]], there are scalars $a_1, \dots, a_n \in \mathbb{K}$ with $v = \sum_{j=1}^{n} a_j e_j$.
3. Fix $i$ with $1 \le i \le n$. Linearity in the first argument gives $\ip{v}{e_i} = \sum_{j=1}^{n} a_j \ip{e_j}{e_i}$.
4. By [[orthonormality|09VYHEF2VT]], every term with $j \ne i$ is $0$, and the term with $j = i$ is $a_i$. So $\ip{v}{e_i} = a_i$.
5. Substituting step 4 into step 2 gives $v = \sum_{i=1}^{n} \ip{v}{e_i} e_i$.
6. The coordinates of $v$ in a basis are unique, so they are the numbers $a_i = \ip{v}{e_i}$.

## Idea

Write $v$ in the basis with unknown coefficients. The inner product with $e_i$ kills every term except the one with $e_i$, because the basis vectors are orthogonal unit vectors. So this inner product is exactly the coefficient $a_i$.
