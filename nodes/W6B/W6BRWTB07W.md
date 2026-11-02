---
tag: W6BRWTB07W
kind: definition
name: Euler summation
msc: ["40G05"]
defines: 81Q4ERP594
uses: [8X25Q4XYMN, 0JH4MN4K1C, 092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_summation
---

## Definition

Let $\sum_{k \ge 0} a_k$ be a [[series|0JH4MN4K1C]] of complex numbers, and let $q \ge 0$ be real.
The series is *Euler summable* with parameter $q$, or $(E, q)$ summable, to $s$ if the series
$$\sum_{p \ge 0} \frac{1}{(1 + q)^{p + 1}} \sum_{k=0}^{p} \binom{p}{k} q^{p - k} a_k$$
converges and its sum is $s$.
Here $\binom{p}{k}$ is the [[binomial coefficient|092GEF38YD]].
The case $q = 1$ is called Euler summation without qualification:
$$\sum_{p \ge 0} \frac{1}{2^{p + 1}} \sum_{k=0}^{p} \binom{p}{k} a_k = s.$$

## Remarks

For $q = 0$ the inner sum is $a_p$ alone, and $(E, 0)$ is ordinary convergence.

Example: take $a_k = (-1)^k (k + 1)$, that is $1 - 2 + 3 - 4 + \cdots$, and $q = 1$.
The identities $\sum_{k=0}^{p} \binom{p}{k} (-1)^k = 0$ for $p \ge 1$ and $\sum_{k=0}^{p} \binom{p}{k} (-1)^k k = 0$ for $p \ge 2$ show that only $p = 0$ and $p = 1$ contribute.
These give $\frac12 \cdot 1 + \frac14 \cdot (1 - 2) = \frac14$, so the series is $(E, 1)$ summable to $1/4$.

Non-example: for $1 + 1 + 1 + \cdots$ and $q = 1$, the inner sum is $2^p$, and every term of the new series is $\frac12$.
That series diverges, so $1 + 1 + 1 + \cdots$ is not $(E, 1)$ summable.
