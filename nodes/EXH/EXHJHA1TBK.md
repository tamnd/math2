---
tag: EXHJHA1TBK
kind: definition
name: Quillen equivalence
msc: [18N40, 55U35]
defines: KZCXHTEYK7
sources:
  - url: https://en.wikipedia.org/wiki/Quillen_adjunction
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be [[model categories|SDTZVZ6B4Q]], and let $F \colon \mathcal{C} \rightleftarrows \mathcal{D} \colon G$ be a [[Quillen adjunction|SY38F954FE]], with $F$ [[left adjoint|TZHF6ZM92S]] to $G$.
For $X$ in $\mathcal{C}$ and $Y$ in $\mathcal{D}$, write $g^\flat \colon X \to GY$ for the adjoint of a map $g \colon FX \to Y$.
The adjunction is a *Quillen equivalence* if the following holds for every cofibrant object $X$ of $\mathcal{C}$ and every fibrant object $Y$ of $\mathcal{D}$.
A map $g \colon FX \to Y$ is a weak equivalence in $\mathcal{D}$ if and only if $g^\flat$ is a weak equivalence in $\mathcal{C}$.

## Remarks

Equivalently, the derived adjunction $\mathbf{L}F \colon \operatorname{Ho}(\mathcal{C}) \rightleftarrows \operatorname{Ho}(\mathcal{D}) \colon \mathbf{R}G$ is an [[equivalence of categories|K7A04ZBD92]].

Example: geometric realization $\abs{\cdot}$ from simplicial sets to topological spaces is left adjoint to the singular complex functor $\operatorname{Sing}$.
It is a Quillen equivalence between the Kan–Quillen model structure and the Quillen model structure.
Every simplicial set is cofibrant and every space is fibrant.
The check reduces to two facts: the unit $K \to \operatorname{Sing}\abs{K}$ is a weak equivalence, and the counit $\abs{\operatorname{Sing} Y} \to Y$ is a weak homotopy equivalence.

Non-example: give the category of sets the model structure whose weak equivalences are the bijections and in which every map is a cofibration and a fibration.
The functor $\pi_0$ from simplicial sets to sets is left adjoint to the functor that sends a set to the discrete simplicial set on it.
This is a Quillen adjunction.
It is not a Quillen equivalence.
Take the simplicial circle $K = \Delta^1 / \partial \Delta^1$; the identity map of the one-point set $\pi_0 K$ is a bijection.
Its adjoint $K \to \Delta^0$ is not a weak equivalence, since $\abs{K}$ is a circle.
