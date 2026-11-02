---
tag: ZPVRRQDYRB
kind: definition
name: Irreducible component
msc: [14A10, 14A15]
defines: SY2MWC434Z
uses: [0CQHFPGJ45, 0ZCK8DQYN1, 2VQX2E8EAH, VHFMQQYSTN]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_component
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A subset $Y \subseteq X$, with the subspace topology, is *irreducible* if $Y$ is nonempty and has the following property.
$Y$ is not the union of two [[closed subsets|0ZCK8DQYN1]] of $Y$ that are both different from $Y$.
An *irreducible component* of $X$ is an irreducible subset $Y \subseteq X$ that is maximal: no irreducible subset of $X$ contains $Y$ strictly.

## Remarks

Equivalently, a nonempty space is irreducible when any two nonempty open subsets meet, that is, when every nonempty open subset is dense.
The closure of an irreducible subset is irreducible, so irreducible components are closed.
By Zorn's lemma every irreducible subset lies in an irreducible component, so $X$ is the union of its irreducible components.

Example: the [[algebraic set|VHFMQQYSTN]] $X = V(xy) \subseteq \C^2$ is the union of the axes $V(x)$ and $V(y)$.
Each axis is irreducible, since it is homeomorphic to $\C$ with the topology whose proper closed sets are the finite sets, and two finite sets cannot cover an infinite set.
Neither axis contains the other, and $X$ itself is not irreducible, so the two axes are the irreducible components of $X$.

Non-example: the set $\set{0, 1} \subseteq \C$ is not irreducible, because it is the union of the closed sets $\set{0}$ and $\set{1}$.

In a [[Noetherian topological space|2VQX2E8EAH]], there are only finitely many irreducible components, and none of them lies in the union of the others.
