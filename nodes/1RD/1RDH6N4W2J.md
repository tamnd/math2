---
tag: 1RDH6N4W2J
kind: proof
name: Proof of the mean of the binomial distribution by direct summation
msc: ["60E05"]
proves: 0PVCTCKD3C
uses: [0VRWZDWW6B, 0WF4EJP91W, 0TST4MHA3A, 0DCT0QZVQ1, 01ZWX875AT, GEA8H3228S, XVEWR93EMV, 7WMBX7M4P6, 092GEF38YD, 033KTKKRV6, 0EHWPWGHB2]
sources:
  - url: https://proofwiki.org/wiki/Expectation_of_Binomial_Distribution
---

## Proof

We first express $E[X]$ as a finite sum, then evaluate the sum with the binomial theorem.

1. Let $n \ge 1$, $p \in [0, 1]$, $q = 1 - p$ and $S = \set{0, 1, \dots, n}$. Let $p(k) = \binom{n}{k} p^k q^{n-k}$ for $k \in S$.
2. Let $\mu$ be the [[law|0TST4MHA3A]] of $X$. Since $X$ has the [[binomial distribution|0VRWZDWW6B]], $\mu(B) = \sum_{k \in B \cap S} p(k)$ for each Borel set $B \subseteq \R$. In particular $\mu(\set{k}) = p(k)$ for $k \in S$.
3. Let $h \colon \R \to [0, \infty)$ be Borel measurable. We show $\int_\R h \, d\mu = \sum_{k \in S} h(k) \, p(k)$, using the [[integral of a non-negative function|GEA8H3228S]].
4. Let $s = \sum_{i=1}^{m} a_i \mathbf{1}_{A_i}$ be a [[simple function|7WMBX7M4P6]] with $0 \le s \le h$, $a_i \ge 0$ and pairwise disjoint Borel sets $A_i$. By step 2, $\int s \, d\mu = \sum_{i} a_i \sum_{k \in A_i \cap S} p(k)$.
5. Each $k \in S$ lies in at most one $A_i$, and $s(k) = a_i$ when $k \in A_i$. So the sum in step 4 equals $\sum_{k \in S} s(k) \, p(k) \le \sum_{k \in S} h(k) \, p(k)$.
6. Taking the supremum over all such $s$ gives $\int h \, d\mu \le \sum_{k \in S} h(k) \, p(k)$.
7. The function $s_0 = \sum_{k \in S} h(k) \mathbf{1}_{\set{k}}$ is simple, with disjoint Borel sets $\set{k}$, and $0 \le s_0 \le h$. Its integral is $\sum_{k \in S} h(k) \, p(k)$. So equality holds in step 6.
8. Apply step 3 to $h(x) = \abs{x}$. This gives $\int \abs{x} \, \mu(dx) = \sum_{k=0}^{n} k \, p(k) < \infty$.
9. By the [[law of the unconscious statistician|01ZWX875AT]] with $g(x) = x$, $X$ is integrable and $E[X] = \int_\R x \, \mu(dx)$.
10. By the definition of the [[Lebesgue integral|XVEWR93EMV]], $\int x \, \mu(dx) = \int x^+ \, \mu(dx) - \int x^- \, \mu(dx)$, with $x^+ = \max(x, 0)$ and $x^- = \max(-x, 0)$.
11. On $S$ we have $x^+ = x$ and $x^- = 0$. Step 3 gives $\int x^+ \, d\mu = \sum_{k=0}^{n} k \, p(k)$ and $\int x^- \, d\mu = 0$. So $E[X] = \sum_{k=0}^{n} k \binom{n}{k} p^k q^{n-k}$, the first equality.
12. The term with $k = 0$ is zero. Let $1 \le k \le n$. By the [[factorial formula|033KTKKRV6]] for [[binomial coefficients|092GEF38YD]], $k \binom{n}{k} = \dfrac{n!}{(k-1)! \, (n-k)!} = n \binom{n-1}{k-1}$, since $(n-1) - (k-1) = n - k$.
13. So $E[X] = \sum_{k=1}^{n} n \binom{n-1}{k-1} p^k q^{n-k}$. Put $j = k - 1$, so that $n - k = (n - 1) - j$. Then $E[X] = np \sum_{j=0}^{n-1} \binom{n-1}{j} p^j q^{(n-1)-j}$.
14. By the [[binomial theorem|0EHWPWGHB2]] with exponent $n - 1 \ge 0$, the last sum is $(p + q)^{n-1} = 1^{n-1} = 1$.
15. Hence $E[X] = np$.

## Idea

For a distribution on finitely many points, the expectation is the weighted sum $\sum_k k \, p(k)$. The identity $k \binom{n}{k} = n \binom{n-1}{k-1}$ pulls out a factor $np$. What is left is the full sum of the $\operatorname{Bin}(n - 1, p)$ probabilities, which is $1$ by the binomial theorem.
