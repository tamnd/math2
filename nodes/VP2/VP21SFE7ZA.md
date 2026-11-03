---
tag: VP21SFE7ZA
kind: concept
name: Quantum complexity class BQP
msc: [68Q12, 68Q15, 81P68]
sources:
  - url: https://en.wikipedia.org/wiki/BQP
same_as:
  wikidata: Q601325
  wikipedia: BQP
---

## Summary

BQP, for bounded-error quantum polynomial time, is a [[complexity class|ESPYW94XGR]] of decision problems.
It contains the problems that a quantum computer solves in polynomial time with error probability at most $1/3$.
It is the quantum analogue of [[BPP|PTD7E1PKV4]].
It contains BPP and is contained in PSPACE.
Integer factorization, in its decision form, lies in BQP by [[Shor's algorithm|83G4EPJ3EJ]], while no classical polynomial-time algorithm for it is known.

## Explanations

### L1 human

A quantum computer manipulates superpositions of many bit strings at once, and at the end it measures and gets a random answer.
BQP collects the yes-or-no questions it can answer quickly, if we only ask that the answer be right with probability at least $2/3$.
Repeating the computation and taking a majority vote makes the error as small as we like.
Every problem that an ordinary randomized computer solves quickly is in BQP.
Whether BQP is strictly larger than BPP is unknown, but factoring large numbers is a candidate.
