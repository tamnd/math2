---
tag: WB8GGAWQNP
kind: definition
name: K-theory
msc: [19A99, 18F30]
defines: ZT11JGCWX0
uses: [B2VP96NJSK, 0N6R902FG1, 5FDMY7PDYY]
sources:
  - url: https://en.wikipedia.org/wiki/K-theory
---

## Definition

Let $\mathcal{C}$ be an [[additive category|B2VP96NJSK]] whose isomorphism classes of objects form a set.
The isomorphism classes form a commutative [[monoid|0N6R902FG1]] $\mathrm{Iso}(\mathcal{C})$, with sum $[A] + [B] = [A \oplus B]$ and zero element the class of the zero object.
The group $K_0(\mathcal{C})$ is the [[Grothendieck group|5FDMY7PDYY]] of this monoid.
*K-theory* is the study of $K_0(\mathcal{C})$ and of the higher groups $K_n(\mathcal{C})$ that extend it, for categories $\mathcal{C}$ of vector bundles, projective modules or projections.

## Remarks

Every element of $K_0(\mathcal{C})$ is a difference $[A] - [B]$.
Two objects have the same class exactly when $A \oplus C \cong B \oplus C$ for some object $C$.

Example: let $\mathcal{C}$ be the category of finite-dimensional vector spaces over a field $F$.
Two such spaces are isomorphic exactly when they have the same dimension, and $\dim(V \oplus W) = \dim V + \dim W$.
So $\mathrm{Iso}(\mathcal{C}) \cong \N$ and $K_0(\mathcal{C}) \cong \Z$.

Non-example: the monoid $\mathrm{Iso}(\mathcal{C})$ alone is not the K-group.
For vector spaces it is $\N$, which has no negatives; the group completion is needed to get $\Z$.

The three classical instances are these.
For a ring $R$ and the category of finitely generated projective $R$-modules one gets [[$K_0(R)$|Q14JS2MA1C]].
For a compact Hausdorff space $X$ and the category of complex vector bundles on $X$ one gets the [[topological K-theory|6XCFW7YGX8]] group $K^0(X)$.
For a unital C*-algebra and its projections one gets [[operator K-theory|DQZ8S67ZE6]].
