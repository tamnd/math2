---
tag: AN9SKEZ3VY
kind: concept
name: Multiplicative set
msc: [13B30, 13A99]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicatively_closed_set
same_as:
  wikidata: Q2917823
  wikipedia: Multiplicatively closed set
---

## Summary

A multiplicative set in a [[commutative ring|0310REJJY8]] is a subset that contains $1$ and is closed under multiplication.
These sets are exactly the sets of elements that one may turn into units by [[localization|4C1AE84N5N]].
The complement of a [[prime ideal|00MHHZ9SNE]] and the set of powers of one element are the two main examples.

## Explanations

### L1 human

Think of a multiplicative set as a list of allowed denominators.
If you may divide by $s$ and by $t$, then you may also divide by $st$, so the list must be closed under products.
You may always divide by $1$, so $1$ is on the list.
In the integers, the powers $1, 2, 4, 8, \ldots$ form a multiplicative set, and allowing them as denominators gives the fractions $a / 2^k$.
The [[definition|PCH3G8BJ9Y]] gives the precise conditions.
