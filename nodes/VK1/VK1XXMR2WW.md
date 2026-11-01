---
tag: VK1XXMR2WW
kind: definition
name: Graph embedding
msc: [05C10, 57M15]
defines: CG91WNMG2T
uses: [0JD5C82QMB, 08SVRVHJNY, 0EKZW08FQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_embedding
---

## Definition

Let $G = (V, E)$ be a finite [[graph|0JD5C82QMB]] and let $\Sigma$ be a surface.
An embedding of $G$ in $\Sigma$ consists of a point $p_v \in \Sigma$ for each vertex $v$ and a subset $\gamma_e \subseteq \Sigma$ for each edge $e$ such that:

1. The points $p_v$ are distinct.
2. For each edge $e = uv$, the set $\gamma_e$ is the image of a [[topological embedding|08SVRVHJNY]] of $[0, 1]$ into $\Sigma$ with ends $p_u$ and $p_v$.
3. An arc $\gamma_e$ contains no point $p_w$ other than its two ends.
4. Two distinct arcs meet at most in common ends.

## Remarks

Example: drawing $K_4$ in the plane as a triangle with a central vertex joined to its three corners satisfies all four clauses.
Non-example: drawing $K_4$ as a square with both diagonals is not an embedding, because the diagonals cross at an inner point, which violates clause 4.
A graph is planar exactly when it has an embedding in the plane, or equivalently in the sphere.
The genus of $G$ is the least $g$ such that $G$ embeds in the [[orientable surface|0EKZW08FQ5]] of genus $g$; for example $K_5$ and $K_{3,3}$ have genus $1$.
