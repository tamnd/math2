---
tag: 3S2BKJKC7R
kind: definition
name: Spectral synthesis
msc: [43A45, 43A20]
defines: JBHTE03V78
uses: [ZR09S9R3AW, FMW57WNPDB, 6GD25S53ND, VHN5VW5Q92, V20376HXHD]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%27s_Tauberian_theorem
---

## Definition

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] with [[Pontryagin dual|FMW57WNPDB]] $\widehat{G}$, and let $L^1(G)$ be its [[group algebra|6GD25S53ND]].
For $f \in L^1(G)$ let $\widehat{f}$ be its [[Fourier transform|VHN5VW5Q92]].

1. The *hull* of a closed ideal $I$ of $L^1(G)$ is $Z(I) = \set{\chi \in \widehat{G} : \widehat{f}(\chi) = 0 \text{ for all } f \in I}$.
2. For a closed set $E \subseteq \widehat{G}$, let $I(E) = \set{f \in L^1(G) : \widehat{f}(\chi) = 0 \text{ for all } \chi \in E}$, a closed ideal with hull $E$.
3. A closed set $E \subseteq \widehat{G}$ is a *set of spectral synthesis* if $I(E)$ is the only closed ideal of $L^1(G)$ whose hull is $E$.

*Spectral synthesis holds* for $G$ if every closed subset of $\widehat{G}$ is a set of spectral synthesis.

## Remarks

Every closed ideal $I$ with hull $E$ satisfies $I \subseteq I(E)$, so $E$ is a set of synthesis exactly when $I(E)$ is the smallest closed ideal with hull $E$.
The hull of $I(E)$ is $E$ because $L^1(G)$ is a regular algebra: for $\chi \notin E$ there is $f$ whose transform vanishes on $E$ but not at $\chi$.

Example: $E = \emptyset$ is a set of synthesis.
Here $I(\emptyset) = L^1(G)$, and [[Wiener's Tauberian theorem|V20376HXHD]] says that a closed ideal whose transforms have no common zero is all of $L^1(G)$.

Example: if $G$ is compact, then $\widehat{G}$ is discrete and spectral synthesis holds for $G$.

Non-example: for $G = \R^3$, the unit sphere in $\widehat{\R^3} \cong \R^3$ is not a set of spectral synthesis, by a result of Laurent Schwartz.

Other names are a set of synthesis and a set that admits spectral synthesis.
