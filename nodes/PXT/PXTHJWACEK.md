---
tag: PXTHJWACEK
kind: definition
name: Feasible region
msc: [90C30, 90C05]
defines: 1TTKMRW8PD
uses: [X3663P90AE, 0BJR9QR08E, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Feasible_region
---

## Definition

Let $X$ be a set, and let $g_1, \dots, g_m$ and $h_1, \dots, h_p$ be functions from $X$ to $\R$.
Consider the [[constraints|X3663P90AE]] $g_i(x) \le 0$ for $i = 1, \dots, m$ and $h_j(x) = 0$ for $j = 1, \dots, p$.
The *feasible region* (or *feasible set*) of these constraints is the [[subset|0BJR9QR08E]]
$$F = \set{x \in X : g_i(x) \le 0 \text{ for all } i, \ h_j(x) = 0 \text{ for all } j}.$$
A point of $F$ is a *feasible point* or *feasible solution*.
The constraints, and a problem that has them, are *feasible* if $F \neq \emptyset$ and *infeasible* if $F = \emptyset$.

## Remarks

Example: on $X = \R^2$, the constraints $-x \le 0$, $-y \le 0$ and $x + y - 1 \le 0$ have the closed triangle with vertices $(0,0)$, $(1,0)$, $(0,1)$ as feasible region.
The point $(1/4, 1/2)$ is feasible: $-1/4 \le 0$, $-1/2 \le 0$ and $1/4 + 1/2 - 1 = -1/4 \le 0$.

Non-example: the point $(1, 1)$ is not feasible, since $1 + 1 - 1 = 1 > 0$ violates the third constraint.

If every $g_i$ is convex and every $h_j$ is affine on $X = \R^n$, then $F$ is a [[convex set|02AS45T3H9]].
For linear constraints, $F$ is a polyhedron, an intersection of finitely many closed half-spaces and hyperplanes.
