---
tag: JGZWHWA8P8
kind: concept
name: NP-completeness
msc: [68Q17, 68Q15]
specializes: [MHA48AWBXN]
sources:
  - url: https://en.wikipedia.org/wiki/NP-completeness
same_as:
  wikidata: Q215206
  wikipedia: NP-completeness
---

## Summary

A decision problem is NP-complete when it lies in [[NP|QQRA9GBW51]] and is [[NP-hard|MHA48AWBXN]].
The NP-complete problems are the hardest problems in NP: a polynomial-time algorithm for any one of them gives polynomial-time algorithms for all of NP.
Thousands of natural problems are NP-complete, among them satisfiability, graph colouring, the Hamiltonian cycle problem and subset sum.
So P equals NP exactly when some NP-complete problem lies in $\mathrm{P}$.

## Explanations

### L1 human

NP-complete problems are puzzles whose solutions are easy to check, and which are as hard as any such puzzle.
Each one can stand in for all the others, since quick translations link them all.
So a fast method for one would solve them all, and nobody has found such a method.
For example, deciding whether a map can be coloured with three colours so that neighbouring countries differ is NP-complete.
When a problem turns out to be NP-complete, people usually stop looking for an exact fast algorithm and look for approximations instead.
