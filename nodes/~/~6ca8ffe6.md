---
tag: ~6ca8ffe6
kind: definition
name: Number of distinct prime factors
aliases: [little-omega-function]
msc: [11A25]
defines: ~c1c79163
uses: [~f3c51c16, ~0abb0ec7]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_omega_function
    locator: lead section
---

## Definition

For a positive integer $n$, $\omega(n)$ is the number of distinct [[prime numbers|~f3c51c16]] that divide $n$.
So if $n = p_1^{e_1} \cdots p_k^{e_k}$ with distinct primes $p_i$ and $e_i \ge 1$, then $\omega(n) = k$.

## Remarks

For example, $\omega(1) = 0$, $\omega(12) = 2$ and $\omega(30) = 3$.
The function $\omega$ is additive: $\omega(mn) = \omega(m) + \omega(n)$ for coprime $m$ and $n$.
Compare with the [[number of prime factors with multiplicity|~a8bd24f0]] $\Omega(n)$. We have $\omega(n) \le \Omega(n)$, with equality exactly for squarefree $n$.

## Explanations

### L1 human

The function $\omega(n)$ counts the different primes in $n$ and ignores repeats.
For $360 = 2^3 \cdot 3^2 \cdot 5$, the different primes are $2$, $3$ and $5$, so $\omega(360) = 3$.
