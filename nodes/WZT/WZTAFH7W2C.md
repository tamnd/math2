---
tag: WZTAFH7W2C
kind: concept
name: Shapley–Shubik power index
msc: [91B12, 91A12]
sources:
  - url: https://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index
same_as:
  wikidata: Q2915939
  wikipedia: Shapley–Shubik power index
---

## Summary

The Shapley–Shubik power index measures the voting power of each member of a committee that decides by a voting rule.
Voters join in a random order, and a voter is pivotal if her arrival turns a losing group into a winning one.
The index of a voter is the probability that she is pivotal.
It is the [[Shapley value|QVK36CXP03]] of the voting game, and Lloyd Shapley and Martin Shubik proposed it in 1954.

## Explanations

### L1 human

Imagine the voters lining up in a random order and announcing yes one after another.
The pivotal voter is the one whose yes first makes the group large enough to win.
A voter's power is the chance of being the pivotal voter.
With three parties of $2$, $1$ and $1$ seats and a quota of $3$, the big party is pivotal in $4$ of the $6$ orders, so its power is $2/3$.
