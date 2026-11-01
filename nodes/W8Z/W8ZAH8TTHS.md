---
tag: W8ZAH8TTHS
kind: concept
name: Rees algebra
msc: [13A30]
sources:
  - url: https://en.wikipedia.org/wiki/Rees_algebra
same_as:
  wikidata: Q7306976
  wikipedia: Rees algebra
---

## Summary

The Rees algebra of an [[ideal|096Z9MP2ME]] $I$ of a [[commutative ring|0310REJJY8]] $R$ is the [[graded ring|8KB4SQGC0C]] $R[It] = \bigoplus_{n \ge 0} I^n t^n$, a subring of the polynomial ring $R[t]$.
It packs all the powers of $I$ into one ring, so that statements about all $I^n$ become statements about a single ring.
Its quotient by $I R[It]$ is the [[associated graded ring|8HFAEGFQT1]], and in geometry it gives the blowing up along $I$.

## Explanations

### L1 human

The powers $I, I^2, I^3, \dots$ of an ideal form an infinite list.
The Rees algebra stores the whole list in one ring, using a new variable $t$ to label which power each element comes from.
For $R = k[x]$ and $I = (x)$, the Rees algebra is $k[x, xt]$, a polynomial ring in the two elements $x$ and $xt$.
The [[definition|6YCKECNR3T]] makes this precise.
