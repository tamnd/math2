---
tag: KKEHEMTSYY
kind: proof
name: Proof of the general Laplace expansion by grouping the Leibniz terms
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: 541X51GQTV
methods: [0NTF6DMVAP]
uses: [016PE4VZ8Q, 0SD528P0EK, 0SK90238BH, 0JEJJCB0EX, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: Laplace expansion of a determinant by complementary minors
---

## Proof

Write $I = \set{i_1 < \dots < i_k}$ and $I^c = \set{i_{k+1} < \dots < i_n}$, and in the same way $J = \set{j_1 < \dots < j_k}$ and $J^c$.

1. Let $\pi_I$ be the [[permutation|05RWFKVTJ7]] with $\pi_I(r) = i_r$ for all $r$. Define $\pi_J$ from $J$ in the same way.
2. By the [[Leibniz formula|016PE4VZ8Q]], $\det A = \sum_{\tau \in S_n} \sgn(\tau) \prod_{r} a_{r \tau(r)}$.
3. Each $\tau$ maps $I$ onto a $k$-element set $\tau(I)$. Group the terms by $J = \tau(I)$, and fix $J$.
4. For $\tau$ with $\tau(I) = J$, put $\sigma = \pi_J^{-1} \tau \pi_I$. Then $\sigma$ maps $\set{1, \dots, k}$ onto itself, and so also $\set{k+1, \dots, n}$.
5. So $\sigma$ is the product of a permutation $\sigma_1$ of $\set{1, \dots, k}$ and a permutation $\sigma_2$ of $\set{k+1, \dots, n}$.
6. Conversely, each such pair gives $\tau = \pi_J \sigma \pi_I^{-1}$ with $\tau(I) = J$. So $\tau \mapsto (\sigma_1, \sigma_2)$ is a bijection.
7. Writing $\sigma_1$ and $\sigma_2$ as products of transpositions, the [[definition of the sign|0SK90238BH]] gives $\sgn(\sigma) = \sgn(\sigma_1) \sgn(\sigma_2)$.
8. Since the [[sign is a homomorphism|0JEJJCB0EX]], $\sgn(\tau) = \sgn(\pi_I) \sgn(\pi_J) \sgn(\sigma_1) \sgn(\sigma_2)$.
9. Reindex the product by $r = \pi_I(s)$. Then $\prod_r a_{r \tau(r)} = \prod_s a_{\pi_I(s), \pi_J(\sigma(s))}$.
10. The factors with $s \le k$ are the entries $(A_{I,J})_{s, \sigma_1(s)}$. The factors with $s > k$ are the entries of $A_{I^c, J^c}$ in the places given by $\sigma_2$.
11. Sum over all pairs $(\sigma_1, \sigma_2)$. By steps 8 to 10 and the Leibniz formula for both blocks, the terms with $\tau(I) = J$ add up to $\sgn(\pi_I) \sgn(\pi_J) \det A_{I,J} \det A_{I^c, J^c}$.
12. It remains to find $\sgn(\pi_I)$. Start from the list $(1, \dots, n)$ and move $i_1$ to place $1$ by $i_1 - 1$ swaps of neighbours.
13. Then move $i_2$ to place $2$ by $i_2 - 2$ such swaps, and so on up to $i_k$. The result is the list $(i_1, \dots, i_n)$ of $\pi_I$.
14. So $\pi_I$ is a product of $\sum_r (i_r - r) = \Sigma I - k(k+1)/2$ transpositions, and $\sgn(\pi_I) = (-1)^{\Sigma I - k(k+1)/2}$.
15. In the same way, $\sgn(\pi_J) = (-1)^{\Sigma J - k(k+1)/2}$. So $\sgn(\pi_I) \sgn(\pi_J) = (-1)^{\Sigma I + \Sigma J - k(k+1)} = (-1)^{\Sigma I + \Sigma J}$.
16. Summing step 11 over all $J$ and using step 15 gives the formula.
17. The column version follows by the same grouping, with $\tau^{-1}(J) = I$ for a fixed set $J$ of columns.

## Idea

Each term of the Leibniz formula sends the chosen rows $I$ to some set of columns $J$.
The terms with the same $J$ split into a term of the minor on $(I, J)$ times a term of the complementary minor.
The sign comes from moving the rows $I$ and the columns $J$ to the front.

## Variants

A proof by multilinearity expands the rows in $I$ into standard rows and uses the uniqueness of alternating forms on the remaining rows.
For $k = 1$ the proof is the [[proof of the Laplace expansion by the Leibniz formula|AF3XSRXE6T]].
