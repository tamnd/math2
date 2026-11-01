---
tag: JJA90EB2PS
kind: concept
name: Doubly stochastic matrix
msc: [15B51]
specializes: [JPQCCFCY8X]
sources:
  - url: https://en.wikipedia.org/wiki/Doubly_stochastic_matrix
same_as:
  wikidata: Q1243340
  wikipedia: Doubly stochastic matrix
---

## Summary

A doubly stochastic matrix is a square [[nonnegative matrix|JPQCCFCY8X]] in which every row and every column sums to $1$.
[[Permutation matrices|08SP3DF8NB]] are doubly stochastic, and by the [[Birkhoff–von Neumann theorem|3KY1RMEDMJ]] every doubly stochastic matrix is a convex combination of them.
These matrices describe averaging processes and appear in [[majorization|5K7VT2VKZT]], assignment problems and Markov chains with a uniform stationary distribution.

## Explanations

### L1 human

Imagine $n$ glasses of water and a rule that pours fixed fractions of each glass into the others.
Suppose that no water is lost, and that glasses which start equally full stay equally full.
Then the table of fractions is doubly stochastic.
Each row and each column of the table adds up to $1$.
For example, $\frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ mixes two glasses evenly.
