---
tag: QSX12D8RQM
kind: concept
name: Valuation ring
msc: [13F30, 12J20]
specializes: [0QVD7WBFGN]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_ring
same_as:
  wikidata: Q12013681
  wikipedia: Valuation ring
---

## Summary

A valuation ring is an [[integral domain|0QVD7WBFGN]] $R$ with a simple property, see the [[definition|YVQ9CKGA0T]].
For each nonzero $x$ in its [[field of fractions|0F2PTGX1A2]], either $x$ or $1/x$ lies in $R$.
Valuation rings are exactly the rings of elements of nonnegative value for a [[valuation|B85T5VKR3M]].
They are [[local rings|MZ02BKPHJA]], and their ideals are totally ordered by inclusion.
[[Discrete valuation rings|MGM3CNJW9V]] are the Noetherian valuation rings that are not fields.

## Explanations

### L1 human

Think of the fractions whose denominator is not divisible by a prime $p$, such as $3/5$ or $7/2$ for $p = 3$.
They form a ring, and any fraction that is not in it, such as $5/3$, has its inverse $3/5$ in it.
So the ring takes "half" of the fractions in a precise sense: from each pair $x, 1/x$ at least one is in.
This half is decided by one rule, the size of the power of $p$, and in general by a valuation.
