---
tag: WPC2XRMB9Y
kind: concept
name: Essential supremum
msc: [28A20, 28A25]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_infimum_and_essential_supremum
same_as:
  wikidata: Q104804789
  wikipedia: Essential infimum and essential supremum
---

## Summary

The essential supremum of a measurable function is the smallest number that the function exceeds only on a set of measure zero.
It is the supremum that ignores what happens on null sets.
It gives the norm of the space $L^\infty$, and it is the natural bound when functions are only known up to equality almost everywhere.

## Explanations

### L1 human

The ordinary supremum is the least upper bound of all the values of a function.
A single wild value at one point can make it huge, even though one point does not matter for integrals.
The essential supremum throws away such values when they live on a set of measure zero.
For example, let $f(x) = 0$ for $x \ne 0$ and $f(0) = 100$ on the real line with Lebesgue measure.
Its supremum is $100$, but its essential supremum is $0$.
