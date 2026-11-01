---
tag: 5K7VT2VKZT
kind: concept
name: Majorization
msc: [26D15, 15B51]
sources:
  - url: https://en.wikipedia.org/wiki/Majorization
same_as:
  wikidata: Q1994695
  wikipedia: Majorization
---

## Summary

Majorization compares two vectors of real numbers with the same sum by how spread out their entries are.
A vector $x$ majorizes $y$ when, for each $k$, the sum of the $k$ largest entries of $x$ is at least that of $y$.
Equivalently, $y$ is obtained from $x$ by a [[doubly stochastic matrix|JJA90EB2PS]], that is, by averaging.
It organises many inequalities, including the [[Schur–Horn theorem|Y553MSYDAH]] on diagonals and eigenvalues of Hermitian matrices.

## Explanations

### L1 human

Think of a fixed amount of money shared among $n$ people.
One sharing majorizes another when it is less equal: the richest person, the two richest people, and so on, always hold at least as much.
Moving an amount from a richer person to a poorer one, no larger than the gap between them, gives a sharing that is majorized by the old one.
For example, $(1, 0, 0)$ majorizes $(\frac{1}{2}, \frac{1}{2}, 0)$, which majorizes $(\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$.
