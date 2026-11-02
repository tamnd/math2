---
tag: NFQ9FVCP31
kind: concept
name: Axiom of regularity
msc: ["03E30"]
uses: [0HE5WDQ9FJ, 0BSJ7RQ9BW, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_of_regularity
same_as:
  wikidata: Q470981
  wikipedia: Axiom of regularity
---

## Summary

The axiom of regularity, also called the axiom of foundation, is an axiom of [[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]].
It says that every nonempty [[set|0BSJ7RQ9BW]] has an element that shares no element with it.
In other words, the membership relation $\in$ is [[well-founded|0DQPNJNPYK]].
It rules out sets such as $x = \set{x}$, and it implies that every set appears at some stage of the cumulative hierarchy $V_\alpha$.

## Explanations

### L1 human

Think of building sets in stages: first the empty set, then sets of what you have, and so on.
Regularity says that every set is built this way, from the bottom up.
So no set can contain itself, and there is no endless chain $x_1 \ni x_2 \ni x_3 \ni \cdots$ going down.
For example, in the set $\set{\emptyset, \set{\emptyset}}$, the element $\emptyset$ has no element in common with the set.
The axiom is almost never used in ordinary mathematics, but it makes the universe of sets much easier to describe.
