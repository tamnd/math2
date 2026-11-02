---
tag: TDZVCWYJ9F
kind: concept
name: Functional completeness
msc: [08A40, "06E30", 03B50]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
---

## Summary

A set of operations on a finite set $A$ is functionally complete if every finitary operation on $A$ can be built from it by composition.
In other words, the [[clone|PTKR703G6A]] it generates is the clone of all operations.
For $A = \set{0, 1}$ this is the familiar notion for sets of [[logical connectives|QS0XVAN9BG]], such as $\set{\wedge, \neg}$.
Criteria for functional completeness are given by [[Post's lattice|MA20X7JCET]] in the two-valued case and by maximal clones in general.

## Explanations

### L1 human

A set of logic gates is functionally complete if every truth table can be realised by a circuit built from those gates.
For example, AND and NOT suffice: OR can be written as $x \vee y = \neg(\neg x \wedge \neg y)$, and every truth table has a disjunctive normal form.
AND and OR together do not suffice, because they can never turn an input of all ones into a zero.
