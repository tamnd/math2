---
tag: 84XDSB1RJ7
kind: proof
name: Proof that the matrix of a composition is the product of the matrices
msc: [15A04]
proves: 05Q1B7MH0M
uses: [0YQSGNYE3K, 032Q9FB8MT, 00BKRZKMSS, 0NRYHJPQG2, 0KCQ9Y3QKA]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.2
---

## Proof

We compute the image of each basis vector of $U$ under $T \circ S$ in two steps.

1. Write $A = (a_1, \dots, a_p)$, $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$ for the [[bases|0KCQ9Y3QKA]] of $U$, $V$ and $W$.
2. Let $[S]_{B,A} = (s_{jk})$, an $n \times p$ matrix. By the definition of the [[matrix of a linear map|0YQSGNYE3K]], $S(a_k) = \sum_{j=1}^n s_{jk} b_j$ for $1 \le k \le p$.
3. Let $[T]_{C,B} = (t_{ij})$, an $m \times n$ matrix. Then $T(b_j) = \sum_{i=1}^m t_{ij} c_i$ for $1 \le j \le n$.
4. The [[composition|00BKRZKMSS]] $T \circ S$ is linear: $T(S(u + \lambda u')) = T(S(u)) + \lambda T(S(u'))$ for $u, u' \in U$ and $\lambda \in F$, since $S$ and $T$ are [[linear|0NRYHJPQG2]].
5. Fix $k$ with $1 \le k \le p$. By step 2 and the linearity of $T$, $(T \circ S)(a_k) = T\left(\sum_{j=1}^n s_{jk} b_j\right) = \sum_{j=1}^n s_{jk} T(b_j)$.
6. By step 3, this equals $\sum_{j=1}^n s_{jk} \sum_{i=1}^m t_{ij} c_i = \sum_{i=1}^m \left(\sum_{j=1}^n t_{ij} s_{jk}\right) c_i$.
7. By the definition of the [[matrix product|032Q9FB8MT]], $\sum_{j=1}^n t_{ij} s_{jk}$ is the entry $(i, k)$ of $[T]_{C,B}\,[S]_{B,A}$.
8. The coordinates of a vector in the basis $C$ are unique. So, by step 6, entry $(i, k)$ of $[T \circ S]_{C,A}$ is $\sum_{j=1}^n t_{ij} s_{jk}$.
9. By steps 7 and 8, the two $m \times p$ matrices have the same entries. Hence $[T \circ S]_{C,A} = [T]_{C,B}\,[S]_{B,A}$.

## Idea

Column $k$ of a matrix records where the $k$-th basis vector goes. Pushing $a_k$ first through $S$ and then through $T$ produces exactly the sum that defines the $(i, k)$ entry of the product. This is why matrix multiplication is defined the way it is.
