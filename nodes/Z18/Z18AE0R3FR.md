---
tag: Z18AE0R3FR
kind: definition
name: Duality in category theory
msc: [18A05]
defines: Z5EETTFWAN
uses: [A2DE66937D, DAMK8XE1FR, Y2NP1JFR86, RVXDSY04KG, DXJH3DGXBC, 07JBSZE0V4]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_(category_theory)
---

## Definition

Let $\Sigma$ be a statement in the first-order language of [[categories|A2DE66937D]], built from objects, morphisms, domains, codomains, identities and composition.
The *dual statement* $\Sigma^{\mathrm{op}}$ is obtained from $\Sigma$ by these changes:

1. each domain is replaced by the codomain, and each codomain by the domain;
2. each composite $g \circ f$ is replaced by $f \circ g$.

The *duality principle* states that $\Sigma$ holds in the [[opposite category|DAMK8XE1FR]] $\mathcal{C}^{\mathrm{op}}$ if and only if $\Sigma^{\mathrm{op}}$ holds in $\mathcal{C}$.
In particular, if $\Sigma$ holds in every category, then so does $\Sigma^{\mathrm{op}}$.

## Remarks

Two notions are *dual* when the defining statement of one is the dual of the defining statement of the other.
Example: "$f$ is a [[monomorphism|Y2NP1JFR86]]" says that $f \circ g_1 = f \circ g_2$ implies $g_1 = g_2$.
Its dual says that $g_1 \circ f = g_2 \circ f$ implies $g_1 = g_2$, which is "$f$ is an [[epimorphism|RVXDSY04KG]]".
Hence the fact "a composite of monomorphisms is a monomorphism" gives at once "a composite of epimorphisms is an epimorphism".
Likewise a section and a retraction are dual, as in [[section and retraction|DXJH3DGXBC]].
Non-example: the dual of a statement true in one particular category need not be true in that category.
In the category of sets, every morphism $X \to \emptyset$ is an isomorphism, since $X$ must then be empty.
The dual statement says that every morphism $\set{0} \to X$ out of the one-point set is an isomorphism, and it fails for $X = \set{0, 1}$.
Duality in this sense is different from the duality of vector spaces, although the [[dual space|07JBSZE0V4]] functor turns linear maps around.
