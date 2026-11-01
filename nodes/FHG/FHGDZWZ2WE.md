---
tag: FHGDZWZ2WE
kind: concept
name: Schreier–Sims algorithm
msc: [68W30, 20B05]
sources:
  - url: https://en.wikipedia.org/wiki/Schreier–Sims_algorithm
same_as:
  wikidata: Q7432874
  wikipedia: Schreier–Sims algorithm
---

## Summary

The Schreier–Sims algorithm takes a few permutations that generate a [[permutation group|ZDJQRKPWGA]] $G$ and computes a base and a strong generating set of $G$.
With this data one can find the [[order|0B85S2V2DR]] of $G$ and test whether a permutation belongs to $G$.
This takes time polynomial in the degree and the number of generators.
It is the basic algorithm of computational group theory, used in systems such as GAP and Magma.
It is named after Otto Schreier and Charles Sims.

## Explanations

### L1 human

A group of permutations of $n$ points can have far more elements than one could ever list, for example $n!$.
The Schreier–Sims algorithm avoids listing them.
It looks first at where the group can send point $1$, then at where the elements fixing point $1$ can send point $2$, and so on.
The order of the group is the product of the sizes of these sets of possible images.
For the six permutations of $\set{1, 2, 3}$: point $1$ can go to $3$ places, and then point $2$ can go to $2$ places, so the order is $3 \cdot 2 = 6$.
