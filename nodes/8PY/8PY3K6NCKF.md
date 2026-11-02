---
tag: 8PY3K6NCKF
kind: concept
name: Kolmogorov complexity
msc: [68Q30, 03D32]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_complexity
same_as:
  wikidata: Q1456811
  wikipedia: Kolmogorov complexity
---

## Summary

The Kolmogorov complexity of a finite string is the length of a shortest program that prints the string.
It measures how much information the string contains, or how far it can be compressed.
By the invariance theorem the choice of programming language changes the complexity only by a bounded amount.
It is the basis of algorithmic information theory and of [[algorithmic randomness|KW3V44GPPC]].

## Explanations

### L1 human

A string like $0101010101\ldots01$ with a million digits has a short description: "print $01$ half a million times".
A string of a million coin flips usually has no description much shorter than the string itself.
Kolmogorov complexity makes this precise: it is the length of the shortest program that outputs the string.
Simple, patterned strings have low complexity, and typical random strings have complexity close to their length.
