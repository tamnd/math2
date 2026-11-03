---
tag: MM4XQXEQQG
kind: concept
name: Costas array
msc: [05B20, 94A55, 05B15]
sources:
  - url: https://en.wikipedia.org/wiki/Costas_array
same_as:
  wikidata: Q2114132
  wikipedia: Costas array
---

## Summary

A Costas array is an $n \times n$ [[permutation matrix|08SP3DF8NB]] in which the vectors joining pairs of its ones are all different.
Equivalently, no two pairs of dots are related by a translation.
Costas arrays describe frequency-hopping patterns whose shifted copies, in both time and frequency, overlap in at most one point.
This is what radar and sonar need.
Algebraic constructions over finite fields, due to Welch and to Lempel and Golomb, give Costas arrays of many orders.
It is not known whether they exist for every $n$.
See the [[definition|ZBE13GJ90N]].

## Explanations

### L1 human

Place $n$ dots on an $n \times n$ grid, one in each row and one in each column, like rooks that do not attack each other.
Now draw an arrow from each dot to each other dot.
The arrangement is a Costas array when no two arrows have the same length and direction.
Then sliding a copy of the pattern in any direction other than not at all makes at most one dot land on a dot.
For example, the dots at $(1, 1)$, $(2, 3)$, $(3, 2)$ form a Costas array of order $3$.
