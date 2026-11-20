---
tag: 86J5B0YFNK
kind: proof
name: Proof of multiplicativity by uniqueness of alternating forms
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 04CPJ6AF00
methods: [GQHHNV79PA]
uses: [076JGP6R3T, 0C3CFHDN6R, ~1e90e396, 06DW9BAWB1]
sources:
  - url: https://proofwiki.org/wiki/Determinant_of_Matrix_Product
    locator: Proof 4
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

Fix $B$, and let $\beta_1, \dots, \beta_n$ be its rows.
For an $n \times n$ matrix $X$, put $D(X) = \det(XB)$.

1. By the definition of the [[matrix product|076JGP6R3T]], row $i$ of $XB$ is $\sum_{k} x_{ik} \beta_k$. So row $i$ of $XB$ depends only on row $i$ of $X$, and linearly.
2. By property 1 of the [[definition of the determinant|0C3CFHDN6R]], $\det$ is linear in row $i$ of $XB$. With step 1, $D$ is linear in row $i$ of $X$.
3. So $D$ is multilinear in the rows of $X$.
4. If rows $i \neq k$ of $X$ are equal, then rows $i$ and $k$ of $XB$ are equal, by step 1.
5. By property 2 of the definition, $D(X) = \det(XB) = 0$ in that case. So $D$ is alternating.
6. By part 2 of the [[existence and uniqueness theorem|~1e90e396]], $D(X) = D(I_n) \det X$ for every $X$.
7. For the [[identity matrix|06DW9BAWB1]], $D(I_n) = \det(I_n B) = \det B$.
8. With $X = A$, steps 6 and 7 give $\det(AB) = \det B \det A = \det A \det B$.

## Idea

With $B$ fixed, the map $X \mapsto \det(XB)$ is again alternating and multilinear in the rows of $X$.
Such a map is a multiple of $\det$, and the multiple is its value at $I_n$, which is $\det B$.

## Variants

The same argument made explicit: expand each row $\sum_k a_{ik} \beta_k$ of $AB$ by multilinearity.
Terms with a repeated $\beta_k$ vanish, and the rest are row permutations of $B$ with determinant $\sgn(\sigma) \det B$.
The coefficients add up to the [[Leibniz formula|016PE4VZ8Q]] for $\det A$.
A second proof, by elementary matrices over a field, is the [[proof by row reduction|~33453c01]].
