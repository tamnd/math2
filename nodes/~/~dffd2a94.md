---
tag: ~dffd2a94
kind: statement
role: theorem
name: Edge bound for planar graphs
msc: [05C10]
uses: [~04906f4a]
sources:
  - url: https://en.wikipedia.org/wiki/Planar_graph
    locator: "Euler's formula"
---

## Statement

Let $G$ be a finite simple connected [[planar graph|~276b1882]] with $v \ge 3$ vertices and $e$ edges.
Then $e \le 3v - 6$.

## Remarks

Proof idea: each face is bounded by at least $3$ edges, and each edge touches at most $2$ faces. Thus $3f \le 2e$, and [[Euler's formula|~04906f4a]] gives the bound.
If $G$ also has no cycle of length $3$, then $e \le 2v - 4$.
A consequence: each finite simple planar graph has a vertex of [[degree|~939465ed]] at most $5$.

## Explanations

### L1 human

A planar graph cannot have too many edges: at most about three times its number of vertices.
This simple count already shows that some graphs, such as $K_5$, are not planar.
