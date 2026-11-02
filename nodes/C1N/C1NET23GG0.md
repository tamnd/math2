---
tag: C1NET23GG0
kind: concept
name: Semimodular lattice
msc: [06C10, 06B05]
specializes: [WH4SFAACAS]
sources:
  - url: https://en.wikipedia.org/wiki/Semimodular_lattice
same_as:
  wikidata: Q1748671
  wikipedia: Semimodular lattice
---

## Summary

A semimodular lattice is a [[lattice|WH4SFAACAS]] in which joining with an element preserves the covering relation: if $a$ covers $a \wedge b$, then $a \vee b$ covers $b$.
It is a one-sided weakening of the [[modular law|QX7WZ92QAK]], and every modular lattice is semimodular.
Lattices of flats of [[matroids|PX31ZNYS3Z]] and lattices of partitions of a set are semimodular without being modular in general.
In lattices of finite length, semimodularity is what makes a well-behaved rank function exist.

## Explanations

### L1 human

Think of the elements of a lattice as subspaces and of a cover as a step up by one dimension.
Semimodularity says: if $a$ is one step above $a \wedge b$, then adding $a$ to $b$ moves $b$ up by at most one step, and in fact by exactly one.
So "one more generator" never gives more than "one more dimension".
In the lattice of partitions of a set, merging two blocks is one step up, and this rule holds there too.
