---
tag: ZHM0D5JAKJ
kind: definition
name: Brouwerian modal logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
defines: 2QPT4KCM0Q
uses: [JS8W7PA6JK, FDFQFWPM4X, 0X8NMST0J2, 061J5VGSPT]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
---

## Definition

The Brouwerian modal logic $\mathsf{B} = \mathsf{KTB}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains the axioms
$$\mathrm{T}: \square p \to p \qquad \text{and} \qquad \mathrm{B}: p \to \square\lozenge p.$$
The logic $\mathsf{KB}$ is the smallest normal logic that contains $\mathrm{B}$.
A $\mathsf{B}$-frame is a frame whose relation is [[reflexive|0X8NMST0J2]] and [[symmetric|061J5VGSPT]].

## Notation

The letter $\mathsf{B}$ refers to Brouwer, and the logic is also written $\mathsf{KTB}$; the axiom $\mathrm{B}$ is the Brouwerian axiom.
The dual form of the axiom is $\lozenge\square p \to p$.

## Remarks

1. A frame validates $\mathsf{B}$ iff its relation is reflexive and symmetric, by [[common modal axiom schemata|FDFQFWPM4X]].
2. The name comes from an analogy with the intuitionistic law $p \to \neg\neg p$: reading each $\neg$ as $\square\neg$ turns it into $p \to \square\neg\square\neg p$, which is $p \to \square\lozenge p$.
3. The full discussion is in [[Brouwerian modal logic|2QPT4KCM0Q]].

## Explanations

### L1 human

The Brouwerian logic adds two laws to the basic logic: what is necessary is true, and what is true is necessarily possible.
Its worlds see themselves, and every arrow between two worlds has an arrow back.

### L2 human

We derive the dual form $\lozenge\square p \to p$ in $\mathsf{KB}$.

1. The instance of $\mathrm{B}$ with $\neg p$ is $\neg p \to \square\lozenge\neg p$.
2. Contraposition gives $\neg\square\lozenge\neg p \to p$.
3. By duality, $\lozenge\neg p$ is equivalent to $\neg\square p$, so $\neg\square\lozenge\neg p$ is equivalent to $\neg\square\neg\square p$, which is $\lozenge\square p$.
4. So $\mathsf{KB} \vdash \lozenge\square p \to p$.

The typical use of the dual form is in completeness proofs, where it gives symmetry of the canonical relation.
A trap: the dual form does not need $\mathrm{T}$, but the logic $\mathsf{B}$ does contain $\mathrm{T}$.

### L3 human

The pair $\mathrm{B}$ and its dual expresses that $\lozenge$ is left adjoint to $\square$ on symmetric frames.
This is the same pattern as the future and past operators of temporal logic.
