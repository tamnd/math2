---
tag: VSNQV29KFJ
kind: concept
name: Interval order
msc: [06A06, 91B08]
sources:
  - url: https://en.wikipedia.org/wiki/Interval_order
same_as:
  wikidata: Q6057290
  wikipedia: Interval order
---

## Summary

An interval order is a partial order whose elements can be drawn as [[intervals|0Q1D85B8G6]] of the real line.
One element is below another exactly when its interval lies entirely to the left.
Interval orders model events in time and preferences with a threshold of indifference.
A finite poset is an interval order exactly when it contains no copy of two incomparable two-element chains, a result of Fishburn.

## Explanations

### L1 human

Give each element a time slot, such as a meeting from $9$ to $10$ o'clock.
Say that one meeting comes before another when it ends before the other starts.
Overlapping meetings are then incomparable.
For the slots $a = [0, 1]$, $b = [2, 3]$ and $c = [0.5, 2.5]$, the only relation is $a < b$, while $c$ overlaps both.
