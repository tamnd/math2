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

A proof system is sound when everything it derives really follows.
Take a toy [[Hilbert system|1MGMQX43B8]] with one axiom schema $\varphi \to \varphi$ and one rule, "from $\varphi$ infer $\psi \to \varphi$".
Here is a two-line derivation in it:
$$1.\ p \to p \quad \text{(axiom)}, \qquad 2.\ q \to (p \to p) \quad \text{(rule, from line 1)}.$$
Line 1 is true under every valuation.
The rule keeps truth: if $\varphi$ is true, then $\psi \to \varphi$ is true whatever $\psi$ is.
So line 2 is true under every valuation as well, and the same argument works for every derivation in the system.
Change the rule to "from $\varphi$ infer $\varphi \to \psi$", and the derivation $p \to p$, $(p \to p) \to q$ ends in a formula that is false when $q$ is false.

In general, let a proof system give a derivability relation $\Gamma \vdash \varphi$ between sets of formulas and formulas.
Let a semantics give a relation of [[logical consequence|1HK0VYWTV7]] $\Gamma \models \varphi$: every interpretation that makes all members of $\Gamma$ true makes $\varphi$ true.
The proof system is *sound*, or *strongly sound*, for the semantics when $\Gamma \vdash \varphi$ implies $\Gamma \models \varphi$ for every set $\Gamma$ and every formula $\varphi$.
It is *weakly sound* when $\vdash \varphi$ implies $\models \varphi$, that is, when every theorem is valid.

Soundness is the converse of completeness of a proof system.
It is usually proved by induction on derivations, since each axiom is valid and each rule keeps truth.
It makes proofs reliable, and it lets a single counter-model show that a formula is not derivable.

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
If $\Gamma \vdash \varphi$, a derivation uses a finite part $\gamma_1, \ldots, \gamma_n$ of $\Gamma$.
The deduction theorem gives $\vdash \gamma_1 \to (\cdots \to (\gamma_n \to \varphi))$, and weak soundness makes this formula valid, so $\Gamma \models \varphi$.

For completeness the two forms differ.
Strong completeness needs, in addition, the [[compactness theorem|1NR3HAWG9D]] for the semantics.
The provability logic GL is weakly complete for its class of Kripke frames but not strongly complete, because that semantics is not compact.
Here "complete" means complete for a semantics.
It is not negation completeness of a theory, which decides each sentence, and it is not [[Post completeness|WK2P0E82B4]].

### Sound systems

The [[Hilbert system for classical propositional logic|HZCFTQDRA5]] is sound for truth tables.
Its three axiom schemas are tautologies, and modus ponens keeps truth.
The [[resolution rule|BVYHBAT59N]] is sound for propositional logic, so a derivation of the empty clause shows that a set of clauses is unsatisfiable.

The standard proof systems for first-order logic are sound for structures.
These include Hilbert systems, [[natural deduction|6KT3BJZ7D1]] and the [[sequent calculus|W72CA3R9MP]].
The rule of generalization needs care: it is sound because the variable does not occur free in the hypotheses.

Intuitionistic propositional logic is sound for [[Kripke semantics|NGHWZ9Y7ZV]] and for Heyting algebras.
It is also sound for truth tables, because the two-element Boolean algebra is a Heyting algebra.
In the philosophical sense, [[a valid argument with true premises|P1S8YHRFJ4]] about divisibility is a sound argument.

### Unsound systems

A [[system with the rule of affirming the consequent|5WQDFMR91G]] is not sound.
It derives $p$ from $p \to q$ and $q$, and the valuation $p = \mathsf{F}$, $q = \mathsf{T}$ makes the premises true and the conclusion false.

Consider a first-order system in which generalization is allowed without the side condition.
It derives $\forall x \, P(x)$ from $P(x)$.
The structure $\{ 0, 1 \}$ with $P = \{ 0 \}$ and $x \mapsto 0$ makes $P(x)$ true and $\forall x \, P(x)$ false.

