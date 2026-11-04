---
tag: 86J5B0YFNK
kind: proof
name: Proof that the determinant is multiplicative by expanding the rows
msc: [15A15]
proves: 04CPJ6AF00
uses: [076JGP6R3T, 0PPG793642, 0K4VQB7HWR, 09YB3WQG38, 016PE4VZ8Q, 05RWFKVTJ7]
sources:
  - url: https://proofwiki.org/wiki/Determinant_of_Matrix_Product
    locator: Proof 4
---

## Proof

We expand the rows of $AB$ by multilinearity, as in the proof of the Leibniz formula.

1. Let $A = (a_{ij})$ and let $\beta_1, \dots, \beta_n$ be the rows of $B = (b_{kj})$.
2. By the definition of the [[matrix product|076JGP6R3T]], $(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$. So row $i$ of $AB$ is $\sum_{k=1}^{n} a_{ik} \beta_k$.
3. For a map $f \colon \set{1, \dots, n} \to \set{1, \dots, n}$, let $B_f$ be the matrix whose row $i$ is $\beta_{f(i)}$.
4. Apply [[multilinearity|0PPG793642]] in each of the rows $1, \dots, n$ in turn to the sums of step 2.
5. This gives $\det(AB) = \sum_{f} \left(\prod_{i=1}^{n} a_{i, f(i)}\right) \det B_f$, over all maps $f$ of step 3.
6. If $f$ is not injective, then $B_f$ has two equal rows. So $\det B_f = 0$ by the rule for [[two equal rows|0K4VQB7HWR]].
7. The injective maps $f$ are bijections, so they are the [[permutations|05RWFKVTJ7]] $\sigma \in S_n$.
8. For $\sigma \in S_n$, row $i$ of $B_\sigma$ is row $\sigma(i)$ of $B$. By the rule for [[permuting rows|09YB3WQG38]], $\det B_\sigma = \sgn(\sigma) \det B$.
9. By steps 5 to 8, $\det(AB) = \left(\sum_{\sigma \in S_n} \sgn(\sigma) \prod_{i=1}^{n} a_{i, \sigma(i)}\right) \det B$.
10. By the [[Leibniz formula|016PE4VZ8Q]], the sum in step 9 is $\det A$. So $\det(AB) = \det A \cdot \det B$.

## Idea

Each row of $AB$ is a combination of the rows of $B$ with coefficients from $A$. Expanding by multilinearity leaves only the row permutations of $B$, each with determinant $\pm \det B$. The coefficients that remain add up to the Leibniz formula for $\det A$.
