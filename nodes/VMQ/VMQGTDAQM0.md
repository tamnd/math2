---
tag: VMQGTDAQM0
kind: definition
name: Laman graph
msc: [52C25, 05C10]
defines: C81JPZ51NA
uses: [0JD5C82QMB, 0V05FC4GKQ]
sources:
  - url: https://en.wikipedia.org/wiki/Laman_graph
---

## Definition

Let $G = (V, E)$ be a finite simple [[graph|0JD5C82QMB]] with $n = \abs{V} \ge 2$ vertices.
The graph $G$ is a *Laman graph* if both conditions hold.

1. $\abs{E} = 2n - 3$.
2. For every set $S \subseteq V$ with $k = \abs{S} \ge 2$, the [[induced subgraph|0V05FC4GKQ]] on $S$ has at most $2k - 3$ edges.

## Remarks

Example: the complete graph $K_4$ minus one edge has $4$ vertices and $5 = 2 \cdot 4 - 3$ edges.
Each $3$-vertex subset spans at most $3$ edges, and each pair spans at most $1$ edge, so condition 2 holds.

Non-example: two triangles that share one vertex have $5$ vertices and $6$ edges, but $2 \cdot 5 - 3 = 7$, so condition 1 fails.
Such a framework in the plane can rotate one triangle about the shared vertex.

Laman's theorem concerns a generic placement of the vertices in $\R^2$.
It states that $G$ is a Laman graph if and only if this framework is rigid and becomes flexible when any edge is removed.
Hilda Pollaczek-Geiringer found this result earlier, so it is also called the Geiringer–Laman theorem.
