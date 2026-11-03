---
tag: 2TSJFYVFS8
kind: concept
name: Analysis of algorithms
msc: [68W40, 68Q25]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_of_algorithms
same_as:
  wikidata: Q333464
  wikipedia: Analysis of algorithms
---

## Summary

The analysis of algorithms determines the resources, chiefly time and memory, that an [[algorithm|9DMSG5HAQX]] needs, as a function of the size of its input.
Results are usually stated up to constant factors with [[big O notation|0TGV80E6A4]], in the worst case or on average over a distribution of inputs.
It lets one compare algorithms independently of the machine and predict how they behave on large inputs.

## Explanations

### L1 human

Instead of timing a program with a stopwatch, count its basic steps, such as comparisons, as a function of the input size $n$.
Linear search through a list of $n$ items uses up to $n$ comparisons.
[[Binary search|V67H7YCQ17]] in a sorted list uses about $\log_2 n$.
For a list of a million items, that is a million steps against about twenty, whatever computer runs the code.
