---
tag: G206NVQYVD
kind: definition
name: Section and retraction
msc: [18A20]
defines: DXJH3DGXBC
uses: [A2DE66937D, 859F0TFVA3, Y2NP1JFR86, RVXDSY04KG, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Section_(category_theory)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $f \colon A \to B$ and $r \colon B \to A$ be [[morphisms|859F0TFVA3]] of $\mathcal{C}$ with $r \circ f = 1_A$.
Then $f$ is a *section* of $r$, and $r$ is a *retraction* of $f$.
A morphism that has a retraction is a *split monomorphism*.
A morphism that has a section is a *split epimorphism*.

## Remarks

Every split monomorphism is a [[monomorphism|Y2NP1JFR86]]: if $f \circ g_1 = f \circ g_2$, then $g_1 = r \circ f \circ g_1 = r \circ f \circ g_2 = g_2$.
Dually, every split epimorphism is an [[epimorphism|RVXDSY04KG]].
Example: in the category of sets, the inclusion $f \colon \set{0} \to \set{0, 1}$ and the constant map $r \colon \set{0, 1} \to \set{0}$ satisfy $r \circ f = 1_{\set{0}}$.
Non-example: in the category of [[abelian groups|082GHNPJ53]], the map $f \colon \Z \to \Z$, $f(x) = 2x$, is a monomorphism but not a split monomorphism.
A retraction $r$ would satisfy $r(2) = 1$, so $2 r(1) = 1$ in $\Z$, which is impossible.
A morphism is an isomorphism exactly when it is both a split monomorphism and an epimorphism.
In the category of sets, the statement that every surjection is a split epimorphism is equivalent to the axiom of choice.
