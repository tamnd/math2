---
tag: HN5A4M2GE8
kind: definition
name: Minkowski sum of polytopes
msc: [52B11, 52A39]
defines: 7GK5417BJF
uses: [300K6CB1KH, SXS6D87PHE, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_addition
---

## Definition

Let $P$ and $Q$ be [[convex polytopes|300K6CB1KH]] in $\R^n$.
Their *Minkowski sum* is the set
$$P + Q = \set{p + q : p \in P, \ q \in Q}.$$

## Remarks

The set $P + Q$ is again a convex polytope.
If $P$ has vertex set $V$ and $Q$ has vertex set $W$, then $P + Q$ is the [[convex hull|0FQSDC2EQ2]] of the finite set $\set{v + w : v \in V, \ w \in W}$.
For a linear functional $u$, the face of $P + Q$ on which $u$ is largest is the sum of the faces of $P$ and of $Q$ on which $u$ is largest.
So each vertex of $P + Q$ is $v + w$ for a unique vertex $v$ of $P$ and a unique vertex $w$ of $Q$.

Example: let $T$ be the triangle with vertices $(0,0)$, $(1,0)$, $(0,1)$ in $\R^2$, and let $-T$ be its image under $x \mapsto -x$.
The sums of vertices of $T$ and $-T$ are the differences of vertices of $T$, namely $(0,0)$, $(\pm 1, 0)$, $(0, \pm 1)$, $(1,-1)$ and $(-1,1)$.
Their convex hull is the hexagon with vertices $(1,0)$, $(1,-1)$, $(0,-1)$, $(-1,0)$, $(-1,1)$, $(0,1)$, so $T + (-T)$ is this hexagon.

Non-example: the closed unit disk $D$ is convex but not a polytope, and $[0,1]^2 + D$ is a square with rounded corners, which is not a polytope.
So the closure of polytopes under the sum needs both summands to be polytopes.

The operation is commutative and associative, and $\set{0}$ is its neutral element.
It is the general [[Minkowski addition|SXS6D87PHE]] of sets, restricted to polytopes.
