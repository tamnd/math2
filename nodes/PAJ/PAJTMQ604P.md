---
tag: PAJTMQ604P
kind: concept
name: Combinatorial design
msc: [05B05, 05B30]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_design
same_as:
  wikidata: Q5150824
  wikipedia: Combinatorial design
---

## Summary

A combinatorial design is a finite set together with a family of subsets, called blocks, that satisfies a balance condition.
A typical condition is that every pair of points lies in the same number of blocks.
Design theory studies when such systems exist and how to build them.
The main families include [[block designs|4JCSS2Z1BA]], [[Steiner systems|7BPSC4T4M3]], [[finite projective planes|2HWB7P1DZN]] and, in a wider sense, [[Latin squares|CDVRMVED2V]].
Designs are used in the planning of experiments, in coding theory and in finite geometry.

## Explanations

### L1 human

Suppose you want to test $7$ products in groups of $3$ so that every two products are compared in exactly one group.
This is possible with $7$ groups: $\set{1,2,4}$, $\set{2,3,5}$, $\set{3,4,6}$, $\set{4,5,7}$, $\set{5,6,1}$, $\set{6,7,2}$, $\set{7,1,3}$.
Such a fair arrangement is a combinatorial design; this one is the Fano plane.
