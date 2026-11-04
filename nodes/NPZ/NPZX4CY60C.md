---
tag: NPZX4CY60C
kind: proof
name: Proof that the matrix of the dual map is the transpose
msc: [15A04]
proves: 0ZPB3180AY
uses: [0YYMY95FWS, 0C2TQMW5A1, 0W6M3PSD08, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Representation as a matrix
---

## Proof

1. Write $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$. Let $B^* = (b_1^*, \dots, b_n^*)$ and $C^* = (c_1^*, \dots, c_m^*)$ be the [[dual bases|0W6M3PSD08]], so $b_l^*(b_j) = \delta_{lj}$ and $c_i^*(c_k) = \delta_{ik}$.
2. Here $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ otherwise.
3. Let $[T]_{C,B} = (a_{ij})$, an $m \times n$ matrix. By the [[definition of the matrix of a linear map|0YYMY95FWS]], $T(b_j) = \sum_{k=1}^{m} a_{kj} c_k$ for $1 \le j \le n$.
4. The [[dual map|0C2TQMW5A1]] is $T^* \colon W^* \to V^*$, $T^*(f) = f \circ T$. Its matrix $[T^*]_{B^*, C^*} = (d_{li})$ is $n \times m$.
5. By the same definition, $T^*(c_i^*) = \sum_{l=1}^{n} d_{li} b_l^*$ for $1 \le i \le m$.
6. Fix $i \le m$ and $j \le n$. Evaluating step 5 at $b_j$ gives $T^*(c_i^*)(b_j) = \sum_{l=1}^{n} d_{li} \delta_{lj} = d_{ji}$.
7. On the other hand, by step 4 and step 3, $T^*(c_i^*)(b_j) = c_i^*(T(b_j)) = \sum_{k=1}^{m} a_{kj} c_i^*(c_k)$.
8. Since $c_i^*(c_k) = \delta_{ik}$, the sum in step 7 equals $a_{ij}$.
9. By steps 6 to 8, $d_{ji} = a_{ij}$ for all $i \le m$ and $j \le n$.
10. By the definition of the [[transpose|0W809K6AW0]], step 9 says $[T^*]_{B^*, C^*} = \left([T]_{C,B}\right)^T$.

## Idea

The entries of both matrices can be read off by pairing a dual basis form with a basis vector. The number $c_i^*(T(b_j))$ is entry $(i, j)$ of $[T]$ and also entry $(j, i)$ of $[T^*]$, so the two matrices are transposes.
