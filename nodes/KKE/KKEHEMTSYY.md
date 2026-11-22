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

We group the terms of the Leibniz formula by the set of columns that they use in the rows $I$, and we show that each group is one term of the expansion.
Write $I = \{i_1 < \dots < i_k\}$ and $I^c = \{i_{k+1} < \dots < i_n\}$, and in the same way $J = \{j_1 < \dots < j_k\}$ and $J^c = \{j_{k+1} < \dots < j_n\}$.

*Grouping the terms.*

1. Let $\pi_I$ be the [[permutation|05RWFKVTJ7]] with $\pi_I(r) = i_r$ for $1 \le r \le n$, and define $\pi_J$ from $J$ in the same way.
2. By the [[Leibniz formula|016PE4VZ8Q]],
$$\det A = \sum_{\tau \in S_n} \sgn(\tau) \prod_{r=1}^{n} a_{r, \tau(r)}.$$
3. Each $\tau$ maps $I$ onto a $k$-element set $\tau(I)$.
   We group the terms by $J = \tau(I)$, and from now on we fix $J$.

*Splitting each permutation.*

4. For $\tau$ with $\tau(I) = J$, put $\sigma = \pi_J^{-1} \tau \pi_I$.
   Then $\sigma$ maps $\{1, \dots, k\}$ onto itself, because $\pi_I$ maps it onto $I$, $\tau$ maps $I$ onto $J$ and $\pi_J^{-1}$ maps $J$ onto $\{1, \dots, k\}$.
   So $\sigma$ also maps $\{k+1, \dots, n\}$ onto itself.
5. So $\sigma$ is the product of a permutation $\sigma_1$ of $\{1, \dots, k\}$ and a permutation $\sigma_2$ of $\{k+1, \dots, n\}$.
6. Conversely, each such pair gives $\tau = \pi_J \sigma \pi_I^{-1}$ with $\tau(I) = J$.
   So $\tau \mapsto (\sigma_1, \sigma_2)$ is a bijection from the permutations with $\tau(I) = J$ onto the pairs.

*Signs and products.*

7. Write $\sigma_1$ and $\sigma_2$ as products of transpositions.
   Their product is a product of transpositions for $\sigma$, so the [[definition of the sign|0SK90238BH]] gives $\sgn(\sigma) = \sgn(\sigma_1) \sgn(\sigma_2)$.
8. Since the [[sign is a homomorphism|0JEJJCB0EX]] with values $\pm 1$,
$$\sgn(\tau) = \sgn(\pi_J) \sgn(\sigma) \sgn(\pi_I)^{-1} = \sgn(\pi_I) \sgn(\pi_J) \sgn(\sigma_1) \sgn(\sigma_2).$$
9. Reindex the product by $r = \pi_I(s)$:
$$\prod_{r=1}^{n} a_{r, \tau(r)} = \prod_{s=1}^{n} a_{\pi_I(s), \pi_J(\sigma(s))}.$$
10. For $s \le k$ the factor is $a_{i_s, j_{\sigma_1(s)}}$, the entry of $A_{I,J}$ in place $(s, \sigma_1(s))$.
    For $s > k$ the factor is the entry of $A_{I^c, J^c}$ in place $(s - k, \sigma_2(s) - k)$.
11. Sum over all pairs $(\sigma_1, \sigma_2)$.
    By steps 8 to 10 and the Leibniz formula for the two submatrices, the terms with $\tau(I) = J$ add up to
$$\sgn(\pi_I) \sgn(\pi_J) \det A_{I,J} \det A_{I^c, J^c}.$$

*The sign of $\pi_I$.*

12. In the list $(i_1, \dots, i_n)$ of values of $\pi_I$, an inversion is a pair of places where a larger number comes first.
    The element $i_r$ of $I$ comes before exactly $i_r - r$ smaller elements of $I^c$, and no other pair is inverted.
13. So $\pi_I$ has $\sum_{r=1}^{k} (i_r - r) = \Sigma I - k(k+1)/2$ inversions, and $\sgn(\pi_I) = (-1)^{\Sigma I - k(k+1)/2}$.
14. In the same way, $\sgn(\pi_J) = (-1)^{\Sigma J - k(k+1)/2}$.
    Since $k(k+1)$ is even,
$$\sgn(\pi_I) \sgn(\pi_J) = (-1)^{\Sigma I + \Sigma J - k(k+1)} = (-1)^{\Sigma I + \Sigma J}.$$

*Conclusion.*

15. Summing step 11 over all $k$-element sets $J$ and using step 14 gives
$$\det A = \sum_{J} (-1)^{\Sigma I + \Sigma J} \det A_{I,J} \det A_{I^c, J^c}.$$
16. The column version follows by the same grouping, with the sets $\tau^{-1}(J)$ for a fixed set $J$ of columns in place of the sets $\tau(I)$.

## Idea

Each term of the Leibniz formula sends the chosen rows $I$ to some set $J$ of columns.
The terms with the same $J$ split as a term of the minor on $(I, J)$ times a term of the complementary minor, and every such pair of terms occurs exactly once.
The only real work is the sign.
It comes from moving the rows $I$ and the columns $J$ to the front, and the two moves cost $(-1)^{\Sigma I - k(k+1)/2}$ and $(-1)^{\Sigma J - k(k+1)/2}$.

## Variants

A proof by multilinearity expands each row in $I$ as a combination of standard rows, as in the [[proof of the ordinary expansion by multilinearity|97HQ4MPNBS]], and then uses the uniqueness of alternating forms on the remaining rows.
For $k = 1$ the present proof is the [[proof of the Laplace expansion by the Leibniz formula|AF3XSRXE6T]].
