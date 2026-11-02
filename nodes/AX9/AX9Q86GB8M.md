---
tag: AX9Q86GB8M
kind: concept
name: Ultraproduct
msc: [03C20]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
same_as:
  wikidata: Q1535225
  wikipedia: Ultraproduct
---

## Summary

An ultraproduct combines a family of structures of the same language into one new structure.
An [[ultrafilter|J64Y3JC0RE]] on the index set decides which properties hold in it.
A property holds in the ultraproduct when it holds in a "large" set of factors, where "large" means "in the ultrafilter".
By [[Łoś's theorem|AGYBSTD7BG]], this rule works for every first-order formula.
Ultraproducts give a short proof of the [[compactness theorem|1NR3HAWG9D]] and build nonstandard models such as the [[hyperreal numbers|421QMTFG9T]].

## Explanations

### L1 human

Take infinitely many copies of a structure, say the real numbers, one for each natural number.
An element of the new structure is a sequence, one entry from each copy.
Two sequences count as equal when they agree on a large set of indices, and an ultrafilter says which sets are large.
For example, with a non-principal ultrafilter on $\N$, the sequence $(1, 2, 3, \dots)$ becomes a number larger than every ordinary real number.
This is how infinitely large and infinitely small numbers can be built rigorously.
