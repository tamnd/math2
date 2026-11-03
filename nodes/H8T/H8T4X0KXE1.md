---
tag: H8T4X0KXE1
kind: concept
name: Floyd–Warshall algorithm
msc: [05C85, 90C35, 68W40]
specializes: [R3FXF08WBH]
sources:
  - url: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
same_as:
  wikidata: Q1047576
  wikipedia: Floyd–Warshall algorithm
---

## Summary

The Floyd–Warshall algorithm computes the shortest path lengths between all pairs of vertices of a weighted [[directed graph|0KFYGSHHF5]].
It is a [[dynamic programming|R3FXF08WBH]] method that allows the vertices $1, \dots, k$ as intermediate stops, one more at each stage.
It accepts negative edge weights as long as there is no negative cycle, and it runs in time $O(n^3)$ on $n$ vertices.

## Explanations

### L1 human

Number the cities $1$ to $n$ and keep a table of the best known travel cost between every pair.
At stage $k$, ask for every pair $(i, j)$ whether going through city $k$ is cheaper than the current best route.
If it is, write the cheaper cost into the table.
After all $n$ stages, every route may pass through any city, so the table holds the true shortest distances.
For example, if the direct road from $1$ to $3$ costs $10$ but $1 \to 2$ costs $3$ and $2 \to 3$ costs $4$, stage $2$ lowers the entry for $(1, 3)$ to $7$.
