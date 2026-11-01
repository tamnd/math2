---
tag: 78GT1VFFPR
kind: definition
name: Complete local ring
msc: [13J10]
defines: G9Q61B8A7C
uses: [MZ02BKPHJA, 0670T59HGE, NS84D2920R, 2VF2TSJ3PY, 033WGN00BF]
sources:
  - url: https://en.wikipedia.org/wiki/Completion_of_a_ring
---

## Definition

Let $(R, \mathfrak m)$ be a [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]].
The ring $R$ is *complete* if the natural map $R \to \hat R = \varprojlim_n R/\mathfrak m^n$ to its [[$\mathfrak m$-adic completion|NS84D2920R]] is an isomorphism.

## Remarks

Equivalently, $R$ is Hausdorff for the [[$\mathfrak m$-adic topology|2VF2TSJ3PY]] and every Cauchy sequence for this topology converges; for Noetherian local rings the Hausdorff condition always holds by the Krull intersection theorem.
Example: the ring $k[\![x]\!]$ of [[formal power series|033WGN00BF]] over a field $k$ is complete: a compatible sequence of truncations modulo $x^n$ defines a unique series.
Non-example: $R = \Q[x]_{(x)}$ is a Noetherian local ring that is not complete; its completion $\Q[\![x]\!]$ is uncountable while $R$ is countable, so $R \to \hat R$ is not surjective.
The completion $\hat R$ of any Noetherian local ring is a complete Noetherian local ring with maximal ideal $\mathfrak m \hat R$.
