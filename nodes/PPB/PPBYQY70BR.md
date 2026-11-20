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

Let $V$, $v_1, \dots, v_k$ and $G$ be as in the statement.

1. Part 1. Let the $v_j$ be independent. By the [[Gram-Schmidt process|A1Y41YZFB6]], $u_j = v_j - \sum_{i<j} m_{ij} u_i$ with $m_{ij} = \ip{v_j}{u_i} / \ip{u_i}{u_i}$.
2. So $v_j = \sum_{i=1}^k M_{ij} u_i$, where $M_{jj} = 1$, $M_{ij} = m_{ij}$ for $i < j$, and $M_{ij} = 0$ for $i > j$.
3. By part 1 of the [[Gram-Schmidt theorem|0WXBGBTA3D]], the $u_i$ are nonzero and pairwise orthogonal.
4. So the Gram matrix of $u_1, \dots, u_k$ is the diagonal matrix $D$ with the entries $\norm{u_1}^2, \dots, \norm{u_k}^2$.
5. By step 2 and sesquilinearity of the [[inner product|0VGSYBWHV2]], $G_{ij} = \sum_p \sum_q M_{pi}\, \overline{M_{qj}}\, \ip{u_p}{u_q}$.
6. By step 4, this is $\sum_p M_{pi}\, D_{pp}\, \overline{M_{pj}}$, the $(i, j)$ entry of $M^T D \overline{M}$. So $G = M^T D \overline{M}$.
7. $M^T$ is lower triangular and $\overline{M}$ is upper triangular, both with diagonal entries $1$.
8. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det M^T = \det \overline{M} = 1$, and $\det D = \prod_j \norm{u_j}^2$.
9. [[Multiplicativity of the determinant|04CPJ6AF00]] gives $\det G = 1 \cdot \det D \cdot 1 = \prod_j \norm{u_j}^2$.
10. Each $u_j$ is nonzero by step 3, so each factor is positive, and $\det G > 0$.
11. Part 2. Let the $v_j$ be dependent. By part 4 of the [[Gram invertibility theorem|EM1QNRGWQ8]], $G$ is not invertible.
12. So $\det G = 0$, by the [[invertible matrix theorem|ACDFDABVQK]], conditions 1 and 21.
13. Steps 10 and 12 give $\det G \geq 0$ in both cases, and $\det G = 0$ exactly for dependent families.
14. Part 3. For an independent family, step 9 gives $\det G = (\norm{u_1} \cdots \norm{u_k})^2 = \operatorname{vol}^2$.
15. For a dependent family, step 12 gives $\det G = 0 = \operatorname{vol}^2$.
16. Part 4. The entry $G_{ij} = \sum_l A_{li}\, \overline{A_{lj}}$ is the $(i, j)$ entry of $A^T \overline{A}$. So $G = A^T \overline{A}$.
17. The determinant is a sum of products of entries with integer coefficients. Conjugation preserves sums and products, so $\det \overline{A} = \overline{\det A}$.
18. By multiplicativity and the [[determinant of the transpose|0ZZQ2E1MTE]], $\det G = \det A \cdot \overline{\det A} = |\det A|^2$.
19. By part 3, $\operatorname{vol}^2 = |\det A|^2$. Both numbers are $\geq 0$, so $\operatorname{vol} = |\det A|$.

## Idea

The Gram-Schmidt process writes the $v_j$ in terms of the orthogonal $u_i$ with a unitriangular matrix $M$.
Then $G = M^T D \overline{M}$, with $D$ the diagonal Gram matrix of the $u_i$.
Unitriangular matrices have determinant $1$, so $\det G = \det D$.

## Variants

- Row operations: subtract multiples of earlier rows and the matching columns from $G$. These operations do not change $\det G$, and they produce $D$.
- For column vectors, $G = A^T \overline{A}$ and the QR factorization $A = QR$ give $\det G = |\det R|^2$ when $k = n$.
