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

The three group axioms, written as formal sentences, form a first-order theory:
$$\forall x \, \forall y \, \forall z \, ((x \cdot y) \cdot z = x \cdot (y \cdot z)), \quad \forall x \, (x \cdot e = x \land e \cdot x = x), \quad \forall x \, (x \cdot x^{-1} = e \land x^{-1} \cdot x = e).$$
The groups are exactly the structures in which all three sentences are true.

In general, a theory in a first-order language is a set of [[sentences|DKFGQTRYZE]] of that language, and its sentences play the role of axioms.
The structures in which all its sentences hold are its [[models|MVCH6N9SNW]].
Theories are the syntactic side of model theory, and proofs start from them.

## Motivation

Mathematics studies classes of structures through their axioms: groups, fields, orders, sets.
A first-order theory makes the axioms into a precise object, a set of formal sentences over a [[signature|WDVVEYD6AT]].
Then we can ask exact questions about the axioms themselves.
Are they consistent?
Do they decide every sentence?
Which structures satisfy them?

The answers can be surprising.
[[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]] is a first-order theory with one binary relation symbol $\in$, and most of mathematics can be written inside it.

## Notation

A theory is written $T$, $\Sigma$ or $\Gamma$, and an $L$-theory is a theory in the signature $L$.
$\mathrm{Mod}(T)$ is the class of models of $T$, and $\mathcal{M} \models T$ says that $\mathcal{M}$ is a model.
$\mathrm{Th}(\mathcal{M})$ is the set of sentences true in $\mathcal{M}$, the theory of $\mathcal{M}$.
$T \models \varphi$ says that $\varphi$ is a [[logical consequence|1HK0VYWTV7]] of $T$, and $T \vdash \varphi$ says that $\varphi$ is provable from $T$.
Some books call any set of sentences a theory.
Others ask a theory to be closed under consequence, and call a set that generates it a set of axioms.
In Mathlib, `FirstOrder.Language.Theory L` is `Set L.Sentence`.

## Remarks

### Examples

The theory of groups above has three sentences in the signature $\{ \cdot, e, {}^{-1} \}$.
The theory of [[dense linear orders without endpoints|2W4S2H4VYA]] is another finite theory, in the signature $\{ < \}$.
[[First-order Peano arithmetic|MPSCREYC3M]] has six axioms and one induction axiom for each formula, so it is infinite.
[[The theory of infinite sets|KFWXHKBHYT]] has, for each $n$, a sentence saying "there are at least $n$ elements", and its models are the infinite sets.
ZFC is infinite too, because its separation and replacement axioms are schemas with one axiom for each formula.
For each structure $\mathcal{M}$, the set $\mathrm{Th}(\mathcal{M})$ is a theory, often with no simple list of axioms.

### Non-examples

[[A set of formulas with a free variable|CSBB8RA545]], such as $\{ x \cdot e = x \}$, is not a theory, because its formula is not a sentence.
The class of all groups is not a theory either; it is the class of models of the theory of groups.
The second-order Peano axioms are not a first-order theory, because their induction axiom quantifies over sets.

### Axioms and closure

The [[deductive closure|CT4FZ84V45]] of $T$ is the set of sentences provable from $T$.
It has the same models as $T$, by the [[soundness theorem|AVD7T7J063]].
So a theory and its closure describe the same class of structures, and $T$ is a set of axioms for its closure.

A theory is [[recursively axiomatizable|3ANXZC3BEG]] when it has the same consequences as a decidable set of sentences.
Peano arithmetic and ZFC are recursively axiomatizable: an algorithm checks whether a string is one of their axioms.
$\mathrm{Th}(\mathbb{N}, 0, S, +, \cdot)$ is not, by Gödel's incompleteness theorem.

### Basic properties

If $T \subseteq T'$, then every model of $T'$ is a model of $T$.
$T$ is [[consistent|VM8TQ70CVJ]] exactly when it has a model, by [[Gödel's completeness theorem|WQ1ZE255SF]].
$\mathrm{Th}(\mathcal{M})$ is [[complete|655K8Y7VS8]]: for each sentence $\varphi$, it contains $\varphi$ or $\neg \varphi$.
A theory with arbitrarily large finite models has an infinite model, by the [[compactness theorem|1NR3HAWG9D]].

### Watch out

Do not confuse a theory with its models.
The theory of groups is a set of three sentences, and the groups are its models.

A theory need not be consistent.
The set $\{ \exists x \, (x = x), \neg \exists x \, (x = x) \}$ is a theory with no model.

An axiom of a first-order theory is a sentence.
So a law such as $x \cdot e = x$ is written $\forall x \, (x \cdot e = x)$.

### History

Hilbert's Foundations of Geometry of 1899 presented geometry as a list of axioms about undefined terms, and later axiomatic theories followed this pattern.
In the 1930s Tarski studied deductive systems, the sets of sentences closed under consequence.
Model theory then took a theory as a set of first-order sentences and studied the classes of its models.

### Try it

Is $\{ \forall x \, \forall y \, (x \cdot y = y \cdot x) \}$ a theory in the signature of groups?
Yes: both variables are bound, so its only element is a sentence.
Its models include all abelian groups, but also every commutative structure for $\cdot$, such as $(\mathbb{N}, +)$ with $e$ and ${}^{-1}$ read in any way.

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
2. The group of permutations of $\{ 1, 2, 3 \}$ is a model of the theory of groups.
3. In it, the two transpositions $(1\,2)$ and $(2\,3)$ do not commute, so the sentence is false there.
4. So the sentence is not a logical consequence of the theory, and by soundness it is not provable from it.
5. The sentence is true in $(\mathbb{Z}, +, 0, -)$, so its negation is not a consequence either.

The typical use of models is to show that a sentence is independent of a theory, as here.
Watch out: a theory may have true sentences that it does not prove, so "true in the intended model" and "provable" differ.

### L3 human

A theory $T$ determines the class $\mathrm{Mod}(T)$, and a class $K$ of structures determines its theory $\mathrm{Th}(K)$.
These two maps form a Galois connection, and its closed classes are the [[elementary classes|MEC3ZMC4F1]].
Complete consistent theories correspond to the classes of elementarily equivalent structures.
Model theory classifies complete theories by the number and the kind of their models, as in Morley's categoricity theorem and stability theory.
Proof theory studies the consequences of recursively axiomatized theories, such as Peano arithmetic and ZFC.
Gödel's incompleteness theorems show that a consistent, recursively axiomatizable theory that contains enough arithmetic is not complete.
