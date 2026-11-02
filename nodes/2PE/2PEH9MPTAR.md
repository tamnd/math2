---
tag: 2PEH9MPTAR
kind: statement
role: proposition
name: Uniqueness of adjoints
msc: [18A40]
uses: [TZHF6ZM92S, KYCPCC57FT]
about: [TZHF6ZM92S]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_functors
---

## Statement

Let $F \colon \mathcal{C} \to \mathcal{D}$ be a functor.

1. If $G$ and $G'$ from $\mathcal{D}$ to $\mathcal{C}$ are both [[right adjoint|TZHF6ZM92S]] to $F$, then there is a natural isomorphism $G \cong G'$.
2. Dually, if $F$ and $F'$ from $\mathcal{C}$ to $\mathcal{D}$ are both left adjoint to a functor $G$, then $F \cong F'$.

## Remarks

For each $d$, the adjunctions give bijections $\Hom(c, G d) \cong \Hom(F c, d) \cong \Hom(c, G' d)$, natural in $c$.
By the Yoneda lemma, these come from a unique isomorphism $G d \cong G' d$.
Naturality in $d$ makes these isomorphisms a [[natural isomorphism|KYCPCC57FT]].
The isomorphism is the unique one compatible with the two adjunctions.

Example: the free group on a set can be built from reduced words or as a quotient of a free monoid.
Both constructions are left adjoint to the forgetful functor, so they give isomorphic functors.
Likewise the abelianization $H \mapsto H/[H, H]$ is determined up to isomorphism by being left adjoint to the inclusion of abelian groups into groups.

## Explanations

### L1 human

An adjoint of a functor, when it exists, is unique up to isomorphism.
So it does not matter which construction one uses for a free object or a quotient, as long as it has the right universal property.
This is why one may speak of the left adjoint of a functor.

### L2 human

The proposition is a form of the uniqueness of objects with a universal property, applied object by object.
It lets one define a functor by asking that it be an adjoint, as for the tensor product, the abelianization or the Stone–Čech compactification.
It also shows that adjunctions compose up to isomorphism: if $F \dashv G$ and $F' \dashv G'$, then $F' F \dashv G G'$, and any other left adjoint of $G G'$ is isomorphic to $F' F$.
