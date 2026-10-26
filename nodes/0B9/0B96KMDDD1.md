---
tag: 0B96KMDDD1
kind: statement
role: theorem
name: Cauchy condensation test
msc: [40A05]
uses: [0MX1HZBBXJ, 0KN22AAW5R]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_condensation_test
    locator: Estimate
same_as:
  wikidata: Q1051423
  wikipedia: Cauchy condensation test
---

## Statement

Let $(a_n)_{n \ge 1}$ be a decreasing real sequence with $a_n \ge 0$ for all $n$.
Then $\sum_{n=1}^{\infty} a_n$ converges if and only if the condensed series $\sum_{k=0}^{\infty} 2^k a_{2^k}$ converges.

## Remarks

The proof groups the terms from $2^k$ to $2^{k+1} - 1$. Since the sequence decreases, $\sum_{n=1}^{\infty} a_n \le \sum_{k=0}^{\infty} 2^k a_{2^k} \le 2 \sum_{n=1}^{\infty} a_n$.
With $a_n = 1/n^p$ it gives the [[p-series test|0ZNSSK8ZK1]].
With $a_n = 1/(n \ln n)$ for $n \ge 2$, the condensed series is a multiple of $\sum 1/k$, so $\sum 1/(n \ln n)$ diverges.

## Explanations

### L1 human

For a decreasing sequence, the terms between $2^k$ and $2^{k+1}$ are all about the same size as $a_{2^k}$.
So only one term out of each such block matters, weighted by the size $2^k$ of the block.
