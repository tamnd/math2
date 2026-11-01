---
tag: GWA0T1WKCN
kind: concept
name: Global dimension
msc: [13D05, "16E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Global_dimension
same_as:
  wikidata: Q5570832
  wikipedia: Global dimension
---

## Summary

The global dimension of a ring is the supremum of the [[projective dimensions|MR9QCH1PNA]] of all its modules.
It is $0$ for fields and $1$ for principal ideal domains that are not fields.
It is $n$ for a polynomial ring in $n$ variables over a field.
By [[Serre's theorem|93RQRG9R1P]], a Noetherian local ring has finite global dimension exactly when it is a [[regular local ring|63XXTF6B5M]].

## Explanations

### L1 human

The global dimension says how complicated the modules over a ring can be, in the worst case.
A ring of global dimension $0$ is one where every module is projective, as for vector spaces over a field.
Over the integers, every module has a resolution of length at most $1$, so the global dimension of $\Z$ is $1$.
Over $\Z/4\Z$, the module $\Z/2\Z$ needs an infinite resolution, so the global dimension is infinite.
