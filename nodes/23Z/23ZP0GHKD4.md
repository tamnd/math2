---
tag: 23ZP0GHKD4
kind: concept
name: Dinic's algorithm
msc: [90C35, 05C21, 05C85]
sources:
  - url: https://en.wikipedia.org/wiki/Dinic%27s_algorithm
same_as:
  wikidata: Q730933
  wikipedia: Dinic's algorithm
---

## Summary

Dinic's algorithm solves the [[maximum flow problem|EXMR7RYRTP]] in $O(\abs{V}^2 \abs{A})$ steps.
It was published by Yefim Dinitz in 1970.
In each phase it builds the level graph of shortest augmenting paths by [[breadth-first search|52XF4HS0X3]].
Then it pushes a blocking flow through this graph, which saturates all shortest paths at once.
On networks with unit capacities it is much faster, and on bipartite matching it gives the bound $O(\abs{A} \sqrt{\abs{V}})$ of the Hopcroft–Karp algorithm.

## Explanations

### L1 human

The Edmonds–Karp algorithm sends flow along one shortest path at a time.
Dinic's algorithm instead handles all shortest paths of the current length together.
It first labels each vertex by its distance from the source and keeps only edges that go one level forward.
Then it fills this layered network until every path from source to sink is blocked.
After each phase the shortest augmenting path becomes longer, so there are at most $\abs{V} - 1$ phases.
