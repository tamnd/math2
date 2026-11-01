---
tag: VFCN5HDH7S
kind: definition
name: Perfect graph
msc: [05C17]
defines: 1YZ7NV161A
uses: [0JD5C82QMB, 0V05FC4GKQ, 0C5M7AM6FH, 0WCKRBHFFD]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_graph
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]].
For a graph $H$, let $\chi(H)$ be its [[chromatic number|0C5M7AM6FH]] and $\omega(H)$ its [[clique number|0WCKRBHFFD]].
The graph $G$ is perfect if $\chi(H) = \omega(H)$ for every [[induced subgraph|0V05FC4GKQ]] $H$ of $G$.

## Remarks

Example: every bipartite graph $G$ is perfect.
An induced subgraph $H$ of $G$ is again bipartite, so $\chi(H) = \omega(H) = 2$ if $H$ has an edge, and $\chi(H) = \omega(H) = 1$ if $H$ has vertices but no edge.
Non-example: the cycle $C_5$ is not perfect, because $\omega(C_5) = 2$ while $\chi(C_5) = 3$, so the condition fails for $H = C_5$ itself.
The condition must hold for all induced subgraphs, not just for $G$: the disjoint union of $C_5$ and a triangle has $\chi = \omega = 3$ but is not perfect.
By the weak perfect graph theorem of Lovász, the complement of a perfect graph is perfect.
