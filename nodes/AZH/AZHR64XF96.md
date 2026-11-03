---
tag: AZHR64XF96
kind: definition
name: Burnside ring
msc: [19A22, 20C99]
defines: HKKBGRHNMY
uses: [G5S1M9, 0WCY42EV9V, 5FDMY7PDYY, 0310REJJY8, 0DEBXAJ5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Burnside_ring
---

## Definition

Let $G$ be a finite [[group|G5S1M9]].
A finite $G$-set is a finite set with a [[group action|0WCY42EV9V]] of $G$.
Isomorphism classes of finite $G$-sets form a commutative semiring under disjoint union $[S] + [T] = [S \sqcup T]$ and Cartesian product $[S] \cdot [T] = [S \times T]$, where $G$ acts on $S \times T$ by $g(s, t) = (gs, gt)$.
The *Burnside ring* $A(G)$ is the [[Grothendieck group|5FDMY7PDYY]] of the additive monoid of this semiring, with the multiplication extended bilinearly.
It is a [[commutative ring|0310REJJY8]] whose unit is the class of the one-point $G$-set.

## Remarks

As an abelian group, $A(G)$ is free with basis the classes $[G/H]$, where $H$ runs over representatives of the [[conjugacy classes|0DEBXAJ5SA]] of subgroups of $G$.
This holds because each finite $G$-set is the disjoint union of its orbits, and the orbit $G/H$ is isomorphic to $G/K$ exactly when $H$ and $K$ are conjugate.
Example: for $G = \Z/2\Z$, the basis is $a = [G/G]$, the point, and $b = [G/\set{0}]$, the free orbit with two elements.
The product $b \cdot b = [G \times G]$ is a free $G$-set with $4$ elements, so $b^2 = 2b$, and $A(\Z/2\Z) \cong \Z[b]/(b^2 - 2b)$.
Non-example: the set of isomorphism classes of finite $G$-sets is not itself $A(G)$, since a nonempty $G$-set has no additive inverse there.
For a subgroup $H$, the map $S \mapsto \abs{S^H}$, counting fixed points, extends to a ring homomorphism $A(G) \to \Z$.
