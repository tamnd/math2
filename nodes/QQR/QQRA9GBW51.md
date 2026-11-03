---
tag: QQRA9GBW51
kind: concept
name: NP
msc: [68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/NP_(complexity)
same_as:
  wikidata: Q628036
  wikipedia: NP (complexity)
---

## Summary

NP is the [[complexity class|ESPYW94XGR]] of decision problems whose "yes" answers can be checked in polynomial time with the help of a suitable certificate.
Equivalently, it is the class of problems that a [[nondeterministic Turing machine|M7SDX137WE]] solves in polynomial time.
It contains [[P|GVT2NKN37K]] and many problems of practical interest, such as satisfiability, graph colouring and scheduling.
Whether NP equals P is the central open question of complexity theory.

## Explanations

### L1 human

Some puzzles are hard to solve but easy to check.
Given a filled-in Sudoku grid, anyone can quickly check that it is correct, even if finding the solution took hours.
NP is the class of yes-or-no questions with this property: when the answer is yes, there is a short proof, and checking the proof is fast.
For example, "does this number have a factor between $2$ and $m$?" is in NP, since a factor is a proof that one can check by a single division.
