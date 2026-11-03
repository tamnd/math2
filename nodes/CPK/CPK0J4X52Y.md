---
tag: CPK0J4X52Y
kind: concept
name: Amortized analysis
msc: [68W40, 68P05]
specializes: [2TSJFYVFS8]
sources:
  - url: https://en.wikipedia.org/wiki/Amortized_analysis
same_as:
  wikidata: Q331716
  wikipedia: Amortized analysis
---

## Summary

Amortized analysis bounds the total cost of a sequence of operations on a data structure, rather than the cost of each operation alone.
An occasional expensive operation is paid for by many cheap ones.
So the worst-case average cost per operation over a sequence can be much smaller than the worst single cost.
The main techniques are the aggregate method, the accounting method and the potential method.

## Explanations

### L1 human

A growable array doubles its storage when it is full, and copying all elements is expensive.
But after a doubling to size $2m$, the next $m$ insertions are cheap, so the expensive copy happens rarely.
Spreading the copy cost over those insertions shows that each insertion costs only a constant on average.
Unlike an average-case analysis, no randomness is assumed: the bound holds for every sequence of operations.
