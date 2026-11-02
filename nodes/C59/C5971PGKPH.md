---
tag: C5971PGKPH
kind: concept
name: Classical ring of quotients
msc: [16S85, 16U20, 16P60]
specializes: [SG7AQ9T8HD]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_condition
---

## Summary

The classical ring of quotients of a ring $R$ is obtained by inverting all regular elements of $R$.
These are the elements that are not [[zero divisors|0NNRDW10RZ]] on either side.
It is the [[Ore localization|SG7AQ9T8HD]] of $R$ at the set of regular elements, when that localization exists.
For an integral domain it is the [[field of fractions|0F2PTGX1A2]], and for a commutative ring it is the [[total ring of fractions|K5Z67HR9ET]].
[[Goldie's theorem|MDS8655N0Z]] says exactly when this ring is semisimple Artinian.

## Explanations

### L1 human

The rationals are built from the integers by allowing division by every nonzero integer.
For a general ring one cannot divide by an element that kills some other nonzero element, so one only tries to divide by the regular elements.
The classical ring of quotients is the ring of fractions whose denominators are all the regular elements, if it exists.
For a ring of $2 \times 2$ matrices over $\Z$, it is the ring of $2 \times 2$ matrices over $\Q$, since an integer matrix with nonzero determinant becomes invertible over $\Q$.
