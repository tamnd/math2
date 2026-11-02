---
tag: GT687SNZMQ
kind: definition
name: Hyperstructure
msc: [20N20, 08A99]
defines: 1HJF40J5AK
uses: [0SJ3RX9TXA, 00E0YZCERH, 09CEDJYBKP, 0K8F7PVDMX]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperstructure
---

## Definition

Let $H$ be a nonempty [[set|0SJ3RX9TXA]] and let $\mathcal{P}^*(H)$ be the set of nonempty subsets of $H$, a part of the [[power set|00E0YZCERH]].
A *hyperoperation* on $H$ is a map $\circ \colon H \times H \to \mathcal{P}^*(H)$ on the [[Cartesian product|09CEDJYBKP]].
For subsets $X, Y \subseteq H$ write $X \circ Y = \bigcup_{x \in X, y \in Y} x \circ y$, and $x \circ Y = \set{x} \circ Y$.
An *(algebraic) hyperstructure* is a set $H$ with one or more hyperoperations, possibly together with ordinary operations.
A set with one hyperoperation $(H, \circ)$ is a *hypergroupoid*, and it is a *hypergroup* if:

1. $(x \circ y) \circ z = x \circ (y \circ z)$ for all $x, y, z \in H$ ([[associativity|0K8F7PVDMX]]);
2. $x \circ H = H \circ x = H$ for all $x \in H$ (reproduction axiom).

A hypergroupoid that satisfies clause 1 is a *semihypergroup*.

## Remarks

Example: $H = \R$ with $x \circ y = [\min(x, y), \max(x, y)]$.
Both sides of clause 1 equal $[\min(x, y, z), \max(x, y, z)]$, since the union of the intervals between $z$ and the points of $[a, b]$ is the interval from $\min(a, z)$ to $\max(b, z)$.
For clause 2, every $y \in \R$ lies in $x \circ y$, so $x \circ \R = \R \circ x = \R$.

Non-example: $H = [0, \infty)$ with $x \circ y = [\max(x, y), \infty)$.
Clause 1 holds, since both sides equal $[\max(x, y, z), \infty)$.
Clause 2 fails: for $x = 1$, $x \circ H = [1, \infty) \ne H$.
So this is a semihypergroup but not a hypergroup.

A group $G$ is a hypergroup with $x \circ y = \set{xy}$.
