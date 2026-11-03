---
tag: PTD7E1PKV4
kind: concept
name: BPP
msc: [68Q15, 68Q10, 68W20]
specializes: [ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/BPP_(complexity)
same_as:
  wikidata: Q796890
  wikipedia: BPP (complexity)
---

## Summary

BPP, for bounded-error probabilistic polynomial time, is a [[complexity class|ESPYW94XGR]] of decision problems.
A problem is in BPP when a polynomial-time [[probabilistic Turing machine|K99S0Q0814]] solves it with error probability at most $1/3$ on every input.
It is the usual formal notion of a problem that is efficiently solvable with randomness.
It contains [[P|GVT2NKN37K]], [[RP|TPDMV6ZXN3]] and [[ZPP|QJZ5ZY0HJ8]], and it lies in the second level of the [[polynomial hierarchy|TDQ7AXGM6P]].
Many researchers conjecture that $\mathrm{BPP} = \mathrm{P}$.

## Explanations

### L1 human

A BPP algorithm flips coins and may give a wrong answer, but on each input it is right at least two times out of three.
Running it many times and taking the majority answer makes the error tiny, smaller than the chance of a hardware fault.
For practical purposes, BPP problems are thus as easy as problems solvable in polynomial time.
A classical example is testing whether a polynomial given by an arithmetic formula is identically zero: plug in random values and see whether the result is zero.
