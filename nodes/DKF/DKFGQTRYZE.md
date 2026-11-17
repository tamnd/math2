---
tag: DKFGQTRYZE
kind: concept
name: Sentence
aliases: [closed-formula]
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
uses: [HYJ10AF6RT, 9CNGDRAMGC, 983GZBQYT4, K7XDVK5854, 2RBQPV02AS]
sources:
  - url: https://en.wikipedia.org/wiki/Sentence_(mathematical_logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
  - book: isbn:9780122384523
    locator: Section 2.1
same_as:
  wikidata: Q2509500
  wikipedia: Sentence (mathematical logic)
---

## Summary

Let $\sigma$ be a signature.
A *sentence* over $\sigma$, or *closed formula*, is a [[formula|HYJ10AF6RT]] $\varphi$ over $\sigma$ with no [[free variables|9CNGDRAMGC]], that is, with $\operatorname{FV}(\varphi) = \emptyset$.
Every occurrence of a variable in a sentence is bound by a quantifier.
So in a [[structure|983GZBQYT4]] $\mathcal{M}$ a sentence is either [[true|K7XDVK5854]] or false, with no values of variables to choose.
Sentences are the statements of mathematics in first-order form: axioms, theories and theorems consist of sentences.

## Motivation

A formula with a free variable, such as $x < 1$, makes no claim on its own.
In the natural numbers it holds when $x = 0$ and fails when $x = 5$.
Its meaning is a set, here $\set{0}$, and not a truth value.
To state a property of a whole structure, such as "the order has no largest element", we need a formula whose truth does not depend on any variable.
The sentences are these formulas.
They are what a theory assumes and what a proof proves, and they are the objects of the [[completeness theorem|WQ1ZE255SF]].

## Notation

1. The [[formal definition|Q85MMH5DEY]] uses the set $\operatorname{FV}(\varphi)$ of free variables.
2. For a sentence $\varphi$, we write $\mathcal{M} \models \varphi$ when $\varphi$ is true in $\mathcal{M}$. For a formula with free variables we write $\mathcal{M} \models \varphi[s]$, with an assignment $s$.
3. Some books write $\operatorname{Sent}_\sigma$ for the set of sentences over $\sigma$.
4. If $\operatorname{FV}(\varphi) = \set{x_1, \ldots, x_n}$, the *universal closure* of $\varphi$ is the sentence $\forall x_1 \cdots \forall x_n \, \varphi$, and the *existential closure* is $\exists x_1 \cdots \exists x_n \, \varphi$.
5. In Mathlib a sentence is a term of `FirstOrder.Language.Sentence L`. It is a formula whose free variables come from the empty type.

## Remarks

### Examples

1. In the signature of orders, $\forall x \, \exists y \, (x < y)$ is a [[sentence|C0AVCG4SGF]]. It says that there is no largest element.
2. In the signature of arithmetic, $0 = S(0)$ is a sentence without quantifiers. It has no variables at all, and it is false in $\mathbb{N}$.
3. The group axiom $\forall x \, \forall y \, \forall z \, (x \cdot (y \cdot z) = (x \cdot y) \cdot z)$ is a sentence in the signature $\set{\cdot, e}$.
4. In the empty signature, $\exists x \, \exists y \, \neg x = y$ is a sentence. It is true exactly in the structures with at least two elements.
5. The [[universal closure|YH98P98WA2]] of $x + 0 = x$ is the sentence $\forall x \, (x + 0 = x)$.

### Non-examples

1. $\exists y \, (x < y)$ is [[not a sentence|QMZVVXT9Q2]], because $x$ is free. Its truth in a finite order depends on the value of $x$.
2. $x + 0 = x$ is not a sentence, because $x$ is free. The quantifier is missing.
3. $\forall x \, (x < y)$ is not a sentence. The quantifier binds $x$, and $y$ stays free.

### Basic properties

