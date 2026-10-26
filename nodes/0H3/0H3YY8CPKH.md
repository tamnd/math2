---
tag: 0H3YY8CPKH
kind: object
name: Euclidean group
msc: [20H15]
instance_of: [G5S1M9]
uses: [0J1N3WTKM4, 087VJM5Q77]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euclidean_group
    locator: Direct and indirect isometries
  - url: https://en.wikipedia.org/wiki/Translation_(geometry)
    locator: As a group
same_as:
  wikidata: Q852195
  wikipedia: Euclidean group
---

## Description

The Euclidean group $\mathrm{E}(n)$ is the set of all [[Euclidean isometries|0J1N3WTKM4]] of $\mathbb{R}^n$, with the composition of maps as the operation. It is a [[group|G5S1M9]]: the identity map is the neutral element, and the inverse of an isometry is an isometry.
Each element has the form $x \mapsto A x + b$, with $A$ in the orthogonal group $\mathrm{O}(n)$ and $b \in \mathbb{R}^n$.
The direct isometries, with $\det A = 1$, form a subgroup $\mathrm{SE}(n)$ of index $2$. Its elements are the rigid motions.

## Remarks

The [[translations|087VJM5Q77]] form an abelian normal subgroup $T \cong \mathbb{R}^n$, and $\mathrm{E}(n) / T \cong \mathrm{O}(n)$.
The group $\mathrm{E}(n)$ has $n(n+1)/2$ degrees of freedom: $3$ for $n = 2$ and $6$ for $n = 3$.
The group is not abelian for $n \geq 2$. For example, a rotation about the origin and a translation do not commute in general.
The symmetry group of each figure in $\mathbb{R}^n$ is a subgroup of $\mathrm{E}(n)$.

## Explanations

### L1 human

The Euclidean group collects all the ways to move space without changing distances. Two such moves done one after the other give again such a move, and each move can be undone. In the plane, three numbers fix a direct move: two for a shift and one for a turn.
