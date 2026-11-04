---
tag: RP8X5R1AGX
kind: proof
name: Proof of the mean of the Poisson distribution
msc: ["60E05"]
proves: 086HEVXR9Z
uses: [0VEFSSKX18, 0WF4EJP91W, 0TST4MHA3A, 0DCT0QZVQ1, 01ZWX875AT, GEA8H3228S, XVEWR93EMV, 7WMBX7M4P6, 06JZGMYTYD, 0E8HNVBCSP]
sources:
  - url: https://proofwiki.org/wiki/Expectation_of_Poisson_Distribution
---

## Proof

We first express $E[X]$ as a series, then shift the index and recognise the exponential series.

1. Let $\lambda > 0$, $S = \set{0, 1, 2, \dots}$ and $p(k) = e^{-\lambda} \lambda^k / k!$ for $k \in S$.
2. Let $\mu$ be the [[law|0TST4MHA3A]] of $X$. Since $X$ has the [[Poisson distribution|0VEFSSKX18]], $\mu(B) = \sum_{k \in B \cap S} p(k)$ for each Borel set $B \subseteq \R$. In particular $\mu(\set{k}) = p(k)$ for $k \in S$.
3. Let $h \colon \R \to [0, \infty)$ be Borel measurable. We show $\int_\R h \, d\mu = \sum_{k \in S} h(k) \, p(k)$ in $[0, \infty]$, using the [[integral of a non-negative function|GEA8H3228S]].
4. Let $s = \sum_{i=1}^{m} a_i \mathbf{1}_{A_i}$ be a [[simple function|7WMBX7M4P6]] with $0 \le s \le h$, $a_i \ge 0$ and pairwise disjoint Borel sets $A_i$. By step 2, $\int s \, d\mu = \sum_{i} a_i \sum_{k \in A_i \cap S} p(k)$.
5. Each $k \in S$ lies in at most one $A_i$, and $s(k) = a_i$ when $k \in A_i$. All terms are nonnegative, so the sum in step 4 equals $\sum_{k \in S} s(k) \, p(k) \le \sum_{k \in S} h(k) \, p(k)$.
6. Taking the supremum over all such $s$ gives $\int h \, d\mu \le \sum_{k \in S} h(k) \, p(k)$.
7. For each $N$, the function $s_N = \sum_{k=0}^{N} h(k) \mathbf{1}_{\set{k}}$ is simple with $0 \le s_N \le h$. So $\sum_{k=0}^{N} h(k) \, p(k) = \int s_N \, d\mu \le \int h \, d\mu$.
8. Letting $N \to \infty$ in step 7 gives $\sum_{k \in S} h(k) \, p(k) \le \int h \, d\mu$. With step 6, equality holds.
9. We compute $\sum_{k \in S} k \, p(k)$. The term with $k = 0$ is zero. For $k \ge 1$, $k \, \lambda^k / k! = \lambda \cdot \lambda^{k-1} / (k-1)!$.
10. So for each $N \ge 1$, $\sum_{k=0}^{N} k \, p(k) = \lambda e^{-\lambda} \sum_{j=0}^{N-1} \lambda^j / j!$, with $j = k - 1$.
11. By the [[power series of the exponential function|06JZGMYTYD]], the right side tends to $\lambda e^{-\lambda} e^{\lambda}$ as $N \to \infty$. By the [[exponential of a sum|0E8HNVBCSP]], $e^{-\lambda} e^{\lambda} = e^0 = 1$. So $\sum_{k \in S} k \, p(k) = \lambda$.
12. Step 3 with $h(x) = \abs{x}$ and step 11 give $\int \abs{x} \, \mu(dx) = \lambda < \infty$.
13. By the [[law of the unconscious statistician|01ZWX875AT]] with $g(x) = x$, $X$ is integrable and $E[X] = \int_\R x \, \mu(dx)$.
14. By the definition of the [[Lebesgue integral|XVEWR93EMV]], $\int x \, \mu(dx) = \int x^+ \, \mu(dx) - \int x^- \, \mu(dx)$, with $x^+ = \max(x, 0)$ and $x^- = \max(-x, 0)$.
15. On $S$ we have $x^+ = x$ and $x^- = 0$. Step 3 gives $\int x^+ \, d\mu = \sum_{k \in S} k \, p(k)$ and $\int x^- \, d\mu = 0$.
16. Hence $E[X] = \sum_{k=0}^{\infty} k \, e^{-\lambda} \lambda^k / k! = \lambda$, by step 11.

## Idea

The expectation of a variable on $\set{0, 1, 2, \dots}$ is the weighted sum $\sum_k k \, p(k)$. The factor $k$ cancels against $k!$ and leaves $(k-1)!$. After a shift of index, the sum is $\lambda e^{-\lambda}$ times the exponential series for $e^{\lambda}$.
