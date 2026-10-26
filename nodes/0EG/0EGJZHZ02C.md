---
tag: 0EGJZHZ02C
kind: concept
name: Primality test
msc: [11Y11]
uses: [0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Primality_test
    locator: lead section
same_as:
  wikidata: Q829546
  wikipedia: Primality test
---

## Summary

A primality test is an algorithm that decides whether a given natural number is [[prime|0SN0MAEKYX]].
Unlike factorization, it does not need to find the factors of a composite number.

## Remarks

The simplest test is [[trial division|0Z962ECCXR]] by the primes up to $\sqrt{n}$, but it is slow for large $n$.
Probabilistic tests, such as the [[Fermat test|0N5ZSZMYH6]] and the [[Miller–Rabin test|0SZCSYHW60]], are fast but can accept a composite number with a small probability.
In 2002, Agrawal, Kayal and Saxena gave the first deterministic test that runs in polynomial time without an unproven hypothesis.

## Explanations

### L1 human

A primality test answers the question "is $n$ prime?".
For numbers with hundreds of digits, this is much easier than finding the factors of $n$.
