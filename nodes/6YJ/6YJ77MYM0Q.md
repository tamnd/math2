---
tag: 6YJ77MYM0Q
kind: definition
name: Topological monoid
msc: [22A15]
defines: RA56GHB9JZ
uses: [0N6R902FG1, 0CQHFPGJ45, ZZK2GM1V15]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_monoid
---

## Definition

A *topological monoid* is a [[monoid|0N6R902FG1]] $M$ together with a [[topology|0CQHFPGJ45]] on $M$ such that the multiplication $M \times M \to M$, $(x, y) \mapsto xy$, is a [[continuous multiplication|ZZK2GM1V15]].
That is, the map is continuous when $M \times M$ carries the product topology.

## Remarks

Example: $(\R, \cdot)$ with the usual topology.
Multiplication is associative with identity $1$, and $(x, y) \mapsto xy$ is continuous on $\R^2$.
Non-example: the monoid $(\Z, +)$ with the cofinite topology.
It has identity $0$, but addition is not jointly continuous, because every nonempty open set $U \times V$ of $\Z \times \Z$ contains a pair $(x, -x)$, so the preimage of $\Z \setminus \set{0}$ is not open.
No condition on the identity element is needed beyond its existence.
A topological monoid in which every element is invertible and inversion is continuous is a topological group.
