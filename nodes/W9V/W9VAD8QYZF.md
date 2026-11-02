---
tag: W9VAD8QYZF
kind: definition
name: Geometric graph
msc: [05C62, 52C10, 05C10]
defines: HFJCAPWWD4
uses: [00C0BR7D7H, VQ4Q2V45RP]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_graph_theory
---

## Definition

A *geometric graph* is a pair $(V, E)$ such that:

1. $V$ is a finite set of points in $\R^2$ in general position, that is, no three of them lie on a common line;
2. $E$ is a set of closed [[line segments|VQ4Q2V45RP]] each of whose two endpoints lie in $V$.

The points of $V$ are its vertices and the segments of $E$ are its edges.
Its underlying abstract [[graph|00C0BR7D7H]] has vertex set $V$, with $u$ and $v$ adjacent when the segment from $u$ to $v$ is in $E$.
Two edges cross if they meet at a point that is not a common endpoint.

## Remarks

Example: let $V$ be the four points $(0,0)$, $(1,0)$, $(1,1)$, $(0,1)$ and let $E$ be all six segments between them.
No three of these points are collinear and every segment has its endpoints in $V$, so this is a geometric graph.
Its underlying graph is $K_4$, and the two diagonals cross at $(1/2, 1/2)$.

Non-example: the points $(0,0)$, $(1,0)$, $(2,0)$ with the segment from $(0,0)$ to $(2,0)$ fail clause 1, since the three points are collinear, and the segment passes through a third vertex.

A geometric graph is called plane when no two of its edges cross.
Some authors drop the general position condition and only require that no edge passes through a vertex other than its endpoints.
