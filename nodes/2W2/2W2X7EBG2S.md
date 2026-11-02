---
tag: 2W2X7EBG2S
kind: statement
role: theorem
name: Mac Lane's coherence theorem
msc: [18M05, 18N20]
uses: [M3MSQ3NKAE, XM4NTS5BGG, WV898P4X16, PY430TXMG0, K7A04ZBD92]
about: [M3MSQ3NKAE]
sources:
  - url: https://en.wikipedia.org/wiki/Coherency_(homotopy_theory)
---

## Statement

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a [[monoidal category|M3MSQ3NKAE]].
Call a formal word any expression built from variables $x_1, x_2, \ldots$ and the unit $I$ with the binary operation $\otimes$.
Call a formal morphism between two words any composite of formal instances of $\alpha$, $\lambda$, $\rho$ and their inverses, tensored on both sides with identities.

1. Any two formal morphisms between the same two words are equal after every substitution of objects of $\mathcal{C}$ for the variables. In other words, every formal [[diagram|WV898P4X16]] built from $\alpha$, $\lambda$ and $\rho$ commutes.
2. $\mathcal{C}$ is equivalent, by a strong [[monoidal functor|PY430TXMG0]] that is an [[equivalence of categories|K7A04ZBD92]], to a strict monoidal category.

## Remarks

Proof idea for part 1: every word can be moved by a formal morphism to a normal form.
For example, the normal form can put all brackets to the right and remove all copies of $I$.
One shows that any two such moves to normal form are equal, using the [[pentagon identity|XM4NTS5BGG]] and the triangle identity to compare the possible first steps.
Then any formal morphism $u \to v$ equals the composite of the move $u \to$ normal form and the inverse of the move $v \to$ normal form.
Equivalently, the free monoidal category on a set of variables is a preorder.

The word "formal" is necessary.
A diagram of instances of $\alpha$, $\lambda$, $\rho$ on actual objects may fail to commute.
This can happen when the diagram only makes sense because two different words give equal objects, for example when $A \otimes B = C$ holds in $\mathcal{C}$.
Formal diagrams track each variable, so such accidental identifications are not allowed.

## Explanations

### L1 human

In a monoidal category, brackets and unit objects can be moved around using fixed isomorphisms.
The theorem says that it never matters which route of such moves one takes: all routes give the same isomorphism.
So one may safely write $A \otimes B \otimes C$ without brackets, as for an ordinary associative product.

### L2 human

Coherence is what makes calculations in monoidal categories practical: it justifies string diagrams and the habit of pretending that the tensor product is strictly associative.
It reduces infinitely many coherence conditions to the two axioms of the definition, the pentagon and the triangle.
For braided monoidal categories the analogous statement says that formal diagrams commute when they have the same underlying braid; for symmetric ones, when they have the same underlying permutation.
