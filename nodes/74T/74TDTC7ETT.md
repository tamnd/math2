---
tag: 74TDTC7ETT
kind: definition
name: Continuous multiplication
msc: [22A15, 22A05]
defines: ZZK2GM1V15
uses: [0CQHFPGJ45, 0GBG8B49AA, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Definition

Let $M$ be a [[topological space|0CQHFPGJ45]] with a binary operation $M \times M \to M$, written $(x, y) \mapsto xy$.
The operation is a *continuous multiplication* if the map $\mu \colon M \times M \to M$, $\mu(x, y) = xy$, is [[continuous|0VGFHTM75Y]].
Here $M \times M$ carries the [[product topology|0GBG8B49AA]].

## Remarks

Example: $\R$ with its usual topology and ordinary multiplication.
The map $(x, y) \mapsto xy$ is a polynomial in the coordinates, so it is continuous on $\R^2$.
Non-example: $\Z$ with the cofinite topology and addition.
Every nonempty open set $U \times V$ of $\Z \times \Z$ meets the set $\set{(x, -x) : x \in \Z}$, because $U$ and $-V$ are cofinite and so they intersect.
So the preimage of the open set $\Z \setminus \set{0}$ under addition contains no nonempty open set, and addition is not continuous.
Continuity of $\mu$ implies that every left translation $y \mapsto xy$ and every right translation $x \mapsto xy$ is continuous.
The converse fails: in the non-example above every translation is a bijection of $\Z$, hence a homeomorphism for the cofinite topology.
In additive notation the same condition is called continuous addition.
