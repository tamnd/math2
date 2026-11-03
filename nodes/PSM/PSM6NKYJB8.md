---
tag: PSM6NKYJB8
kind: concept
name: Greedy algorithm
msc: [68W40, 90C27]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Greedy_algorithm
same_as:
  wikidata: Q504353
  wikipedia: Greedy algorithm
---

## Summary

A greedy algorithm builds a solution step by step, at each step making the choice that looks best at that moment and never revising it.
Greedy algorithms are simple and fast, but they find an optimal solution only for problems with special structure.
For choosing a maximum-weight independent set, the greedy rule is optimal for every weight function exactly when the independent sets form a [[matroid|PX31ZNYS3Z]].
[[Kruskal's algorithm|5FPWTYFJRA]], [[Prim's algorithm|ZAKCAS4GC7]] and [[Dijkstra's algorithm|VZZMASEEC8]] are greedy.

## Explanations

### L1 human

Paying an amount with coins by always taking the largest coin that fits is a greedy method.
With coins $1$, $5$, $10$ and $25$ it gives the fewest coins: $30 = 25 + 5$.
With coins $1$, $3$ and $4$ it fails for $6$: greedy gives $4 + 1 + 1$, three coins, but $3 + 3$ uses two.
So being greedy is right for some problems and wrong for others, and a proof is always needed.
