---
tag: AEF4CBRAMN
kind: definition
name: Abelian category
msc: ["18E10"]
defines: Y9CZ3MTNF1
uses: [B2VP96NJSK, S417YNEJ6M, H8W38933NC, Y2NP1JFR86, RVXDSY04KG, 0NZ8JA25WK, 0WJX8MGG37]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_category
    locator: Definitions
---

## Definition

An *abelian category* is an [[additive category|B2VP96NJSK]] $\mathcal{A}$ such that:

1. every morphism of $\mathcal{A}$ has a [[kernel|S417YNEJ6M]] and a [[cokernel|H8W38933NC]];
2. every [[monomorphism|Y2NP1JFR86]] of $\mathcal{A}$ is the kernel of some morphism;
3. every [[epimorphism|RVXDSY04KG]] of $\mathcal{A}$ is the cokernel of some morphism.

## Remarks

Clauses 2 and 3 are equivalent, given clause 1, to the condition that for every morphism $f$ the canonical morphism $\operatorname{coim} f \to \operatorname{im} f$ is an isomorphism, where $\operatorname{coim} f = \operatorname{coker}(\ker f)$ and $\operatorname{im} f = \ker(\operatorname{coker} f)$.
In an abelian category, a morphism that is both a monomorphism and an epimorphism is an isomorphism.

Example: the category of left [[modules|0NZ8JA25WK]] over a ring $R$ is abelian.
A monomorphism $m \colon M \to N$ is injective, and it is the kernel of the quotient map $N \to N / m(M)$.
An epimorphism $e \colon N \to P$ is surjective, and it is the cokernel of the inclusion of its kernel.

Non-example: the category of [[free abelian groups|0WJX8MGG37]] is additive but not abelian.
Multiplication by $2$ on $\Z$ is an epimorphism there: if $u \circ 2 = v \circ 2$ with torsion-free target, then $2(u - v) = 0$ forces $u = v$.
It is not the cokernel of any morphism $k$: from $2 \circ k = 0$ follows $k = 0$, whose cokernel is the identity of $\Z$, not multiplication by $2$.
So clause 3 fails.
