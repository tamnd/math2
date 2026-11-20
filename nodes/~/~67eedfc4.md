---
tag: ~67eedfc4
kind: concept
name: Axiomatic theories of truth
aliases: [axiomatic-truth, truth-theories-over-pa]
msc: ["03F25", "03A05"]
topics: [6Q4JJ2MMV8]
audience: grad
uses: [HACXBCM7SS, MFJXPAF0R0, ~34d21c75, Z6MCGB0ZFX]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 2.2 Notational conventions"
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 3.2 The T-sentences"
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 3.3 Compositional truth"
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 4.3 The Friedman-Sheard theory and revision semantics"
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 4.4 The Kripke-Feferman theory"
  - book: isbn:9780521115810
---

## Summary

An *axiomatic theory of truth* is a theory in the language $\mathcal{L}_T$ of [[Peano arithmetic|HACXBCM7SS]] with a new unary predicate $T$.
It consists of the axioms of $\mathsf{PA}$, axioms or rules for $T$, and usually the induction schema for all formulas of $\mathcal{L}_T$.
The codes of sentences, given by a [[Gödel numbering|MFJXPAF0R0]], are the objects to which $T$ applies.
Truth is a primitive notion, described by axioms, and not a defined one.
A theory is *typed* if it proves the truth only of sentences without $T$; otherwise it is *type-free*.
The main theories are $\mathsf{TB}$, $\mathsf{UTB}$, $\mathsf{CT}^-$, $\mathsf{CT}$, $\mathsf{FS}$ and $\mathsf{KF}$.

## Motivation

