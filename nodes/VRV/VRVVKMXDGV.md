---
tag: VRVVKMXDGV
kind: concept
name: Uniform integrability
msc: [28A25, 60A10]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_integrability
same_as:
  wikidata: Q1530275
  wikipedia: Uniform integrability
---

## Summary

A family of integrable functions is uniformly integrable when the part of each function above a large level carries uniformly little integral.
It prevents mass from escaping into tall spikes, in the same way for every member of the family.
On a finite measure space it is exactly the condition that upgrades convergence almost everywhere or in measure to convergence in $L^1$.
It plays a central role in probability, for instance in martingale convergence.

## Explanations

### L1 human

A single integrable function puts only a small part of its integral on the set where it is very large.
Uniform integrability asks this for a whole family at once, with the same threshold for all members.
For example, all functions bounded by the constant $1$ on $[0, 1]$ form a uniformly integrable family.
The spikes $n \mathbf{1}_{(0, 1/n)}$ do not, since each one puts all of its integral $1$ above the level $n - 1$.
