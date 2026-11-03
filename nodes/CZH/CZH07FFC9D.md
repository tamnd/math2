---
tag: CZH07FFC9D
kind: definition
name: Univalence axiom
msc: [03B38, 55U35, 03F55]
defines: A53TSXZTW5
uses: [ESVYD9CZ8C, M6W6ZB4PPX, EPAAKD80H9]
sources:
  - url: https://en.wikipedia.org/wiki/Univalent_foundations
---

## Definition

Work in [[Martin-Löf type theory|ESVYD9CZ8C]] with [[dependent types|M6W6ZB4PPX]] $\Pi$ and $\Sigma$, identity types $x =_A y$ and a universe $\mathcal{U}$.
For $f, g : \Pi_{x : A} B(x)$, write $f \sim g$ for the type $\Pi_{x : A} (f\, x = g\, x)$.
A function $f : A \to B$ is an *equivalence* if the type
$$\mathrm{isequiv}(f) = \Big(\Sigma_{g : B \to A}\, g \circ f \sim \mathrm{id}_A\Big) \times \Big(\Sigma_{h : B \to A}\, f \circ h \sim \mathrm{id}_B\Big)$$
has a term, and $A \simeq B$ is the type $\Sigma_{f : A \to B} \mathrm{isequiv}(f)$.
For $A, B : \mathcal{U}$, let $\mathrm{idtoeqv} : (A =_{\mathcal{U}} B) \to (A \simeq B)$ be the map defined by path induction that sends $\mathrm{refl}_A$ to the identity equivalence of $A$.
The *univalence axiom* for $\mathcal{U}$ states that for all $A, B : \mathcal{U}$, the map $\mathrm{idtoeqv}$ is an equivalence.

## Remarks

Example: Voevodsky's model of type theory in Kan simplicial sets, where types are Kan complexes and identity types are path spaces, satisfies the univalence axiom.
So the axiom is consistent relative to the set theory in which this model is built.

Non-example: consider type theory with uniqueness of identity proofs, which says that any two terms of $x =_A y$ are equal.
It does not satisfy univalence for a universe containing the booleans $\mathbf{2}$.
Univalence would turn the swap $\mathbf{2} \simeq \mathbf{2}$ and the identity $\mathbf{2} \simeq \mathbf{2}$ into two terms of $\mathbf{2} =_{\mathcal{U}} \mathbf{2}$.
These terms are different because the swap is not the identity, but uniqueness of identity proofs says they are equal.

The inverse of $\mathrm{idtoeqv}$ is often written $\mathrm{ua}$.
Univalence implies function extensionality: two functions $f, g$ with $f \sim g$ are equal.
It is the basic new axiom of [[homotopy type theory|EPAAKD80H9]].
