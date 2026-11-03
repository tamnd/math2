---
tag: JN0XPZB213
kind: definition
name: Schur multiplier
msc: [19C09, 20J06, 20C25]
defines: AZDECAWGD0
uses: [G5S1M9, CFAG3VRXEA]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_multiplier
---

## Definition

Let $G$ be a [[group|G5S1M9]].
The *Schur multiplier* of $G$ is the abelian group
$$M(G) = H_2(G, \Z),$$
the second [[homology group|CFAG3VRXEA]] of $G$ with coefficients in $\Z$ with the trivial action.

## Remarks

By Hopf's formula, if $G \cong F/R$ with $F$ a free group and $R$ a normal subgroup, then $M(G) \cong (R \cap [F, F])/[F, R]$.
For a finite group $G$, $M(G)$ is finite and isomorphic to $H^2(G, \C^\times)$, with $\C^\times$ under multiplication and the trivial action.

Example: for a cyclic group $G = \Z/m\Z$, take $F = \Z$ and $R = m\Z$.
Then $[F, F]$ is trivial, so $M(\Z/m\Z) = 0$.

Example: $M(\Z^2) \cong \Z$, and for the Klein four-group, $M(\Z/2\Z \times \Z/2\Z) \cong \Z/2\Z$.

Non-example: the first homology group $H_1(G, \Z)$ is the abelianization $G/[G, G]$, not the multiplier.
For $G = \Z/m\Z$ with $m \ge 2$ it is $\Z/m\Z$, while $M(G) = 0$.

If $G$ is perfect, $M(G)$ is the kernel of the universal central extension of $G$.
