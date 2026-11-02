---
tag: 5R76HPDB8W
kind: definition
name: Monoidal category
msc: [18M05]
defines: M3MSQ3NKAE
uses: [A2DE66937D, 28NQ0KRHD3, AFNE9C4NH6, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Monoidal_category
---

## Definition

A *monoidal category* is a [[category|A2DE66937D]] $\mathcal{C}$ together with the following data:

1. a [[functor|28NQ0KRHD3]] $\otimes \colon \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ on the [[product category|AFNE9C4NH6]], called the tensor product;
2. an object $I$, called the unit object;
3. a natural isomorphism $\alpha$ with components $\alpha_{A,B,C} \colon (A \otimes B) \otimes C \to A \otimes (B \otimes C)$, called the associator;
4. natural isomorphisms $\lambda$ and $\rho$ with components $\lambda_A \colon I \otimes A \to A$ and $\rho_A \colon A \otimes I \to A$, called the left and right unitors.

Here natural means natural as a [[natural transformation|KYCPCC57FT]] in each object variable.
These data must satisfy two axioms for all objects $A, B, C, D$:

1. pentagon: $(\id_A \otimes \alpha_{B,C,D}) \circ \alpha_{A, B \otimes C, D} \circ (\alpha_{A,B,C} \otimes \id_D) = \alpha_{A,B,C \otimes D} \circ \alpha_{A \otimes B, C, D}$ as morphisms $((A \otimes B) \otimes C) \otimes D \to A \otimes (B \otimes (C \otimes D))$;
2. triangle: $(\id_A \otimes \lambda_B) \circ \alpha_{A,I,B} = \rho_A \otimes \id_B$ as morphisms $(A \otimes I) \otimes B \to A \otimes B$.

## Remarks

Example: $\mathbf{Set}$ with the Cartesian product $A \times B$, a one-point set $I = \set{*}$, $\alpha((a,b),c) = (a,(b,c))$, $\lambda(*,a) = a$ and $\rho(a,*) = a$.
Both sides of the pentagon send $(((a,b),c),d)$ to $(a,(b,(c,d)))$, and both sides of the triangle send $((a,*),b)$ to $(a,b)$.
Non-example: on the category of $\R$-vector spaces with $\otimes$ the usual tensor product, take $\alpha$ to be $-1$ times the usual associator and the usual unitors.
For nonzero spaces the pentagon then fails: its left side contains three copies of $\alpha$ and its right side two, so the two sides differ by the sign $-1$.
A monoidal category is *strict* when $\alpha$, $\lambda$ and $\rho$ are identities.
