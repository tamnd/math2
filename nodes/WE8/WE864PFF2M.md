---
tag: WE864PFF2M
kind: problem
name: Shortest path problem
msc: [90C35, 05C38, 05C85]
uses: [0KFYGSHHF5, 03NAMV1DHJ, 0Z05VCBQ7Y]
about: [03NAMV1DHJ]
sources:
  - url: https://en.wikipedia.org/wiki/Shortest_path_problem
same_as:
  wikidata: Q1058754
  wikipedia: Shortest path problem
history:
  posed_by: "unknown; early algorithms were given in the 1950s by Shimbel, Ford, Bellman, Moore and Dijkstra"
  first_stated: "unknown"
---

## Problem

Let $(V, E)$ be a finite [[directed graph|0KFYGSHHF5]] with a weight $w(e) \in \R$ on each edge $e$, and let $s, t \in V$.
The weight of a directed [[path|03NAMV1DHJ]] is the sum of the weights of its edges.
Assume that no directed [[cycle|0Z05VCBQ7Y]] reachable from $s$ has negative total weight.
Find a directed path from $s$ to $t$ of least weight, or report that $t$ is not reachable from $s$.

## Remarks

The single-source version asks for shortest paths from $s$ to all vertices, and the all-pairs version for all pairs.
Shortest paths from $s$ can be chosen to form a tree, because a subpath of a shortest path is again shortest.
For nonnegative weights, [[Dijkstra's algorithm|VZZMASEEC8]] solves the single-source version.
For arbitrary weights without negative cycles, the [[Bellman–Ford algorithm|8AH0QN3D7Y]] solves it in $O(\abs{V}\abs{E})$ time and detects negative cycles.
In an [[acyclic|0SXHBTNM9T]] graph, one pass in [[topological order|HMK2MT9FYZ]] suffices, and [[Floyd–Warshall|H8T4X0KXE1]] handles all pairs.

The hypothesis on cycles matters.
If a negative cycle is reachable from $s$ and can reach $t$, then paths that repeat it have weight tending to $-\infty$.
Asking instead for a lightest simple path is then [[NP-hard|MHA48AWBXN]], since it contains the Hamiltonian path problem.

Example: with edges $s \to a$ of weight $1$, $a \to t$ of weight $1$ and $s \to t$ of weight $3$, the shortest path is $s \to a \to t$ of weight $2$.
It is also a special case of the [[minimum-cost flow problem|899795HN7H]] with one unit of flow.

## Explanations

### L1 human

A shortest path is the cheapest route between two places in a network of one-way roads, where each road has a length or a cost.
Route planners, network routing and many planning problems solve it millions of times a day.
The main trap is a loop of negative cost, which would let one go round forever and gain without limit.
