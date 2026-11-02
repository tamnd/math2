---
tag: DPZ76D18DD
kind: definition
name: Stable homotopy category
msc: [55P42, 18G80]
defines: 26GTNMAF7B
uses: [1GHF4EKBXS, P976WYEFMB]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(topology)
---

## Definition

Let $\mathbf{Sp}$ be the category of [[spectra|1GHF4EKBXS]] and maps of spectra.
A map $f \colon E \to F$ of spectra is a *stable weak equivalence* if $\pi_k(f) \colon \pi_k(E) \to \pi_k(F)$ is an isomorphism of [[homotopy groups|P976WYEFMB]] for every $k \in \Z$.
The *stable homotopy category* $\mathrm{Ho}(\mathbf{Sp})$ is the localization of $\mathbf{Sp}$ at the stable weak equivalences.
It has the same objects as $\mathbf{Sp}$.
It is the universal category under $\mathbf{Sp}$ in which every stable weak equivalence becomes an isomorphism.

## Remarks

The stable weak equivalences are the weak equivalences of a model structure on spectra.
So the localization exists with small morphism sets, and it is the homotopy category of that model structure.

Basic properties:

1. Every morphism set $[E, F]$ is an abelian group, and composition is bilinear.
2. The suspension $\Sigma$ is an equivalence of categories, with inverse the loop functor $\Omega$.
3. With $\Sigma$ as shift and cofibre sequences as distinguished triangles, $\mathrm{Ho}(\mathbf{Sp})$ is a triangulated category.
4. The smash product makes it a symmetric monoidal category, with the sphere spectrum as unit.

Example: for finite pointed CW complexes $X$ and $Y$, $[\Sigma^\infty X, \Sigma^\infty Y] \cong \operatorname{colim}_k [\Sigma^k X, \Sigma^k Y]_*$, the group of stable maps.

Non-example: in the homotopy category of pointed CW complexes, suspension is not an equivalence.
The suspension map $\pi_3(S^2) = [S^3, S^2]_* \to [S^4, S^3]_* = \pi_4(S^3)$ goes from $\Z$ onto $\Z/2$, so it is not injective, and $\Sigma$ is not fully faithful there.

The first construction of a stable homotopy category with a well-behaved smash product is due to Boardman.
Modern models, such as symmetric spectra and orthogonal spectra, have homotopy categories equivalent to it.
