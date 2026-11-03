---
tag: GVT2NKN37K
kind: concept
name: P
msc: [68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/P_(complexity)
same_as:
  wikidata: Q846354
  wikipedia: P (complexity)
---

## Summary

P is the [[complexity class|ESPYW94XGR]] of decision problems that a deterministic [[Turing machine|758EYCN27B]] can solve in polynomial time.
It is the usual formal model of the problems that are "efficiently solvable".
The class does not change if the Turing machine is replaced by any other reasonable deterministic model, such as a random-access machine.
Whether P equals NP is the central open question of complexity theory.

## Explanations

### L1 human

A problem is in P when some algorithm answers it in a number of steps bounded by a fixed power of the input length.
Doubling the input then multiplies this bound by only a fixed factor.
Sorting a list, finding shortest paths in a graph and testing whether a number is prime all belong to P, by known algorithms.
Problems whose best known algorithms try every possibility, such as testing all $2^n$ subsets of a set, are not known to be in $\mathrm{P}$.
