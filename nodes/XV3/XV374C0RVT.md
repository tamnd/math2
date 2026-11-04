---
tag: XV374C0RVT
kind: proof
name: Proof that a series of nonnegative terms converges iff its partial sums are bounded
msc: [40A05]
proves: 0MX1HZBBXJ
uses: [0CVVKY7GY2, 0NB643K60Q, 0FM6N4R0VB, 0S4JF619V7, 0KN22AAW5R, 0K0H5E3Z5N]
sources:
  - url: https://en.wikipedia.org/wiki/Convergent_series
---

## Proof

1. Let $s_N = \sum_{n=0}^{N} a_n$ be the [[partial sums|0NB643K60Q]]. Since $s_{N+1} - s_N = a_{N+1} \ge 0$, the sequence $(s_N)$ is increasing, as a [[monotone sequence|0KN22AAW5R]].
2. Assume that $(s_N)$ is bounded above. By the [[monotone convergence theorem|0FM6N4R0VB]], $(s_N)$ converges, and its limit is $\sup_N s_N$.
3. By the definition of a [[convergent series|0CVVKY7GY2]], $\sum a_n$ converges. Its [[sum|0K0H5E3Z5N]] is the limit of $(s_N)$, which is $\sup_N s_N$ by step 2.
4. Conversely, assume that $\sum a_n$ converges. Then $(s_N)$ is a convergent sequence.
5. [[Convergent sequences are bounded|0S4JF619V7]], so $(s_N)$ is bounded, and in particular bounded above.
6. Steps 2 to 5 prove the equivalence. When it holds, step 3 gives $\sum_{n=0}^{\infty} a_n = \sup_N s_N$.

## Idea

Nonnegative terms make the partial sums increase. An increasing sequence has only one way to fail to converge: it grows without bound. So boundedness is exactly what is needed.
