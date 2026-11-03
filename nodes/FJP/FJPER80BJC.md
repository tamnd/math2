---
tag: FJPER80BJC
kind: concept
name: Combinatorial optimization
msc: [90C27]
specializes: [NS0Q42Y3FX]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_optimization
same_as:
  wikidata: Q1333872
  wikipedia: Combinatorial optimization
---

## Summary

Combinatorial optimization is the search for a best element of a finite but usually huge set of discrete objects.
The objects are paths, trees, matchings, tours, schedules and the like.
Typical problems are the [[shortest path problem|WE864PFF2M]], minimum spanning trees, the [[assignment problem|K65YS73SBW]], [[maximum flow|EXMR7RYRTP]], the [[knapsack problem|6G8WNXTJAN]] and the travelling salesman problem.
Some of these have polynomial-time algorithms, often explained by [[polyhedral combinatorics|DKNC3NS0YH]] and linear programming duality.
Others are [[NP-hard|MHA48AWBXN]] and are attacked by [[integer programming|9GX3WH5EQF]], approximation algorithms and heuristics.
The field lies between graph theory, algorithms and mathematical programming, and it is central to [[operations research|PSE3NRBXKY]].

## Explanations

### L1 human

A delivery driver must visit $20$ addresses and wants the shortest round trip.
There are finitely many orders in which to visit them, so in principle one could try them all, but there are more than $10^{17}$ of them.
Combinatorial optimization studies how to find the best choice among such enormous but finite collections without checking every option.
For some problems, such as finding the shortest route between two places, fast exact methods exist; for others, such as the round trip, no fast method is known.
