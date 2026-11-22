---
tag: PPBYQY70BR
kind: proof
name: Proof that the Gram determinant is the squared volume
msc: ["15A63", "15A15"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: FWA0AKJA2R
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [A1Y41YZFB6, 0WXBGBTA3D, 0VGSYBWHV2, 0HX8HZ1WTQ, 0K1KKMFHYH, 04CPJ6AF00, 0ZZQ2E1MTE, EM1QNRGWQ8, ACDFDABVQK]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Gram determinant
---

## Proof

We write the vectors in terms of their Gram-Schmidt outputs with a triangular matrix, factor $G$ through the diagonal Gram matrix of the outputs, and take determinants.
Let $V$, $v_1, \dots, v_k$ and $G$ be as in the statement, with the inner product linear in the first slot.

1. Part 1. Let the $v_j$ be independent. The [[Gram-Schmidt process|A1Y41YZFB6]] gives $u_j = v_j - \sum_{i < j} m_{ij} u_i$ with $m_{ij} = \ip{v_j}{u_i} / \ip{u_i}{u_i}$.
2. So $v_j = \sum_{i=1}^k M_{ij} u_i$, where $M$ is the $k \times k$ matrix with $M_{jj} = 1$, $M_{ij} = m_{ij}$ for $i < j$, and $M_{ij} = 0$ for $i > j$.
3. By the [[Gram-Schmidt theorem|0WXBGBTA3D]], the $u_i$ are nonzero and pairwise orthogonal.
4. So the Gram matrix of $u_1, \dots, u_k$ is the diagonal matrix $D$ with the entries $\norm{u_1}^2, \dots, \norm{u_k}^2$.
5. By step 2, linearity in the first slot and conjugate-linearity in the second slot of the [[inner product|0VGSYBWHV2]], $G_{ij} = \sum_p \sum_q M_{pi}\, \overline{M_{qj}}\, \ip{u_p}{u_q}$.
6. By step 4 only the terms with $p = q$ remain, so $G_{ij} = \sum_p M_{pi}\, D_{pp}\, \overline{M_{pj}}$. This is the $(i, j)$ entry of $M^{\mathsf{T}} D \overline{M}$, so $G = M^{\mathsf{T}} D \overline{M}$.
7. The matrix $M^{\mathsf{T}}$ is lower triangular and $\overline{M}$ is upper triangular, and both have all diagonal entries equal to $1$.
8. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det M^{\mathsf{T}} = \det \overline{M} = 1$ and $\det D = \prod_j \norm{u_j}^2$.
9. [[Multiplicativity of the determinant|04CPJ6AF00]] gives $\det G = 1 \cdot \det D \cdot 1 = \prod_j \norm{u_j}^2$.
10. Each $u_j$ is nonzero by step 3, so each factor is positive, and $\det G > 0$.
11. Part 2. Let the $v_j$ be dependent. By part 4 of the [[Gram invertibility theorem|EM1QNRGWQ8]], $G$ is not invertible.
12. A square matrix that is not invertible has determinant $0$, by the [[invertible matrix theorem|ACDFDABVQK]]. So $\det G = 0$.
13. Steps 10 and 12 give $\det G \ge 0$ in both cases, with $\det G = 0$ exactly for dependent families.
14. Part 3. For an independent family, step 9 gives $\det G = (\norm{u_1} \cdots \norm{u_k})^2 = \operatorname{vol}(v_1, \dots, v_k)^2$. For a dependent family, step 12 gives $\det G = 0 = \operatorname{vol}(v_1, \dots, v_k)^2$.
15. Part 4. For the standard inner product, $G_{ij} = \sum_l A_{li}\, \overline{A_{lj}}$, which is the $(i, j)$ entry of $A^{\mathsf{T}} \overline{A}$. So $G = A^{\mathsf{T}} \overline{A}$.
16. The determinant is a sum of products of entries with integer coefficients, and conjugation preserves sums and products. So $\det \overline{A} = \overline{\det A}$.
17. By multiplicativity and the [[determinant of the transpose|0ZZQ2E1MTE]], $\det G = \det A \cdot \overline{\det A} = \abs{\det A}^2$.
18. By part 3, $\operatorname{vol}^2 = \abs{\det A}^2$. Both $\operatorname{vol}$ and $\abs{\det A}$ are $\ge 0$, so $\operatorname{vol} = \abs{\det A}$.

This proves parts 1 to 4.

## Idea

The Gram-Schmidt process says that each $v_j$ is $u_j$ plus a combination of the earlier $u_i$, and that is a triangular change of basis with ones on the diagonal.
Such a change does not alter determinants, so $\det G$ equals the determinant of the Gram matrix of the $u_i$.
That Gram matrix is diagonal, because the $u_i$ are orthogonal, and its determinant is the product of the squared lengths: base times height, repeated.

## Variants

The same factorization can be done with row and column operations on $G$ itself.
Subtract a multiple of an earlier row from a later row, and the conjugate multiple of the matching column from the matching column; each such pair keeps $\det G$ and keeps $G$ Hermitian.
These operations are Gaussian elimination on $G$, and they end at the diagonal matrix $D$.

For column vectors with $k = n$, the [[QR decomposition|0ERWG4NXQ9]] $A = Q R$ with $Q$ unitary gives $A^* A = R^* R$, so $\det G = \abs{\det A}^2 = \abs{\det R}^2$, the product of the squared diagonal entries of $R$.
Those diagonal entries are the lengths $\norm{u_j}$, so this is the same proof in matrix form.
