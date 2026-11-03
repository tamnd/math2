---
tag: DZBM27VRAF
kind: concept
name: Bass stable range
msc: [19B10, 19A13]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_range_condition
same_as:
  wikidata: Q18192482
  wikipedia: Stable range condition
---

## Summary

The stable range condition of Hyman Bass is a condition on a ring that lets one shorten unimodular rows by elementary operations.
The least $n$ for which it holds is the stable rank of the ring.
It controls stability results in K-theory.
Above the stable rank, projective modules can be cancelled, as in the [[Bass cancellation theorem|2NEKYG83WZ]].
It also gives surjective stability for $K_1$: every element of $K_1(R)$ comes from $GL_n(R)$ once $n$ is at least the stable rank.
A commutative Noetherian ring of Krull dimension $d$ has stable rank at most $d + 1$.

## Explanations

### L1 human

A row of ring elements is unimodular if some combination of its entries equals $1$, like the row $(2, 5)$ of integers.
The stable range condition says that a long unimodular row can be shortened: add multiples of the last entry to the others, and the first entries alone are already unimodular.
Over a field, a row of length two can always be shortened to one invertible element.
Over the integers this fails for $(2, 5)$ but works for every row of length three.
The smaller the stable rank, the closer the ring behaves to a field in linear algebra.
