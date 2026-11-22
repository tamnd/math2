---
tag: X7GPHANKB6
kind: proof
name: Proof of the Cauchy-Binet formula by multilinearity
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: 08WE2W7DYS
methods: [0NTF6DMVAP]
uses: [0C3CFHDN6R, 076JGP6R3T, 0PPG793642, 0K4VQB7HWR, 09YB3WQG38, 016PE4VZ8Q, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Binet_formula
    locator: Proof
---

## Proof

We expand each row of $AB$ by multilinearity and sort the surviving terms by the set of rows of $B$ that they use.

1. Let $A = (a_{ik})$ be an $m \times n$ matrix and $B$ an $n \times m$ matrix over the commutative ring $K$, with $m, n \ge 1$.
   Let $\beta_1, \dots, \beta_n$ be the rows of $B$.
2. By the definition of the [[matrix product|076JGP6R3T]], row $i$ of the $m \times m$ matrix $AB$ is $\sum_{k=1}^{n} a_{ik} \beta_k$.
3. For a map $f \colon \{1, \dots, m\} \to \{1, \dots, n\}$, let $B_f$ be the $m \times m$ matrix whose row $i$ is $\beta_{f(i)}$.
4. The [[determinant|0C3CFHDN6R]] is [[linear in each row|0PPG793642]].
   Expand row $1$ of $AB$ by step 2, then row $2$ in each of the resulting terms, and so on up to row $m$.
   Each term of the result picks one index $f(i)$ for each row $i$, so
$$\det(AB) = \sum_{f} \Bigl(\prod_{i=1}^{m} a_{i, f(i)}\Bigr) \det B_f,$$
   where $f$ runs over all maps of step 3.
5. If $f$ is not injective, then $B_f$ has two equal rows, so $\det B_f = 0$ by the rule for [[two equal rows|0K4VQB7HWR]].
   So only injective maps $f$ contribute to the sum in step 4.
6. If $m > n$, then no map $f$ is injective, so $\det(AB) = 0$.
   This proves part 2, and from now on we let $m \le n$.
7. Let $f$ be injective, and let $S = f(\{1, \dots, m\})$.
   Then $S$ has $m$ elements, and we write $S = \{s_1, \dots, s_m\}$ with $s_1 < s_2 < \dots < s_m$.
8. There is exactly one [[permutation|05RWFKVTJ7]] $\sigma \in S_m$ with $f(i) = s_{\sigma(i)}$ for all $i$.
   Conversely, every pair $(S, \sigma)$ of a set $S$ with $m$ elements and a permutation $\sigma \in S_m$ defines an injective $f$ in this way.
   So the injective maps $f$ correspond one to one to these pairs.
9. Row $r$ of $B^S$ is $\beta_{s_r}$, so row $i$ of $B_f$ is row $\sigma(i)$ of $B^S$.
   By the rule for [[permuting rows|09YB3WQG38]], $\det B_f = \operatorname{sgn}(\sigma) \det B^S$.
10. Column $r$ of $A_S$ is column $s_r$ of $A$, so
$$a_{i, f(i)} = a_{i, s_{\sigma(i)}} = (A_S)_{i, \sigma(i)}.$$
11. Steps 4, 5, 8, 9 and 10 give
$$\det(AB) = \sum_{S} \Bigl(\sum_{\sigma \in S_m} \operatorname{sgn}(\sigma) \prod_{i=1}^{m} (A_S)_{i, \sigma(i)}\Bigr) \det B^S,$$
   where $S$ runs over the subsets of $\{1, \dots, n\}$ with $m$ elements.
12. By the [[Leibniz formula|016PE4VZ8Q]], the inner sum is $\det A_S$.
   So $\det(AB) = \sum_{S} \det(A_S) \det(B^S)$, which proves part 1.

## Idea

Each row of $AB$ is a combination of the rows of $B$, with coefficients from the matching row of $A$.
Expanding the determinant by multilinearity gives one term for each way of choosing a row of $B$ for each row of $AB$.
Choices that repeat a row of $B$ give $0$, so only choices of $m$ distinct rows survive.
For a fixed set $S$ of rows, the different orders of $S$ produce the signs, and they assemble into $\det B^S$ times the Leibniz formula for $\det A_S$.

For $m = 2$ and $n = 3$, the nine maps $f$ give three with repeated rows, which vanish, and six injective ones.
These six come in pairs, one pair for each of the sets $\{1, 2\}$, $\{1, 3\}$ and $\{2, 3\}$.
For $S = \{1, 2\}$, the pair is $f = (1, 2)$ and $f = (2, 1)$, with the two terms
$$a_{11} a_{22} \det \begin{pmatrix} \beta_1 \\ \beta_2 \end{pmatrix} + a_{12} a_{21} \det \begin{pmatrix} \beta_2 \\ \beta_1 \end{pmatrix} = (a_{11} a_{22} - a_{12} a_{21}) \det B^{\{1,2\}} = \det A_{\{1,2\}} \det B^{\{1,2\}}.$$

## Variants

A second proof fixes $B$ and views $\det(AB)$ as a function of the rows of $A$.
This function is multilinear and alternating, and so is each maximal minor $A \mapsto \det A_S$.
The minors form a basis of the alternating multilinear functions of $m$ vectors in $K^n$, so $\det(AB)$ is a combination $\sum_S c_S \det A_S$.
Taking for the rows of $A$ the unit vectors $e_{s_1}, \dots, e_{s_m}$ makes $AB = B^S$ and $\det A_T = 0$ for $T \ne S$, which gives $c_S = \det B^S$.
For $m = n$ the same argument is a standard proof of the [[multiplicativity of the determinant|04CPJ6AF00]].
