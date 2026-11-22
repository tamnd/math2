---
tag: DBYTK4D7YV
kind: proof
name: Proof that the matrix of the adjoint is the conjugate transpose
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
proves: 0DBTE6HVBD
uses: [0VGSYBWHV2, 0ST8QF9T3T, 0YYMY95FWS, 0EX045E2BP, 0FWJ0VW561, 09DZ8CD1AK, 00SPJSDT3Z]
methods: [0NTF6DMVAP]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 7.9
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

For part 1, we compute both matrices entry by entry with the formula for coordinates in an orthonormal basis.
For part 2, we write the inner product in coordinates.

1. Let $V$ and $W$ be finite-dimensional inner product spaces over $\mathbb{K} = \R$ or $\C$, with [[inner products|0VGSYBWHV2]] written $\ip{\cdot}{\cdot}$. Let $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$ be [[orthonormal bases|0FWJ0VW561]] of $V$ and $W$.
2. Let $T \colon V \to W$ be linear, with [[adjoint|0ST8QF9T3T]] $T^* \colon W \to V$. So $\ip{T(v)}{w} = \ip{v}{T^*(w)}$ for all $v \in V$ and $w \in W$.
3. By the definition of the [[matrix of a linear map|0YYMY95FWS]], $[T]_{C,B} = (a_{ij})$ is the $m \times n$ matrix with $T(b_j) = \sum_{i=1}^{m} a_{ij} c_i$.
4. Likewise, $[T^*]_{B,C} = (d_{ji})$ is the $n \times m$ matrix with $T^*(c_i) = \sum_{j=1}^{n} d_{ji} b_j$, for $1 \le i \le m$.
5. By the [[formula for coordinates|09DZ8CD1AK]] in the orthonormal basis $C$, the coordinates of $T(b_j)$ are $a_{ij} = \ip{T(b_j)}{c_i}$.
6. By the same formula in the orthonormal basis $B$, the coordinates of $T^*(c_i)$ are $d_{ji} = \ip{T^*(c_i)}{b_j}$.
7. By conjugate symmetry and step 2, $d_{ji} = \overline{\ip{b_j}{T^*(c_i)}} = \overline{\ip{T(b_j)}{c_i}} = \overline{a_{ij}}$.
8. By the definition of the [[conjugate transpose|0EX045E2BP]], the $(j, i)$ entry of $([T]_{C,B})^*$ is $\overline{a_{ij}}$.
9. So $[T^*]_{B,C}$ and $([T]_{C,B})^*$ have the same size $n \times m$ and the same entries. Hence $[T^*]_{B,C} = ([T]_{C,B})^*$. This proves part 1.
10. Part 2. Let $V = W$ and let $B = (b_1, \dots, b_n)$ be any basis. For $v = \sum_j x_j b_j$ and $w = \sum_i y_i b_i$, write $x$ and $y$ for the coordinate columns.
11. Linearity in the first slot and conjugate linearity in the second slot give $\ip{v}{w} = \sum_{i,j} \overline{y_i}\, \ip{b_j}{b_i}\, x_j = y^* H x$.
12. The matrix $H$ is invertible. If $Hx = 0$, then $x^* H x = \ip{v}{v} = 0$ for $v = \sum_j x_j b_j$. So $v = 0$, and $x = 0$ because $B$ is a basis.
13. Let $M = [T]_B$ and $N = [T^*]_B$. By the definition of the [[matrix of a linear map|0YYMY95FWS]], the coordinates of $Tv$ are $Mx$, and the coordinates of $T^* w$ are $Ny$.
14. By step 11, $\ip{Tv}{w} = y^* H M x$ and $\ip{v}{T^* w} = (Ny)^* H x = y^* N^* H x$.
15. The [[definition of the adjoint|0ST8QF9T3T]] says that these numbers agree for all $x, y \in \mathbb{K}^n$. With $x = e_j$ and $y = e_i$, the $(i, j)$ entries of $HM$ and $N^* H$ agree. So $HM = N^* H$.
16. The matrix $H$ is Hermitian, since $\overline{H_{ji}} = \overline{\ip{b_i}{b_j}} = \ip{b_j}{b_i} = H_{ij}$. Taking the conjugate transpose of step 15 gives $M^* H = H N$.
17. Multiplying on the left by $H^{-1}$ gives $N = H^{-1} M^* H$. This proves part 2.

## Idea

In an orthonormal basis, each matrix entry is an inner product: the $(i, j)$ entry of $[T]$ is $\ip{T(b_j)}{c_i}$.
The defining property of the adjoint moves $T$ across the inner product.
Conjugate symmetry then turns the entry of $[T^*]$ into the conjugate of the mirrored entry of $[T]$.
In a general basis, the inner product in coordinates is $y^* H x$, and the matrix $H$ appears in the formula.

## Variants

Part 1 is the special case $H = I$ of part 2, since $H_{ij} = \ip{b_j}{b_i} = \delta_{ij}$ for an orthonormal basis.
So one can prove part 2 first and deduce part 1 for $V = W$.
For a matrix $A$ and the standard inner products, a one-line proof of part 1 is $\ip{Ax}{y} = y^* A x = (A^* y)^* x = \ip{x}{A^* y}$, which uses only the rule $(MN)^* = N^* M^*$ for matrices.
The general case reduces to this one, because orthonormal bases turn $V$ and $W$ into $\mathbb{K}^n$ and $\mathbb{K}^m$ with their standard inner products.