Classical propositional logic is not sound for the three-element Heyting algebra $\{ 0, \tfrac12, 1 \}$.
It proves $p \lor \lnot p$, which takes the value $\tfrac12$ when $p$ has the value $\tfrac12$.

The argument "all squares are rectangles; this figure is a rectangle; so it is a square" is not valid.
So it is not sound, even if its premises and conclusion happen to be true.

### How soundness is used

Soundness is proved by induction on the length of derivations, or on the structure of derivation trees.
The [[soundness theorem for propositional logic|HZCFTQDRA5]] is the model case.
The proof splits into one check per axiom and one per [[rule of inference|QPD3X471Q1]], so a new rule can be added after one check.

If the system is sound and some interpretation satisfies $\Gamma$, then $\Gamma$ is [[consistent|VM8TQ70CVJ]].
In particular a sound system does not derive every formula, as long as some formula is not valid.

Counter-models show unprovability.
If some interpretation makes $\Gamma$ true and $\varphi$ false, then a sound system has $\Gamma \nvdash \varphi$.
This is the usual way to show unprovability and independence.

A system that is sound and strongly complete has $\vdash$ equal to $\models$.
For first-order logic this is the content of soundness together with [[Gödel's completeness theorem|WQ1ZE255SF]].

### Watch out

Do not call an argument sound because its conclusion is true.
A sound argument must be valid and have true premises, and a true conclusion is not enough.

Do not mix up soundness and completeness.
Soundness says that the rules prove only consequences, and completeness says that they prove all consequences.

Do not forget the side conditions of the quantifier rules.
Without them the first-order system is unsound, as the example with generalization shows.

### History

Post's paper of 1921 compared the propositional calculus of *Principia Mathematica* with truth tables, and showed that its theorems are exactly the tautologies.
One half of that result is soundness, the other half is completeness for truth tables.
Gödel's thesis of 1929 proved completeness for first-order logic, and textbooks have stated soundness and completeness together since then.

### Try it

Is the rule "from $\varphi \land \psi$ infer $\varphi$" sound for truth tables?
Answer: yes, since a valuation that makes $\varphi \land \psi$ true makes $\varphi$ true.

Is the rule "from $\varphi \lor \psi$ infer $\varphi$" sound for truth tables?
Answer: no, since the valuation with $\varphi$ false and $\psi$ true makes the premise true and the conclusion false.

Show that $p_1 \to p_2$ is not a theorem of the [[Hilbert system|HZCFTQDRA5]].
Answer: the valuation $p_1 = \mathsf{T}$, $p_2 = \mathsf{F}$ makes it false, so it is not a tautology, and by soundness it is not a theorem.

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
3. If $v(\varphi) = \mathsf{T}$, then $v(\psi) = \mathsf{T}$ by step 1, and then $v(\chi) = \mathsf{T}$ by step 1 again.
   So $v(\varphi \to \chi) = \mathsf{T}$.
4. In both cases $v(\varphi \to \chi) = \mathsf{T}$, so the rule keeps truth under every valuation.

The typical use is to add such a checked rule to a Hilbert system without losing soundness, as in the [[induction on derivations|E2KHD79NF4]].
A trap is to check a rule only for one valuation, for example the one in which all variables are true.
The rule must keep truth under every valuation.

### L3 human

In abstract terms a proof system gives a closure operator on sets of formulas, and a semantics gives another one.
Soundness says that the first is below the second.
The same pattern appears for equational logic and varieties of algebras, and for type systems, where it reads "well-typed programs do not go wrong".
It also appears for program logics such as Hoare logic, where soundness of each rule is checked against an operational semantics.
For non-classical logics one proves soundness for each semantics separately: intuitionistic logic for Kripke models and Heyting algebras, modal logics for classes of frames.
The deeper questions concern completeness, the converse, treated in [[completeness, compactness and interpolation|FBWW4J1XWG]].
