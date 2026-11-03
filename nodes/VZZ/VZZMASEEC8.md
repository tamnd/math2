---
tag: VZZMASEEC8
kind: concept
name: Dijkstra's algorithm
msc: [05C85, 68R10, 90C35]
specializes: [PSM6NKYJB8]
sources:
  - url: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
same_as:
  wikidata: Q8548
  wikipedia: Dijkstra's algorithm
---

## Summary

Dijkstra's algorithm computes the shortest-path [[distances|0QV9VNNB4Z]] from one source vertex to all other vertices of a graph whose edge weights are nonnegative.
It is a [[greedy algorithm|PSM6NKYJB8]]: it repeatedly settles the unsettled vertex with the smallest tentative distance and updates the tentative distances of its neighbours.
With a binary heap it runs in time $O((\abs{V} + \abs{E}) \log \abs{V})$.
It needs nonnegative weights; with negative weights one uses the [[Bellman–Ford algorithm|8AH0QN3D7Y]] instead.

## Explanations

### L1 human

Imagine water flowing out from the source along the roads at constant speed.
The water reaches the nearest town first, then the next nearest, and so on.
Dijkstra's algorithm simulates this: at each step it fixes the distance of the closest town not yet reached.
Then it checks whether going through that town gives shorter routes to its neighbours.
A satellite navigation system that finds the shortest driving route uses ideas of this kind.
