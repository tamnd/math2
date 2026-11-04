---
tag: 8W8P5BK6XH
kind: proof
name: Erdős's proof of the divergence of the sum of the reciprocals of the primes
msc: [11N05]
proves: 00RA98X2CP
uses: [0SN0MAEKYX, 0292EPPPT0, 0AXWET80YW, 0M8TGGP9JP, 080Q3RPKY6, 004JW7A2N5, 020K0X7HVR, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes
    locator: Erdős's proof by upper and lower estimates
---

## Proof

We argue by contradiction and count the integers up to $x$ in two ways.

1. By [[Euclid's theorem|0292EPPPT0]], there are infinitely many [[prime numbers|0SN0MAEKYX]]. List them in increasing order as $p_1 < p_2 < p_3 < \cdots$.
2. For $j \ge 1$, put $s_j = \sum_{i=1}^{j} 1/p_i$. Every partial sum $\sum_{p \le x} 1/p$ equals some $s_j$ or $0$, and every $s_j$ is such a partial sum.
3. Suppose the partial sums are bounded. Then the set $\set{s_j : j \ge 1}$ is bounded above. By the [[completeness axiom|0AXWET80YW]], it has a supremum $L$.
4. By the [[approximation property of the supremum|0M8TGGP9JP]], there is an index $k$ with $s_k > L - 1/2$.
5. For every $j > k$, we get $\sum_{i=k+1}^{j} 1/p_i = s_j - s_k < L - (L - 1/2) = 1/2$, because $s_j \le L$.
6. Put $x = 2^{2k+2}$. Let $M$ be the set of integers $n$ with $1 \le n \le x$ such that no prime $p_i$ with $i > k$ [[divides|096PW7Q014]] $n$.
7. Upper estimate. Let $n \in M$. By [[the square times square-free decomposition|080Q3RPKY6]], $n = m^2 r$ with positive integers $m$, $r$ and $r$ [[square-free|004JW7A2N5]].
8. Every prime that divides $r$ divides $n$, so it is one of $p_1, \dots, p_k$.
9. By the [[existence of prime factorization|020K0X7HVR]], $r$ is a product of primes. No prime occurs twice, since then its square would divide $r$.
10. So $r$ is the product of a subset of $\set{p_1, \dots, p_k}$. There are $2^k$ subsets, so $r$ takes at most $2^k$ values.
11. Also $m^2 \le n \le x$, so $m \le \sqrt{x} = 2^{k+1}$. So $m$ takes at most $2^{k+1}$ values.
12. The pair $(m, r)$ determines $n$. Hence $|M| \le 2^k \cdot 2^{k+1} = 2^{2k+1} = x/2$.
13. Lower estimate. Let $1 \le n \le x$ with $n \notin M$. Then some $p_i$ with $i > k$ divides $n$, and $p_i \le n \le x$.
14. Let $J$ be the largest index with $p_J \le x$. If $J \le k$, no such $n$ exists, and $|M| = x > x/2$.
15. If $J > k$, each such $n$ is a multiple of some $p_i$ with $k < i \le J$. The number of multiples of $p_i$ in $\set{1, \dots, x}$ is at most $x / p_i$.
16. So $x - |M| \le \sum_{i=k+1}^{J} x / p_i = x \sum_{i=k+1}^{J} 1/p_i < x/2$ by step 5. Hence $|M| > x/2$.
17. Steps 12, 14 and 16 give $x/2 < |M| \le x/2$, which is a contradiction.
18. So the partial sums $\sum_{p \le x} 1/p$ are not bounded, and the series $\sum_p 1/p$ diverges.

## Idea

If the series converged, the primes beyond some $p_k$ would have reciprocal sum below $1/2$. Then fewer than half of the numbers up to $x$ could have a large prime factor. But numbers built only from $p_1, \dots, p_k$ are rare: writing them as a square times a square-free part shows there are at most $2^k \sqrt{x}$ of them. For $x = 4^{k+1}$ the two counts cannot both hold.
