---
tag: X9HV9C6X4F
kind: concept
name: Theory of a structure
aliases: [complete-theory-of-a-structure, theory-of-a-class-of-structures]
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
uses: [K7XDVK5854, 983GZBQYT4, DKFGQTRYZE, 92SWXST1ZM, MVCH6N9SNW, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_(mathematical_logic)
    locator: Theories associated with a structure
  - url: https://en.wikipedia.org/wiki/Complete_theory
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Summary

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]].
The *theory of $\mathcal{M}$* is the set $\operatorname{Th}(\mathcal{M}) = \set{\sigma : \sigma \text{ is an } L\text{-sentence and } \mathcal{M} \models \sigma}$ of all [[sentences|DKFGQTRYZE]] [[true in|K7XDVK5854]] $\mathcal{M}$.
For a class $K$ of $L$-structures, $\operatorname{Th}(K)$ is the set of $L$-sentences true in every member of $K$.
For a set $T$ of $L$-sentences, $\operatorname{Mod}(T)$ is the class of [[models|MVCH6N9SNW]] of $T$.
The theory $\operatorname{Th}(\mathcal{M})$ is always [[complete|655K8Y7VS8]], and two structures have the same theory exactly when they are [[elementarily equivalent|P3B1V182N4]].
The theory of a structure is the full first-order description of the structure, and it is the object that model theory tries to axiomatize and to understand.

## Motivation

A structure such as $(\N, +, \cdot)$ or $(\R, +, \cdot, <)$ is given to us before any axioms.
A natural question is which first-order statements are true in it.
The answer is one set of sentences, $\operatorname{Th}(\mathcal{M})$.
Many problems of logic are questions about this set: is it decidable, is it given by a simple list of axioms, does it have other models?
Tarski showed that $\operatorname{Th}(\R, +, \cdot, <)$ is axiomatized by the axioms of real closed fields, and Gödel's work shows that $\operatorname{Th}(\N, +, \cdot)$ has no computable axiomatization.

## Notation

The symbols are $\operatorname{Th}(\mathcal{M})$, $\operatorname{Th}(K)$ and $\operatorname{Mod}(T)$.
Some books write $\operatorname{Th}_L(\mathcal{M})$ to show the signature.
Mathlib calls $\operatorname{Th}(\mathcal{M})$ `FirstOrder.Language.completeTheory`, because it is a complete theory.
For a theory $T$, the set of sentences true in all models of $T$ is $\operatorname{Th}(\operatorname{Mod}(T))$, the set of [[consequences|1HK0VYWTV7]] of $T$.

## Remarks

### Examples

- For the structure with domain $\set{0, 1}$ and one unary relation $P = \set{1}$, the theory is axiomatized by one sentence; see [[this example|GR2JNR4030]].
- $\operatorname{Th}(\Q, <)$ is the set of consequences of the axioms of dense linear orders without endpoints; see [[this example|41Z2M61ZNV]].
- $\operatorname{Th}(\C, +, \cdot, 0, 1)$ is the set of consequences of the axioms of algebraically closed fields of characteristic $0$; see [[ACF|MT8TDVPBXB]].
- $\operatorname{Th}(\N, +, \cdot, 0, 1)$ is [[true arithmetic|9YQFEPHWJW]]; it is complete, but no computable set of axioms gives it.
- For the class $K$ of all groups, $\operatorname{Th}(K)$ is the set of consequences of the group axioms.

### Non-examples

- The theory of groups is not the theory of any structure, because it is not complete; see [[this non-example|3G396B8TR9]].
- A finite set of sentences that is true in $\mathcal{M}$ is a subset of $\operatorname{Th}(\mathcal{M})$, but in general it is not all of it; for $(\Q, <)$ the axioms of linear orders alone do not imply density.

### Basic properties

