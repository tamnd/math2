---
tag: 1XWBY4N0VT
kind: concept
name: Riemann zeta function
msc: [11M06]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_zeta_function
same_as:
  wikidata: Q187235
  wikipedia: Riemann zeta function
---

## Summary

The Riemann zeta function is given by the series $\zeta(s) = \sum_{n \ge 1} n^{-s}$ for complex $s$ with $\operatorname{Re} s > 1$.
It extends to a [[meromorphic function|0ZZ7ZYDR8W]] on $\C$ with a single pole at $s = 1$.
Through the [[Euler product formula|0C3PN4075R]] it encodes the [[prime numbers|01826KMG2H]], and the location of its zeros controls the error term in the [[prime number theorem|0EHBY5Y84N]].
The [[Riemann hypothesis|VCGF9YR36X]] about these zeros is one of the main open problems of mathematics.

## Explanations

### L1 human

Start with the sum $1 + 1/2^s + 1/3^s + \cdots$ of the reciprocals of the powers $n^s$.
For $s = 2$ the sum is $\pi^2/6$, and for $s = 1$ it is the harmonic series, which diverges.
Letting $s$ be a complex number turns this sum into a function with a rich structure.
Because each integer factors into primes in one way, the function carries information about all primes at once.
