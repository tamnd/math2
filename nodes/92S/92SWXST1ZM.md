---
tag: 92SWXST1ZM
kind: concept
name: First-order theory
aliases: [theory, theory-mathematical-logic]
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: ug2
uses: [WDVVEYD6AT, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_(mathematical_logic)
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 2
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
same_as:
  wikidata: Q10859910
  wikipedia: Theory (mathematical logic)
---

## Summary

A theory in a first-order language is a set of [[sentences|DKFGQTRYZE]] of that language.
Its sentences play the role of axioms, such as the axioms of groups or of fields.
The structures in which all its sentences hold are its [[models|MVCH6N9SNW]].
Theories are the syntactic side of model theory, and they are the objects that proofs start from.

## Motivation

Mathematics studies classes of structures through their axioms: groups, fields, orders, sets.
A first-order theory makes the axioms into a precise object, a set of formal sentences over a [[signature|WDVVEYD6AT]].
Then one can ask exact questions about the axioms themselves.
Examples are whether they are consistent, whether they decide every sentence, and which structures satisfy them.

## Notation

1. A theory is written $T$, $\Sigma$ or $\Gamma$, and an $L$-theory is a theory in the signature $L$.
2. $\mathrm{Mod}(T)$ is the class of models of $T$, and $\mathcal{M} \models T$ says that $\mathcal{M}$ is a model.
3. $\mathrm{Th}(\mathcal{M})$ is the set of sentences true in $\mathcal{M}$, the theory of $\mathcal{M}$.
4. $T \models \varphi$ says that $\varphi$ is a [[logical consequence|1HK0VYWTV7]] of $T$, and $T \vdash \varphi$ says that $\varphi$ is provable from $T$.
5. Some books call any set of sentences a theory. Others ask a theory to be closed under consequence and call a generating set a set of axioms.
6. In Mathlib, `FirstOrder.Language.Theory L` is `Set L.Sentence`.

## Remarks

### Examples

1. The theory of groups has three sentences in the signature $\set{\cdot, e, {}^{-1}}$: associativity, the identity law and the inverse law.
2. [[First-order Peano arithmetic|~f46a5ae7]] has six axioms and one induction axiom for each formula.
3. [[The theory of infinite sets|~d9ce4b08]] has, for each $n$, a sentence saying "there are at least $n$ elements", and its models are the infinite sets.
4. The theory of [[dense linear orders without endpoints|2W4S2H4VYA]] is a finite theory in the signature $\set{<}$.
5. For each structure $\mathcal{M}$, the theory $\mathrm{Th}(\mathcal{M})$ is a theory, often with no simple list of axioms.

### Non-examples

1. [[A set of formulas with a free variable|~87057868]], such as $\set{x \cdot e = x}$, is not a theory, because its formula is not a sentence.
2. The class of all groups is not a theory. It is the class of models of the theory of groups, a class of structures and not a set of sentences.
3. The second-order Peano axioms are not a first-order theory, because the induction axiom quantifies over sets.

### Basic properties

1. If $T \subseteq T'$, then every model of $T'$ is a model of $T$.
2. The [[deductive closure|CT4FZ84V45]] of $T$ has the same models as $T$, by soundness and completeness.
3. $T$ is [[consistent|VM8TQ70CVJ]] exactly when it has a model, by Gödel's completeness theorem.
4. $\mathrm{Th}(\mathcal{M})$ is [[complete|655K8Y7VS8]]: for each sentence $\varphi$, it contains $\varphi$ or $\neg \varphi$.
5. A theory is [[recursively axiomatizable|3ANXZC3BEG]] when it has the same consequences as a decidable set of sentences, as Peano arithmetic does.
6. A theory with arbitrarily large finite models has an infinite model, by the [[compactness theorem|1NR3HAWG9D]].

### History

Hilbert's Foundations of Geometry of 1899 set the model of a theory as a list of axioms about undefined terms.
In the 1930s Tarski studied deductive systems, the sets of sentences closed under consequence.
Model theory then took a theory as a set of first-order sentences and studied the classes of its models.

### Common errors

1. A student confuses a theory with its models. The theory of groups is a set of three sentences, and the groups are its models.
2. A student thinks a theory must be consistent. The set $\set{\exists x \, (x = x), \neg \exists x \, (x = x)}$ is a theory with no model.
3. A student writes axioms with free variables. An axiom of a first-order theory is a sentence, so a law such as $x \cdot e = x$ is written $\forall x \, (x \cdot e = x)$.

## Explanations

### L1 human

A theory is a list of rules written in a formal language.
For example, the three group axioms, written with the symbols $\cdot$, $e$ and ${}^{-1}$, form the theory of groups.
A theory does not say which objects satisfy the rules.
The objects that satisfy all the rules, here all groups, are the models of the theory.
The integers with addition are one model, and the rotations of a square are another.

### L2 human

We decide whether the sentence $\forall x \, \forall y \, (x \cdot y = y \cdot x)$ follows from the theory of groups.

1. The sentence says that the group is abelian.
2. The group of permutations of $\set{1, 2, 3}$ is a model of the theory of groups.
3. In it, the two transpositions $(1\,2)$ and $(2\,3)$ do not commute, so the sentence is false there.
4. So the sentence is not a logical consequence of the theory, and by completeness it is not provable from it.
5. The sentence is true in $(\mathbb{Z}, +, 0, -)$, so its negation is not a consequence either.

The typical use of models is to show that a sentence is independent of a theory, as here.
A trap: a theory may have true sentences that it does not prove, so "true in the intended model" and "provable" differ.

### L3 human

A theory $T$ determines the class $\mathrm{Mod}(T)$, and a class $K$ of structures determines its theory $\mathrm{Th}(K)$.
These two maps form a Galois connection, and its closed classes are the [[elementary classes|MEC3ZMC4F1]].
Complete theories correspond to classes of structures that satisfy the same sentences, the elementary equivalence classes.
Model theory classifies complete theories by the number and the kind of their models, as in Morley's categoricity theorem and stability theory.
Proof theory studies the consequences of recursively axiomatized theories, such as Peano arithmetic and ZFC.
Gödel's incompleteness theorems show that a consistent, recursively axiomatizable theory that contains enough arithmetic is not complete.
