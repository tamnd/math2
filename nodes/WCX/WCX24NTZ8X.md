---
tag: WCX24NTZ8X
kind: definition
name: Azumaya algebra
msc: [16H05, 16K50]
defines: VKZTT484WQ
uses: [0GYGHKX834, 3CTW1P4HBP, CRE6VEKT32, 0XHM30WBVB, TB40Y3SNSX, M8Q24XB0AF, SMFZN9E2ZB, AWSBZWWMG9]
sources:
  - url: https://en.wikipedia.org/wiki/Azumaya_algebra
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $R$ with identity.
Let $A^{\mathrm{op}}$ be the [[opposite ring|M8Q24XB0AF]] of $A$.
The algebra $A$ is an *Azumaya algebra* over $R$ if the following hold.

1. $A$ is a [[finitely generated|0XHM30WBVB]] [[projective|CRE6VEKT32]] $R$-module.
2. $A$ is a [[faithful|TB40Y3SNSX]] $R$-module.
3. The $R$-linear map $A \otimes_R A^{\mathrm{op}} \to \End_R(A)$ that sends $a \otimes b$ to the map $x \mapsto axb$ is an isomorphism.

Here $\otimes_R$ is the [[tensor product of modules|SMFZN9E2ZB]] and $\End_R(A)$ is the [[endomorphism ring|AWSBZWWMG9]] of the $R$-module $A$.

## Remarks

Example: $A = M_n(R)$ with $n \ge 1$.
It is free of rank $n^2$, hence projective and faithful, and the map $M_n(R) \otimes_R M_n(R)^{\mathrm{op}} \to \End_R(M_n(R))$ sends the basis elements $e_{ij} \otimes e_{kl}$ to the maps $x \mapsto e_{ij} x e_{kl}$, which form a basis of $\End_R(M_n(R)) \cong M_{n^2}(R)$.
Non-example: let $L/K$ be a field extension of degree $2$ and $A = L$ over $R = K$.
Clauses 1 and 2 hold, but $L \otimes_K L$ is commutative while $\End_K(L) \cong M_2(K)$ is not, so the map in clause 3 is not an isomorphism.
Over a field $K$, the Azumaya algebras are exactly the [[central simple algebras|5HRKJBAY2V]] over $K$.
Equivalently, $A$ is an Azumaya algebra when it is a central [[separable algebra|X8H7A98Q55]] over $R$.
Another equivalent form: clauses 1 and 2 hold and $A / \mathfrak{m}A$ is central simple over $R/\mathfrak{m}$ for every maximal ideal $\mathfrak{m}$ of $R$.
