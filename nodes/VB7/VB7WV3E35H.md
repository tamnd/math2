---
tag: VB7WV3E35H
kind: definition
name: Morita duality
msc: [16D90, 16D50]
defines: M3YXA82ZFX
uses: [0B1261B5ED, EM7FHAFD3N, 85H7PRHDPZ, AWSBZWWMG9, 05QY1VEBYD]
sources:
  - url: https://en.wikipedia.org/wiki/Morita_equivalence
---

## Definition

Let $R$ and $S$ be [[rings|0B1261B5ED]] with identity and let $U$ be an $R$-$S$-[[bimodule|EM7FHAFD3N]].
A left $R$-module $C$ is a *cogenerator* if every left $R$-module embeds in a direct product of copies of $C$; likewise on the right.
The bimodule $U$ defines a *Morita duality* between $R$ and $S$ if these hold:

1. $U$ is an [[injective|85H7PRHDPZ]] cogenerator as a left $R$-module and as a right $S$-module.
2. The map $R \to \End(U_S)$ sending $r$ to left multiplication by $r$ is a ring isomorphism.
3. The map $S \to \End({}_R U)^{\mathrm{op}}$ sending $s$ to right multiplication by $s$ is a ring isomorphism.

Here $\End(U_S)$ and $\End({}_R U)$ are the [[endomorphism rings|AWSBZWWMG9]] of $U$ as a right $S$-module and as a left $R$-module.
A ring $R$ *has a Morita duality* if such $S$ and $U$ exist.

## Remarks

A left $R$-module $M$ is *reflexive* if the evaluation map $M \to \Hom_S(\Hom_R(M, U), U)$ is an isomorphism, and likewise for right $S$-modules.
Under a Morita duality, the functors $\Hom_R(-, U)$ and $\Hom_S(-, U)$ are mutually inverse contravariant equivalences between the reflexive modules on the two sides.
The reflexive modules include all [[finitely generated|05QY1VEBYD]] modules and all finitely cogenerated modules.
Example: for a field $k$, take $R = S = U = k$.
The space $k$ is injective and is a cogenerator of $k$-vector spaces, the multiplication maps $k \to \End(k)$ are isomorphisms, and the duality is $V \mapsto V^*$ on finite-dimensional spaces.
Non-example: $R = S = U = \Z$ fails clause 1, since $\Z$ is not an injective $\Z$-module; the map $2\Z \to \Z$, $2 \mapsto 1$, does not extend to $\Z$.
Over a quasi-Frobenius ring $R$, the bimodule $U = R$ gives a Morita duality between $R$ and itself.
Over a complete Noetherian local commutative ring with residue field $k$, the [[injective hull|QCJN05GN64]] of $k$ gives a Morita duality, known as Matlis duality.
