---
tag: 8HFAEGFQT1
kind: concept
name: Associated graded ring
msc: [13A30, 13A02]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_graded_ring
same_as:
  wikidata: Q17097755
  wikipedia: Associated graded ring
---

## Summary

The associated graded ring of a [[commutative ring|0310REJJY8]] $R$ with respect to an [[ideal|096Z9MP2ME]] $I$ is the [[graded ring|8KB4SQGC0C]] $\operatorname{gr}_I(R) = \bigoplus_{n \ge 0} I^n/I^{n+1}$.
It keeps the leading terms of elements and forgets the rest.
For a local ring and its maximal ideal it describes the tangent cone of the point.
Since it is graded, tools for graded rings such as the [[Hilbert polynomial|RMH4FBCFDA]] apply to local rings through it.

## Explanations

### L1 human

Near a point, a curve looks to first approximation like its tangent lines.
The associated graded ring records only these first approximations, by keeping the lowest-degree part of each function.
For the integers and a prime $p$, the piece $p^n\Z/p^{n+1}\Z$ records one digit in base $p$, and these pieces together form the polynomial ring $\F_p[t]$.
The [[definition|XBZ99KH3RP]] makes this precise.
