---
tag: MAQKH72P6V
kind: concept
name: Additive energy
msc: [11B30, 11P70]
sources:
  - url: https://en.wikipedia.org/wiki/Additive_combinatorics
---

## Summary

The additive energy of two finite sets $A$ and $B$ in an abelian group counts the quadruples $(a_1, a_2, b_1, b_2)$ with $a_1 + b_1 = a_2 + b_2$.
It measures how often sums repeat, so it is large when the [[sumset|XNBN31HQWB]] $A + B$ is small.
It is a more robust measure of additive structure than the size of the sumset.
The [[Balog–Szemerédi–Gowers theorem|W5BZZ59CVM]] turns large energy into a small sumset for large subsets.

## Explanations

### L1 human

Add each element of $A$ to each element of $B$ and look for coincidences among the sums.
The additive energy counts these coincidences, including trivial ones.
For an arithmetic progression many sums coincide, so the energy is large.
For a set like $\set{1, 2, 4, 8}$, almost all sums are different, so the energy is as small as possible.
