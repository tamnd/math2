---
tag: TW0AXSD756
kind: definition
name: Invertible module
msc: [13C10, 14C22]
defines: HYRK3K52ET
uses: [0310REJJY8, 0NZ8JA25WK, F0HQXQ0HCD]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_sheaf
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $M$ be an [[$R$-module|0NZ8JA25WK]].
The module $M$ is *invertible* if there is an $R$-module $N$ with $M \otimes_R N \cong R$, where $\otimes_R$ is the [[tensor product|F0HQXQ0HCD]] over $R$.

## Remarks

An $R$-module is invertible exactly when it is [[finitely generated projective|HQA9YHDSH5]] of constant [[rank|1WTNGZ5T5A]] $1$.
In that case one can take $N = \Hom_R(M, R)$, and the evaluation map $M \otimes_R \Hom_R(M, R) \to R$ is an isomorphism.
The isomorphism classes of invertible modules form an abelian group under $\otimes_R$, the [[Picard group|3Z9DCWYXQZ]] $\mathrm{Pic}(R)$.

Example: let $R$ be a [[Dedekind domain|7NPY2CN5KB]] with field of fractions $K$ and $I$ a nonzero ideal.
The inverse fractional ideal $I^{-1} = \set{x \in K : xI \subseteq R}$ satisfies $I I^{-1} = R$, and multiplication gives $I \otimes_R I^{-1} \cong I I^{-1} = R$.
So $I$ is invertible.

Non-example: over $R = \Z$, the module $\Z/2\Z$ is not invertible.
For every $\Z$-module $N$, the group $\Z/2\Z \otimes_\Z N \cong N/2N$ is killed by $2$, so it is not isomorphic to $\Z$.
The free module $R^2$ over a nonzero ring is not invertible either, since it has rank $2$.