- $\operatorname{Th}(\mathcal{M})$ is complete: $\mathcal{M}$ is a model, and for each sentence $\sigma$ either $\sigma$ or $\neg\sigma$ is true in $\mathcal{M}$.
- $\mathcal{M} \equiv \mathcal{N}$ if and only if $\operatorname{Th}(\mathcal{M}) = \operatorname{Th}(\mathcal{N})$, and [[isomorphic structures have the same theory|NDTJ2E895C]].
- A complete theory $T$ with a model $\mathcal{M}$ has the same consequences as $\operatorname{Th}(\mathcal{M})$.
- *Galois connection.* For a set $T$ of sentences and a class $K$ of structures, $K \subseteq \operatorname{Mod}(T)$ if and only if $T \subseteq \operatorname{Th}(K)$. So $\operatorname{Mod}$ and $\operatorname{Th}$ form an antitone [[Galois connection|Q5JHEPRYQ6]].
- Hence $T \mapsto \operatorname{Th}(\operatorname{Mod}(T))$ and $K \mapsto \operatorname{Mod}(\operatorname{Th}(K))$ are closure operators. The first gives the set of consequences of $T$; the second gives the smallest [[elementary class|MEC3ZMC4F1]] that contains $K$.

### History

The relation between a structure and the set of sentences true in it goes back to Tarski's definition of truth of 1933.
Tarski's decision method for elementary algebra, which gives $\operatorname{Th}(\R, +, \cdot, <)$ by the axioms of real closed fields, was an early study of the theory of one particular structure.

### Common errors

- To think that $\operatorname{Th}(\mathcal{M})$ determines $\mathcal{M}$ up to isomorphism. It does so only for finite $\mathcal{M}$; $(\Q, <)$ and $(\R, <)$ have the same theory.
- To confuse $\operatorname{Th}(\mathcal{M})$ with a list of axioms for it. The set $\operatorname{Th}(\mathcal{M})$ always exists, but it may have no simple or computable axiomatization.
- To think that $\operatorname{Th}(K)$ is complete for a class $K$. The theory of the class of all groups does not decide commutativity.

## Explanations

### L1 human

The theory of a structure is the list of all true statements about it that a fixed language can make.
For the numbers $1, 2, 3, \dots$ with their order, the list contains "there is a smallest number" and "after each number comes a next one".
It does not contain "between any two numbers is a third", because that statement is false here.
Every statement or its opposite is on the list, so the list answers every question.

### L2 human

We decide three sentences for $\mathcal{M} = (\Z, <)$.

1. $\forall x \, \exists y \, (x < y)$: for each integer $x$, take $y = x + 1$. So the sentence is in $\operatorname{Th}(\mathcal{M})$.
2. $\exists x \, \forall y \, \neg(y < x)$: no integer is smallest, since $x - 1 < x$. So the negation of this sentence is in $\operatorname{Th}(\mathcal{M})$.
3. $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \land z < y))$: false for $x = 0$, $y = 1$. So its negation is in $\operatorname{Th}(\mathcal{M})$.

The typical use of $\operatorname{Th}(\mathcal{M})$ is to compare structures: if $\operatorname{Th}(\mathcal{M}) = \operatorname{Th}(\mathcal{N})$, a first-order result about one holds for the other.
A trap is to put a statement about subsets, such as "every nonempty bounded set has a least element", into $\operatorname{Th}(\mathcal{M})$; it is not a first-order sentence.

### L3 human

The pair $\operatorname{Mod}$, $\operatorname{Th}$ is the syntax-semantics duality of logic, of the same form as the duality between ideals and varieties in algebraic geometry.
The closed sets of sentences are the deductively closed theories, and the closed classes are the elementary classes.
The complete theories are the maximal satisfiable closed sets, and they are the points of the Stone space of the Lindenbaum algebra of sentences.
So the space of complete $L$-theories is a compact Hausdorff space, and the [[compactness theorem|1NR3HAWG9D]] is the compactness of this space.
The study of the theories of particular structures, such as fields and groups, is the subject of the later sub-areas on [[the model theory of fields|Q3S2YF9BCR]] and [[decidability in number theory|ZQFA17MJSB]].
