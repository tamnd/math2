---
tag: 86J5B0YFNK
kind: proof
name: Proof of multiplicativity by uniqueness of alternating forms
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 04CPJ6AF00
methods: [GQHHNV79PA]
uses: [076JGP6R3T, 0C3CFHDN6R, 1C8RRWHD45, 06DW9BAWB1]
sources:
  - url: https://proofwiki.org/wiki/Determinant_of_Matrix_Product
    locator: Proof 4
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

We fix $B$, show that $X \mapsto \det(XB)$ is multilinear and alternating in the rows of $X$, and then use the uniqueness of such functions up to a factor.
Let $\beta_1, \dots, \beta_n$ be the rows of $B$, and for an $n \times n$ matrix $X$ over $K$ put $D(X) = \det(XB)$.

1. By the definition of the [[matrix product|076JGP6R3T]], row $i$ of $XB$ is
$$\sum_{k=1}^{n} x_{ik} \beta_k.$$
   So row $i$ of $XB$ depends only on row $i$ of $X$, and it depends on it linearly.
2. By property 1 of the [[definition of the determinant|0C3CFHDN6R]], $\det$ is linear in row $i$ of $XB$ when the other rows are fixed.
   Combined with step 1, $D$ is linear in row $i$ of $X$ when the other rows of $X$ are fixed.
3. Step 2 holds for each $i$, so $D$ is multilinear in the rows of $X$.
4. Suppose that rows $i$ and $k$ of $X$ are equal, with $i \ne k$.
   By step 1, rows $i$ and $k$ of $XB$ are then equal too.
5. By property 2 of the definition, $D(X) = \det(XB) = 0$ in that case.
   So $D$ is alternating.
6. By part 2 of the [[existence and uniqueness theorem|1C8RRWHD45]], a multilinear alternating function of the rows satisfies $D(X) = D(I_n) \det X$ for every $X$.
7. For the [[identity matrix|06DW9BAWB1]], $D(I_n) = \det(I_n B) = \det B$.
8. Take $X = A$ in step 6 and use step 7:
$$\det(AB) = D(A) = \det B \cdot \det A = \det A \cdot \det B,$$
   where the last equality uses that $K$ is commutative.

## Idea

With $B$ fixed, the map $X \mapsto \det(XB)$ obeys the first two rules of the determinant, because each row of $XB$ is a linear function of the matching row of $X$.
A function that obeys those two rules is a multiple of $\det$, and the multiple is its value at $I_n$.
That value is $\det B$, so $\det(XB) = \det B \det X$.

## Variants

The same argument can be made explicit.
Expand each row $\sum_k a_{ik} \beta_k$ of $AB$ by multilinearity.
The terms with a repeated $\beta_k$ vanish, and the others are $B$ with its rows permuted by some $\sigma$, with determinant $\operatorname{sgn}(\sigma) \det B$.
The coefficients of these terms add up to the [[Leibniz formula|016PE4VZ8Q]] for $\det A$.

A second proof, by elementary matrices over a field, is the [[proof by row reduction|3WPWGE036Q]].
