---
tag: DKFGQTRYZE
kind: concept
name: Sentence
aliases: [closed-formula]
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
uses: [HYJ10AF6RT, 9CNGDRAMGC, 983GZBQYT4, 2RBQPV02AS]
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

A sentence is a formula that makes a complete claim, so that a structure alone decides whether it is true.
Compare $\exists y \, (x < y)$ with $\forall x \, \exists y \, (x < y)$ in the order $\{ 0, 1, 2 \}$.
The first is true when $x = 0$ and false when $x = 2$, so it has no truth value until we choose $x$.
The second says "no element is largest", and it is simply false in $\{ 0, 1, 2 \}$.

Let $\sigma$ be a signature.
A *sentence* over $\sigma$, or *closed formula*, is a [[formula|HYJ10AF6RT]] $\varphi$ over $\sigma$ with no [[free variables|9CNGDRAMGC]]:
$$\operatorname{FV}(\varphi) = \emptyset.$$
Every occurrence of a variable in a sentence is bound, and in every [[structure|983GZBQYT4]] a sentence is either [[true|K7XDVK5854]] or false.

## Motivation

A formula with a free variable, such as $x < 1$ in the natural numbers, holds for $x = 0$ and fails for $x = 5$.
Its meaning is a set, here $\{ 0 \}$, not a truth value.
To state a property of a whole structure, such as "the order has no largest element", we need a formula whose truth depends on no variable.

Sentences are these formulas, and they carry the main weight of logic.
The axioms of a [[theory|92SWXST1ZM]] are sentences, a proof from axioms ends in a sentence, and the [[completeness theorem|WQ1ZE255SF]] compares provable sentences with true ones.
Later sub-areas on model theory and on incompleteness are, at heart, statements about sets of sentences.

## Notation

The [[formal definition|Q85MMH5DEY]] uses the set $\operatorname{FV}(\varphi)$ of free variables.
For a sentence we write $\mathcal{M} \models \varphi$ when $\varphi$ is true in $\mathcal{M}$, while a formula with free variables needs an assignment $s$, as in $\mathcal{M} \models \varphi[s]$.
If $\operatorname{FV}(\varphi) = \{ x_1, \ldots, x_n \}$, the *universal closure* of $\varphi$ is $\forall x_1 \cdots \forall x_n \, \varphi$ and the *existential closure* is $\exists x_1 \cdots \exists x_n \, \varphi$.
In Mathlib a sentence is a term of `FirstOrder.Language.Sentence L`, a formula whose free variables come from the empty type.

## Remarks

### Three quick checks

In the signature of orders, $\forall x \, \exists y \, (x < y)$ is a [[sentence|C0AVCG4SGF]].
Compute: $\operatorname{FV}(x < y) = \{ x, y \}$, then $\exists y$ removes $y$ and $\forall x$ removes $x$, which leaves $\emptyset$.

In the signature of arithmetic, $0 = S(0)$ is a sentence with no quantifier at all.
It has no variables, so $\operatorname{FV} = \emptyset$, and it is false in $\mathbb{N}$.

The group law $\forall x \, \forall y \, \forall z \, (x \cdot (y \cdot z) = (x \cdot y) \cdot z)$ is a sentence in the signature $\{ \cdot, e \}$, and so is the [[universal closure|YH98P98WA2]] $\forall x \, (x + 0 = x)$ of the equation $x + 0 = x$.
In the empty signature, $\exists x \, \exists y \, \neg x = y$ is a sentence that is true exactly in the structures with at least two elements.

### What fails to be a sentence

The formula $\exists y \, (x < y)$ is [[not a sentence|QMZVVXT9Q2]], because $x$ is free.
The equation $x + 0 = x$ is not a sentence either, since its quantifier is missing.
In $\forall x \, (x < y)$ the quantifier binds $x$, but $y$ stays free, so one quantifier is not enough.

### The rules you can use

If $\varphi$ is a sentence, all assignments give it the same truth value in $\mathcal{M}$, by the coincidence lemma of [[structures and satisfaction|NJDME6F845]].
So for a sentence exactly one of $\mathcal{M} \models \varphi$ and $\mathcal{M} \models \neg \varphi$ holds.
This fails for $x = 0$ in $\mathbb{N}$: neither $x = 0$ nor $\neg x = 0$ holds under every assignment.
Sentences are closed under the connectives, and $\forall x \, \varphi$ is a sentence exactly when $\operatorname{FV}(\varphi) \subseteq \{ x \}$.
A formula holds under every assignment exactly when its universal closure is true, and under some assignment exactly when its existential closure is true.
Two structures that make the same sentences true are [[elementarily equivalent|P3B1V182N4]].

### Watch out

In algebra, $x + y = y + x$ silently means "for all $x$ and $y$".
In logic the formula and its closure are different objects, and only the closure is a sentence.

A sentence need not contain a quantifier.
The atomic formula $0 = S(0)$ is a sentence because it has no variables.

The law "$\varphi$ fails, so $\neg \varphi$ holds" is safe only for sentences.
In $\mathbb{N}$, the formula $x = 0$ is not true under every assignment, and its negation is not true under every assignment either.

### History

Tarski's 1933 work on the concept of truth in formalized languages defined truth for sentences.
He first defined when a sequence of objects satisfies a formula, and then called a sentence true when every sequence satisfies it.
This two-step pattern is still the standard definition of truth in a structure.

### Try it

Is $\forall x \, (P(x) \to \exists y \, (R(x, y) \land \forall x \, P(x)))$ a sentence?
Yes: the inner $\forall x$ binds only the $x$ of its own scope, $\exists y$ removes $y$, and the outer $\forall x$ removes the remaining $x$, so $\operatorname{FV} = \emptyset$.

Write the universal closure of $x \cdot y = y \cdot x$.
It is $\forall x \, \forall y \, (x \cdot y = y \cdot x)$, and $\forall y \, \forall x \, (x \cdot y = y \cdot x)$ is an equivalent closure.

## Explanations

### L1 human

A sentence is a complete claim, which is right or wrong once we know which world we talk about.
"Every number has a larger number" is a sentence, and in the natural numbers it is true.
"$x$ has a larger number" is not a sentence, because we must first know which number $x$ is.
In the numbers $0, 1, 2$ it is true for $x = 0$ and false for $x = 2$.
In a sentence every letter is tied to a "for all" or a "there exists".

### L2 human

Here is the typical use: turning a law into an axiom.
The commutative law $\varphi = (x \cdot y = y \cdot x)$ has $\operatorname{FV}(\varphi) = \{ x, y \}$, so it is not yet a sentence.
Closing $y$ gives $\forall y \, \varphi$ with $\operatorname{FV} = \{ x \}$, still not a sentence.
Closing $x$ as well gives $\forall x \, \forall y \, \varphi$ with $\operatorname{FV} = \emptyset$.
In the group of integers under addition, read with $\cdot$ as $+$, this sentence is true, and in the group of permutations of three objects it is false.
Before you write a theory, check each axiom in this way and close the formulas that are not sentences.

### L3 human

For a structure $\mathcal{M}$, the set $\operatorname{Th}(\mathcal{M})$ of sentences true in $\mathcal{M}$ is a complete theory, since each sentence or its negation is true.
The sentences modulo logical equivalence form a Boolean algebra, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], and the complete theories correspond to the points of its Stone space.
A formula with $n$ free variables defines an $n$-ary relation in each structure, and a sentence is the case $n = 0$, where the relation is a truth value.
This view leads to types in model theory and to the categorical semantics of logic.
In Mathlib the same idea is in the types: `FirstOrder.Language.Sentence L` is the case of formulas over the empty type of free variables.
