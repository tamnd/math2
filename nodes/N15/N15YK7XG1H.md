---
tag: N15YK7XG1H
kind: concept
name: Large sieve
msc: [11N35, 11N36]
sources:
  - url: https://en.wikipedia.org/wiki/Large_sieve
same_as:
  wikidata: Q5495242
  wikipedia: Large sieve
---

## Summary

The large sieve is a method of analytic number theory.
It applies when a set of integers is sifted by many residue classes modulo each prime.
Its core is an inequality for exponential sums: a trigonometric polynomial cannot be large at many well-spaced points at once.
In arithmetic form it bounds the size of a set of integers that misses many residue classes modulo many primes.
It is a key tool in the proof of the [[Bombieri–Vinogradov theorem|B3JMY54GJF]].

## Explanations

### L1 human

Classical sieves remove a few residue classes modulo each prime, for example the class $0$.
The large sieve handles the case where a large fraction of the classes is removed.
For example, the perfect squares fall into only $(p+1)/2$ of the $p$ residue classes modulo an odd prime $p$.
Its engine is a kind of uncertainty principle: a sum of waves $e^{2\pi i n \alpha}$ with $n$ in a short interval cannot be big at many points $\alpha$ that are far apart.
A set of integers that avoids many residue classes would make such a sum big at many fractions $a/q$, so such a set must be small.
