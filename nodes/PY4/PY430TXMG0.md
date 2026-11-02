---
tag: PY430TXMG0
kind: concept
name: Monoidal functor
msc: [18M05, 18A22]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Monoidal_functor
same_as:
  wikidata: Q6901642
  wikipedia: Monoidal functor
---

## Summary

A monoidal functor is a [[functor|28NQ0KRHD3]] between [[monoidal categories|M3MSQ3NKAE]] that is compatible with the tensor products and units.
It comes with maps $F(A) \otimes F(B) \to F(A \otimes B)$ and $I \to F(I)$ that respect the associators and unitors.
When these maps are isomorphisms the functor is called strong, and when they are identities it is called strict.
Monoidal functors send monoid objects to monoid objects, and they are the morphisms of the category of monoidal categories.

## Explanations

### L1 human

A monoidal functor translates one "side-by-side" world into another.
It gives a way to combine the images of $A$ and $B$ into the image of $A \otimes B$, in a way that ignores how the brackets are placed.
For example, the free vector space functor sends a product of sets $X \times Y$ to a space isomorphic to $k[X] \otimes k[Y]$.
The forgetful functor from abelian groups to sets is monoidal in the weaker sense: there is a map $(a, b) \mapsto a \otimes b$ from $A \times B$ to $A \otimes B$, but it is not a bijection.
