---
tag: BAADB7WHWZ
kind: concept
name: Sidon set
msc: [11B83, 11B13, 05B10]
sources:
  - url: https://en.wikipedia.org/wiki/Sidon_sequence
same_as:
  wikidata: Q748968
  wikipedia: Sidon sequence
---

## Summary

A Sidon set is a set of integers, or of elements of an abelian group, in which all sums of two elements are different.
Here sums that differ only in the order of the summands count as the same.
For sets of integers this is the same as saying that all differences of two distinct elements are different.
Sidon sets are the extreme opposite of sets with additive structure: their [[additive energy|MAQKH72P6V]] is as small as possible.
The largest Sidon subset of $\set{1, \dots, N}$ has size asymptotic to $\sqrt{N}$.

## Explanations

### L1 human

Pick numbers so that no two pairs of them have the same sum.
The powers of two $1, 2, 4, 8, 16$ work, because binary expansions show each sum of two of them only once.
Such sets cannot be very dense: among the numbers up to $N$, a Sidon set has only on the order of $\sqrt{N}$ elements.
The reason is that its roughly $n^2/2$ pairwise sums must all be different and at most $2N$.