[[Tarski's undefinability theorem|YRV6SYK2BY]] shows that no formula of arithmetic defines arithmetical truth.
So to reason about truth inside a theory, we must add $T$ as a new primitive.
The [[naive truth schema|~34d21c75]] is inconsistent, so we must choose which principles to add.
Each choice gives a theory whose consequences we can study by proof theory.
The SEP entry gives two further motives: truth theories can express reflection principles, and they give a test for deflationism.

## Notation

1. $\mathcal{L}_T$ has the connectives $\neg, \wedge, \vee$ and the quantifiers $\forall, \exists$. As in the SEP entry, $+$ and $\cdot$ are predicates, so the closed terms are the numerals.
2. Variables $A, B$ range over codes of sentences. So $\forall A\, (T[\neg A] \leftrightarrow \neg T A)$ is a single sentence.
3. $\mathrm{Tr}_0(x)$ is a formula of arithmetic that defines truth for atomic sentences of arithmetic.
4. $\mathsf{T}[\mathsf{PA}]$ means the truth axioms over the base theory $\mathsf{PA}$. A superscript minus means that induction is only for formulas without $T$.

The main theories are as follows.

| theory | axioms for $T$ | typed | over $\mathsf{PA}$ |
|---|---|---|---|
| $\mathsf{TB}$ | $T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for $\varphi$ without $T$ | yes | conservative |
| $\mathsf{UTB}$ | $\forall x\,(T(\ulcorner \varphi(\dot x) \urcorner) \leftrightarrow \varphi(x))$ for $\varphi$ without $T$ | yes | conservative |
| $\mathsf{CT}^-$ | Tarski's compositional clauses for sentences without $T$, induction without $T$ | yes | conservative |
| $\mathsf{CT}$ | the clauses of $\mathsf{CT}^-$, induction for all of $\mathcal{L}_T$ | yes | same arithmetic as $\mathsf{ACA}$ |
| $\mathsf{FS}$ | type-free clauses, with $T[\neg A] \leftrightarrow \neg T A$, and two rules | no | ramified analysis of finite levels |
| $\mathsf{KF}$ | type-free Kripke clauses, with $T[TA] \leftrightarrow TA$ | no | ramified analysis below $\varepsilon_0$ |

The last column gives the strength as reported in the SEP entry.

## Remarks

### Examples

1. [[The theory TB is conservative over PA|~cdf09097]]; the example gives the syntactic proof.
2. [[The compositional theory CT|~5af95d4a]]: $\mathsf{CT}^-$ is conservative over $\mathsf{PA}$, and $\mathsf{CT}$ proves the consistency of $\mathsf{PA}$.
3. [[The Friedman-Sheard theory FS|~c09ae4a3]] keeps classical truth and the rules of necessitation and conecessitation.
4. [[The Kripke-Feferman theory KF|~a625d303]] axiomatizes Kripke's fixed points.
5. An axiomatization of the [[Tarskian hierarchy|Z6MCGB0ZFX]] uses truth predicates $T_\alpha$ indexed by ordinal notations. The SEP entry relates it to ramified analysis.

### Non-examples

1. $\mathsf{PA}$ plus all instances of the naive truth schema is not a theory of truth in a useful sense. It is inconsistent, by the [[liar paradox|~005ac188]].
2. $\mathsf{PA}$ with a defined partial truth predicate for $\Sigma_n$ sentences adds nothing. The SEP entry calls such definable predicates redundant.
3. [[Kripke's theory of truth|~1dd87a57]] is a semantic construction, not an axiomatic theory. $\mathsf{KF}$ is its axiomatic counterpart.

### Basic properties

1. $\mathsf{TB}$ does not prove that every sentence or its negation is true, as the SEP entry reports from Tarski. Its axioms are instances and do not prove generalizations.
2. The compositional axioms imply each typed T-sentence, by induction on the build-up of the sentence in the metatheory.
3. A theory with induction for $\mathcal{L}_T$ and the compositional axioms proves the global reflection principle for $\mathsf{PA}$. So it is not conservative over $\mathsf{PA}$, by [[Gödel's second incompleteness theorem|4PZM5GJTR5]].
4. Over $\mathsf{PA}$, the type-free axioms $\forall A\,(T[TA] \leftrightarrow TA)$ and $\forall A\,(T[\neg A] \leftrightarrow \neg TA)$ are jointly inconsistent. $\mathsf{FS}$ keeps the second and $\mathsf{KF}$ keeps the first.
5. Every theory in the table except $\mathsf{FS}$ has a standard model. $\mathsf{FS}$ is $\omega$-inconsistent, by [[McGee's theorem|~e7fe60d3]].

### History

The SEP entry reports that Tarski criticized the T-sentences as deductively too weak.
It credits the conservativity of $\mathsf{CT}^-$ to Kotlarski, Krajewski and Lachlan (1981), and the first finitary proofs to Enayat and Visser (2015) and Leigh (2015).
It names $\mathsf{FS}$ after Friedman and Sheard (1987), and credits $\mathsf{KF}$ to Feferman, who published his version in 1991.
The book of Halbach (2011) is a monograph on these theories.

### Common errors

1. Thinking that "conservative" means "weak in every sense". $\mathsf{CT}^-$ is conservative over $\mathsf{PA}$, but it proves many generalizations that $\mathsf{TB}$ does not prove.
2. Confusing a schema with a single sentence. The schema $T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ has infinitely many instances, while $\forall A\, (T[\neg A] \leftrightarrow \neg TA)$ is one sentence.
3. Thinking that a type-free theory must be non-classical. $\mathsf{FS}$ and $\mathsf{KF}$ are formulated in classical logic.

## Explanations

### L1 human

We cannot define "true sentence of arithmetic" inside arithmetic.
So we add a new word "true" and write down rules for it.
Different rule books give different theories.
Some rule books add nothing new about numbers, and some prove new facts, such as the consistency of arithmetic.

### L2 human

1. Take $\mathsf{TB}$. It proves $T(\ulcorner 0 = 0 \urcorner)$, since $\mathsf{PA} \vdash 0 = 0$ and the axiom gives $T(\ulcorner 0 = 0 \urcorner) \leftrightarrow 0 = 0$.
2. It does not prove $\forall A\, (T A \vee T[\neg A])$, with $A$ over sentences without $T$. The SEP entry reports this observation of Tarski.
3. $\mathsf{CT}$ proves this sentence, by its axiom for negation.
4. $\mathsf{CT}$ also proves "every theorem of $\mathsf{PA}$ is true", and hence $\mathrm{Con}(\mathsf{PA})$.

The typical use is to measure the strength of a truth principle by the arithmetic it proves.
The trap is to forget induction: $\mathsf{CT}^-$ and $\mathsf{CT}$ have the same truth axioms, but different strength.

### L3 human

Axiomatic truth theories are a uniform way to describe reflection over a base theory.
$\mathsf{CT}$ has the same arithmetical consequences as $\mathsf{ACA}$, and iterated truth corresponds to ramified analysis.
The type-free theories reach further: $\mathsf{KF}$ is as strong as ramified analysis below $\varepsilon_0$.
The SEP entry reports that Cantini's supervaluation theory $\mathsf{VF}$ reaches $\mathsf{ID}_1$, which is impredicative.
