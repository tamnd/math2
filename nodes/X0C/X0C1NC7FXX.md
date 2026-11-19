---
tag: X0C1NC7FXX
kind: definition
name: Definition of Kreisel-Putnam logic KP
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
defines: 669Y0EGM3N
uses: [H5NSKEP3P2, 52XCYMK0WW]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
---

## Definition

*Kreisel-Putnam logic* is the [[intermediate logic|H5NSKEP3P2]]
$$\mathsf{KP} = \mathsf{IPC} + (\neg p \to q \vee r) \to (\neg p \to q) \vee (\neg p \to r).$$
So $\mathsf{KP}$ is the least set of formulas that contains the [[axioms of IPC|52XCYMK0WW]] and every substitution instance of the *Kreisel-Putnam axiom* $\mathrm{kp}$ above, and is closed under modus ponens.

## Notation

We write $\vdash_{\mathsf{KP}} \varphi$ or $\varphi \in \mathsf{KP}$.
The rule form, from $\neg p \to q \vee r$ infer $(\neg p \to q) \vee (\neg p \to r)$, is the *Kreisel-Putnam rule*.
*Scott's logic* is $\mathsf{SL} = \mathsf{IPC} + ((\neg \neg p \to p) \to p \vee \neg p) \to \neg \neg p \vee \neg p$.

## Remarks

1. $\mathsf{KP} \subseteq \mathsf{CPC}$: if $\neg p$ is false, both disjuncts of the conclusion are true. If $\neg p$ is true, the premise makes $q$ or $r$ true, and the matching disjunct is true.
2. The axiom is a form of the independence of premise principle, restricted to negated premises.
3. The converse implication $(\neg p \to q) \vee (\neg p \to r) \to (\neg p \to q \vee r)$ is a theorem of $\mathsf{IPC}$.
4. The Kreisel-Putnam rule is admissible in $\mathsf{IPC}$, while the axiom is not a theorem; see [[the Kreisel-Putnam rule|ZBTCC4C61S]].

## Explanations

### L1 human

A negated statement $\neg p$ carries no constructive information: it only says that $p$ leads to a contradiction.
So if $\neg p$ gives "$q$ or $r$", it should already give one of them, decided in advance.
Kreisel-Putnam logic adds this principle to intuitionistic logic.

### L2 human

1. To use the axiom, prove $\neg \varphi \to \psi \vee \chi$ first.
2. Then the axiom gives $(\neg \varphi \to \psi) \vee (\neg \varphi \to \chi)$ in $\mathsf{KP}$.
3. In $\mathsf{IPC}$ this step is only admissible: it applies to theorems, not to hypotheses.

The typical use is as the standard example of a proper intermediate logic with the disjunction property.
A trap: the premise must be a negation.
With $p$ in place of $\neg p$, the axiom axiomatizes [[Gödel-Dummett logic|FA88H7FDPY]], which lacks the disjunction property.
