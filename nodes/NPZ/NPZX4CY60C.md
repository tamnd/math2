---
tag: NPZX4CY60C
kind: proof
name: Proof that the matrix of the dual map is the transpose
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: 0ZPB3180AY
methods: [0NTF6DMVAP]
uses: [0YYMY95FWS, 0C2TQMW5A1, 0W6M3PSD08, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Representation as a matrix
---

## Proof

We compute the number $c_i^*(T b_j)$ in two ways, once with the matrix of $T$ and once with the matrix of $T^*$.

1. Let $B^* = (b_1^*, \dots, b_n^*)$ and $C^* = (c_1^*, \dots, c_m^*)$ be the [[dual bases|0W6M3PSD08]], so that $b_l^*(b_j) = \delta_{lj}$ and $c_i^*(c_k) = \delta_{ik}$, where $\delta_{ij}$ is $1$ for $i = j$ and $0$ otherwise.
2. Let $[T]_{C, B} = (a_{ij})$, an $m \times n$ matrix. By the [[definition of the matrix of a linear map|0YYMY95FWS]], $T(b_j) = \sum_{k=1}^{m} a_{kj} c_k$ for $1 \le j \le n$.
3. The [[dual map|0C2TQMW5A1]] is $T^* \colon W^* \to V^*$, $T^*(\varphi) = \varphi \circ T$. Let $[T^*]_{B^*, C^*} = (d_{li})$, an $n \times m$ matrix, so that $T^*(c_i^*) = \sum_{l=1}^{n} d_{li} b_l^*$ for $1 \le i \le m$.
4. Fix $i \le m$ and $j \le n$. Evaluating the sum of step 3 at $b_j$ and using step 1, only the term with $l = j$ survives:
$$T^*(c_i^*)(b_j) = \sum_{l=1}^{n} d_{li} \, b_l^*(b_j) = d_{ji}.$$
5. By the definition of $T^*$ and step 2, the same number can be computed as follows, and by step 1 only the term with $k = i$ survives:
$$T^*(c_i^*)(b_j) = c_i^*(T b_j) = \sum_{k=1}^{m} a_{kj} \, c_i^*(c_k) = a_{ij}.$$
6. Steps 4 and 5 give $d_{ji} = a_{ij}$ for all $i \le m$ and $j \le n$.
7. By the definition of the [[transpose|0W809K6AW0]], step 6 says $[T^*]_{B^*, C^*} = \left([T]_{C, B}\right)^{\mathsf{T}}$.

## Idea

The dual basis is made for reading off coordinates: $c_i^*$ applied to a vector of $W$ gives its $i$-th coordinate in the basis $C$.
So the single number $c_i^*(T b_j)$ is the $i$-th coordinate of $T b_j$, which is entry $(i, j)$ of $[T]$.
The same number is also the value of the form $T^*(c_i^*)$ at $b_j$, which is entry $(j, i)$ of $[T^*]$.
One number in two places means the two matrices are transposes of each other.

## Variants

For $V = F^n$ and $W = F^m$ with the standard bases, write forms as rows.
Then $T^*(y) = yA$ by associativity, and in columns $(yA)^{\mathsf{T}} = A^{\mathsf{T}} y^{\mathsf{T}}$, as in the example on [[the dual of a matrix map|QM8XZDS9TK]].
The general case reduces to this one through the coordinate isomorphisms $V \cong F^n$ and $W \cong F^m$ given by the bases, together with the [[functoriality of the dual map|XBKREPBM9D]].
