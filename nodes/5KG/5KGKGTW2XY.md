---
tag: 5KGKGTW2XY
kind: definition
name: Satellite knot
msc: [57K10]
defines: A1E8TDEVJ9
uses: [QYEAZTYGPT, 1TQ06R4Q66]
sources:
  - url: https://en.wikipedia.org/wiki/Satellite_knot
---

## Definition

Let $V = S^1 \times D^2$ be the solid torus, and let $P \subset \operatorname{int} V$ be a tame [[knot|QYEAZTYGPT]], the *pattern*, such that:

1. $P$ is not contained in any $3$-ball in $V$;
2. $P$ is not isotopic in $V$ to the core circle $S^1 \times \set{0}$.

Let $C \subset S^3$ be a knot that is not the [[unknot|1TQ06R4Q66]], the *companion*.
Let $h \colon V \to S^3$ be an embedding onto a closed tubular neighbourhood of $C$.
A knot in $S^3$ is a *satellite knot* if it is isotopic to $h(P)$ for some such $P$, $C$ and $h$.

## Remarks

Equivalently, a knot $K$ is a satellite knot if $S^3 \setminus K$ contains an incompressible torus that is not parallel to the boundary of a neighbourhood of $K$.
Example: let $C$ be a [[trefoil knot|VYTYSVHN4A]] and let $P$ be the $(2, 1)$-curve on a smaller concentric torus in $V$.
Then $h(P)$ is a cable of the trefoil and a satellite knot.
Non-example: if $P$ is the core circle, clause 2 fails and $h(P)$ is just $C$.
Every [[knot sum|AGZSZW7GYE]] $K_1 \# K_2$ of nontrivial knots is a satellite with companion $K_1$.
Whitehead doubles are satellites whose pattern has winding number $0$ in $V$.
