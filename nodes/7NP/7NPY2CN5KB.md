---
tag: 7NPY2CN5KB
kind: concept
name: Dedekind domain
msc: [13F05, 11R04]
specializes: [0QVD7WBFGN, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_domain
same_as:
  wikidata: Q254347
  wikipedia: Dedekind domain
---

## Summary

A Dedekind domain is an integral domain in which every nonzero proper ideal is, in a unique way, a product of prime ideals.
Rings of integers of [[number fields|MWBDFS2KJ5]] are Dedekind domains, and so are all [[principal ideal domains|0CMD0BCH8T]].
In such rings unique factorisation of elements may fail, but unique factorisation of ideals always holds.
The [[ideal class group|WQ46BD3ARY]] measures the gap between the two.

## Explanations

### L1 human

In the integers every number splits into primes in only one way.
In larger number rings this can fail: in $\Z[\sqrt{-5}]$, $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ are two different factorisations into irreducible elements.
Dedekind's repair was to factor ideals instead of numbers.
In a Dedekind domain every nonzero proper ideal splits into prime ideals in exactly one way, and the two factorisations of $6$ come from regrouping the same four prime ideals.
