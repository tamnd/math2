---
tag: 1ZDAGGGRP4
kind: definition
name: Dual cone
msc: [52A20, 90C25]
defines: QFY1JR1TK4
uses: [0XPR1E85W0, 0S52TNNTH9, 6VE4KA12VD]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_cone_and_polar_cone
---

## Definition

Let $n \ge 1$ and let $C \subseteq \R^n$ be any subset.
The *dual cone* of $C$ is the set
$$C^* = \set{y \in \R^n : x \cdot y \ge 0 \text{ for all } x \in C},$$
where $x \cdot y$ is the [[dot product|0S52TNNTH9]].

## Remarks

The set $C^*$ is an intersection of closed half-spaces through $0$, so it is a closed [[convex cone|6VE4KA12VD]] that contains $0$.
If $C$ is a closed convex cone, then $(C^*)^* = C$.

Example: for $C = \R^n_{\ge 0}$, one has $C^* = \R^n_{\ge 0}$.
If $y$ has nonnegative coordinates, then $x \cdot y \ge 0$ for each $x \in C$; conversely, taking $x = e_i$ gives $y_i \ge 0$.
A cone with $C^* = C$ is called self-dual; the cone of positive semidefinite matrices with the trace inner product is another self-dual cone.

Non-example: the vector $y = (1, -1)$ is not in the dual of $\R^2_{\ge 0}$, since $(0, 1) \cdot y = -1 < 0$.

The *polar cone* is $C^\circ = -C^* = \set{y : x \cdot y \le 0 \text{ for all } x \in C}$.
In a general real inner product space, or with a pairing between a space and its dual, the same formula defines the dual cone.
