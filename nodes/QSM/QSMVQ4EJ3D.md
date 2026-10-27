---
tag: QSMVQ4EJ3D
kind: example
name: The symmetric group S3 is not abelian
msc: [20B30]
instance_of: [G5S1M9]
not_instance_of:
  - target: 082GHNPJ53
    note: two transpositions do not commute
  - target: 071DDFVG4J
    note: (1 2)(1 3) is not (1 3)(1 2)
uses: [0515A6D2Y1, 02DTRYKGE8]
sources:
  - url: https://en.wikipedia.org/wiki/Dihedral_group_of_order_6
    locator: lead section
---

## Example

Let $S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$. Compose permutations from right to left.
Take the [[transpositions|02DTRYKGE8]] $(1\,2)$ and $(1\,3)$.
Then $(1\,2)(1\,3) = (1\,3\,2)$ and $(1\,3)(1\,2) = (1\,2\,3)$.
These two products are different. Thus $S_3$ is not [[abelian|071DDFVG4J]].

## Remarks

$S_3$ has $6$ elements. It is the smallest group that is not abelian.
