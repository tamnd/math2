---
tag: 72K5F9VPCR
kind: definition
name: Global dimension
msc: [13D05, "16E10"]
defines: GWA0T1WKCN
uses: [0310REJJY8, 0NZ8JA25WK, MR9QCH1PNA]
sources:
  - url: https://en.wikipedia.org/wiki/Global_dimension
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
The *global dimension* of $R$ is
$$\operatorname{gl.dim} R = \sup \set{\operatorname{pd}_R M : M \text{ a nonzero } R\text{-module}},$$
where $\operatorname{pd}_R M$ is the [[projective dimension|MR9QCH1PNA]] of the [[$R$-module|0NZ8JA25WK]] $M$.
It is an integer $\ge 0$ or $\infty$.

## Remarks

By a theorem of Auslander, the supremum can be taken over the cyclic modules $R/I$ only, with $I$ an ideal.
For a ring that is not commutative, the same definition with left modules or right modules gives the left and right global dimensions, which can differ.
Example: $\operatorname{gl.dim} \Z = 1$; every subgroup of a free abelian group is free, so every module has a free resolution of length at most $1$, and $\Z/2\Z$ is not projective.
Example: a ring has global dimension $0$ if and only if every module is projective; for a field this holds since every vector space is free.
Non-example of finiteness: $\Z/4\Z$ has infinite global dimension, because the projective dimension of $\Z/2\Z$ over it is infinite.
For a Noetherian local ring $(R, \mathfrak{m}, k)$, the global dimension equals $\operatorname{pd}_R k$.
