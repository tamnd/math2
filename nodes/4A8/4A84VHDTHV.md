---
tag: 4A84VHDTHV
kind: concept
name: Soundness
msc: ["03B05", "03B10", "03F03"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [1HK0VYWTV7, 1MGMQX43B8, 0Y0MQYST0M, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Soundness
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Completeness_(logic)
    locator: Strong completeness
  - book: isbn:9780122384523
  - book: isbn:9781447145578
same_as:
  wikidata: Q693083
  wikipedia: Soundness
---

## Summary

Let a proof system give a derivability relation $\Gamma \vdash \varphi$ between sets of formulas and formulas, and let a semantics give a relation of [[logical consequence|1HK0VYWTV7]] $\Gamma \models \varphi$, "every interpretation that makes all members of $\Gamma$ true makes $\varphi$ true".
The proof system is *sound* for the semantics, or *strongly sound*, when $\Gamma \vdash \varphi$ implies $\Gamma \models \varphi$ for every set $\Gamma$ and every formula $\varphi$.
It is *weakly sound* when $\vdash \varphi$ implies $\models \varphi$, that is, when every theorem is valid.
Soundness is the converse of completeness of a proof system, and it is usually proved by induction on derivations: each axiom is valid and each rule keeps truth.
It matters because it makes proofs reliable: a sound system never derives a false conclusion from true premises, and so a single counter-model shows that a formula is not derivable.

## Motivation

A proof system is a set of formal rules for writing lists of formulas.
Nothing in the rules themselves says that the last formula is true.
To trust a derivation, we must check once and for all that the rules agree with the intended meaning of the connectives and quantifiers.
That check is the soundness theorem.
Its converse question, whether the rules are strong enough to derive every consequence, is completeness, and it is much harder.

## Notation

We write $\Gamma \vdash \varphi$ for derivability in a fixed proof system, often with the name of the system as a subscript, and $\Gamma \models \varphi$ for semantic consequence.
Soundness is then the inclusion ${\vdash} \subseteq {\models}$, and completeness is the reverse inclusion.
In philosophy, "sound" is also used for arguments.
An argument is *valid* when its conclusion is true in every situation in which its premises are true.
It is *sound* when it is valid and its premises are in fact true.
The two uses differ: soundness of a proof system is a property of rules, and soundness of an argument depends on the facts.

## Remarks

### Weak and strong forms

There are four properties that link $\vdash$ and $\models$.

| Property | Statement |
|---|---|
| weak soundness | $\vdash \varphi$ implies $\models \varphi$ |
| strong soundness | $\Gamma \vdash \varphi$ implies $\Gamma \models \varphi$ |
| weak completeness | $\models \varphi$ implies $\vdash \varphi$ |
| strong completeness | $\Gamma \models \varphi$ implies $\Gamma \vdash \varphi$ |

For a Hilbert system with the [[deduction theorem|9X08XK5RV2]], weak soundness implies strong soundness.
If $\Gamma \vdash \varphi$, then a finite part $\gamma_1, \ldots, \gamma_n$ of $\Gamma$ is used, the deduction theorem gives $\vdash \gamma_1 \to (\cdots \to (\gamma_n \to \varphi))$, and weak soundness makes this formula valid, so $\Gamma \models \varphi$.
For completeness the two forms differ: strong completeness needs, in addition, the [[compactness theorem|1NR3HAWG9D]] for the semantics.
The provability logic GL is weakly complete for its class of Kripke frames but not strongly complete, because that semantics is not compact.
Here "complete" means complete for a semantics; it is not the completeness of a theory, which decides each sentence, and it is not [[Post completeness|WK2P0E82B4]].

### Examples

- The [[Hilbert system for classical propositional logic|~4b87d303]] is sound for truth tables: its three axiom schemas are tautologies, and modus ponens keeps truth.
- The [[resolution rule|~55ed4b9f]] is sound for propositional logic, so a derivation of the empty clause shows that a set of clauses is unsatisfiable.
- The standard proof systems for first-order logic (Hilbert systems, [[natural deduction|6KT3BJZ7D1]], the [[sequent calculus|W72CA3R9MP]]) are sound for structures. The rule of generalization needs care: it is sound because the variable does not occur free in the hypotheses.
- Intuitionistic propositional logic is sound for [[Kripke semantics|NGHWZ9Y7ZV]] and for Heyting algebras. It is also sound for truth tables, because the two-element Boolean algebra is a Heyting algebra.
- [[A valid argument with true premises|~5ce55b27]] about divisibility is a sound argument in the philosophical sense.

### Non-examples

- A [[system with the rule of affirming the consequent|~3f2ae663]] is not sound: it derives $p$ from $p \to q$ and $q$, and the valuation $p = \mathsf{F}$, $q = \mathsf{T}$ makes the premises true and the conclusion false.
- A first-order system in which generalization is allowed without the side condition derives $\forall x \, P(x)$ from $P(x)$, and the structure $\set{0, 1}$ with $P = \set{0}$ and $x \mapsto 0$ refutes this step.
- Classical propositional logic is not sound for the three-valued Heyting algebra semantics: it proves $p \lor \lnot p$, which takes the value $\tfrac12$ when $p$ has the value $\tfrac12$.
- The argument "all squares are rectangles; this figure is a rectangle; so it is a square" is not valid, so it is not sound, even if its premises and conclusion happen to be true.

### Basic properties

- Soundness is proved by induction on the length of derivations, or on the structure of derivation trees; the [[soundness theorem for propositional logic|~4b87d303]] is the model case.
- If the system is sound and some interpretation satisfies $\Gamma$, then $\Gamma$ is [[consistent|VM8TQ70CVJ]]. In particular a sound system with a satisfiable empty set does not derive every formula.
- Counter-models: if some interpretation makes $\Gamma$ true and $\varphi$ false, then a sound system has $\Gamma \nvdash \varphi$. This is the usual way to show unprovability and independence.
- Soundness of a system follows from the validity of each axiom and the soundness of each [[rule of inference|QPD3X471Q1]] separately. So a new rule can be added after one check.
- A system that is sound and strongly complete has $\vdash$ equal to $\models$; for first-order logic this is the content of [[Gödel's completeness theorem|WQ1ZE255SF]] together with soundness.

### History

Post's paper of 1921 compared the propositional calculus of *Principia Mathematica* with truth tables, and showed that its theorems are exactly the tautologies.
One half of that result is soundness, the other half is completeness for truth tables.
Gödel's thesis of 1929 proved completeness for first-order logic, and the textbooks state soundness and completeness together since then.

### Common errors

- Calling an argument sound because its conclusion is true. A sound argument must be valid and have true premises; a true conclusion is not enough.
- Mixing up soundness and completeness. Soundness says that the rules prove only consequences; completeness says that they prove all consequences.
- Forgetting the side conditions of the quantifier rules. Without them the first-order system is unsound, as the non-example with generalization shows.

## Explanations

### L1 human

A set of rules for proofs is sound when it never leads from true statements to a false one.
Take the rule "from 'if $p$ then $q$' and '$p$', conclude '$q$'".
If it is true that "if it rains, the street is wet" and it does rain, then the street is wet.
So this rule is safe.
The rule "from 'if $p$ then $q$' and '$q$', conclude '$p$'" is not safe.
The street can be wet because someone washed it, while it does not rain.

### L2 human

We check that the rule of hypothetical syllogism, from $\varphi \to \psi$ and $\psi \to \chi$ infer $\varphi \to \chi$, is sound for truth tables.

1. Let $v$ be a valuation with $v(\varphi \to \psi) = \mathsf{T}$ and $v(\psi \to \chi) = \mathsf{T}$.
2. If $v(\varphi) = \mathsf{F}$, then $v(\varphi \to \chi) = \mathsf{T}$ by the truth table of $\to$.
3. If $v(\varphi) = \mathsf{T}$, then $v(\psi) = \mathsf{T}$ by step 1, and then $v(\chi) = \mathsf{T}$ by step 1 again. So $v(\varphi \to \chi) = \mathsf{T}$.
4. In both cases $v(\varphi \to \chi) = \mathsf{T}$, so the rule keeps truth under every valuation.

The typical use is to add such a checked rule to a Hilbert system without losing soundness, as in the [[induction on derivations|~48af3302]].
A trap is to check a rule only for one valuation, for example the one in which all variables are true; the rule must keep truth under every valuation.

### L3 human

In abstract terms a proof system gives a closure operator on sets of formulas, a semantics gives another closure operator, and soundness says that the first is below the second.
The same pattern appears for equational logic and varieties of algebras, for type systems ("well-typed programs do not go wrong"), and for program logics such as Hoare logic, where soundness of each rule is checked against an operational semantics.
For non-classical logics one proves soundness for each semantics separately: intuitionistic logic for Kripke models and Heyting algebras, modal logics for classes of frames.
The deeper questions of the area concern completeness, the converse, treated in [[completeness, compactness and interpolation|FBWW4J1XWG]].
