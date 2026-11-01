---
tag: BQJ9ZX9P3V
kind: concept
name: Ramification group
msc: [11S15, 11S20]
specializes: [0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Ramification_group
same_as:
  wikidata: Q7289549
  wikipedia: Ramification group
---

## Summary

The ramification groups of a finite Galois extension of local fields form a decreasing chain of normal subgroups $G_0 \supseteq G_1 \supseteq G_2 \supseteq \cdots$ of its [[Galois group|0XTY86BZKY]].
The group $G_0$ is the inertia group, and $G_1$ is the wild inertia group.
The chain measures how deeply the extension is [[ramified|H5RC67SD24]].
It controls the different and the conductor of the extension.

## Explanations

### L1 human

An automorphism of a field extension moves elements of the ring of integers.
Some automorphisms move every integer only a little, in the sense of the valuation.
The group $G_i$ collects the automorphisms that move every integer by an amount divisible by the $(i+1)$-st power of a uniformizer.
The larger $i$ is, the closer to the identity these automorphisms are.
For the extension $\Q_2(i) / \Q_2$, complex conjugation lies in $G_0$ and $G_1$, but not in $G_2$.
