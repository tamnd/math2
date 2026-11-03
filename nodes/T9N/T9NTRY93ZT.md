---
tag: T9NTRY93ZT
kind: concept
name: PSPACE
msc: [68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/PSPACE
same_as:
  wikidata: Q500716
  wikipedia: PSPACE
---

## Summary

PSPACE is the [[complexity class|ESPYW94XGR]] of decision problems that a deterministic Turing machine can solve with polynomial [[space|FDNFGKEEJR]].
It contains [[P|GVT2NKN37K]] and [[NP|QQRA9GBW51]], since a machine running in polynomial time can only use polynomial space.
Typical problems in PSPACE ask who wins a two-player game of polynomial length, or whether a quantified Boolean formula is true.
It is not known whether P or NP equals PSPACE.

## Explanations

### L1 human

PSPACE limits memory but not time.
Memory can be reused, so a machine may run for an exponentially long time while still using little space.
For example, a machine can try all $2^n$ assignments to $n$ variables one after the other, reusing the same $n$ cells.
So checking every assignment of a formula is in PSPACE, even though it may take a very long time.
