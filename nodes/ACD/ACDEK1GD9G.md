---
tag: ACDEK1GD9G
kind: concept
name: GCD domain
msc: [13F15, 13G05]
specializes: [0QVD7WBFGN]
sources:
  - url: https://en.wikipedia.org/wiki/GCD_domain
same_as:
  wikidata: Q2851438
  wikipedia: GCD domain
---

## Summary

A GCD domain is an [[integral domain|09S3PFBEPM]] in which any two elements have a [[greatest common divisor|0F7KNJ1ZYN]].
Every [[unique factorisation domain|06YMXJMXYS]] and every [[Bézout domain|HGEX40P0Z0]] is a GCD domain.
In a GCD domain every [[irreducible element|052SDEPZH7]] is [[prime|0MNHXBSX3M]], and the ring is [[integrally closed|H20P600HQS]].
GCD domains need not have factorizations into irreducibles, so the notion is strictly weaker than unique factorization.

## Explanations

### L1 human

In the integers, any two numbers have a greatest common divisor, such as $\gcd(12, 18) = 6$.
A GCD domain is a ring where this keeps working: among the common divisors of $a$ and $b$ there is one that every other common divisor divides.
The ring $\Z[\sqrt{-5}]$ is not a GCD domain: the elements $6$ and $2(1 + \sqrt{-5})$ have the common divisors $2$ and $1 + \sqrt{-5}$, but no common divisor is divisible by both.
