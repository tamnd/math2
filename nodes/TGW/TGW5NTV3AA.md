---
tag: TGW5NTV3AA
kind: definition
name: Down-closure
msc: [06A06]
defines: 839P1ZNRD7
uses: [011C29Q1S1, BWYFKCWRW5]
sources:
  - url: https://en.wikipedia.org/wiki/Upper_and_lower_sets
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]] and let $S \subseteq P$.
The *down-closure* of $S$ is the set
$$\downarrow S = \set{x \in P : x \le s \text{ for some } s \in S}.$$
For $x \in P$, the set $\downarrow x = \downarrow \set{x} = \set{y \in P : y \le x}$ is the *principal down-set* of $x$.

## Remarks

In the subsets of $\set{1, 2, 3}$ ordered by inclusion, $\downarrow \set{\set{1, 2}, \set{3}} = \set{\emptyset, \set{1}, \set{2}, \set{1, 2}, \set{3}}$.
Each listed set is contained in $\set{1, 2}$ or in $\set{3}$, and no other subset is.
The set $\downarrow S$ is a [[lower set|BWYFKCWRW5]] that contains $S$, and it lies inside each lower set that contains $S$.
So $S$ is a lower set if and only if $\downarrow S = S$.
The map $S \mapsto \downarrow S$ is a [[closure operator|17FVAN6HXX]] on the subsets of $P$.
Dually, the up-closure is $\uparrow S = \set{x \in P : s \le x \text{ for some } s \in S}$.

## Explanations

### L1 human

The down-closure fills in everything below the given elements.
It turns any subset into a lower set in the most economical way.
