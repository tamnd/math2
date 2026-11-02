---
tag: 6GSTSR4V09
kind: example
name: Category of rings
msc: [16B50, 13B10, 18A05]
instance_of: [A2DE66937D]
uses: [0B1261B5ED, 0VTH8KPCG2]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_rings
same_as:
  wikidata: Q5051859
  wikipedia: Category of rings
---

## Example

The *category of rings* $\mathbf{Ring}$ has the [[rings|0B1261B5ED]] with identity as objects and the [[ring homomorphisms|0VTH8KPCG2]] that send $1$ to $1$ as morphisms.
Composition is the composition of maps, and the identity of $R$ is $\id_R$.
This is a [[category|A2DE66937D]].
A composite of two maps that preserve sums, products and $1$ again preserves them, and identity maps preserve them, so composites and identities are morphisms.
Composition of maps is associative.

## Remarks

The ring $\Z$ is an [[initial object|EK85VSSRMR]]: for each ring $R$ the only homomorphism $\Z \to R$ sends $n$ to $n \cdot 1_R$.
The zero ring is a terminal object, since every ring has exactly one map to it.
The zero ring is not initial, because a homomorphism from it must send $1 = 0$ to $1_R = 0_R$, which fails when $R$ is nonzero; so $\mathbf{Ring}$ has no zero object.
The [[product|S5744QZV4N]] is the direct product $R \times S$ with componentwise operations.
The commutative rings form a full subcategory $\mathbf{CRing}$, in which the [[coproduct|4FJ0S71P58]] of $R$ and $S$ is the tensor product $R \otimes_{\Z} S$.
The inclusion $\Z \to \Q$ is an epimorphism of $\mathbf{Ring}$ that is not surjective: two homomorphisms out of $\Q$ that agree on $\Z$ agree on all fractions $m/n$.

## Explanations

### L1 human

The category of rings collects all rings and the maps between them that respect addition, multiplication and the unit.
The integers sit at the start of this category, since every ring receives exactly one map from $\Z$.
For example, reduction modulo $5$ is a morphism $\Z \to \Z/5\Z$.
