---
tag: X7GPHANKB6
kind: proof
name: Proof of the Cauchy–Binet formula by multilinearity
msc: [15A15]
proves: 08WE2W7DYS
uses: [0C3CFHDN6R, 076JGP6R3T, 0PPG793642, 0K4VQB7HWR, 09YB3WQG38, 016PE4VZ8Q, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Binet_formula
    locator: Proof
---

## Proof

We expand the rows of $AB$ by multilinearity and sort the terms by the set of rows of $B$ that they use.

1. Let $A = (a_{ik})$ be $m \times n$ and $B$ be $n \times m$ over $K$, with $1 \le m \le n$. Here $m \ge 1$, since the [[determinant|0C3CFHDN6R]] is defined for sizes at least $1$. Let $\beta_1, \dots, \beta_n$ be the rows of $B$.
2. By the definition of the [[matrix product|076JGP6R3T]], row $i$ of the $m \times m$ matrix $AB$ is $\sum_{k=1}^{n} a_{ik} \beta_k$.
3. For a map $f \colon \set{1, \dots, m} \to \set{1, \dots, n}$, let $B_f$ be the $m \times m$ matrix whose row $i$ is $\beta_{f(i)}$.
4. Apply [[multilinearity in the rows|0PPG793642]] to the sums of step 2, in each of the rows $1, \dots, m$ in turn.
5. This gives $\det(AB) = \sum_{f} \left(\prod_{i=1}^{m} a_{i, f(i)}\right) \det B_f$, over all maps $f$ of step 3.
6. If $f$ is not injective, then $B_f$ has two equal rows. So $\det B_f = 0$ by the rule for [[two equal rows|0K4VQB7HWR]].
7. Let $f$ be injective, and let $S = f(\set{1, \dots, m})$. Then $S$ has $m$ elements. Write $S = \set{s_1 < s_2 < \cdots < s_m}$.
8. There is exactly one [[permutation|05RWFKVTJ7]] $\sigma \in S_m$ with $f(i) = s_{\sigma(i)}$ for all $i$. Conversely, each pair $(S, \sigma)$ defines an injective $f$ in this way.
9. So the injective maps $f$ correspond one to one to the pairs $(S, \sigma)$, where $S$ has $m$ elements and $\sigma \in S_m$.
10. Row $r$ of $B^S$ is $\beta_{s_r}$. So row $i$ of $B_f$ is row $\sigma(i)$ of $B^S$.
11. By the rule for [[permuting rows|09YB3WQG38]], $\det B_f = \sgn(\sigma) \det B^S$.
12. Column $r$ of $A_S$ is column $s_r$ of $A$. So $a_{i, f(i)} = a_{i, s_{\sigma(i)}} = (A_S)_{i, \sigma(i)}$.
13. By steps 5 to 12, $\det(AB) = \sum_{S} \left(\sum_{\sigma \in S_m} \sgn(\sigma) \prod_{i=1}^{m} (A_S)_{i, \sigma(i)}\right) \det B^S$.
14. By the [[Leibniz formula|016PE4VZ8Q]], the inner sum is $\det A_S$. So $\det(AB) = \sum_{S} \det(A_S) \det(B^S)$, over the subsets $S$ with $m$ elements.

## Idea

Each row of $AB$ is a combination of the rows of $B$. Expanding by multilinearity leaves only choices of $m$ distinct rows of $B$. For a fixed set $S$ of rows, the orderings of $S$ give $\det B^S$ times the Leibniz formula for $\det A_S$.
