---
tag: AF3XSRXE6T
kind: proof
name: Proof of the Laplace expansion along a row by the Leibniz formula
msc: [15A15]
proves: 0C08BQ3M05
uses: [016PE4VZ8Q, 0W2QAVJQ1W, 0SD528P0EK, 05RWFKVTJ7, 0V0E04DWX2, 0JEJJCB0EX, 0SK90238BH]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: Proof
---

## Proof

We group the terms of the Leibniz formula by the column of the factor taken from row $i$.

1. Let $A = (a_{kl})$ be an $n \times n$ matrix over $K$ with $n \ge 2$, and fix a row $i$.
2. By the [[Leibniz formula|016PE4VZ8Q]], $\det A = \sum_{\tau \in S_n} \sgn(\tau) \prod_{k=1}^{n} a_{k, \tau(k)}$, where $S_n$ is the set of [[permutations|05RWFKVTJ7]] of $\set{1, \dots, n}$.
3. Each $\tau \in S_n$ has exactly one value $\tau(i)$. Sort the terms by $j = \tau(i)$ and take out the factor $a_{ij}$.
4. This gives $\det A = \sum_{j=1}^{n} a_{ij} T_j$, where $T_j = \sum_{\tau \in S_n,\ \tau(i) = j} \sgn(\tau) \prod_{k \ne i} a_{k, \tau(k)}$.
5. By the definition of the [[cofactor|0W2QAVJQ1W]], it is enough to show $T_j = (-1)^{i+j} M_{ij}$ for each $j$. Fix $j$.
6. Let $\alpha \colon \set{1, \dots, n-1} \to \set{1, \dots, n} \setminus \set{i}$ be the increasing bijection. So $\alpha(r) = r$ for $r < i$ and $\alpha(r) = r + 1$ for $r \ge i$.
7. Let $\beta \colon \set{1, \dots, n-1} \to \set{1, \dots, n} \setminus \set{j}$ be the increasing bijection in the same way.
8. Let $A_{ij}$ be $A$ with row $i$ and column $j$ deleted. Its entry in position $(r, s)$ is $a_{\alpha(r), \beta(s)}$. By the definition of the [[minor|0SD528P0EK]], $M_{ij} = \det A_{ij}$.
9. Let $\tau \in S_n$ with $\tau(i) = j$. Then $\tau$ maps $\set{1, \dots, n} \setminus \set{i}$ bijectively onto $\set{1, \dots, n} \setminus \set{j}$.
10. So $\sigma = \beta^{-1} \circ \tau \circ \alpha$ is a permutation of $\set{1, \dots, n-1}$.
11. Conversely, each $\sigma \in S_{n-1}$ comes from exactly one such $\tau$. It is given by $\tau(i) = j$ and $\tau(\alpha(r)) = \beta(\sigma(r))$ for $1 \le r \le n-1$.
12. So $\tau \mapsto \sigma$ is a bijection from $\set{\tau \in S_n : \tau(i) = j}$ onto $S_{n-1}$.
13. For such $\tau$ and $\sigma$, the indices $k \ne i$ are exactly the values $\alpha(r)$. So $\prod_{k \ne i} a_{k, \tau(k)} = \prod_{r=1}^{n-1} a_{\alpha(r), \beta(\sigma(r))}$.
14. By step 8, this is $\prod_{r=1}^{n-1} (A_{ij})_{r, \sigma(r)}$.
15. Now we compare signs. Extend $\alpha$ to $\hat\alpha \in S_n$ by $\hat\alpha(n) = i$. It sends $i \mapsto i+1 \mapsto \cdots \mapsto n \mapsto i$ and fixes the other points.
16. So $\hat\alpha$ is a cycle of length $n - i + 1$. By the [[sign of a cycle|0V0E04DWX2]], $\sgn(\hat\alpha) = (-1)^{n-i}$.
17. In the same way, extend $\beta$ to $\hat\beta \in S_n$ by $\hat\beta(n) = j$. Then $\sgn(\hat\beta) = (-1)^{n-j}$.
18. Let $\hat\sigma = \hat\beta^{-1} \circ \tau \circ \hat\alpha$. Then $\hat\sigma(n) = \hat\beta^{-1}(\tau(i)) = \hat\beta^{-1}(j) = n$.
19. For $r \le n-1$, $\tau(\alpha(r)) \ne j$, so $\hat\sigma(r) = \beta^{-1}(\tau(\alpha(r))) = \sigma(r)$. So $\hat\sigma$ fixes $n$ and agrees with $\sigma$ elsewhere.
20. Write $\sigma$ as a product of $m$ transpositions of $\set{1, \dots, n-1}$, with $m = 0$ if $\sigma$ is the identity. The same product, read in $S_n$, is $\hat\sigma$.
21. By the definition of the [[sign|0SK90238BH]], $\sgn(\hat\sigma) = (-1)^m = \sgn(\sigma)$.
22. Since $\tau = \hat\beta \circ \hat\sigma \circ \hat\alpha^{-1}$ and the [[sign is a homomorphism|0JEJJCB0EX]], $\sgn(\tau) = \sgn(\hat\beta) \sgn(\sigma) \sgn(\hat\alpha)^{-1}$.
23. By steps 16 and 17, $\sgn(\tau) = (-1)^{n-j} (-1)^{n-i} \sgn(\sigma) = (-1)^{i+j} \sgn(\sigma)$.
24. By steps 12, 14 and 23, $T_j = (-1)^{i+j} \sum_{\sigma \in S_{n-1}} \sgn(\sigma) \prod_{r=1}^{n-1} (A_{ij})_{r, \sigma(r)}$.
25. By the Leibniz formula for the $(n-1) \times (n-1)$ matrix $A_{ij}$, the sum in step 24 is $\det A_{ij} = M_{ij}$. So $T_j = (-1)^{i+j} M_{ij} = C_{ij}$.
26. By step 4, $\det A = \sum_{j=1}^{n} a_{ij} C_{ij} = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$.

## Idea

Every term of the Leibniz formula uses exactly one entry of row $i$. The terms that use $a_{ij}$ are, after renumbering, the terms of the Leibniz formula for the minor $M_{ij}$. The renumbering moves row $i$ and column $j$ to the end, and this costs the sign $(-1)^{i+j}$.
