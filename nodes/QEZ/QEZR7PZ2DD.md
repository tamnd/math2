---
tag: QEZR7PZ2DD
kind: definition
name: Double-negation translation
msc: ["03F25", "03F55", "03B20"]
uses: [Q11N8X99FK, 0XR7A7RSXB, 0QFT7Z76N5, RXHJPVMPJH, 0RYYK8PG4S]
defines: HGJVM49PA4
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
---

## Definition

Fix a first-order language, and read $\neg A$ as $A \to \bot$.
The *Gödel–Gentzen negative translation* is the map $A \mapsto A^N$ on formulas defined by these clauses.

1. $\bot^N = \bot$, and $P^N = \neg \neg P$ for every other atomic formula $P$.
2. $(A \wedge B)^N = A^N \wedge B^N$.
3. $(A \vee B)^N = \neg (\neg A^N \wedge \neg B^N)$.
4. $(A \to B)^N = A^N \to B^N$.
5. $(\forall x\, A)^N = \forall x\, A^N$.
6. $(\exists x\, A)^N = \neg \forall x\, \neg A^N$.

For a set of formulas $\Gamma$, let $\Gamma^N = \set{A^N : A \in \Gamma}$.
Its main property is this: $\Gamma \vdash A$ in classical logic if and only if $\Gamma^N \vdash A^N$ in [[intuitionistic logic|Q11N8X99FK]].
A *double-negation translation* is any map with this property obtained by inserting double [[negations|0XR7A7RSXB]], such as the translations of Kolmogorov and Kuroda.

## Remarks

Example: for the [[law of excluded middle|0RYYK8PG4S]] with $P$ atomic, $(P \vee \neg P)^N = \neg (\neg \neg \neg P \wedge \neg \neg \neg \neg P)$.
Since $\neg \neg \neg P$ is equivalent to $\neg P$ in intuitionistic logic, this is equivalent to $\neg (\neg P \wedge \neg \neg P)$, which is intuitionistically provable.
Non-example: the identity map $A \mapsto A$ is not a double-negation translation, because $P \vee \neg P$ is classically provable but not intuitionistically provable.
For arithmetic, [[Peano arithmetic|0QFT7Z76N5]] proves $A$ if and only if [[Heyting arithmetic|RXHJPVMPJH]] proves $A^N$.
In particular, if HA is consistent, then PA is consistent, because $\bot^N = \bot$.
In arithmetic, atomic formulas are equations, which are decidable in HA, so one may take $P^N = P$.
