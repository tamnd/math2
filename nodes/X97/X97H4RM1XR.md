---
tag: X97H4RM1XR
kind: concept
name: Hardness of approximation
msc: [68Q17, 68W25]
sources:
  - url: https://en.wikipedia.org/wiki/Hardness_of_approximation
same_as:
  wikidata: Q5656275
  wikipedia: Hardness of approximation
---

## Summary

Hardness of approximation studies how well an NP-hard optimization problem can be approximated in polynomial time.
A result of this kind shows that an [[approximation algorithm|4WEVBDQ8SR]] with a given ratio would imply $\mathrm{P} = \mathrm{NP}$, or would refute another standard conjecture.
Together with algorithms, such results often pin down the best possible ratio exactly.
The main tool is the [[PCP theorem|WJXX7H6B6V]].

## Explanations

### L1 human

Many optimization problems are too hard to solve exactly in reasonable time.
One then asks for an answer that is close to the best one, say within a factor of two.
Hardness of approximation shows that for some problems even this is out of reach.
Take 3-SAT instances where each clause has exactly three different variables and all clauses can be satisfied at once.
A fast algorithm that always satisfies a fraction $7/8 + 0.01$ of the clauses would give a fast algorithm for every problem in NP.
Yet a random assignment already satisfies $7/8$ of the clauses on average, so the trivial method is essentially the best possible.
