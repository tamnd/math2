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

We compute each entry of $M'$ by bilinearity, recognize a matrix product, and then read off the rank and the determinant from the rules for products.

1. Write $P = (p_{ij})$. By the definition of the [[change of basis matrix|0KWXYZPJKN]], column $k$ of $P$ holds the coordinates of $b'_k$, so
$$b'_k = \sum_{i=1}^n p_{ik}\, b_i \quad \text{for } k = 1, \dots, n.$$
2. By the definition of the [[matrix of a bilinear form|0P24YW565F]], $M_{ij} = B(b_i, b_j)$ and $M'_{kl} = B(b'_k, b'_l)$. Substitute step 1 into both slots:
$$M'_{kl} = B\Bigl(\sum_{i} p_{ik}\, b_i, \; \sum_{j} p_{jl}\, b_j\Bigr).$$
3. A [[bilinear form|0P799D6AMN]] is linear in the first slot and in the second slot, so the sums and the scalars come out of both slots:
$$M'_{kl} = \sum_{i=1}^n \sum_{j=1}^n p_{ik}\, B(b_i, b_j)\, p_{jl} = \sum_{i, j} p_{ik}\, M_{ij}\, p_{jl}.$$
4. By the definition of the [[transpose|0W809K6AW0]], $p_{ik}$ is the entry $(k, i)$ of $P^{\mathsf{T}}$. So the double sum is the entry $(k, l)$ of the product of $P^{\mathsf{T}}$, $M$ and $P$, by the definition of matrix multiplication:
$$M'_{kl} = \sum_{i, j} (P^{\mathsf{T}})_{ki}\, M_{ij}\, P_{jl} = (P^{\mathsf{T}} M P)_{kl}.$$
5. Step 4 holds for all $k$ and $l$, so $M' = P^{\mathsf{T}} M P$. This proves part 1.
6. The matrix $P$ is invertible, because it changes one basis into another, by the [[change of basis formula|0MQXVZEBMT]]. Then $P^{\mathsf{T}}$ is invertible too, with inverse $(P^{-1})^{\mathsf{T}}$, since $(P^{-1})^{\mathsf{T}} P^{\mathsf{T}} = (P P^{-1})^{\mathsf{T}} = I$.
7. By the [[rank of a product|02FDWY55AS]], multiplying by an invertible matrix on either side keeps the rank. So $\operatorname{rank}(P^{\mathsf{T}} M P) = \operatorname{rank}(M P) = \operatorname{rank} M$. This proves part 2.
8. By the [[multiplicativity of the determinant|04CPJ6AF00]] and the [[determinant of the transpose|0ZZQ2E1MTE]],
$$\det M' = \det(P^{\mathsf{T}}) \det M \det P = (\det P)^2 \det M.$$
9. Since $P$ is invertible by step 6, $\det P \neq 0$, so $(\det P)^2$ is a nonzero square in $F$. This proves part 3.

## Idea

Each new basis vector is a combination of the old ones, with its coefficients in one column of $P$.
Put two such combinations into the form and expand both slots: you get a double sum of old entries.
That double sum has the coefficients of the first vector on the left and those of the second on the right, and this is exactly the product $P^{\mathsf{T}} M P$.
Rank and determinant then follow from the general rules for products of matrices.

## Variants

A shorter proof uses coordinate vectors.
If $x'$ and $y'$ are the coordinates of $u$ and $v$ in $\mathcal{B}'$, then their coordinates in $\mathcal{B}$ are $Px'$ and $Py'$.
By the [[transpose of a product|09GK5PS824]],
$$B(u, v) = (Px')^{\mathsf{T}} M (Py') = x'^{\mathsf{T}} (P^{\mathsf{T}} M P)\, y'.$$
A form has only one matrix in a given basis, because the entries are its values on pairs of basis vectors, so $M' = P^{\mathsf{T}} M P$.
