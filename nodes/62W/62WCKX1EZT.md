---
tag: 62WCKX1EZT
kind: definition
name: Locale
msc: [06D22, 18F70, 54A05]
defines: G2QNFT210W
uses: [306PWGH7BF, 0CQHFPGJ45, 02BH3MCBQB, 0X3WGX95FE, 4N4DNDR22Z, CYEMGH98WN]
sources:
  - url: https://en.wikipedia.org/wiki/Pointless_topology
---

## Definition

The category of *locales* is the opposite of the category of [[frames|306PWGH7BF]] and frame homomorphisms.
So a *locale* $X$ is given by a frame $\mathcal{O}(X)$, and a *locale map* $f \colon X \to Y$ is a frame homomorphism $f^* \colon \mathcal{O}(Y) \to \mathcal{O}(X)$.

## Remarks

Example: each [[topological space|0CQHFPGJ45]] $X$ gives the locale with frame $\Omega(X)$ of [[open sets|02BH3MCBQB]].
Each [[continuous map|0X3WGX95FE]] $f \colon X \to Y$ gives the locale map with $f^* = f^{-1} \colon \Omega(Y) \to \Omega(X)$, since preimages preserve unions and finite intersections.
A point of a locale $X$ is a locale map from the one-point locale, that is, a frame homomorphism $\mathcal{O}(X) \to \set{0, 1}$.
A locale is spatial if it comes from a topological space; the functor $\Omega$ is an equivalence between [[sober spaces|4N4DNDR22Z]] and spatial locales.
Non-example of spatiality: a nontrivial complete Boolean algebra without atoms is a frame with no frame homomorphisms to $\set{0, 1}$.
As a locale it has no points, so it is not spatial.
Locales are the subject of [[pointless topology|CYEMGH98WN]].
