---
tag: DPE8EDD9W7
kind: definition
name: Dual graph
msc: [05C10]
defines: 1QHTD1DS5J
uses: [029JQEK15B, CG91WNMG2T, 01M5T0KDG7]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_graph
---

## Definition

Let $G$ be a [[planar graph|029JQEK15B]] together with a fixed [[embedding|CG91WNMG2T]] in the plane, called a plane graph.
The faces of $G$ are the connected components of the complement of the drawing in the plane.
The dual $G^*$ is the [[multigraph|01M5T0KDG7]], possibly with loops, defined as follows.

1. The vertices of $G^*$ are the faces of $G$.
2. For each edge $e$ of $G$ there is one edge $e^*$ of $G^*$.
3. The ends of $e^*$ are the faces on the two sides of $e$; if the same face lies on both sides, $e^*$ is a loop.

## Remarks

Example: draw $K_4$ in the plane as a triangle with a central vertex joined to the corners.
This drawing has $4$ faces, and every two of them share exactly one edge, so its dual is again $K_4$.
Non-example: $K_5$ has no dual in this sense, since it is not planar and so it has no plane embedding, which the setting requires.
An edge $e$ is a [[bridge|0D81KWH9ZM]] exactly when $e^*$ is a loop.
If $G$ is connected, then $(G^*)^*$ is isomorphic to $G$.
A set of edges is a cycle of $G$ exactly when the dual edges form a minimal cut of $G^*$.
Different embeddings of the same planar graph can have non-isomorphic duals.
