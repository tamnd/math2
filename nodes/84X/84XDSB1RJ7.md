---
tag: 84XDSB1RJ7
kind: proof
name: Proof that the matrix of a composition is the product of the matrices
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
proves: 05Q1B7MH0M
uses: [0YQSGNYE3K, 032Q9FB8MT, 00BKRZKMSS, 0NRYHJPQG2, 0KCQ9Y3QKA]
methods: [0NTF6DMVAP, 41JZ39GE3F]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.2
---

## Proof

We compute the image of each basis vector of $U$ under $T \circ S$ in two stages and compare its coordinates with the entries of the product.

1. Write $A = (a_1, \dots, a_p)$, $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$ for the [[bases|0KCQ9Y3QKA]] of $U$, $V$ and $W$.
2. Let $[S]_{B,A} = (s_{jk})$, an $n \times p$ matrix; by the definition of the [[matrix of a linear map|0YQSGNYE3K]], $S(a_k) = \sum_{j=1}^n s_{jk} b_j$ for $1 \le k \le p$.
3. Let $[T]_{C,B} = (t_{ij})$, an $m \times n$ matrix; in the same way, $T(b_j) = \sum_{i=1}^m t_{ij} c_i$ for $1 \le j \le n$.
4. The [[composite|00BKRZKMSS]] $T \circ S$ is linear, since $S$ and $T$ are [[linear|0NRYHJPQG2]], so its matrix $[T \circ S]_{C,A}$ is defined.
5. Fix $k$ with $1 \le k \le p$; step 2 and the linearity of $T$ give
$$(T \circ S)(a_k) = T\Bigl(\sum_{j=1}^n s_{jk} b_j\Bigr) = \sum_{j=1}^n s_{jk}\, T(b_j).$$
6. We put in step 3 and exchange the two finite sums:
$$\sum_{j=1}^n s_{jk} \sum_{i=1}^m t_{ij} c_i = \sum_{i=1}^m \Bigl(\sum_{j=1}^n t_{ij} s_{jk}\Bigr) c_i.$$
7. Coordinates in the basis $C$ are unique, so step 6 shows that entry $(i, k)$ of $[T \circ S]_{C,A}$ is $\sum_{j=1}^n t_{ij} s_{jk}$.
8. By the definition of the [[matrix product|032Q9FB8MT]], $\sum_{j=1}^n t_{ij} s_{jk}$ is also entry $(i, k)$ of $[T]_{C,B}\,[S]_{B,A}$.
9. By steps 7 and 8, the two $m \times p$ matrices have the same entries, so $[T \circ S]_{C,A} = [T]_{C,B}\,[S]_{B,A}$.

## Idea

Column $k$ of a matrix records where the $k$-th basis vector goes.
Push $a_k$ first through $S$, which gives a combination of the $b_j$, and then through $T$, which turns each $b_j$ into a combination of the $c_i$.
Collecting the coefficient of $c_i$ gives exactly the sum that defines entry $(i, k)$ of the product.
In this sense the definition of matrix multiplication is the bookkeeping of composition.

## Variants

A shorter proof uses the [[coordinate formula|8B63KHW6D5]].
For each $u \in U$ it gives $[T(S(u))]_C = [T]_{C,B}[S(u)]_B = [T]_{C,B}\bigl([S]_{B,A}[u]_A\bigr)$, and associativity of matrix products turns this into $\bigl([T]_{C,B}[S]_{B,A}\bigr)[u]_A$.
The uniqueness part of the coordinate formula then gives the theorem.
This proof needs associativity of matrix multiplication as an input, while the proof by sums above gives associativity as an output.

A proof column by column uses the fact that column $k$ of a product $MN$ is $M$ times column $k$ of $N$.
So column $k$ of $[T]_{C,B}[S]_{B,A}$ is $[T]_{C,B}[S(a_k)]_B$, which is $[T(S(a_k))]_C$ by the coordinate formula, and that is column $k$ of $[T \circ S]_{C,A}$.
