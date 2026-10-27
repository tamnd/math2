---
tag: 0N5ZSZMYH6
kind: concept
name: Fermat primality test
msc: [11Y11]
specializes: [0EGJZHZ02C]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_primality_test
    locator: Concept
same_as:
  wikidata: Q737492
  wikipedia: Fermat primality test
---

## Summary

The Fermat primality test is a probabilistic test of whether an integer $n > 1$ is prime.
It chooses a base $a$ with $1 < a < n - 1$ and computes $a^{n-1} \bmod n$ by [[modular exponentiation|04DR5PM25N]].
If the result is not $1$, then $n$ is composite, by [[Fermat's little theorem|0M25PRN3WQ]]. If the result is $1$, then $n$ is called a probable prime to the base $a$.

## Remarks

A probable prime can be composite. Such a number is a [[Fermat pseudoprime|02M2K4QH9P]].
The [[Carmichael numbers|0TA7WT68RK]] pass the test for each base coprime to them. So repeated tests with many bases cannot detect all composite numbers.
The [[Miller–Rabin primality test|0SZCSYHW60]] is a stronger test of the same kind, without this weakness.

## Explanations

### L1 human

To test $n = 15$ with $a = 2$, compute $2^{14} = 16384 \equiv 4 \pmod{15}$.
The result is not $1$, so $15$ is surely composite. The test does not find a factor; it only proves that one exists.
