---
tag: V24HACXCVG
kind: definition
name: Tensegrity
msc: [52C25, 74K99]
defines: 2ZYK00K18N
uses: [V5YS9BZX0N]
sources:
  - url: https://en.wikipedia.org/wiki/Tensegrity
---

## Definition

Let $G = (V, E)$ be a finite graph and let $d \ge 1$.
A *tensegrity framework* in $\R^d$ is a triple $(G, p, \tau)$ with two parts besides the graph.
The map $p \colon V \to \R^d$ is a configuration of the vertices, and $\tau$ labels each edge as a *cable*, a *strut* or a *bar*.
A configuration $q \colon V \to \R^d$ satisfies the constraints of the framework when, for each edge $ij$:

1. if $ij$ is a cable, then $\abs{q_i - q_j} \le \abs{p_i - p_j}$;
2. if $ij$ is a strut, then $\abs{q_i - q_j} \ge \abs{p_i - p_j}$;
3. if $ij$ is a bar, then $\abs{q_i - q_j} = \abs{p_i - p_j}$.

The tensegrity framework is *rigid* when every continuous path of configurations that starts at $p$ and satisfies the constraints consists of configurations congruent to $p$.
A *proper self-stress* is a family of real numbers $\omega_{ij}$, one for each edge, with $\omega_{ij} \ge 0$ on cables and $\omega_{ij} \le 0$ on struts.
It must satisfy $\sum_{j : ij \in E} \omega_{ij} (p_j - p_i) = 0$ for every vertex $i$.

## Remarks

Example: the unit square in $\R^2$ with its four sides as cables and its two diagonals as struts.
The self-stress $\omega = 1$ on the sides and $\omega = -1$ on the diagonals is proper and in equilibrium.
At the corner $(0,0)$ the sum is $(1,0) + (0,1) - (1,1) = 0$, and the other corners are alike by symmetry.
This tensegrity framework is rigid in the plane.
Non-example: the unit square with four cables as sides and a single strut on one diagonal is not rigid.
It can be flattened into a rhombus whose strut diagonal grows and whose other diagonal shrinks, while the sides keep their length.
A [[bar framework|V5YS9BZX0N]] is the special case in which every edge is a bar.

## Explanations

### L1 human

A cable is a member that can get shorter but not longer, and a strut is one that can get longer but not shorter.
A tensegrity framework is a graph drawn in space with each edge marked as cable, strut or bar.
It is rigid when no motion respecting these rules changes its shape.
