---
tag: ~dbdabe57
kind: concept
name: Ludics
msc: ["03F52", "03B70"]
topics: [98QF5J4W16]
audience: research
uses: [2P2184B6HE, H408H4WHBA, K67C2N2QAH]
sources:
  - url: https://en.wikipedia.org/wiki/Ludics
    locator: lead
  - url: https://en.wikipedia.org/wiki/Affine_logic
    locator: lead
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.2 Focused proofs; 3.2 Semantics of proofs
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - doi: 10.1017/S096012950100336X
    locator: pages 301-506
    note: Girard, Locus Solum, From the rules of logic to the logic of rules, Mathematical Structures in Computer Science 11 (2001)
---

## Summary

*Ludics* is an analysis of the principles that govern the inference rules of logic, proposed by Girard.
It works with *loci*, or locations over a base, in place of formulas.
It builds compound connectives by *focusing*, a technique for [[linear logic|2P2184B6HE]] that the Wikipedia article attributes to Andreoli.
The Wikipedia article states that ludics follows the paradigm of interactive computation and that it is closely related to game semantics.

## Motivation

The Wikipedia article contrasts two views of a proposition.
In the first view, the meaning of a proposition comes from its introduction and elimination rules.
In the second view, we fix a computational system first, and a proposition means the set of its realizers.
The article states that the main result of ludics is a relation between these two views.

## Notation

Focusing classifies formulas by polarity.
The Wikipedia article calls a proposition *positive* if its meaning comes from its introduction rules, and *negative* if it comes from its elimination rules.
The SEP entry calls a formula *asynchronous* if its main connective is $\top$, $\mathbin{\&}$, $\bot$, $\mathbin{\wp}$, $?$ or $\forall$.
It calls a formula *synchronous* if its main connective is $0$, $\oplus$, $1$, $\otimes$, $!$ or $\exists$.

## Remarks

### Examples

1. Loci: the Wikipedia article states that ludics abstracts from formulas to their distinct occurrences, and that loci can be seen as pointers to memory.
2. Focused proofs: the SEP entry states that, in the one-sided [[sequent calculus of linear logic|H408H4WHBA]], proof search can alternate two phases without loss of completeness.
   In the asynchronous phase, the rules for asynchronous formulas apply in any order.
   In the synchronous phase, one synchronous formula is the focus, and its rules apply to it and to its synchronous subformulas.
3. Compound connectives: in a focused calculus, a positive connective is defined by its introduction rules alone, and the form of its elimination rules follows.
4. Realizers: the Wikipedia article states that a realizer for "$A$ implies $B$" is a computable function from realizers for $A$ to realizers for $B$.

### Non-examples

1. A derivation in the sequent calculus of linear logic is not itself an object of ludics, since ludics replaces formulas by loci.
2. Game semantics is not ludics.
   The SEP entry describes game semantics as the reading of formulas as games and proofs as strategies; the Wikipedia article calls ludics closely related to it.

### Basic properties

1. The Wikipedia article states that Girard shows this for second-order [[affine logic|K67C2N2QAH]]:
   with a computational system that has nontermination and error stops as effects, realizability and focalization give the same meaning to types.
2. The Wikipedia article on affine logic states that affine logic is the foundation of ludics.
3. The SEP entry states that the completeness of focused proofs for linear logic is proved in Andreoli's paper of 1992.

### History

The Wikipedia article states that Girard proposed ludics in the paper "Locus Solum: from the rules of logic to the logic of rules".
The DOI cited here gives the journal: Mathematical Structures in Computer Science, volume 11, 2001, pages 301 to 506.

### Common errors

Focusing is not an invention of ludics: the Wikipedia article attributes it to Andreoli, and ludics uses it.
Ludics is not a new set of connectives on top of linear logic; it is a theory of what the rules of a connective are.

## Explanations

### L1 human

Ludics asks what a logical rule is, before it asks what a formula means.
It replaces formulas by addresses, and it follows the model of interactive computation, as game semantics does.

### L2 human

We search for a focused proof of $\vdash p^{\perp} \mathbin{\wp} q^{\perp}, q \otimes p$.

1. The formula $p^{\perp} \mathbin{\wp} q^{\perp}$ is asynchronous, so the asynchronous phase applies the rule for $\mathbin{\wp}$.
2. This gives $\vdash p^{\perp}, q^{\perp}, q \otimes p$, with no asynchronous formula left.
3. The formula $q \otimes p$ is synchronous, so it becomes the focus.
4. The rule for $\otimes$ splits the context into $\vdash q^{\perp}, q$ and $\vdash p^{\perp}, p$.
5. Each premise is an axiom.

The typical use of focusing is to cut down the search space: the order of the asynchronous rules does not matter.
A trap: in step 4, the split $\vdash p^{\perp}, q$ and $\vdash q^{\perp}, p$ does not lead to a proof, so the focus must choose the split.

### L3 human

Ludics starts from focusing, where the rules of each connective are grouped by polarity.
It then replaces formulas by loci, so that what remains is the structure of the rules.
The Wikipedia article states that ludics gives in this way an abstract syntax for computer science.
