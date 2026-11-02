---
tag: 9SEF1CWT6X
kind: definition
name: Topological semigroup
msc: [22A15]
defines: QXB6JDG68F
uses: [0XMEM406JM, 0CQHFPGJ45, ZZK2GM1V15]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_semigroup
---

## Definition

A *topological semigroup* is a [[semigroup|0XMEM406JM]] $S$ together with a [[topology|0CQHFPGJ45]] on $S$ such that the multiplication $S \times S \to S$, $(x, y) \mapsto xy$, is a [[continuous multiplication|ZZK2GM1V15]].
That is, the map is continuous when $S \times S$ carries the product topology.

## Remarks

Example: $[0, 1]$ with ordinary multiplication and the topology from $\R$.
The product is associative, it maps $[0,1] \times [0,1]$ into $[0,1]$, and it is continuous as the restriction of a polynomial.
Non-example: the semigroup $(\Z, +)$ with the cofinite topology.
Addition is associative, but it is not jointly continuous: the preimage of $\Z \setminus \set{0}$ is not open, since every nonempty basic open set $U \times V$ contains a pair $(x, -x)$.
If one asks only that each translation $y \mapsto xy$ and $y \mapsto yx$ be continuous, the weaker structure is called a semitopological semigroup.
