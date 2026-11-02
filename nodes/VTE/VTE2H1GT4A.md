---
tag: VTE2H1GT4A
kind: example
name: Cantor algebra
msc: ["06E05", 08A99, 03G05]
instance_of: [0XADJKM699]
uses: [W9VYJRBF9N, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_algebra
same_as:
  wikidata: Q18386550
  wikipedia: Cantor algebra
---

## Example

Let $C = \set{0, 1}^{\N}$ be the [[Cantor space|W9VYJRBF9N]] of infinite binary sequences, with the product topology.
The *countable Cantor algebra* is the [[Boolean algebra|0XADJKM699]] of all clopen subsets of $C$, with union, intersection and complement in $C$.

For a finite binary word $w$, let $[w]$ be the set of sequences that begin with $w$.
Each set $[w]$ is clopen, and every clopen subset of $C$ is a finite union of such sets, by compactness of $C$.

Check the main properties.

1. It is [[countable|01TQB88H4C]]. There are countably many finite words, hence countably many finite unions of sets $[w]$.
2. It has no atoms. A nonempty clopen set contains some $[w]$. The set $[w]$ is the disjoint union of the nonempty sets $[w0]$ and $[w1]$, so it is not minimal.
3. It is free on the generators $G_n = \set{s \in C : s_n = 1}$ for $n \in \N$. Each $[w]$ is an intersection of finitely many sets $G_n$ and complements of sets $G_n$, so these sets generate the algebra. Any such intersection over distinct indices $n$ is nonempty. So no nontrivial Boolean relation holds among the $G_n$.

## Remarks

Up to isomorphism, the countable Cantor algebra is the only countable atomless Boolean algebra with more than one element.
The name Cantor algebra is also used for its completion, the *complete Cantor algebra*.
The completion is isomorphic to the algebra of Borel subsets of $\R$ modulo meagre sets.
A finite Boolean algebra with more than one element always has atoms, so it is a non-example of an atomless algebra.

## Explanations

### L1 human

Think of an infinite sequence of coin tosses.
A clopen set is an event that can always be decided after a fixed finite number of tosses, such as "the first two tosses are heads".
These events form a Boolean algebra under "or", "and" and "not".
Every nonempty event can be split into two smaller nonempty events by looking at one more toss, so there is no smallest event.
The events "toss $n$ is heads" are independent generators, and every event is built from finitely many of them.
