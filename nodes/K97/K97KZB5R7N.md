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

What does "and" mean?
A truth table gives one answer, and the rule ${\wedge}$I gives another: a proof of $A \wedge B$ is a proof of $A$ together with a proof of $B$.
Proof-theoretic semantics takes the second kind of answer seriously, and explains the meaning of [[logical connectives|QS0XVAN9BG]] and the validity of arguments by rules and proofs instead of truth in models.
In its main form the introduction rules of a connective in [[natural deduction|PAQ4ZX2TX1]] fix its meaning, and its elimination rules are justified when they are in [[harmony|XJSQVK0G71]] with them.
An argument is *valid* when it can be turned into a canonical proof by reduction steps, a notion of [[proof-theoretic validity|J2883WWC3M]] developed by Prawitz and Dummett.

## Motivation

Model-theoretic semantics defines [[logical consequence|1HK0VYWTV7]] by truth in all structures, and it takes the meaning of the connectives as given.
A different view says that we learn the meaning of "and" or "if" by learning how to use them in arguments.
On this view the rules come first, and truth is explained through proof.
Not every pair of rules gives a meaning: Prior's connective [[tonk|QSVQ1KPNBX]] shows that badly chosen rules let us infer anything from anything.
So the theory must say which rules are acceptable as definitions, and its answer uses normalization and [[cut elimination|AYRZ98Y0NW]].

## Notation

An introduction rule for a connective $\circ$ is written $\circ$I, and an elimination rule $\circ$E.
A *canonical* proof of a formula is one whose last step is an introduction rule.
A *reduction* removes an introduction followed at once by an elimination of the same formula, as in the [[normalization theorem|W33WAE1XTC]].
An *atomic base* is a set of rules for atomic formulas, and base-extension semantics defines validity relative to such bases.

## Remarks

### A valid argument, checked by hand

Take the argument from $A \wedge B$ to $B \wedge A$, given by the following derivation.
$$\dfrac{\dfrac{A \wedge B}{B}\,{\wedge}\mathrm{E}_2 \qquad \dfrac{A \wedge B}{A}\,{\wedge}\mathrm{E}_1}{B \wedge A}\,{\wedge}\mathrm{I}$$
To show that it is valid, put in place of the assumption $A \wedge B$ any canonical proof, which ends with ${\wedge}$I from a proof $D_1$ of $A$ and a proof $D_2$ of $B$.
Now each elimination stands right below an introduction, and the two reductions replace them by $D_2$ and by $D_1$.
The result is ${\wedge}$I applied to $D_2$ and $D_1$, a canonical proof of $B \wedge A$.
We never asked whether $A \wedge B$ is true: the check used only the shape of its proofs.

### Introduction rules as definitions

Gentzen read the introduction rules as definitions and the elimination rules as their consequences.
Prawitz made this precise with the *inversion principle*: an elimination may give only what any canonical proof of its major premise already contains.
For disjunction, a canonical proof of $A \vee B$ comes from a proof of $A$ or from a proof of $B$.
So ${\vee}$E, which derives $C$ from $A \vee B$ when $C$ follows from $A$ and from $B$, is justified: in either case we have what we need.
The rules for conjunction and for implication pass the same test, see [[the conjunction example|53ERPXVZ3S]] and [[the implication example|QWWR80Y2XT]].

### Rules that define nothing

The rules of tonk do not give a meaning, since its elimination takes out what its introduction never put in, see [[the tonk example|JVV2QRX0H2]].
A rule set can also fail the other way.
Conjunction with only ${\wedge}$E$_1$ never lets us use the second conjunct, so its eliminations are weaker than the introduction allows, and it does not define $\wedge$ in this sense.

### What harmony buys

Harmony is checked locally, one connective at a time, by a reduction of an introduction followed by an elimination.
Such reductions remove detours, and when the whole system normalizes, normal derivations have the [[subformula property|Z2NXKDK06G]].
In that case adding a connective with harmonious rules gives a [[conservative extension|N238J43XNE]]: no new formulas of the old language become derivable.
The standard intuitionistic rules are harmonious, while the classical rule of double negation elimination is not an elimination rule of this kind, and this starts a debate about classical logic within the theory.

### Watch out

Local harmony gives a reduction for each detour, but it does not by itself prove that reduction ends, and that needs a separate normalization proof.
Proof-theoretic validity is not derivability in a fixed system: it is defined by reductions to canonical proofs, relative to atomic bases.
Finally, the main forms of the theory validate intuitionistic logic, not classical logic, and excluded middle is not valid in them.

### History

Gentzen wrote in 1934 and 1935 that the introduction rules are, as it were, the definitions of the connectives.
Dag Prawitz developed this idea with his inversion principle and his normalization theorem in *Natural Deduction* of 1965, taking the name of the principle from Paul Lorenzen.
Arthur Prior introduced tonk in *The Runabout Inference-Ticket*, in Analysis in 1960, and Nuel Belnap answered in *Tonk, Plonk and Plink*, in Analysis in 1962.
Michael Dummett introduced the term harmony in *Frege: Philosophy of Language* of 1973, and he developed the theory in *The Logical Basis of Metaphysics* of 1991.
Peter Schroeder-Heister introduced the name proof-theoretic semantics in print in 1991.

### Try it

Exercise 1: show that the argument from $A$ to $A \wedge A$, by one ${\wedge}$I from two copies of the assumption, is valid.
Answer: put a closed valid proof $D$ of $A$ in place of both assumptions, and the result is ${\wedge}$I applied to $D$ and $D$, a canonical proof of $A \wedge A$.

Exercise 2: explain with the inversion principle why tonk-E, from $A \operatorname{tonk} B$ to $B$, is not justified by tonk-I, from $A$ to $A \operatorname{tonk} B$.
Answer: a canonical proof of $A \operatorname{tonk} B$ contains only a proof of $A$, so an elimination may give back only $A$, and tonk-E gives $B$, which no canonical proof provides.

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
