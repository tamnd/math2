---
tag: PT8PN4CS1H
kind: definition
name: Quasi-coherent sheaf
msc: [14F06]
defines: KPKND0K7W6
uses: [5A35TYZD02, B3V3XJ2W8G, S33B2H3MYD, 0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_sheaf
---

## Definition

Let $A$ be a ring and $M$ an $A$-[[module|0NZ8JA25WK]].
For $f \in A$, let $D(f)$ be the basic open set of $\operatorname{Spec} A$ where $f$ does not vanish.
The sheaf $\widetilde{M}$ on $\operatorname{Spec} A$ is the unique sheaf of modules with $\widetilde{M}(D(f)) = M_f$ for every $f \in A$, with restriction maps given by localization.
Let $X$ be a [[scheme|5A35TYZD02]].
A [[sheaf of $\mathcal{O}_X$-modules|S33B2H3MYD]] $\mathcal{F}$ is *quasi-coherent* if $X$ has a cover by open sets $U$ with the following property.
Each $U$ is an [[affine scheme|B3V3XJ2W8G]] $\operatorname{Spec} A$, and $\mathcal{F}|_U \cong \widetilde{M}$ for some $A$-module $M$.

## Remarks

On $X = \operatorname{Spec} A$, the sheaf $\widetilde{I}$ of an ideal $I \subseteq A$ is quasi-coherent, with the cover by $X$ itself.
Let $R$ be a discrete valuation ring with fraction field $K$, and $X = \operatorname{Spec} R = \set{\eta, s}$, with $\eta$ the generic point.
The sheaf $\mathcal{F}$ with $\mathcal{F}(X) = 0$ and $\mathcal{F}(\set{\eta}) = K$ is an $\mathcal{O}_X$-module but is not quasi-coherent.
The only open set containing $s$ is $X$, so $\mathcal{F} \cong \widetilde{M}$ would force $M = \mathcal{F}(X) = 0$ and then $\mathcal{F}(\set{\eta}) = 0$.
If $\mathcal{F}$ is quasi-coherent, then $\mathcal{F}|_U \cong \widetilde{\mathcal{F}(U)}$ for every affine open $U$, not only for those of the chosen cover.
On a general ringed space, $\mathcal{F}$ is called quasi-coherent if it is locally the cokernel of a map between free modules; on schemes the two definitions agree.
