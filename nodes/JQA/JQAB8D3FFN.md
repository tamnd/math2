---
tag: JQAB8D3FFN
kind: definition
name: Reflective subcategory
msc: [18A40]
defines: FC7VB4WSG0
uses: [V3BFGKBJF7, TZHF6ZM92S]
sources:
  - url: https://en.wikipedia.org/wiki/Reflective_subcategory
---

## Definition

Let $\mathcal{C}$ be a category and let $\mathcal{B}$ be a [[full subcategory|V3BFGKBJF7]] of $\mathcal{C}$ with inclusion functor $I \colon \mathcal{B} \to \mathcal{C}$.
$\mathcal{B}$ is *reflective* in $\mathcal{C}$ if $I$ has a [[left adjoint|TZHF6ZM92S]] $R \colon \mathcal{C} \to \mathcal{B}$.
The functor $R$ is called the *reflector*.

## Remarks

Equivalently, every object $c$ of $\mathcal{C}$ has a morphism $\eta_c \colon c \to R c$ with $R c$ in $\mathcal{B}$.
Every morphism $c \to b$ with $b$ in $\mathcal{B}$ must factor through $\eta_c$ in exactly one way.
Some authors also ask $\mathcal{B}$ to be closed under isomorphic objects.
The dual notion is a *coreflective* subcategory.

Example: abelian groups form a reflective subcategory of groups, with reflector $R(H) = H/[H, H]$ and $\eta_H$ the quotient map.
Every homomorphism $H \to A$ with $A$ abelian kills all commutators $x y x^{-1} y^{-1}$, so it factors uniquely through $H/[H, H]$.

Non-example: finite groups do not form a reflective subcategory of groups.
A reflective subcategory closed under isomorphic objects contains every limit, formed in $\mathcal{C}$, of a diagram in $\mathcal{B}$.
But the product of countably many copies of $\Z/2\Z$ is an infinite group.
