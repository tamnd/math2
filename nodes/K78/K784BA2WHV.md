---
tag: K784BA2WHV
kind: concept
name: Walsh–Hadamard transform
msc: [42C10, 65T50, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_transform
same_as:
  wikidata: Q1014065
  wikipedia: Hadamard transform
---

## Summary

The Walsh–Hadamard transform takes a vector of length $2^m$ to the vector of its correlations with all $\pm 1$ patterns given by a Sylvester [[Hadamard matrix|J0N4J606X0]].
It is the discrete Fourier transform of the group $(\Z/2\Z)^m$, and its rows are sampled [[Walsh functions|F12A5QKW8Z]].
A fast algorithm computes it with about $m 2^m$ additions and subtractions, and no multiplications.
It is used in signal processing, coding theory, the analysis of Boolean functions and quantum computing.

## Explanations

### L1 human

Take a list of $2^m$ numbers.
For each pattern of plus and minus signs from a fixed family of $2^m$ patterns, add up the numbers with those signs.
The resulting list of sums is the transform.
For $m = 1$ the patterns are $(+, +)$ and $(+, -)$, so $(a, b)$ goes to $(a + b, a - b)$.
Doing the same step on pairs, then on pairs of pairs, and so on, gives the whole transform quickly.
