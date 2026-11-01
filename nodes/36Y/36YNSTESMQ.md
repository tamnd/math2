---
tag: 36YNSTESMQ
kind: concept
name: Selmer group
msc: [11G05, 11R34, 14H52]
sources:
  - url: https://en.wikipedia.org/wiki/Selmer_group
same_as:
  wikidata: Q7448760
  wikipedia: Selmer group
---

## Summary

The Selmer group of an isogeny of [[elliptic curves|427N6S6QQW]] over a [[number field|MWBDFS2KJ5]] is a group of [[Galois cohomology|9MPCZ3EAJM]] classes.
These classes satisfy local conditions at every place, and the group is finite and computable.
It contains a copy of the quotient $E'(K)/\phi(E(K))$, and the difference is the $\phi$-torsion of the [[Tate–Shafarevich group|BK9WBMF56G]].
Computing a Selmer group is the standard way to bound the rank of $E(K)$ from above.
It is the effective core of the proof of [[Mordell's theorem|BZHGKN6Q3K]].

## Explanations

### L1 human

To find all rational points of an elliptic curve, one would like to describe the points modulo doubles, $E(\Q)/2E(\Q)$.
This group sits inside a larger group of candidates that one can compute from local information, prime by prime.
That larger group is the $2$-Selmer group.
If it is as small as the known points allow, the rank is determined.
If it is larger, the extra candidates come from points not yet found or from elements of the Tate–Shafarevich group.
