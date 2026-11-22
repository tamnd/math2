---
tag: AF3XSRXE6T
kind: proof
name: Proof of the Laplace expansion along a row by the Leibniz formula
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 0C08BQ3M05
methods: [0NTF6DMVAP]
uses: [016PE4VZ8Q, 0W2QAVJQ1W, 0SD528P0EK, 05RWFKVTJ7, 0V0E04DWX2, 0JEJJCB0EX, 0SK90238BH]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: Proof
---

## Proof

We sort the terms of the Leibniz formula by the column that each term uses in row $i$, and we show that the terms for column $j$ add up to $a_{ij} C_{ij}$.

*Sorting the terms.*

1. Let $A = (a_{kl})$ be an $n \times n$ matrix over a commutative ring $K$ with $n \ge 2$, and fix a row $i$.
2. By the [[Leibniz formula|016PE4VZ8Q]],
$$\det A = \sum_{\tau \in S_n} \sgn(\tau) \prod_{k=1}^{n} a_{k, \tau(k)},$$
   where $S_n$ is the set of [[permutations|05RWFKVTJ7]] of $\{1, \dots, n\}$.
3. Each $\tau$ takes exactly one value $\tau(i)$ at $i$.
   We group the terms by $j = \tau(i)$ and take out the common factor $a_{ij}$:
$$\det A = \sum_{j=1}^{n} a_{ij} T_j, \qquad T_j = \sum_{\tau \in S_n,\ \tau(i) = j} \sgn(\tau) \prod_{k \ne i} a_{k, \tau(k)}.$$
4. By the definition of the [[cofactor|0W2QAVJQ1W]], it is enough to show that $T_j = (-1)^{i+j} M_{ij}$ for each $j$.
   From now on we fix $j$.

*Matching the terms with those of the minor.*

5. Let $\alpha \colon \{1, \dots, n-1\} \to \{1, \dots, n\} \setminus \{i\}$ be the increasing bijection.
   So $\alpha(r) = r$ for $r < i$ and $\alpha(r) = r + 1$ for $r \ge i$.
6. Let $\beta \colon \{1, \dots, n-1\} \to \{1, \dots, n\} \setminus \{j\}$ be the increasing bijection, defined in the same way with $j$ in place of $i$.
7. Let $A_{ij}$ be $A$ with row $i$ and column $j$ deleted.
   Its entry in position $(r, s)$ is $a_{\alpha(r), \beta(s)}$, and $M_{ij} = \det A_{ij}$ by the definition of the [[minor|0SD528P0EK]].
8. Let $\tau \in S_n$ with $\tau(i) = j$.
   Then $\tau$ maps $\{1, \dots, n\} \setminus \{i\}$ bijectively onto $\{1, \dots, n\} \setminus \{j\}$, so $\sigma = \beta^{-1} \circ \tau \circ \alpha$ is a permutation of $\{1, \dots, n-1\}$.
9. Conversely, each $\sigma \in S_{n-1}$ comes from exactly one such $\tau$, namely the one with $\tau(i) = j$ and $\tau(\alpha(r)) = \beta(\sigma(r))$ for $1 \le r \le n-1$.
   So $\tau \mapsto \sigma$ is a bijection from $\{\tau \in S_n : \tau(i) = j\}$ onto $S_{n-1}$.
10. The indices $k \ne i$ are exactly the values $\alpha(r)$, so the products match:
$$\prod_{k \ne i} a_{k, \tau(k)} = \prod_{r=1}^{n-1} a_{\alpha(r), \beta(\sigma(r))} = \prod_{r=1}^{n-1} (A_{ij})_{r, \sigma(r)},$$
    where the second equality is step 7.

*Comparing the signs.*

11. Extend $\alpha$ to $\hat\alpha \in S_n$ by $\hat\alpha(n) = i$.
    It sends $i \mapsto i+1 \mapsto \dots \mapsto n \mapsto i$ and fixes the other points, so it is a cycle of length $n - i + 1$.
    By the [[sign of a cycle|0V0E04DWX2]], $\sgn(\hat\alpha) = (-1)^{n-i}$.
12. In the same way, extend $\beta$ to $\hat\beta \in S_n$ by $\hat\beta(n) = j$, so that $\sgn(\hat\beta) = (-1)^{n-j}$.
13. Let $\hat\sigma = \hat\beta^{-1} \circ \tau \circ \hat\alpha$.
    Then $\hat\sigma(n) = \hat\beta^{-1}(\tau(i)) = \hat\beta^{-1}(j) = n$.
    For $r \le n-1$ we have $\tau(\alpha(r)) \ne j$, so $\hat\sigma(r) = \beta^{-1}(\tau(\alpha(r))) = \sigma(r)$.
14. So $\hat\sigma$ fixes $n$ and agrees with $\sigma$ on $\{1, \dots, n-1\}$.
    A product of $m$ transpositions of $\{1, \dots, n-1\}$ that gives $\sigma$ also gives $\hat\sigma$ when read in $S_n$.
    By the definition of the [[sign|0SK90238BH]], $\sgn(\hat\sigma) = (-1)^m = \sgn(\sigma)$.
15. Since $\tau = \hat\beta \circ \hat\sigma \circ \hat\alpha^{-1}$ and the [[sign is a homomorphism|0JEJJCB0EX]], steps 11, 12 and 14 give
$$\sgn(\tau) = \sgn(\hat\beta) \sgn(\sigma) \sgn(\hat\alpha)^{-1} = (-1)^{n-j} (-1)^{n-i} \sgn(\sigma) = (-1)^{i+j} \sgn(\sigma).$$

*Conclusion.*

16. By steps 9, 10 and 15,
$$T_j = (-1)^{i+j} \sum_{\sigma \in S_{n-1}} \sgn(\sigma) \prod_{r=1}^{n-1} (A_{ij})_{r, \sigma(r)}.$$
17. The sum is the Leibniz formula for the $(n-1) \times (n-1)$ matrix $A_{ij}$, so it equals $M_{ij}$.
    Hence $T_j = (-1)^{i+j} M_{ij} = C_{ij}$.
18. By step 3, $\det A = \sum_{j=1}^{n} a_{ij} C_{ij} = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$, which is the Laplace expansion along row $i$.

## Idea

Every term of the Leibniz formula takes exactly one entry from row $i$.
So the terms fall into $n$ groups, one for each entry $a_{ij}$ of that row.
After renumbering, the terms in the group of $a_{ij}$ are exactly the terms of the Leibniz formula for the minor $M_{ij}$.
The renumbering moves row $i$ and column $j$ to the last place, and the two cycles that do this cost the sign $(-1)^{n-i} (-1)^{n-j} = (-1)^{i+j}$.

## Variants

A second proof avoids the count of signs.
It uses linearity in row $i$, row operations and the uniqueness of alternating forms, as in the [[proof by multilinearity|97HQ4MPNBS]].
Grouping the Leibniz terms by the images of $k$ rows at once, in place of one row, gives the [[general Laplace expansion|KKEHEMTSYY]] by the same method.
