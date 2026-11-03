---
tag: MHA48AWBXN
kind: concept
name: NP-hardness
msc: [68Q17, 68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/NP-hardness
same_as:
  wikidata: Q1137554
  wikipedia: NP-hardness
---

## Summary

A problem is NP-hard when every problem in [[NP|QQRA9GBW51]] reduces to it by a [[polynomial-time reduction|V0K79AD81V]].
An NP-hard problem is at least as hard as every problem in NP.
A polynomial-time algorithm for one NP-hard problem would give one for all of NP, and so would prove that P equals NP.
NP-hard problems need not lie in NP; some, such as the halting problem, are not even decidable.

## Explanations

### L1 human

Call a problem NP-hard when a fast method for it would at once give fast methods for every problem in NP.
Such a problem is a universal target: every NP problem can be translated into it quickly.
The travelling salesman problem, asking for a shortest tour through given cities, is a standard example.
NP-hardness is a lower bound on difficulty, and it says nothing about an upper bound.
