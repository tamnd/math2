---
tag: B85T5VKR3M
kind: concept
name: Valuation
msc: [12J20, 13F30]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(algebra)
same_as:
  wikidata: Q852757
  wikipedia: Valuation (algebra)
---

## Summary

A valuation on a [[field|04C5ZBG1WT]] measures how divisible an element is, with values in a totally ordered abelian group, see the [[definition|SVY882HKSJ]].
The value of a product is the sum of the values.
The value of a sum is at least the smaller of the two values.
The [[p-adic valuation|03HDF50VN4]] on the rationals is the model case.
Valuations give [[valuation rings|QSX12D8RQM]], [[non-Archimedean absolute values|1H5F1BP6XS]] and the whole theory of valued fields.

## Explanations

### L1 human

A valuation asks how many times an element can be divided by a fixed "small" quantity.
For a prime $p$ and a nonzero rational number $x$, write $x = p^n a / b$ with $a$ and $b$ prime to $p$; the valuation of $x$ is $n$.
So $12 = 2^2 \cdot 3$ has $2$-adic valuation $2$, and $3/8$ has $2$-adic valuation $-3$.
Multiplying numbers adds their valuations, just as with exponents.
Adding two numbers can only keep or raise the smaller valuation: $4 + 8 = 12$ has $2$-adic valuation $2$, the smaller of $2$ and $3$.
