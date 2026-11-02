---
tag: 25RZTHSRS3
kind: definition
name: Strictly convex set
msc: [52A07, 52A20]
defines: 62FGRXS27K
uses: [T32W553W95, CCZA91NE5X, 0RZH6W98HK, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_set
---

## Definition

Let $V$ be a real [[topological vector space|T32W553W95]], such as $\R^n$, and let $C \subseteq V$.
The set $C$ is *strictly convex* if for all $x, y \in C$ with $x \ne y$, the [[open segment|CCZA91NE5X]] $(x, y)$ lies in the [[interior|0RZH6W98HK]] of $C$.

## Remarks

A strictly convex set is [[convex|02AS45T3H9]], since $(x, y) \subseteq \operatorname{int} C \subseteq C$.

Example: the closed unit disc $D = \set{p \in \R^2 : \abs{p} \le 1}$.
If $x \ne y$ in $D$ and $0 < t < 1$, then $\abs{(1 - t)x + t y} < 1$.
Indeed, equality would need $\abs{x} = \abs{y} = 1$ and equality in the triangle inequality.
For the Euclidean norm this means that $x$ and $y$ point in the same direction, which forces $x = y$.
So the open segment lies in the open disc, the interior of $D$.

Non-example: the closed square $[0, 1]^2$.
The points $(0, 0)$ and $(1, 0)$ lie in it, but the midpoint $(1/2, 0)$ is on the boundary, not in the interior.

Every open convex set is strictly convex, so the notion is of interest mainly for closed sets.
