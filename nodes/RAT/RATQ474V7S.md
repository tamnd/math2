---
tag: RATQ474V7S
kind: proof
name: Proof of the change of basis rule for a bilinear form
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
proves: 0SPYAGE7T0
methods: [0NTF6DMVAP]
uses: [0P799D6AMN, 0P24YW565F, 0KWXYZPJKN, 0W809K6AW0, 0MQXVZEBMT, 02FDWY55AS, 04CPJ6AF00, 0ZZQ2E1MTE]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf
    locator: Theorem 2.8
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: lead section
---

## Proof

We compute the entries of $M'$ directly, and then compare ranks and determinants.

1. Write $\mathcal{B} = (b_1, \dots, b_n)$ and $\mathcal{B}' = (b'_1, \dots, b'_n)$, and let $P = (p_{ij})$.
2. By the definition of the [[change of basis matrix|0KWXYZPJKN]], $b'_k = \sum_{i=1}^n p_{ik} b_i$ for each $k$.
3. By the definition of the [[matrix of a bilinear form|0P24YW565F]], $M_{ij} = B(b_i, b_j)$ and $M'_{kl} = B(b'_k, b'_l)$.
4. By step 2, $M'_{kl} = B\bigl(\sum_i p_{ik} b_i, \sum_j p_{jl} b_j\bigr)$.
5. A [[bilinear form|0P799D6AMN]] is linear in each argument. Expanding both arguments gives $M'_{kl} = \sum_{i=1}^n \sum_{j=1}^n p_{ik}\, B(b_i, b_j)\, p_{jl}$.
6. By the definition of the [[transpose|0W809K6AW0]], $p_{ik} = (P^T)_{ki}$. With step 3, $M'_{kl} = \sum_{i,j} (P^T)_{ki} M_{ij} P_{jl}$.
7. The right side is the $(k, l)$ entry of the product $P^T M P$, by the definition of matrix multiplication.
8. This holds for all $k$ and $l$, so $M' = P^T M P$. This is part 1.
9. The matrix $P$ is invertible, by part 1 of the [[change of basis formula|0MQXVZEBMT]]. So $P^T$ is invertible too, with inverse $(P^{-1})^T$.
10. By the [[rank of a product|02FDWY55AS]], a product with an invertible factor has the rank of the other factor. So $\rank(P^T M P) = \rank(M P) = \rank M$. This is part 2.
11. By the [[multiplicativity of the determinant|04CPJ6AF00]], $\det M' = \det(P^T) \det M \det P$.
12. By the [[determinant of the transpose|0ZZQ2E1MTE]], $\det(P^T) = \det P$. So $\det M' = (\det P)^2 \det M$.
13. $\det P \neq 0$ because $P$ is invertible, by step 9. This is part 3.

## Idea

Each new basis vector is a combination of old ones, with coefficients in a column of $P$.
Bilinearity expands $B(b'_k, b'_l)$ into a double sum of old entries.
That double sum is a matrix product with $P$ on the right and $P^T$ on the left.
Rank and determinant then follow from the general rules for products.

## Variants

With coordinate vectors, $u = Px'$ and $v = Py'$ give $B(u, v) = (Px')^T M (Py') = x'^T (P^T M P) y'$ by the [[transpose of a product|09GK5PS824]].
Since a form determines its matrix, this gives part 1 in one line.
