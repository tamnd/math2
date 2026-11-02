---
tag: YV297TR3SC
kind: definition
name: Classifying topos
msc: [18F10, 03G30, 18B25]
defines: 85ZZ921DWH
uses: [S3YVE24AQK, N5R1WAEPFB, K7A04ZBD92]
sources:
  - url: https://en.wikipedia.org/wiki/Classifying_topos
---

## Definition

Let $\mathbb{T}$ be a geometric theory.
This is a first-order theory whose axioms are sequents between formulas built from finite conjunctions, arbitrary disjunctions and existential quantifiers.
For a [[Grothendieck topos|S3YVE24AQK]] $\mathcal{E}$, let $\mathbb{T}\text{-}\mathrm{Mod}(\mathcal{E})$ be the category of models of $\mathbb{T}$ in $\mathcal{E}$.
For Grothendieck toposes $\mathcal{E}$ and $\mathcal{F}$, let $\mathbf{Geom}(\mathcal{E}, \mathcal{F})$ be the category of [[geometric morphisms|N5R1WAEPFB]] $\mathcal{E} \to \mathcal{F}$, and write $f^*$ for the inverse image part of $f$.
A *classifying topos* of $\mathbb{T}$ is a Grothendieck topos $\mathbf{Set}[\mathbb{T}]$ together with a model $U_{\mathbb{T}}$ of $\mathbb{T}$ in it with the following property.
For every Grothendieck topos $\mathcal{E}$ the functor
$$\mathbf{Geom}(\mathcal{E}, \mathbf{Set}[\mathbb{T}]) \to \mathbb{T}\text{-}\mathrm{Mod}(\mathcal{E}), \qquad f \mapsto f^*(U_{\mathbb{T}})$$
is an [[equivalence of categories|K7A04ZBD92]].
The model $U_{\mathbb{T}}$ is called the generic model of $\mathbb{T}$.

## Remarks

Example: let $\mathbb{O}$ be the theory with one sort, no symbols and no axioms, so that a model of $\mathbb{O}$ in $\mathcal{E}$ is just an object of $\mathcal{E}$.
The functor category $[\mathbf{FinSet}, \mathbf{Set}]$, with the inclusion functor as generic model, is a classifying topos for $\mathbb{O}$; it is called the object classifier.
Non-example: $\mathbf{Set}$ is not a classifying topos for $\mathbb{O}$.
For every Grothendieck topos $\mathcal{E}$ there is, up to isomorphism, only one geometric morphism $\mathcal{E} \to \mathbf{Set}$, while $\mathcal{E}$ has in general many non-isomorphic objects.
Every geometric theory has a classifying topos, and it is unique up to equivalence.
For a discrete group $G$, the topos of $G$-sets classifies $G$-torsors.
