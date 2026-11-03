---
tag: 8AH0QN3D7Y
kind: concept
name: Bellman–Ford algorithm
msc: [05C85, 90C35, 68W40]
specializes: [R3FXF08WBH]
sources:
  - url: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
same_as:
  wikidata: Q816022
  wikipedia: Bellman–Ford algorithm
---

## Summary

The Bellman–Ford algorithm computes the lengths of shortest paths from one source vertex to all other vertices of a weighted [[directed graph|0KFYGSHHF5]].
Unlike [[Dijkstra's algorithm|VZZMASEEC8]], it allows negative edge weights.
It also detects a cycle of negative total weight that can be reached from the source, in which case shortest paths do not exist.
On a graph with $n$ vertices and $m$ edges it runs in time $O(nm)$.

## Explanations

### L1 human

Each vertex keeps a current guess of its distance from the source, starting at $0$ for the source and $\infty$ for the others.
The algorithm looks at every edge again and again and lowers a guess whenever a shorter route through that edge appears.
A shortest path without repeated vertices has at most $n - 1$ edges, so $n - 1$ rounds over all edges are enough.
For example, with edges $s \to a$ of weight $4$, $s \to b$ of weight $1$ and $b \to a$ of weight $2$, the guess for $a$ drops from $4$ to $3$.
If a further round still lowers some guess, there is a negative cycle.
