---
tag: DBYTK4D7YV
kind: proof
name: Proof that the matrix of the adjoint is the conjugate transpose
msc: [15A04, 47A05]
proves: 0DBTE6HVBD
uses: [0VGSYBWHV2, 0ST8QF9T3T, 0YYMY95FWS, 0EX045E2BP, 0FWJ0VW561, 09DZ8CD1AK]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 7.9
---

## Proof

We compute both matrices entry by entry with the formula for coordinates in an orthonormal basis.

1. Let $V$ and $W$ be finite-dimensional inner product spaces over $\mathbb{K} = \R$ or $\C$, with [[inner products|0VGSYBWHV2]] written $\ip{\cdot}{\cdot}$. Let $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$ be [[orthonormal bases|0FWJ0VW561]] of $V$ and $W$.
2. Let $T \colon V \to W$ be linear, with [[adjoint|0ST8QF9T3T]] $T^* \colon W \to V$. So $\ip{T(v)}{w} = \ip{v}{T^*(w)}$ for all $v \in V$ and $w \in W$.
3. By the definition of the [[matrix of a linear map|0YYMY95FWS]], $[T]_{C,B} = (a_{ij})$ is the $m \times n$ matrix with $T(b_j) = \sum_{i=1}^{m} a_{ij} c_i$.
4. Likewise, $[T^*]_{B,C} = (d_{ji})$ is the $n \times m$ matrix with $T^*(c_i) = \sum_{j=1}^{n} d_{ji} b_j$, for $1 \le i \le m$.
5. By the [[formula for coordinates|09DZ8CD1AK]] in the orthonormal basis $C$, the coordinates of $T(b_j)$ are $a_{ij} = \ip{T(b_j)}{c_i}$.
6. By the same formula in the orthonormal basis $B$, the coordinates of $T^*(c_i)$ are $d_{ji} = \ip{T^*(c_i)}{b_j}$.
7. By conjugate symmetry and step 2, $d_{ji} = \overline{\ip{b_j}{T^*(c_i)}} = \overline{\ip{T(b_j)}{c_i}} = \overline{a_{ij}}$.
8. By the definition of the [[conjugate transpose|0EX045E2BP]], the $(j, i)$ entry of $([T]_{C,B})^*$ is $\overline{a_{ij}}$.
9. So $[T^*]_{B,C}$ and $([T]_{C,B})^*$ have the same size $n \times m$ and the same entries. Hence $[T^*]_{B,C} = ([T]_{C,B})^*$.

## Idea

In an orthonormal basis, each matrix entry is an inner product: the $(i, j)$ entry of $[T]$ is $\ip{T(b_j)}{c_i}$. The defining property of the adjoint moves $T$ across the inner product. Conjugate symmetry then turns the entry of $[T^*]$ into the conjugate of the mirrored entry of $[T]$.
