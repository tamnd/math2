---
tag: 4CBCWZQZ12
kind: concept
name: Truth-value gap
aliases: [gap, paracomplete-truth, neither-true-nor-false]
msc: ["03A05", "03B50"]
topics: [6Q4JJ2MMV8]
audience: grad
uses: [SZHA10A9X7, 0RYYK8PG4S, QQPVKJSAX1, ES71QTSTNV]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section T
    note: adopted
    mention: wikipedia://en/76765067#TSHX
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.1 Paracomplete"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.3 Expressive power and 'revenge'"
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 4.6 Axiomatisations of Kripke's theory with supervaluations"
  - url: https://plato.stanford.edu/entries/sorites-paradox/
    locator: "Sorites Paradox, 3.3.1 Supervaluationism"
inventory: [ZEAQCDDCT8]
---

## Summary

A *truth-value gap* is a sentence that is neither true nor false in a given semantics.
In a three-valued semantics such as [[strong Kleene logic|SZHA10A9X7]], a gap is a sentence with the third value $\mathrm{u}$.
In a partial interpretation $(E, A)$ of a truth predicate $T$, a sentence $\varphi$ is a gap if $\ulcorner \varphi \urcorner \notin E$ and $\ulcorner \varphi \urcorner \notin A$.
A theory of truth that allows gaps, and so gives up the [[law of excluded middle|0RYYK8PG4S]] for some sentences, is called *paracomplete*.
The main example is [[Kripke's theory of truth|ES71QTSTNV]], in which the [[liar|KBYY281V8T]] is a gap.

## Motivation

The [[naive truth schema|99XVFR5ZN5]] and classical logic together give the liar paradox.
A paracomplete theory keeps the equivalence of $\varphi$ and $T(\ulcorner \varphi \urcorner)$, and it rejects excluded middle for the liar.
The SEP entry describes this view: the liar teaches that some sentences "neither hold nor do not hold".
The same idea appears for vague predicates, where borderline cases are often treated as gaps.

## Notation

1. The three values are written $1, 0, \mathrm{u}$, or $\mathsf{t}, \mathsf{f}, \mathsf{n}$, or true, false, neither.
2. In a partial model, $E$ is the extension and $A$ the anti-extension of $T$. They are disjoint, and they need not cover the domain.
3. In [[supervaluational semantics|QQPVKJSAX1]], a sentence is *super-true* if it is true on every admissible precisification and *super-false* if false on all. A gap is a sentence that is neither.

## Remarks

### Examples

1. The [[liar is a gap in every Kripke fixed point|XRRGJK0927]].
2. The [[truth-teller|XADBJH4872]] is a gap in the least Kripke fixed point. It is true or false in some other fixed points.
3. In strong Kleene logic, $p \vee \neg p$ is a gap when $p$ is a gap. So $K_3$ has no valid sentences, as the SEP entry notes.
4. In a supervaluation scheme, the liar $\lambda$ is a gap, but $\lambda \vee \neg \lambda$ is super-true. The SEP entry on axiomatic truth reports that Cantini's system VF proves $T(\ulcorner \lambda \vee \neg \lambda \urcorner)$.
5. In supervaluational treatments of vagueness, "$n$ grains make a heap" is a gap for a borderline $n$; see the [[sorites paradox|2BV7KAZG1H]].

### Non-examples

1. The sentence $T(\ulcorner 0 = 0 \urcorner)$ is [[grounded and true|RCGBM5KS25]], so it is not a gap in any fixed point.
2. In the logic of paradox, the liar is a [[truth-value glut|WH94DG6D3Q]], not a gap; see [[this example|4204V9JTCV]].
3. In the [[revision theory|ZQ4TWM7K6E]], each stage is classical, so no sentence is a gap at any stage. The liar is unstable instead.
4. In a [[Tarskian hierarchy|Z6MCGB0ZFX]], a sentence $T_0(\ulcorner \psi \urcorner)$ with $\psi$ outside $\mathcal{L}_0$ is false, not a gap.

### Basic properties

1. In strong Kleene logic, a compound sentence is a gap only if at least one component is a gap.
2. In a Kripke fixed point, $\varphi$ is a gap if and only if $T(\ulcorner \varphi \urcorner)$ is a gap, by the semantic T-schema.
3. A paracomplete theory with a transparent truth predicate cannot assert $\neg T(\ulcorner \lambda \urcorner)$. By transparency this would assert $\lambda$, and then $T(\ulcorner \lambda \urcorner)$.
4. So the claim "the liar is a gap" cannot be stated truly inside the theory; this is the *revenge* problem.
5. A paracomplete theory can still be consistent with the full equivalence of $\varphi$ and $T(\ulcorner \varphi \urcorner)$, as Kripke's construction shows.

### History

The SEP entry names van Fraassen (1968, 1970) as an early proposal to use a logic with gaps for the liar.
It names Kripke (1975) and the related work of Martin and Woodruff (1975) as the most influential.
The SEP entry on the sorites names van Fraassen's supervaluation semantics (1966) as the source of the supervaluational treatment of vagueness.

### Common errors

1. Thinking that a gap is a third truth value that a sentence "has". In a partial model the sentence only lacks the two classical values.
2. Thinking that gaps solve the strengthened liar. The sentence "this sentence is not true" is not true if it is a gap, which is what it says.
3. Confusing supervaluation gaps with strong Kleene gaps. In supervaluation, $\varphi \vee \neg \varphi$ is true even when $\varphi$ is a gap.

## Explanations

### L1 human

Most sentences are true or false.
A gap is a sentence that is neither.
Some logicians say that the liar sentence is a gap: it has no truth value at all.
This avoids the paradox, because the argument needs the liar to be true or false.

### L2 human

1. In a Kripke fixed point $(E, A)$, the liar $\lambda$ has the same value as $\neg T(\ulcorner \lambda \urcorner)$.
2. If $\ulcorner \lambda \urcorner \in E$, then $\lambda$ is true, so $T(\ulcorner \lambda \urcorner)$ is false, so $\ulcorner \lambda \urcorner \in A$. This contradicts $E \cap A = \emptyset$.
3. The same argument starting from $\ulcorner \lambda \urcorner \in A$ gives a contradiction.
4. So $\ulcorner \lambda \urcorner$ is in neither set: the liar is a gap.

The typical use is to keep the transparency of truth at the cost of excluded middle.
The trap is the strengthened liar: "not true" includes "gap", so a gappy liar is not true.

### L3 human

Gaps are the order-theoretic bottom element of a partial information order on values.
The [[Kripke-Feferman theory|VQG258JQAD]] gives an axiomatic form of the gap view in classical logic, with $T$ for "true" and $T(\ulcorner \neg \cdot \urcorner)$ for "false".
The dual idea, a sentence that is both true and false, is a [[glut|WH94DG6D3Q]], and [[first-degree entailment|KXTP4P3GHT]] allows both.
