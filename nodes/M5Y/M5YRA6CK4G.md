---
tag: M5YRA6CK4G
kind: concept
name: Hölder summation
msc: ["40G05"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Hölder_summation
same_as:
  wikidata: Q15694035
  wikipedia: Hölder summation
---

## Summary

Hölder summation is a [[summability method|8X25Q4XYMN]] that averages the partial sums of a series, then averages these averages.
It repeats the averaging a fixed number $k$ of times.
For $k = 1$ it is [[Cesàro summation|N8ZGG7EW6J]] of order $1$.
For each $k$, the Hölder method of order $k$ sums the same series to the same values as the Cesàro method of order $k$.
Repeated averaging can tame series whose partial sums oscillate with growing size.

## Explanations

### L1 human

One round of averaging turns the running totals $1, 0, 1, 0, \dots$ of $1 - 1 + 1 - \cdots$ into a sequence that tends to $1/2$.
Some series need more rounds.
For $1 - 2 + 3 - 4 + \cdots$, one round of averaging gives a sequence that still jumps between about $1/2$ and $0$.
A second round averages this out and gives $1/4$.
Hölder summation of order $k$ simply means $k$ rounds of averaging.
