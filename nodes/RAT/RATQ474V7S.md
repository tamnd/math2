---
tag: RATQ474V7S
kind: proof
name: Proof of the change of basis rule for a bilinear form
msc: [15A63, 15A21]
proves: 0SPYAGE7T0
uses: [0P799D6AMN, 0P24YW565F, 0KWXYZPJKN, 0W809K6AW0]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf
    locator: Theorem 2.8
---

## Proof

We compute the entries of $M'$ directly.

1. Write $\mathcal{B} = (b_1, \dots, b_n)$ and $\mathcal{B}' = (b'_1, \dots, b'_n)$, and let $P = (p_{ij})$.
2. By the definition of the [[change of basis matrix|0KWXYZPJKN]], $b'_k = \sum_{i=1}^n p_{ik} b_i$ for each $k$.
3. By the definition of the [[matrix of a bilinear form|0P24YW565F]], $M_{ij} = B(b_i, b_j)$ and $M'_{kl} = B(b'_k, b'_l)$.
4. By step 2, $M'_{kl} = B\bigl(\sum_i p_{ik} b_i, \sum_j p_{jl} b_j\bigr)$.
5. A [[bilinear form|0P799D6AMN]] is linear in each argument. Expanding both arguments gives $M'_{kl} = \sum_{i=1}^n \sum_{j=1}^n p_{ik}\, B(b_i, b_j)\, p_{jl}$.
6. By step 3 and the definition of the [[transpose|0W809K6AW0]], $p_{ik} = (P^T)_{ki}$. So $M'_{kl} = \sum_{i,j} (P^T)_{ki} M_{ij} P_{jl}$.
7. The right side is the $(k, l)$ entry of the product $P^T M P$, by the definition of matrix multiplication.
8. This holds for all $k$ and $l$, so $M' = P^T M P$.

## Idea

Each new basis vector is a combination of old ones, with coefficients in a column of $P$. Bilinearity expands $B(b'_k, b'_l)$ into a double sum of old entries. That double sum is exactly a matrix product with $P$ on the right and $P^T$ on the left.