1. If $\varphi$ is a sentence and $s, s'$ are assignments into $\mathcal{M}$, then $\mathcal{M} \models \varphi[s]$ exactly when $\mathcal{M} \models \varphi[s']$. This is a case of the coincidence lemma of [[structures and satisfaction|NJDME6F845]], since $\varphi$ has no free variables.
2. For a sentence $\varphi$, exactly one of $\mathcal{M} \models \varphi$ and $\mathcal{M} \models \neg \varphi$ holds. For the formula $x = 0$ in $\mathbb{N}$, neither $x = 0$ nor $\neg x = 0$ holds under every assignment.
3. Sentences are closed under the connectives. A quantification $\forall x \, \varphi$ is a sentence exactly when $\operatorname{FV}(\varphi) \subseteq \set{x}$.
4. A formula $\varphi$ holds in $\mathcal{M}$ under every assignment exactly when its universal closure is true in $\mathcal{M}$. It holds under some assignment exactly when its existential closure is true.
5. A first-order [[theory|92SWXST1ZM]] is a set of sentences. Two structures that make the same sentences true are elementarily equivalent.

### History

Tarski's work of 1933 on the concept of truth in formalized languages defined truth for sentences.
He defined first the satisfaction of formulas by sequences of objects, and then called a sentence true when every sequence satisfies it.
This pattern is still the standard definition of truth in a structure.

### Common errors

1. Students treat a formula with free variables as if it were universally quantified. In algebra $x + y = y + x$ means the closure, but in logic the formula and its closure are different objects.
2. Students think that a sentence must contain a quantifier. The atomic formula $0 = S(0)$ is a sentence.
3. Students think that $\neg \varphi$ is true in $\mathcal{M}$ whenever $\varphi$ fails in $\mathcal{M}$ for a formula with free variables. This holds only for sentences, as property 2 shows.

## Explanations

### L1 human

A sentence is a complete claim, which is right or wrong once we know what world we talk about.
"Every number has a larger number" is a sentence: in the natural numbers it is true.
"$x$ has a larger number" is not a sentence, because we must first know which number $x$ is.
In the numbers $0, 1, 2$ it is true for $x = 0$ and false for $x = 2$.
In a sentence every letter is tied to a "for all" or a "there exists".

### L2 human

We decide whether $\varphi = \forall x \, (P(x) \to \exists y \, (R(x, y) \land \forall x \, P(x)))$ is a sentence.

1. $\operatorname{FV}(P(x)) = \set{x}$, so $\operatorname{FV}(\forall x \, P(x)) = \emptyset$.
2. $\operatorname{FV}(R(x, y) \land \forall x \, P(x)) = \set{x, y} \cup \emptyset = \set{x, y}$.
3. $\exists y$ removes $y$, giving $\set{x}$.
4. The implication gives $\set{x} \cup \set{x} = \set{x}$.
5. The outer $\forall x$ removes $x$, so $\operatorname{FV}(\varphi) = \emptyset$, and $\varphi$ is a sentence.

The typical use is the statement of axioms: before we write a theory, we check that each axiom is a sentence, and we close the formulas that are not.
The trap is to stop at the inner $\forall x$ in step 1: it binds only the $x$ of its own scope, and the $x$ in $R(x, y)$ is bound by the outer quantifier.

### L3 human

For a structure $\mathcal{M}$, the set $\operatorname{Th}(\mathcal{M})$ of sentences true in $\mathcal{M}$ is a complete theory, because of property 2.
The sentences modulo logical equivalence form a Boolean algebra, the Lindenbaum algebra, and the complete theories correspond to the points of its Stone space.
A formula with $n$ free variables defines an $n$-ary relation in each structure, and a sentence is the case $n = 0$, where the relation is a truth value.
So the sentences are the zero-place part of a family of definable relations, and this view leads to types and to the categorical semantics of logic.
In Mathlib the same idea appears in the types: `FirstOrder.Language.Sentence L` is the case of formulas whose free variables come from the empty type.
The incompleteness theorems and the decidability results of later sub-areas are statements about sets of sentences.
