---
tag: 2RDAA4PCK8
kind: concept
name: Prüfer domain
msc: [13F05]
specializes: [0QVD7WBFGN]
sources:
  - url: https://en.wikipedia.org/wiki/Pr%C3%BCfer_domain
same_as:
  wikidata: Q2894873
  wikipedia: Prüfer domain
---

## Summary

A Prüfer domain is an [[integral domain|09S3PFBEPM]] in which every nonzero finitely generated ideal is [[invertible|E190TAV2S6]].
Equivalently, its [[localization|4C1AE84N5N]] at every prime ideal is a valuation ring.
Prüfer domains are the non-Noetherian analogue of Dedekind domains: a Noetherian Prüfer domain is exactly a Dedekind domain.
Every [[Bézout domain|HGEX40P0Z0]] is a Prüfer domain.

## Explanations

### L1 human

In a Dedekind domain, such as the ring of integers of a number field, every nonzero ideal can be "divided out": it has an inverse fractional ideal.
A Prüfer domain keeps this property for finitely generated ideals, without asking that every ideal be finitely generated.
Examples are $\Z$, every Dedekind domain, every valuation ring, and the ring of entire functions on $\C$.
The polynomial ring $\Z[x]$ is not Prüfer: its localization at the prime $(2, x)$ contains neither $2/x$ nor $x/2$, so it is not a valuation ring.
