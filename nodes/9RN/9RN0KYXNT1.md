---
tag: 9RN0KYXNT1
kind: statement
role: theorem
name: Łoś–Tarski preservation theorem
msc: ["03C40", "03C52"]
uses: [92SWXST1ZM, MVCH6N9SNW, 676H7EGTKJ, ZSTEZ3PRT9, 1NR3HAWG9D]
about: [ZSTEZ3PRT9, MEC3ZMC4F1]
sources:
  - url: https://en.wikipedia.org/wiki/Łoś–Tarski_preservation_theorem
same_as:
  wikidata: Q8080822
  wikipedia: Łoś–Tarski preservation theorem
---

## Statement

Let $\sigma$ be a first-order signature and let $T$ be a first-order [[theory|92SWXST1ZM]] in $\sigma$.
Then the following are equivalent.

1. The class of [[models|MVCH6N9SNW]] of $T$ is closed under [[substructures|676H7EGTKJ]]: if $B \models T$ and $A$ is a substructure of $B$, then $A \models T$.
2. There is a set $U$ of universal sentences of $\sigma$ with the same models as $T$; so the models of $T$ form a [[universal class|ZSTEZ3PRT9]].

## Remarks

The direction from 2 to 1 holds because universal sentences pass from a structure to its substructures.
For the other direction, let $U$ be the set of universal sentences that follow from $T$, and let $A \models U$.
Expand the signature by a constant for each element of $A$, and let $D$ be the set of quantifier-free sentences true in $A$, its diagram.
If $T \cup D$ had no model, then by the [[compactness theorem|1NR3HAWG9D]] $T$ would prove the negation of a finite conjunction from $D$.
Replacing the new constants by variables gives a universal sentence in $U$ that fails in $A$.
So $T \cup D$ has a model $B$, into which $A$ embeds, and condition 1 gives $A \models T$.

A version for formulas holds too: a formula is preserved by substructures between models of $T$ exactly when it is equivalent modulo $T$ to a universal formula.
Dually, the class of models of $T$ is closed under extensions exactly when $T$ is equivalent to a set of existential sentences.

Example: the theory of groups in the signature $(\cdot, {}^{-1}, e)$ is closed under substructures, and the group axioms are indeed universal.
In the signature $(\cdot)$ alone, a substructure of a group is only a subsemigroup, such as $\N_{>0}$ in $(\Z, +)$, and the axioms of groups in this signature need existential quantifiers.

The theorem uses compactness, and it fails when only finite structures are considered.

## Explanations

### L1 human

A universal axiom says that something holds for all elements, without asking for any element to exist.
Such axioms survive passing to a part of a structure.
The theorem says the converse: if a first-order axiom system always survives passing to parts, then it can be rewritten with universal axioms only.
So a semantic property, closure under substructures, matches a syntactic one, the shape of the axioms.

### L2 human

The Łoś–Tarski theorem is the first of the preservation theorems of model theory.
Others in the same spirit are the Chang–Łoś–Suszko theorem, for unions of chains and $\forall\exists$ sentences, and Lyndon's theorem, for homomorphic images and positive sentences.
In universal algebra it explains why an elementary class of algebras closed under subalgebras has a universal axiomatization.
This is a first step towards the descriptions of quasivarieties and varieties.
The proof method, realizing the diagram of a structure in a model of $T$, is the method of diagrams used throughout model theory.
