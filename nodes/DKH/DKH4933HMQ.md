---
tag: DKH4933HMQ
kind: concept
name: Dedekind–MacNeille completion
msc: [06B23, 06A06]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind%E2%80%93MacNeille_completion
same_as:
  wikidata: Q5249756
  wikipedia: Dedekind–MacNeille completion
---

## Summary

The Dedekind–MacNeille completion of a partially ordered set is the smallest [[complete lattice|D7A0ZGZT5S]] that contains it as an ordered subset.
It is built from cuts, pairs of sets of lower and upper bounds.
The real numbers are built in the same way from [[Dedekind cuts|0G3RRM41X9]] of the rationals.
Every existing supremum and infimum of the original poset is kept in the completion.

## Explanations

### L1 human

The rational numbers have gaps, such as the place where $\sqrt{2}$ should be.
Dedekind filled these gaps by describing each missing number by the rationals below it.
MacNeille did the same for any ordered set: each new element is a set of elements that is exactly the set of lower bounds of its own upper bounds.
For the rationals, the completion is the real line with $-\infty$ and $+\infty$ added.
For a finite lattice nothing new is added, because it is already complete.
