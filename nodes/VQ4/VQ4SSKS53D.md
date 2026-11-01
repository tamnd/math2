---
tag: VQ4SSKS53D
kind: definition
name: Torsion-free group
msc: [20F99, 20K15]
defines: PEMNN32A43
uses: [G5S1M9, 0WE2NHZJ7B, 0C4JS9RF5M, 0NCJ5WXN6Z, 0KTW26C80J, 0DBWXQRXQJ, 0RY0B72XAS]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_(algebra)
---

## Definition

Let $G$ be a [[group|G5S1M9]] with identity $e$.
$G$ is *torsion-free* if every element $g \ne e$ of $G$ has infinite [[order|0WE2NHZJ7B]], that is, $g^n \ne e$ for all integers $n \ge 1$.

## Remarks

Example: the [[integers|0C4JS9RF5M]] $\Z$ under addition.
If $m \ne 0$ and $n \ge 1$, then $n m \ne 0$.
The groups $\Z^k$, the [[rational numbers|0NCJ5WXN6Z]] under addition, and [[free groups|0KTW26C80J]] are also torsion-free.

Non-example: $\Z \times \Z/2\Z$.
The element $(0, 1)$ is not the identity, but $2 \cdot (0, 1) = (0, 0)$.

For an abelian group $A$ with [[torsion subgroup|0DBWXQRXQJ]] $T$, the quotient $A/T$ is torsion-free.
By the [[structure theorem for finitely generated abelian groups|0RY0B72XAS]], a finitely generated torsion-free abelian group is isomorphic to $\Z^n$ for some $n \ge 0$.
In a nonabelian group the elements of finite order need not form a subgroup.
In the infinite dihedral group, two reflections have order $2$, but their product is a translation of infinite order.
