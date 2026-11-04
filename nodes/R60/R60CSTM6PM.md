---
tag: R60CSTM6PM
kind: proof
name: Proof of the generating function for partitions
msc: [11P81]
proves: 0578PA53VA
uses: [001CX45SWQ, 0404R9P9J3, 0HH6JX5WZZ, 072W67KFYK, 0M98XYVX6S, 0H6KWAYS87]
sources:
  - url: https://en.wikipedia.org/wiki/Partition_function_(number_theory)
    locator: Generating function
---

## Proof

We compute the coefficients of the finite partial products, and we show that they stabilise at $p(n)$.

1. All series are [[formal power series|072W67KFYK]] in $\Z[\![x]\!]$. For $k \ge 1$ let $g_k = \sum_{m \ge 0} x^{km}$. So $[x^j] g_k = 1$ if $k \mid j$, and $[x^j] g_k = 0$ otherwise.
2. By the [[product formula|0H6KWAYS87]], $[x^n](x^k g_k) = [x^{n-k}] g_k$ for $n \ge k$, and $0$ for $n < k$. So $x^k g_k = \sum_{m \ge 1} x^{km}$.
3. Hence $(1 - x^k) g_k = g_k - x^k g_k = 1$. So $1 - x^k$ is a unit and $\frac{1}{1 - x^k} = g_k$.
4. For $N \in \N$ let $P_N = g_1 g_2 \cdots g_N$, with $P_0 = 1$. The infinite product $\prod_{k \ge 1} \frac{1}{1 - x^k}$ means the series whose coefficient of $x^n$ is $[x^n] P_N$ for all $N \ge n$.
5. Steps 6 to 13 show that this is well defined, and compute it. Let $c_N(n)$ be the number of tuples $(m_1, \dots, m_N) \in \N^N$ with $\sum_{k=1}^{N} k\, m_k = n$.
6. Claim: $[x^n] P_N = c_N(n)$ for all $N, n \in \N$. We argue by induction on $N$.
7. For $N = 0$, $P_0 = 1$ has $[x^n] P_0 = 1$ if $n = 0$ and $0$ otherwise. Only the empty tuple has length $0$, and its sum is $0$. So $c_0(n) = [x^n] P_0$.
8. Let $N \ge 1$. By the product formula and step 1, $[x^n] P_N = \sum_{i + j = n} [x^i] P_{N-1} \cdot [x^j] g_N = \sum_{m \ge 0,\ Nm \le n} [x^{n - Nm}] P_{N-1}$.
9. By the induction hypothesis this is $\sum_{m \ge 0,\ Nm \le n} c_{N-1}(n - Nm)$. Sorting the tuples of length $N$ by their last entry $m_N = m$ shows that this sum is $c_N(n)$.
10. A [[partition|0404R9P9J3]] of $n$ with all parts at most $N$ is determined by the numbers $m_k$ of its parts equal to $k$, for $1 \le k \le N$. These satisfy $\sum_k k\, m_k = n$, and each such tuple gives one partition.
11. So $c_N(n)$ is the number of partitions of $n$ with all parts at most $N$.
12. Let $N \ge n$. Each part of a partition of $n$ is at most $n \le N$. So $c_N(n)$ is the number of all partitions of $n$, which is the [[partition function|001CX45SWQ]] value $p(n)$.
13. By steps 6 and 12, $[x^n] P_N = p(n)$ for every $N \ge n$. So the coefficients in step 4 do not depend on $N$, and the infinite product is well defined.
14. Two series with the same coefficients are equal, by the definition of the [[coefficients|0M98XYVX6S]]. Hence $\prod_{k \ge 1} \frac{1}{1 - x^k} = \sum_{n \ge 0} p(n)\, x^n$, the [[generating function|0HH6JX5WZZ]] of $p$.

## Idea

The factor $\frac{1}{1 - x^k} = 1 + x^k + x^{2k} + \dots$ records how many parts equal $k$: choosing $x^{k m_k}$ means taking $m_k$ parts of size $k$.
A term of $x^n$ in the expanded product is then exactly a partition of $n$. Factors with $k > n$ only contribute their constant term $1$ to the coefficient of $x^n$.
