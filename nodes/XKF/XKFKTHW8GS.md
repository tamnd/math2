---
tag: XKFKTHW8GS
kind: definition
name: Quillen adjunction
msc: [18N40, 55U35]
defines: SY38F954FE
uses: [SDTZVZ6B4Q, TZHF6ZM92S, HSV1J7BJXX, E2870TEDG7, 48QQ7T98Z9, TG6WHHR7CF, RWBMXQW6S5]
sources:
  - url: https://en.wikipedia.org/wiki/Quillen_adjunction
---

## Definition

Let $\mathcal{M}$ and $\mathcal{N}$ be [[model categories|SDTZVZ6B4Q]], and let $F \colon \mathcal{M} \rightleftarrows \mathcal{N} \colon G$ be an [[adjunction|TZHF6ZM92S]] with $F$ left adjoint to $G$.
The adjunction is a *Quillen adjunction* if the following equivalent conditions hold.

1. $F$ preserves [[cofibrations|HSV1J7BJXX]] and trivial cofibrations.
2. $G$ preserves fibrations and trivial fibrations.
3. $F$ preserves cofibrations and $G$ preserves fibrations.

Then $F$ is called a *left Quillen functor* and $G$ a *right Quillen functor*.

## Remarks

For an adjunction, $F(i)$ has the left lifting property against $p$ if and only if $i$ has the left lifting property against $G(p)$.
Since the classes of a model structure are characterized by lifting properties, the three conditions are equivalent.

A Quillen adjunction induces an adjunction $\mathbf{L}F \dashv \mathbf{R}G$ between the [[homotopy categories|48QQ7T98Z9]].
Here $\mathbf{L}F$ is computed by applying $F$ to a cofibrant replacement, and $\mathbf{R}G$ by applying $G$ to a fibrant replacement.
This works because $F$ sends [[weak equivalences|E2870TEDG7]] between cofibrant objects to weak equivalences, by Ken Brown's lemma.

Example: [[geometric realization|TG6WHHR7CF]] $\abs{-}$ from simplicial sets to topological spaces is left adjoint to the [[singular simplicial set|RWBMXQW6S5]] functor $\mathrm{Sing}$.
With the Kan–Quillen and Quillen model structures, $\mathrm{Sing}$ sends Serre fibrations to Kan fibrations and trivial ones to trivial ones, so the pair is a Quillen adjunction.

Non-example: let $\mathcal{M}$ and $\mathcal{N}$ both be the category of sets.
Give $\mathcal{M}$ the trivial model structure: $W$ the bijections, and all maps fibrations and cofibrations.
Give $\mathcal{N}$ the model structure with $W$ all maps, cofibrations the bijections, and fibrations all maps.
The identity adjunction fails clause 1, since a non-bijective map is a cofibration of $\mathcal{M}$ but not of $\mathcal{N}$.
