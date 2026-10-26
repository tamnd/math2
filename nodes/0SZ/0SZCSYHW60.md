---
tag: 0SZCSYHW60
kind: concept
name: Miller–Rabin primality test
aliases: [rabin-miller-primality-test]
msc: [11Y11]
uses: [0EGJZHZ02C, 0M25PRN3WQ, 04DR5PM25N]
sources:
  - url: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    locator: Strong probable primes
same_as:
  wikidata: Q980224
  wikipedia: Miller–Rabin primality test
---

## Summary

The Miller–Rabin test is a probabilistic [[primality test|0EGJZHZ02C]] for an odd integer $n > 2$.
Write $n - 1 = 2^s d$ with $d$ odd, and choose a base $a$ with $1 < a < n - 1$.
The number $n$ passes for base $a$ if $a^d \equiv 1 \pmod n$, or if $a^{2^r d} \equiv -1 \pmod n$ for some $r$ with $0 \le r < s$.
Each odd prime $n$ passes for each base. If $n$ fails for some base, then $n$ is composite.

## Remarks

The prime case follows from [[Fermat's little theorem|0M25PRN3WQ]] and the fact that $\pm 1$ are the only square roots of $1$ modulo a prime.
If $n$ is an odd composite number, then at most $\frac{1}{4}$ of the bases let it pass. So $k$ random bases give an error probability of at most $4^{-k}$.
Gary Miller found the test in 1976, in a deterministic form that depends on the extended Riemann hypothesis. Michael Rabin made it an unconditional probabilistic test in 1980.

## Explanations

### L1 human

The test checks a property that every prime has, for a few random bases.
A composite number fails for most bases, so a few rounds expose it with high probability.
The powers are fast to compute by [[modular exponentiation|04DR5PM25N]].
