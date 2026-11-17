---
tag: K97KZB5R7N
kind: concept
name: Proof-theoretic semantics
msc: ["03F03", "03A05"]
topics: [R10RMQCJQX]
audience: grad
uses: [PAQ4ZX2TX1, XJSQVK0G71, QS0XVAN9BG, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Proof-theoretic_semantics
    locator: Philosophical motivation
  - url: https://en.wikipedia.org/wiki/Proof-theoretic_semantics
    locator: Historical development
  - url: https://en.wikipedia.org/wiki/Logical_harmony
    locator: Overview
---

## Summary

Proof-theoretic semantics explains the meaning of [[logical connectives|QS0XVAN9BG]] and the validity of arguments by rules of inference and proofs, instead of truth in models.
In its main form, the meaning of a connective is fixed by its introduction rules in [[natural deduction|PAQ4ZX2TX1]], and its elimination rules are justified when they are in [[harmony|XJSQVK0G71]] with them.
An argument is *valid* when it can be turned into a canonical proof by reduction steps, a notion of [[proof-theoretic validity|J2883WWC3M]] developed by Prawitz and Dummett.

## Motivation

Model-theoretic semantics defines [[logical consequence|1HK0VYWTV7]] by truth in all structures, and it takes the meaning of the connectives as given.
A different view says that we learn the meaning of "and" or "if" by learning how to use them in arguments.
On this view, the rules come first, and truth is derived from proof.
Not every pair of rules gives a meaning: Prior's connective [[tonk|QSVQ1KPNBX]] shows that badly chosen rules let us infer anything from anything.
Proof-theoretic semantics asks which rules are acceptable as definitions, and its answer uses normalization and [[cut elimination|AYRZ98Y0NW]].

## Notation

An introduction rule for a connective $\circ$ is written $\circ$I, and an elimination rule $\circ$E.
A *canonical* proof of a formula is one whose last step is an introduction rule.
A *reduction* removes an introduction followed at once by an elimination of the same formula, as in the [[normalization theorem|W33WAE1XTC]].
An *atomic base* is a set of rules for atomic formulas, and base-extension semantics defines validity relative to such bases.

## Remarks

### Examples

- The rules for conjunction are harmonious, and they give $\wedge$ its usual meaning, see [[this example|53ERPXVZ3S]].
- The rules for implication are harmonious, and the reduction that shows it is the detour reduction of natural deduction, see [[this example|QWWR80Y2XT]].
- The argument from $A \wedge B$ to $B \wedge A$ is valid: given a canonical proof of $A \wedge B$, its two immediate subproofs give a canonical proof of $B \wedge A$.
- For disjunction, the rule $\vee$E is justified by the inversion principle: a canonical proof of $A \vee B$ comes from a proof of $A$ or of $B$, and each case gives the conclusion.

### Non-examples

- The rules of tonk do not give a meaning: they are not harmonious and they make every formula derivable from every formula, see [[this non-example|JVV2QRX0H2]].
- The truth-table definition of $\wedge$ by a function on $\{0, 1\}$ is a model-theoretic semantics. It uses truth values, not rules of proof.
- A rule set whose eliminations are weaker than the introductions allow, such as $\wedge$ with only $\wedge$E$_1$, is not in harmony, so it does not define $\wedge$ in this sense.

### Basic properties

- If every connective has harmonious rules, then detours can be removed, so normal derivations exist and have the [[subformula property|Z2NXKDK06G]].
- If the extended system still normalizes, adding a connective with harmonious rules gives a [[conservative extension|N238J43XNE]]: no new formulas of the old language become derivable.
- Harmony is checked locally: for each connective, one shows a reduction of an introduction followed by an elimination.
- The standard intuitionistic rules are harmonious. The classical rule of double negation elimination is not an elimination rule of this kind, which leads to a debate about classical logic within the theory.

### History

Gentzen wrote that the introduction rules are, as it were, the definitions of the connectives, and that the elimination rules are consequences of them.
Dag Prawitz developed this idea with his inversion principle and his normalization theorem in *Natural Deduction* of 1965.
Arthur Prior introduced tonk in *The Runabout Inference-Ticket*, in Analysis in 1960, and Nuel Belnap answered in *Tonk, Plonk and Plink*, in Analysis in 1962.
Michael Dummett coined the term harmony, and he developed the theory in *The Logical Basis of Metaphysics* of 1991.
Peter Schroeder-Heister introduced the name proof-theoretic semantics in print in 1991.

### Common errors

- Thinking that any set of rules defines a connective. Tonk shows that the rules must satisfy a condition such as harmony.
- Treating proof-theoretic validity as derivability in a fixed system. Validity is defined by reductions to canonical proofs, relative to atomic bases.
- Expecting proof-theoretic semantics to agree with classical semantics. Its main forms validate intuitionistic logic, not classical logic.

## Explanations

### L1 human

Usually the meaning of "and" is explained by a truth table: "$A$ and $B$" is true when both are true.
Proof-theoretic semantics explains it by how we prove and use statements with "and".
To prove "$A$ and $B$", prove $A$ and prove $B$.
From "$A$ and $B$", we may conclude $A$, and we may conclude $B$.
These rules match: what we can get out is exactly what we had to put in.

### L2 human

To check that rules for a connective $\circ$ are acceptable, test two things.

1. Local soundness: a proof that introduces $A \circ B$ and eliminates it at once can be simplified to a proof without this detour.
2. Local completeness: from a proof of $A \circ B$, the elimination rules followed by the introduction rules give back $A \circ B$.

The typical use is to reject a proposed connective by a failure of step 1, as for tonk.
A trap is to check only one direction: rules that pass step 1 can still be too weak, which step 2 detects.

### L3 human

Proof-theoretic validity, in the form of Prawitz, defines a valid argument by induction on formulas, with canonical proofs for compound formulas and an atomic base for atoms.
Base-extension semantics turns this into a semantics with a soundness and completeness question, and for intuitionistic propositional logic the answer depends on the treatment of disjunction.
In the sequent calculus, harmony corresponds to the principal case of cut elimination, where a right rule meets a left rule on the same formula.
Under the [[Curry-Howard correspondence|A77FER1Q5H]], local soundness is beta reduction and local completeness is eta expansion.
