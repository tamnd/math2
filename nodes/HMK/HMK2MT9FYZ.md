---
tag: HMK2MT9FYZ
kind: concept
name: Topological sorting
msc: [05C85, 05C20, 06A06]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_sorting
same_as:
  wikidata: Q753127
  wikipedia: Topological sorting
---

## Summary

A topological sorting of a [[directed graph|0KFYGSHHF5]] lists its vertices so that every edge points from an earlier vertex to a later one.
It exists exactly when the graph has no directed cycle.
It is the first step of many algorithms on directed acyclic graphs, such as scheduling tasks with precedence constraints.
It can be computed in linear time, for instance by [[depth-first search|4TE2X7N728]].

## Explanations

### L1 human

Imagine getting dressed: socks must go on before shoes, and a shirt before a tie.
Draw an arrow from each item to every item that must come after it.
A topological sorting is an order of all items that never breaks an arrow.
For the arrows socks $\to$ shoes and shirt $\to$ tie, the order shirt, socks, tie, shoes works, and so does socks, shirt, shoes, tie.
If the arrows went in a circle, no such order could exist.
