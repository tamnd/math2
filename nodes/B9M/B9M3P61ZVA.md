---
tag: B9M3P61ZVA
kind: statement
role: theorem
name: Glivenko's theorem
msc: ["03B20", "03F25"]
topics: [38EQ20GR7M]
audience: grad
uses: [52XCYMK0WW, 09K9MWD2QQ, 0RYYK8PG4S, 9X08XK5RV2]
about: [Q11N8X99FK, 09K9MWD2QQ]
proofs: [SDTV284B57]
history:
  first_stated: "Glivenko, 1929, Sur quelques points de la logique de M. Brouwer"
sources:
  - url: https://en.wikipedia.org/wiki/Glivenko%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Propositional logic
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 4.1 Translating classical into intuitionistic logic
---

## Statement

Let $\mathsf{CPC}$ be classical [[propositional logic|09K9MWD2QQ]], that is, $\mathsf{IPC}$ plus the [[law of excluded middle|0RYYK8PG4S]].

**Theorem.** For every propositional formula $\varphi$:

1. $\mathsf{CPC} \vdash \varphi$ if and only if $\mathsf{IPC} \vdash \neg \neg \varphi$.
2. $\mathsf{CPC} \vdash \neg \varphi$ if and only if $\mathsf{IPC} \vdash \neg \varphi$.

The proof is in [[the proof of Glivenko's theorem|SDTV284B57]].

## Remarks

### Why each hypothesis is needed

1. The formula must be propositional. In predicate logic, $\forall x\,(Px \vee \neg Px)$ is classically valid, but its double negation is not provable in $\mathsf{IQC}$; see [[the predicate counterexample|ZV2MWBRN04]].
2. In item 2 the negation is needed. $\mathsf{CPC} \vdash \neg \neg p \to p$, but $\mathsf{IPC} \nvdash \neg \neg p \to p$.

### Consequences

1. $\mathsf{IPC}$ is decidable through $\mathsf{CPC}$ for formulas of the form $\neg \psi$: check $\neg \psi$ by truth tables.
2. $\mathsf{IPC}$ is consistent if and only if $\mathsf{CPC}$ is: $\bot$ is equivalent to $\neg \neg \bot$.
3. A classical tautology is never refuted intuitionistically. If $\mathsf{CPC} \vdash \varphi$ and $\mathsf{IPC} \vdash \neg \varphi$, then $\mathsf{CPC}$ proves $\bot$.
4. For propositional formulas, the [[Gödel-Gentzen translation|WC4TDGEWZR]] of $\varphi$ is intuitionistically equivalent to $\neg \neg \varphi$. So it is a [[double-negation translation|HGJVM49PA4]] of the same strength.

### Converse

Item 1 is a biconditional; the direction from right to left holds because $\mathsf{CPC} \vdash \neg \neg \varphi \to \varphi$.
Algebraically, the theorem says that the map $x \mapsto \neg \neg x$ sends every Heyting algebra onto a Boolean algebra, its regular elements.

### Generalizations

1. Glivenko's theorem holds for predicate formulas without $\forall$.
2. Kuroda's translation, which inserts $\neg \neg$ after each $\forall$ and in front of the whole formula, extends the theorem to all predicate formulas.
3. Every intermediate logic $L$ proves the same negated formulas as $\mathsf{CPC}$, by item 2 and $\mathsf{IPC} \subseteq L \subseteq \mathsf{CPC}$.

## Explanations

### L1 human

Intuitionistic logic proves fewer statements than classical logic.
The theorem says that the gap is small for propositional formulas.
A classical law may fail intuitionistically, but its double negation, "it is not refutable", always holds.
For example, "$p$ or not $p$" is not an intuitionistic law, but "it is impossible that neither $p$ nor not $p$" is.

### L2 human

1. Take $\varphi = ((p \to q) \to p) \to p$, Peirce's law, a classical tautology.
2. By item 1, $\mathsf{IPC} \vdash \neg \neg (((p \to q) \to p) \to p)$.
3. But $\mathsf{IPC} \nvdash ((p \to q) \to p) \to p$, as the two-point Kripke model shows with $q$ false everywhere.

The typical use is to transfer a classical proof of a negative statement to intuitionistic logic.
A trap: the theorem is about propositional formulas only, and it fails in predicate logic.

### L3 human

The proof shows that the set of formulas whose double negation is intuitionistic contains the axioms and is closed under modus ponens.
In Kripke terms, a finite rooted model has maximal worlds, where every formula takes a classical value.
A formula $\neg \neg \varphi$ holds at $w$ exactly when $\varphi$ holds at all maximal worlds above $w$, which gives a semantic proof for finite models.
