---
tag: HEKPB3AM57
kind: proof
name: Proof of the mean of the geometric distribution
msc: ["60E05"]
proves: 0DB0R4N5XX
uses: [0XCVV5Q500, 0WF4EJP91W, 0TST4MHA3A, 0DCT0QZVQ1, 01ZWX875AT, GEA8H3228S, XVEWR93EMV, 7WMBX7M4P6, WW53KG71KH, 05APWSX53S, 0Q7K4AXE53, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_distribution
---

## Proof

We express $E[X]$ as a series, evaluate it by exchanging a double sum, and then pass to $T = X + 1$.

1. Let $p \in (0, 1]$, $q = 1 - p \in [0, 1)$, $S = \set{0, 1, 2, \dots}$ and $p(k) = q^k p$ for $k \in S$.
2. Let $\mu$ be the [[law|0TST4MHA3A]] of $X$. Since $X$ has the [[geometric distribution|0XCVV5Q500]], $\mu(B) = \sum_{k \in B \cap S} p(k)$ for each Borel set $B \subseteq \R$. In particular $\mu(\set{k}) = p(k)$ for $k \in S$.
3. Let $h \colon \R \to [0, \infty)$ be Borel measurable. We show $\int_\R h \, d\mu = \sum_{k \in S} h(k) \, p(k)$ in $[0, \infty]$, using the [[integral of a non-negative function|GEA8H3228S]].
4. Let $s = \sum_{i=1}^{m} a_i \mathbf{1}_{A_i}$ be a [[simple function|7WMBX7M4P6]] with $0 \le s \le h$, $a_i \ge 0$ and pairwise disjoint Borel sets $A_i$. By step 2, $\int s \, d\mu = \sum_{i} a_i \sum_{k \in A_i \cap S} p(k)$.
5. Each $k \in S$ lies in at most one $A_i$, and $s(k) = a_i$ when $k \in A_i$. All terms are nonnegative, so the sum in step 4 equals $\sum_{k \in S} s(k) \, p(k) \le \sum_{k \in S} h(k) \, p(k)$.
6. Taking the supremum over all such $s$ gives $\int h \, d\mu \le \sum_{k \in S} h(k) \, p(k)$.
7. For each $N$, the function $s_N = \sum_{k=0}^{N} h(k) \mathbf{1}_{\set{k}}$ is simple with $0 \le s_N \le h$. So $\sum_{k=0}^{N} h(k) \, p(k) = \int s_N \, d\mu \le \int h \, d\mu$.
8. Letting $N \to \infty$ in step 7 gives $\sum_{k \in S} h(k) \, p(k) \le \int h \, d\mu$. With step 6, equality holds.
9. We compute $\sum_{k \in S} k \, p(k)$. For integers $n, k \ge 0$ let $a_{n,k} = q^k p$ if $1 \le n \le k$, and $a_{n,k} = 0$ otherwise. All $a_{n,k}$ are nonnegative.
10. For fixed $k$, we have $a_{n,k} = q^k p$ for the $k$ indices $1 \le n \le k$ and $a_{n,k} = 0$ otherwise. So $\sum_{n=0}^{\infty} a_{n,k} = k q^k p$.
11. For fixed $n \ge 1$ and $N \ge n$, the [[finite geometric sum|05APWSX53S]] with ratio $q \ne 1$ gives $\sum_{k=n}^{N} q^k p = q^n p \, \dfrac{1 - q^{N-n+1}}{1 - q} = q^n (1 - q^{N-n+1})$.
12. Since $0 \le q < 1$, we have [[$q^m \to 0$|0Q7K4AXE53]]. So by step 11, $\sum_{k=0}^{\infty} a_{n,k} = q^n$ for $n \ge 1$. For $n = 0$ this sum is $0$.
13. By [[Fubini's theorem for series|WW53KG71KH]], both iterated sums of $(a_{n,k})$ equal the sum over all pairs. This sum does not depend on the order of the indices, because it is a supremum of finite sums.
14. So steps 10 and 12 give $\sum_{k=0}^{\infty} k q^k p = \sum_{n=1}^{\infty} q^n$.
15. By the finite geometric sum, $\sum_{n=1}^{M} q^n = q \, \dfrac{1 - q^M}{1 - q}$. This tends to $\dfrac{q}{1 - q} = \dfrac{1 - p}{p}$ as $M \to \infty$, since $q^M \to 0$.
16. Step 3 with $h(x) = \abs{x}$ and step 15 give $\int \abs{x} \, \mu(dx) = (1 - p)/p < \infty$.
17. By the [[law of the unconscious statistician|01ZWX875AT]] with $g(x) = x$, $X$ is integrable and $E[X] = \int_\R x \, \mu(dx)$.
18. By the definition of the [[Lebesgue integral|XVEWR93EMV]], $\int x \, \mu(dx) = \int x^+ \, \mu(dx) - \int x^- \, \mu(dx)$, with $x^+ = \max(x, 0)$ and $x^- = \max(-x, 0)$.
19. On $S$ we have $x^+ = x$ and $x^- = 0$. Step 3 and step 15 give $\int x^+ \, d\mu = (1 - p)/p$ and $\int x^- \, d\mu = 0$. So $E[X] = (1 - p)/p$.
20. The constant random variable $1 = \mathbf{1}_\Omega$ is simple, with $E[1] = P(\Omega) = 1$. So it is integrable.
21. By [[linearity of expectation|0P7PTC8DDE]], $T = X + 1$ is integrable and $E[T] = E[X] + 1 = \dfrac{1 - p}{p} + 1 = \dfrac{1}{p}$.

## Idea

The weight $k$ in $\sum_k k q^k p$ is a count, $k = \sum_{n=1}^{k} 1$. Writing it this way and summing in the other order turns the series into $\sum_{n \ge 1} P(X \ge n)$, where each tail $P(X \ge n) = q^n$ is a geometric sum. A last geometric series gives $(1 - p)/p$, and adding $1$ gives the mean of $T$.
