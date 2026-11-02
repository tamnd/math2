---
tag: 61THBNS8WE
kind: definition
name: Provability logic
msc: [03F45, 03B45]
defines: WJK0YA4GP2
uses: [C3RZY20ETK, 0QFT7Z76N5, MFJXPAF0R0]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
---

## Definition

The provability logic $\mathrm{GL}$ is the smallest normal [[modal logic|C3RZY20ETK]] that contains Löb's axiom
$$\square(\square p \to p) \to \square p.$$
Its intended reading interprets $\square$ as provability in [[Peano arithmetic|0QFT7Z76N5]].
An arithmetical realization $*$ maps each propositional variable to a sentence of arithmetic and commutes with the connectives.
It sets $(\square\varphi)^* = \mathrm{Prov}(\ulcorner \varphi^* \urcorner)$, where $\mathrm{Prov}$ is the provability predicate of Peano arithmetic and $\ulcorner \cdot \urcorner$ is a [[Gödel numbering|MFJXPAF0R0]].

## Remarks

Solovay's theorem (1976) says: a modal formula $\varphi$ is in $\mathrm{GL}$ if and only if Peano arithmetic proves $\varphi^*$ for every arithmetical realization $*$.

Example: $\square p \to \square\square p$ is in $\mathrm{GL}$.
Its realizations are instances of the fact that Peano arithmetic proves "if $\sigma$ is provable, then it is provable that $\sigma$ is provable".

Non-example: $\square p \to p$ is not in $\mathrm{GL}$.
Under a realization with $p^* = (0 = 1)$, it becomes the consistency statement of Peano arithmetic, which Peano arithmetic does not prove by Gödel's second incompleteness theorem.

On Kripke frames, $\mathrm{GL}$ is the logic of the finite transitive irreflexive frames.
The name "provability logic" also covers the study of related systems for other theories and other provability notions.

## Explanations

### L1 human

The system $\mathrm{GL}$ is named after Gödel and Löb.
Its one extra axiom is the modal form of [[Löb's theorem|3HD30YG3DG]].
It captures every general law of provability that Peano arithmetic can prove about itself.
