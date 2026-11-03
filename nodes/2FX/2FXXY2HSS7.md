---
tag: 2FXXY2HSS7
kind: concept
name: Computational complexity theory
msc: [68Q15, 68Q25, 03D15]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_complexity_theory
same_as:
  wikidata: Q205084
  wikipedia: Computational complexity theory
---

## Summary

Computational complexity theory studies how much of a resource, such as time or memory, is needed to solve a computational problem.
The amount is measured as a function of the size of the input.
It measures problems by the best algorithm for them, not by one particular algorithm.
Problems with similar needs are grouped into [[complexity classes|ESPYW94XGR]] such as [[P|GVT2NKN37K]] and [[NP|QQRA9GBW51]], which are compared by reductions.
Its central open question is the [[P versus NP problem|MFN5GYZH5Z]].

## Explanations

### L1 human

Computability theory asks whether a problem can be solved by a computer at all.
Complexity theory asks how hard it is: how many steps, or how much memory, the best possible program needs.
For example, sorting $n$ numbers can be done in about $n \log n$ comparisons, and no comparison-based method does better.
Some problems, like finding a shortest route through all of many cities, have no known fast method, and the theory tries to explain why.
The main measures are [[time complexity|T00W8RQT8E]] and [[space complexity|FDNFGKEEJR]].
