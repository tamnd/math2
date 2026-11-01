---
tag: MNMJC8YVBS
kind: concept
name: Tightness of measures
msc: [60B10, 28A33]
sources:
  - url: https://en.wikipedia.org/wiki/Tightness_of_measures
same_as:
  wikidata: Q7801650
  wikipedia: Tightness of measures
---

## Summary

A family of [[probability measures|059TJN0NZ1]] on a topological space is tight if all of them live on one [[compact set|0R6EWFKRCF]] up to a small mass.
The mass left out can be made as small as one likes.
Tightness rules out mass escaping to infinity.
By Prokhorov's theorem, on a Polish space a family is tight if and only if every sequence in it has a weakly convergent subsequence.
So proofs of [[convergence in distribution|0SRYJGXKR4]] often have two steps: prove tightness, then identify the limit.

## Explanations

### L1 human

Think of each measure as a pile of sand of total mass $1$ spread on the line.
The family is tight if one fixed bounded interval holds almost all the sand of every pile, say all but $1\%$, and the same works for any small percentage.
The normal laws with means between $-1$ and $1$ form a tight family.
The point masses at $1, 2, 3, \dots$ do not: the sand runs off to infinity, and no single interval catches it.
