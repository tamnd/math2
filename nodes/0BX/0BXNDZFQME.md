---
tag: 0BXNDZFQME
kind: example
name: Cantor set
aliases: [cantor-ternary-set]
msc: [54F65]
instance_of: [0TVJZYB6SH, 0RJSBR9GW1]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_set
    locator: Construction and formula of the ternary set
  - url: https://en.wikipedia.org/wiki/Cantor_set
    locator: Topological and analytical properties
same_as:
  wikidata: Q273188
  wikipedia: Cantor set
---

## Example

Let $C_0 = [0, 1]$. For $n \ge 0$, let $C_{n+1}$ be the set that we get from $C_n$ when we remove the open middle third of each of its closed intervals. Thus $C_1 = [0, \tfrac{1}{3}] \cup [\tfrac{2}{3}, 1]$.
The Cantor set is $C = \bigcap_{n \ge 0} C_n$, with the subspace topology of $\mathbb{R}$.

## Remarks

Equivalently, $C$ is the set of $x \in [0, 1]$ that have a base-3 expansion $x = \sum_{n \ge 1} a_n 3^{-n}$ with all $a_n \in \{0, 2\}$.
The set $C$ is [[closed|01VT24J1SD]] and bounded, so it is [[compact|07PFYV65MB]]. It is [[totally disconnected|01CYW8S04D]] and has no isolated points.
It is uncountable, and it is [[homeomorphic to the space of binary sequences|0RQ8DHHR8V]]. Its Lebesgue measure is $0$, because $C_n$ has total length $(2/3)^n$.
The Cantor set is [[nowhere dense|0KSM23SN3H]] in $\mathbb{R}$.

## Explanations

### L1 human

Start with $[0, 1]$, remove the middle third, then remove the middle third of each piece that is left, and go on forever.
What remains is a set with no length, but with as many points as $\mathbb{R}$.
