---
tag: H9Z8BWRN69
kind: concept
name: Logic of weak excluded middle
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
uses: [H5NSKEP3P2, 5GTQ69W47T, D9RY4667K6]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section L
    note: adopted
    mention: wikipedia://en/76765067#R19E
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics; Relation to modal logics
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 3.3
inventory: [NAQDKJMENM]
---

## Summary

The *logic of weak excluded middle* is the [[intermediate logic|H5NSKEP3P2]] obtained by adding all instances of weak excluded middle to intuitionistic logic.
So $\mathsf{KC} = \mathsf{IPC} + \neg p \vee \neg \neg p$.
It is also called "KC", "Jankov's logic" and "De Morgan logic".
By [[the theorem on weak excluded middle|CX032ACTMZ]], it is also axiomatized by the De Morgan law $\neg (p \wedge q) \to \neg p \vee \neg q$.
Its frames are the confluent frames, and it is complete for the finite rooted frames with a greatest element.
It is the largest intermediate logic with the same negation-free theorems as $\mathsf{IPC}$.

## Motivation

The weak excluded middle does not decide a statement, only its negation.
It is the classical principle that survives when every two stages of knowledge have a common later stage.
In Kripke terms, such frames are [[directed|D9RY4667K6]]: the future may branch, but the branches always meet again.
So $\mathsf{KC}$ is the logic of a single ideal end state, while $\mathsf{IPC}$ allows incompatible end states.
It also marks where negation stops behaving intuitionistically, by Jankov's theorem on positive fragments.

## Notation

$\mathsf{KC}$ is the usual name, and $\vdash_{\mathsf{KC}}$ denotes derivability in it.
For finite rooted frames, "confluent", "directed" and "with a greatest element" coincide.
Through the Gödel-McKinsey-Tarski translation, $\mathsf{S4.2}$ is a modal companion of $\mathsf{KC}$.

## Remarks

### Examples

1. [[The natural numbers as a frame of KC|HBN6HZYJP3]]: $(\mathbb{N}, \leq)$ validates $\mathsf{KC}$ without a greatest element.
2. [[A double negation shift in KC|ERFK4DR5TV]]: $\mathsf{KC} \vdash \neg \neg (p \vee q) \to \neg \neg p \vee \neg \neg q$.
3. The diamond is a frame of $\mathsf{KC}$ that is not linear; see [[weak excluded middle in LC|F448T49KSX]].
4. The three-element Heyting chain validates the weak excluded middle; see [[the three-element chain|G4S6HY9SHK]].

### Non-examples

1. [[The open sets of the real line|TQ7914VC4C]] refute the weak excluded middle, so they do not form a model of $\mathsf{KC}$.
2. [[The fork|1ENA02ZNAH]] is not a frame of $\mathsf{KC}$: its two leaves have no common upper bound.

### Basic properties

1. $\mathsf{IPC} \subsetneq \mathsf{KC} \subsetneq \mathsf{LC} \subsetneq \mathsf{CPC}$; see [[the theorem|CX032ACTMZ]] and [[the derivation in LC|F448T49KSX]].
2. $\mathsf{KC}$ is complete for finite rooted frames with a greatest element, so it has the finite model property and is decidable.
3. $\mathsf{KC}$ lacks the disjunction property, since it proves $\neg p \vee \neg \neg p$ but neither disjunct.
4. [[Jankov's theorem|DEKDMG563N]]: $\mathsf{KC}$ is the largest intermediate logic whose negation-free theorems are those of $\mathsf{IPC}$.
5. $\mathsf{KC}$ has the Craig interpolation property; it is one of [[Maksimova's seven logics|M3RTNGG3J5]].
6. $\mathsf{KC}$ is not structurally complete, and Visser's rules form a basis of its admissible rules; see [[admissible rules|C5K35H0R4Y]].

### History

Jankov studied the logic in 1968, including its relation to $\mathsf{IPC}$ on formulas without negation.
The name "De Morgan logic" refers to the equivalent axiom $\neg (p \wedge q) \to \neg p \vee \neg q$.

### Common errors

1. Confusing weak excluded middle with double negation elimination. $\mathsf{KC}$ proves excluded middle for every negated formula, but not $\neg \neg p \to p$, which would give $\mathsf{CPC}$.
2. Characterizing the frames of $\mathsf{KC}$ by a greatest element. This is right for finite rooted frames, but infinite directed frames without a top also validate $\mathsf{KC}$.
3. Thinking that $\mathsf{KC}$ changes the implication-only or the disjunction fragment. By Jankov's theorem, it adds nothing without negation.

## Explanations

### L1 human

Imagine research on a question that may split into several lines of work.
In $\mathsf{KC}$, all lines eventually meet in a common state of knowledge.
Then "it is impossible that $p$" or "it is impossible that $p$ is impossible" is settled from the start.
The statement $p$ itself may still be open.

### L2 human

1. To show $\varphi \in \mathsf{KC}$, check $\varphi$ on all finite rooted frames with a top, up to the size bound.
2. To show $\varphi \notin \mathsf{KC}$, find such a frame and a valuation that refutes $\varphi$ at the root.
3. To use the axiom syntactically, split into the cases $\neg p$ and $\neg \neg p$.

The typical use is as the first example of an intermediate logic defined by a frame condition other than linearity.
A trap: a branching frame can still validate $\mathsf{KC}$, as long as the branches meet again.

### L3 human

In algebraic terms, $\mathsf{KC}$ is the logic of the Heyting algebras whose pseudocomplement satisfies $\neg a \vee \neg \neg a = 1$.
Its subdirectly irreducible members are those in which $0$ is meet irreducible.
Through the [[Blok-Esakia theorem|BB9TA5Q9PN]], questions about extensions of $\mathsf{KC}$ become questions about normal extensions of $\mathsf{Grz}$ with a confluence axiom.
