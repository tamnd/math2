---
tag: CB9WJCN9BM
kind: concept
name: Krull domain
msc: [13F05]
specializes: [0QVD7WBFGN]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_ring
same_as:
  wikidata: Q623257
  wikipedia: Krull ring
---

## Summary

A Krull domain is an [[integral domain|09S3PFBEPM]] that is the intersection of a family of discrete valuation rings of its fraction field.
The family must satisfy a finiteness condition: each nonzero element has nonzero valuation for only finitely many of them.
[[Unique factorisation domains|06YMXJMXYS]], Dedekind domains and Noetherian [[integrally closed domains|H20P600HQS]] are Krull domains.
Krull domains are the natural setting for the [[divisor class group|WN8PK6RQZR]], which measures their failure to be factorial.

## Explanations

### L1 human

In $\Z$, a rational number is an integer exactly when no prime appears in its denominator.
For each prime $p$, the exponent of $p$ in a fraction is a "valuation", and $\Z$ is the set of fractions where all these exponents are $\ge 0$.
A Krull domain is a ring that can be described in the same way by a family of such exponent functions.
Each nonzero element must have nonzero exponent for only finitely many of them.
This gives a theory of divisibility by "prime divisors" even when elements do not factor uniquely.
