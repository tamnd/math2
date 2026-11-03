---
tag: 5HWR2NK8N1
kind: concept
name: co-NP
msc: [68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/Co-NP
same_as:
  wikidata: Q955748
  wikipedia: Co-NP
---

## Summary

co-NP is the [[complexity class|ESPYW94XGR]] of decision problems whose complement lies in [[NP|QQRA9GBW51]].
For these problems, the "no" answers have short certificates that can be checked in polynomial time.
The set of propositional tautologies is a typical member.
It is an open question whether co-NP equals NP; if they differ, then P differs from NP as well.

## Explanations

### L1 human

NP collects questions where a "yes" can be proved quickly, for example by showing a solution.
co-NP collects questions where a "no" can be proved quickly.
To show that a formula is not always true, it is enough to give one assignment that makes it false.
So "is this formula always true?" is in co-NP.
Nobody knows a short proof that a formula is always true, which is why this question is not known to be in NP.
