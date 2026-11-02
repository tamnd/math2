---
tag: V3RCQ1J2VV
kind: definition
name: Polar polytope
msc: [52B11, 52B05, 52A20]
defines: 6DXF1T506B
uses: [300K6CB1KH, 0S52TNNTH9, 0RZH6W98HK, KY7SB854VH]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_polyhedron
---

## Definition

Let $P \subset \R^d$ be a [[convex polytope|300K6CB1KH]] whose [[interior|0RZH6W98HK]] contains the origin $0$.
Let $x \cdot y$ denote the [[dot product|0S52TNNTH9]] on $\R^d$.
The *polar polytope* of $P$ is
$$P^\circ = \set{y \in \R^d : x \cdot y \le 1 \text{ for all } x \in P}.$$

## Remarks

If $v_1, \dots, v_m$ are the vertices of $P$, then $P^\circ = \set{y : v_i \cdot y \le 1, \ i = 1, \dots, m}$.
$P^\circ$ is again a convex polytope with $0$ in its interior, and $(P^\circ)^\circ = P$.
The map $F \mapsto \set{y \in P^\circ : x \cdot y = 1 \text{ for all } x \in F}$ is an inclusion-reversing bijection from the [[faces|KY7SB854VH]] of $P$ to the faces of $P^\circ$, sending $k$-faces to $(d - 1 - k)$-faces.

Example: let $P = [-1, 1]^2$.
Its vertices are $(\pm 1, \pm 1)$, so $y \in P^\circ$ means $\pm y_1 \pm y_2 \le 1$ for all signs, that is $\abs{y_1} + \abs{y_2} \le 1$.
So $P^\circ$ is the square with vertices $(\pm 1, 0)$ and $(0, \pm 1)$.

Non-example: for $P = [0,1]^2$ the origin is a vertex, not an interior point, so the definition does not apply.
The same formula gives the unbounded set $\set{y : y_1 \le 1, \ y_2 \le 1, \ y_1 + y_2 \le 1}$, which is not a polytope.
