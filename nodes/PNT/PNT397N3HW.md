---
tag: PNT397N3HW
kind: definition
name: Faithful module
msc: [16D10]
defines: TB40Y3SNSX
uses: [09VDS2W1E8, VQ31D68MDD]
sources:
  - url: https://en.wikipedia.org/wiki/Annihilator_(ring_theory)
---

## Definition

Let $R$ be a ring and let $M$ be a left [[$R$-module|09VDS2W1E8]].
The module $M$ is *faithful* if its [[annihilator|VQ31D68MDD]]
$$\operatorname{ann}_R(M) = \set{r \in R : rm = 0 \text{ for all } m \in M}$$
is $\set{0}$.

## Remarks

Equivalently, the ring homomorphism $R \to \End_\Z(M)$ that sends $r$ to the map $m \mapsto rm$ is injective.
Example: for a field $K$, the column space $K^n$ is a faithful $M_n(K)$-module.
The check: if $A e_j = 0$ for every standard basis vector $e_j$, then every column of $A$ is zero, so $A = 0$.
Non-example: for $n \ge 2$, the $\Z$-module $\Z/n\Z$ is not faithful, since $n \ne 0$ lies in its annihilator.
Every module $M$ is faithful as a module over $R / \operatorname{ann}_R(M)$.
