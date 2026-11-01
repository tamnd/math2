---
tag: SMEFDN2RF5
kind: definition
name: Group algebra
msc: [20C05, 16S34]
defines: MNP2HBWB5Q
uses: [G5S1M9, 04C5ZBG1WT, 000AYPA9AJ, 0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Group_ring
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $F$ be a [[field|04C5ZBG1WT]].
The *group algebra* $F[G]$ is the set of functions $a \colon G \to F$ with $a(g) \ne 0$ for only finitely many $g \in G$, written as finite formal sums $\sum_{g \in G} a_g \, g$.
It is a [[vector space|000AYPA9AJ]] over $F$ under termwise addition and scalar multiplication, with basis $G$.
Its multiplication is
$$\Big(\sum_{g} a_g \, g\Big)\Big(\sum_{h} b_h \, h\Big) = \sum_{k \in G} \Big(\sum_{gh = k} a_g b_h\Big) k.$$

## Remarks

With this product $F[G]$ is an associative [[ring|0B1261B5ED]] with identity $1_G$, and an algebra over $F$ of dimension $\abs{G}$.
It is commutative if and only if $G$ is abelian.
Example: for $G = \set{1, t}$ cyclic of order $2$ and $F = \Q$, the elements $e = \tfrac{1}{2}(1 + t)$ and $f = \tfrac{1}{2}(1 - t)$ satisfy $e^2 = e$, $f^2 = f$, $ef = 0$ and $e + f = 1$, since $t^2 = 1$.
So $\Q[G] \cong \Q \times \Q$ as rings.
Non-example: for infinite $G$, the set of all functions $G \to F$ is not the group algebra, since it fails the finiteness condition.
For $G = \Z$ the product formula then breaks down, as the inner sum $\sum_{gh = k} a_g b_h$ can be an infinite sum.
A [[representation|WYGRXCG2RN]] of $G$ on $V$ is the same as a left $F[G]$-module structure on $V$.
For a commutative ring $R$, the same definition gives the group ring $R[G]$.
