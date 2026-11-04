---
tag: F19XGQZKCG
kind: statement
role: theorem
name: On-line colouring of forests needs few vertices
msc: [05C15, 05C05, 68W27]
uses: [0874138YP6, 09JP6G9FTA]
about: [0NCPXH194Y]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_kitchensink_online.ptx#L24
    locator: source/s_kitchensink_online.ptx:24
---

## Statement

Two players build a graph in rounds.
In each round, Builder adds one new vertex and joins it to any chosen set of earlier vertices.
Then Assigner at once gives the new vertex a colour that differs from the colours of all its neighbours.
A colour is never changed later, and Assigner sees only the part of the graph built so far.
This is an on-line [[colouring|0874138YP6]].

Let $n$ be a positive integer.
Then Builder has a strategy such that the final graph is a [[forest|09JP6G9FTA]] with at most $2^{n-1}$ vertices, and Assigner is forced to use $n$ distinct colours, whatever Assigner does.

## Remarks

A forest is bipartite, so it has an off-line colouring with $2$ colours.
The theorem shows that an on-line Assigner can be forced to use arbitrarily many colours even on forests.
