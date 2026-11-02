---
tag: HSQJSK4E23
kind: definition
name: Additive functor
msc: ["18E05"]
defines: KAN07YC9T2
uses: [SC6FD5F4J0, 28NQ0KRHD3, B2VP96NJSK, BZEJKTQ76T, 082GHNPJ53, F0HQXQ0HCD]
sources:
  - url: https://en.wikipedia.org/wiki/Preadditive_category
    locator: Additive functors
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be [[preadditive categories|SC6FD5F4J0]].
A [[functor|28NQ0KRHD3]] $F \colon \mathcal{C} \to \mathcal{D}$ is *additive* if $F(f + g) = F(f) + F(g)$ for all objects $X, Y$ of $\mathcal{C}$ and all $f, g \colon X \to Y$.
Equivalently, each map $\Hom_{\mathcal{C}}(X, Y) \to \Hom_{\mathcal{D}}(FX, FY)$, $f \mapsto F(f)$, is a homomorphism of abelian groups.

## Remarks

An additive functor sends zero morphisms to zero morphisms and zero objects to zero objects.
If $\mathcal{C}$ and $\mathcal{D}$ are [[additive categories|B2VP96NJSK]], a functor is additive if and only if it preserves binary [[biproducts|BZEJKTQ76T]].

Example: for a fixed [[abelian group|082GHNPJ53]] $A$, the functor $\Hom(A, -)$ from abelian groups to abelian groups is additive.
For $f, g \colon X \to Y$ and $u \colon A \to X$, one has $(f + g) \circ u = f \circ u + g \circ u$.
Likewise the [[tensor product|F0HQXQ0HCD]] functor $- \otimes A$ is additive.

Non-example: the functor $X \mapsto X \otimes X$, $f \mapsto f \otimes f$, on abelian groups is not additive.
On $X = \Z$, with $\Z \otimes \Z = \Z$, the morphism $\id + \id = 2$ goes to multiplication by $4$, while $F(\id) + F(\id)$ is multiplication by $2$.
