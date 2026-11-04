---
tag: AXP2HY5SA8
kind: proof
name: Proof of the Cauchy condensation test
msc: [40A05]
proves: 0B96KMDDD1
uses: [0MX1HZBBXJ, 0KN22AAW5R, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_condensation_test
    locator: Estimate
---

## Proof

We compare the two sequences of partial sums by grouping terms in blocks of length a power of $2$.

1. For $n \ge 1$ let $s_n = \sum_{m=1}^{n} a_m$, and for $K \ge 0$ let $t_K = \sum_{k=0}^{K} 2^k a_{2^k}$. These are the [[partial sums|0NB643K60Q]] of the two series. Both have nonnegative terms, so both sequences are increasing.
2. By the [[criterion for nonnegative series|0MX1HZBBXJ]], each series converges if and only if its partial sums are bounded above. A shift of the starting index does not change this.
3. Let $k \ge 0$. The block of indices $m$ with $2^k \le m \le 2^{k+1} - 1$ has $2^k$ elements. Since $(a_n)$ is decreasing, as a [[monotone sequence|0KN22AAW5R]], each term in it satisfies $a_m \le a_{2^k}$.
4. So the block sum is at most $2^k a_{2^k}$. Adding over $k = 0, \dots, K$ gives $s_{2^{K+1} - 1} \le t_K$.
5. Let $k \ge 1$. The block of indices $m$ with $2^{k-1} < m \le 2^k$ has $2^{k-1}$ elements, and each term in it satisfies $a_m \ge a_{2^k}$.
6. So that block sum is at least $2^{k-1} a_{2^k}$. Adding over $k = 1, \dots, K$ and adding $a_1$ gives $s_{2^K} \ge a_1 + \sum_{k=1}^{K} 2^{k-1} a_{2^k}$.
7. The right side of step 6 is at least $\tfrac12 a_1 + \tfrac12 \sum_{k=1}^{K} 2^k a_{2^k} = \tfrac12 t_K$, since $a_1 \ge 0$. So $t_K \le 2 s_{2^K}$.
8. Assume that the condensed series converges, with sum $T$. Then $t_K \le T$ for all $K$, by step 2. Let $n \ge 1$. Since $n \le 2^{n+1} - 1$ and $(s_n)$ is increasing, step 4 gives $s_n \le s_{2^{n+1}-1} \le t_n \le T$.
9. So $(s_n)$ is bounded above, and $\sum a_n$ converges by step 2.
10. Assume that $\sum a_n$ converges, with sum $S$. Then $s_n \le S$ for all $n$. By step 7, $t_K \le 2 s_{2^K} \le 2S$ for all $K$.
11. So $(t_K)$ is bounded above, and the condensed series converges by step 2.

## Idea

Between consecutive powers of $2$, a decreasing sequence is squeezed between its values at the two ends. So the sum over the block from $2^k$ to $2^{k+1}$ is comparable to $2^k a_{2^k}$. The two series bound each other up to a factor $2$.
