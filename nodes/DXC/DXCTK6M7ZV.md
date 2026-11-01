---
tag: DXCTK6M7ZV
kind: definition
name: CAT(0) group
msc: [20F67, 20F65]
defines: XB9QTY77ZA
uses: [0WCY42EV9V, 02HPP5VCZH, Q4HGMRA9JQ]
sources:
  - url: https://en.wikipedia.org/wiki/CAT(0)_group
---

## Definition

Let $X$ be a CAT(0) space, that is, a geodesic metric space with the following property.
For every geodesic triangle $\Delta$, let $\bar\Delta$ be a triangle in $\R^2$ with the same side lengths.
Then $d(p, q) \le \norm{\bar p - \bar q}$ for all points $p, q$ of $\Delta$ and their comparison points $\bar p, \bar q$ in $\bar\Delta$.
Let a group $G$ [[act|0WCY42EV9V]] on $X$ by [[isometries|02HPP5VCZH]].

1. The action is *proper* if each $x \in X$ has a radius $r > 0$ such that $\set{g \in G : g B(x, r) \cap B(x, r) \neq \emptyset}$ is finite.
2. The action is *cocompact* if there is a compact set $K \subseteq X$ with $GK = X$.

The group $G$ is a *CAT(0) group* if it admits a proper and cocompact action by isometries on some CAT(0) space.

## Remarks

Example: $\Z^n$ acts on $\R^n$ by translations.
The Euclidean space $\R^n$ is CAT(0), since its triangles are exactly as thin as their comparison triangles.
The action is proper, because a ball of radius $1/3$ meets only its own translate, and cocompact, with $K = [0, 1]^n$.

Example: a free group of finite rank acts properly and cocompactly on its Cayley graph for a free basis, which is a tree, and trees are CAT(0).

Non-example: the integer Heisenberg group is not a CAT(0) group.
In a CAT(0) group every solvable subgroup is virtually abelian, and the Heisenberg group is nilpotent but not virtually abelian.

Such an action is also called geometric.
Every CAT(0) group is finitely presented, and its [[Dehn function|Q4HGMRA9JQ]] is at most quadratic.
