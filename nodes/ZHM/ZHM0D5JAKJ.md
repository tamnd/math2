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

The logic $\mathsf{B}$ adds to $\mathsf{K}$ the laws "what is necessary is true" and "what is true is necessarily possible".
Exactly, $\mathsf{B} = \mathsf{KTB}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains these axioms:
$$\mathrm{T}\colon \square p \to p, \qquad \mathrm{B}\colon p \to \square\lozenge p.$$
The logic $\mathsf{KB}$ is the smallest normal modal logic that contains $\mathrm{B}$.
A $\mathsf{B}$-frame is a frame whose relation is [[reflexive|0X8NMST0J2]] and [[symmetric|061J5VGSPT]].

## Notation

The letter $\mathsf{B}$ refers to Brouwer, and the logic is also written $\mathsf{KTB}$.
The axiom $\mathrm{B}$ is the Brouwerian axiom, and its dual form is $\lozenge\square p \to p$.

## Remarks

A frame validates $\mathsf{B}$ exactly when its relation is reflexive and symmetric, by [[common modal axiom schemata|FDFQFWPM4X]].
For symmetry, suppose $p$ is true at $w$ and $w R v$.
Then $v R w$, so $\lozenge p$ is true at $v$, and $\square\lozenge p$ is true at $w$.
For the converse, put $V(p) = \{ w \}$.
Then $\square\lozenge p$ at $w$ says that every successor of $w$ sees $w$, which is symmetry at $w$.

The name comes from an analogy with the intuitionistic law $p \to \neg\neg p$.
Reading each $\neg$ as $\square\neg$ turns that law into $p \to \square\neg\square\neg p$, which is $p \to \square\lozenge p$.
The concept page [[Brouwerian modal logic|2QPT4KCM0Q]] covers examples, finite models and the comparison with $\mathsf{S4}$.

## Explanations

### L1 human

The Brouwerian logic adds two laws to the basic logic: what is necessary is true, and what is true is necessarily possible.
Its worlds see themselves, and every arrow between two worlds has an arrow back.
For example, "is within one meter of" relates each point to itself, and it works in both directions.

### L2 human

We derive the dual form $\lozenge\square p \to p$ in $\mathsf{KB}$.

1. The instance of $\mathrm{B}$ with $\neg p$ is $\neg p \to \square\lozenge\neg p$.
2. Contraposition gives $\neg\square\lozenge\neg p \to \neg\neg p$, and so $\neg\square\lozenge\neg p \to p$.
3. By duality and RE, $\lozenge\neg p$ is equivalent to $\neg\square p$, so $\neg\square\lozenge\neg p$ is equivalent to $\neg\square\neg\square p$, which is $\lozenge\square p$.
4. So $\mathsf{KB} \vdash \lozenge\square p \to p$.

You use the dual form in completeness proofs, where it makes the canonical relation symmetric.
Watch out: the dual form does not need $\mathrm{T}$, but the logic $\mathsf{B}$ contains $\mathrm{T}$ anyway.

### L3 human

The axiom $\mathrm{B}$ and its dual say that $\lozenge$ is left adjoint to $\square$ on symmetric frames.
The future box and the past diamond of temporal logic follow the same pattern.
