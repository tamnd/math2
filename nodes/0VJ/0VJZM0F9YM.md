---
tag: 0VJZM0F9YM
kind: definition
name: Walk
msc: [05C38]
defines: 085CH3CYMX
uses: [0JD5C82QMB]
sources:
  - url: https://en.wikipedia.org/wiki/Path_(graph_theory)
    locator: Walk, trail, and path
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]], let $k$ be a natural number, and let $u, v$ be vertices of $G$.
A walk of length $k$ from $u$ to $v$ is a sequence of vertices $(w_0, w_1, \dots, w_k)$ with $w_0 = u$, $w_k = v$, and $w_{i-1} \sim w_i$ for $1 \le i \le k$.
Its edges are the edges $w_{i-1} w_i$.

## Remarks

A walk may repeat vertices and edges. A walk of length $0$ is a single vertex.
A [[trail|062MQGP8M5]] has no repeated edge, and a [[path|0JDE56HWQ8]] has no repeated vertex.
A walk is closed if $u = v$.

## Explanations

### L1 human

A walk is a route through a graph that goes from vertex to vertex along edges.
You may visit the same vertex or use the same edge more than once.
