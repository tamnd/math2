---
tag: 8QA5DEWNYD
kind: concept
name: Total variation
msc: [26A45]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation
same_as:
  wikidata: Q1936288
  wikipedia: Total variation
---

## Summary

The total variation of a real function on an interval measures how much its values change in total, counting each rise and each fall.
It is the supremum of the sums of the absolute changes over all partitions of the interval.
A function has [[bounded variation|A8251BHCMP]] exactly when its total variation is finite.
The same idea gives the total variation of a signed measure and of functions of several variables.

## Explanations

### L1 human

Think of the graph of a function as a mountain path and measure only the height you climb plus the height you descend.
The total variation is this sum of heights.
For $f(x) = \sin x$ on $[0, 2\pi]$ you go up by $1$, down by $2$, and up by $1$, so the total variation is $4$.
For a monotone function the total variation is just the difference between the end values.
