---
tag: AMC3JCQ497
kind: definition
name: Voronoi diagram
msc: [52C99, 68U05]
defines: QDNEBBVZ84
uses: [0XPR1E85W0, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Voronoi_diagram
---

## Definition

Let $n \ge 1$ and let $S = \set{p_1, \dots, p_k}$ be a finite set of $k \ge 1$ distinct points of [[Euclidean space|0XPR1E85W0]] $\R^n$, called *sites*.
Let $\norm{x - y}$ denote the [[Euclidean distance|0NPPGHQNXQ]].
The *Voronoi cell* of the site $p_i$ is
$$V(p_i) = \set{x \in \R^n : \norm{x - p_i} \le \norm{x - p_j} \text{ for all } j = 1, \dots, k}.$$
The *Voronoi diagram* of $S$ is the family of cells $V(p_1), \dots, V(p_k)$.

## Remarks

Example: for the two sites $p_1 = (-1, 0)$ and $p_2 = (1, 0)$ in $\R^2$, the condition $\norm{x - p_1} \le \norm{x - p_2}$ reduces to $x_1 \le 0$.
So $V(p_1)$ is the closed half-plane $x_1 \le 0$, $V(p_2)$ is the half-plane $x_1 \ge 0$, and they meet along the perpendicular bisector $x_1 = 0$.

Non-example: the cells $\set{x : x_1 \le -1}$ and $\set{x : x_1 \ge -1}$ are not the Voronoi diagram of these two sites, since the point $(-1/2, 0)$ is closer to $p_1$ but lies in the second set only.

Each condition $\norm{x - p_i} \le \norm{x - p_j}$ defines a closed half-space, so each cell is a convex polyhedron.
The cells cover $\R^n$, and two distinct cells have disjoint interiors, so the Voronoi diagram is a tiling of $\R^n$.
The Voronoi cell of a point of a lattice, with all lattice points as sites, is a [[Voronoi cell|V1R1R88GV6]] in the sense of the geometry of numbers.
