---
tag: KXTP4P3GHT
kind: concept
name: First-degree entailment
aliases: [first-degree-entailment-fde, belnap-dunn-logic, fde]
msc: ["03B50", "03B47"]
topics: [WZP584JQ06]
audience: research
uses: [DWYCKAKXZD, P7E926JK13, SZHA10A9X7]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section F
    note: adopted
    mention: wikipedia://en/76765067#26V4
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.3 True, False, Neither, and Both
  - url: https://plato.stanford.edu/entries/truth-values/
    locator: 3.1 The notion of a logical order
  - url: https://plato.stanford.edu/entries/logic-relevance/
    locator: 2. Semantics for Negation
  - url: https://en.wikipedia.org/wiki/Four-valued_logic
    locator: Belnap
inventory: [12BTK3EH85]
---

## Summary

*First-degree entailment* $\mathsf{FDE}$, also called Belnap-Dunn logic $\mathrm{BD}$, is the four-valued [[many-valued logic|DWYCKAKXZD]] in $\neg$, $\land$, $\lor$ whose values are the subsets of $\set{T, F}$.
A sentence can be told true, told false, told both, or told neither; see [[the definition|AWEG5PR3GF]].
Consequence preserves "told at least true".
$\mathsf{FDE}$ contains both [[strong Kleene logic|SZHA10A9X7]] and Priest's $\mathsf{LP}$ as three-valued extensions, and it is neither explosive nor has it any tautologies.

## Motivation

Belnap imagined a computer that collects facts from several users, with no guarantee that they agree.
One user may tell it that $p$ is true, and another that $p$ is false.
In classical logic, $p$ and $\neg p$ entail every $q$, so one conflict would spoil all other data.
$\mathsf{FDE}$ records each sentence's evidence as a set of the values it was told, and conflicts about $p$ say nothing about an unrelated $q$.

## Notation

The four values are written $\mathbf{T} = \set{T}$, $\mathbf{F} = \set{F}$, $\mathbf{B} = \set{T, F}$ (both) and $\mathbf{N} = \emptyset$ (neither).
SEP writes $\mathsf{t}, \mathsf{f}, \mathsf{b}, \mathsf{n}$ and calls the algebra $\mathbf{DM}_4$, the four-element De Morgan algebra.
The SEP entry on truth values calls the structure with both orders the bilattice $\mathrm{FOUR}_2$.

## Remarks

### Examples

1. [[Explosion and excluded middle fail in FDE|5DFTBDQAR4]].
2. [[The two orders of FOUR and the Routley star|ZV62Y5X00V]] give two equivalent pictures of the same logic.
3. De Morgan laws and double negation hold: $\neg \neg p \models p$, $p \models \neg \neg p$, $\neg(p \land q) \models \neg p \lor \neg q$.
4. $p \land q \models p$ and $p \models p \lor q$ hold, as in classical logic.

### Non-examples

1. [[Strong Kleene logic is not FDE|QZ9FRRH7Y1]]: explosion holds in $\mathsf{K}_3$.
2. Classical logic is not $\mathsf{FDE}$, since $\models p \lor \neg p$ classically.

### Basic properties

1. $\mathsf{FDE}$ has no tautologies: the valuation with every variable $\mathbf{N}$ gives every formula the value $\mathbf{N}$.
2. Every $\mathsf{FDE}$-valid inference is valid in $\mathsf{K}_3$ and in $\mathsf{LP}$, since their matrices are submatrices of the four-valued one.
3. By SEP, three definitions give the same relation: preserve "contains $T$", preserve "does not contain $F$", or compare in the truth order.
4. Dunn introduced $\mathsf{FDE}$ as a fragment of the logic of entailment of Anderson and Belnap, as SEP reports.

### History

Dunn introduced the four-valued semantics of first-degree entailment, the system of Anderson and Belnap, in 1976.
Belnap promoted it in 1977 as a logic for computers that handle incomplete and inconsistent information.
Routley and Routley gave the star semantics for negation in 1972.

### Common errors

1. Taking $\mathbf{B}$ as the top of the truth order. In the truth order, $\mathbf{T}$ is top, $\mathbf{F}$ is bottom, and $\mathbf{B}$, $\mathbf{N}$ are incomparable.
2. Designating only $\mathbf{T}$. That gives a different logic, the exactly true logic, not $\mathsf{FDE}$.
3. Expecting $\mathbf{N} \land \mathbf{B} = \mathbf{N}$. It is $\mathbf{F}$, because $\mathbf{B}$ contributes falsity and $\mathbf{N}$ contributes no truth.

## Explanations

### L1 human

Think of a database that collects reports.
About each fact it may have heard "true", "false", both, or nothing.
A conclusion follows when every way of hearing "true" about the premises also gives "true" for the conclusion.
A conflict about one fact does not make every other fact true.

### L2 human

To compute a value, track truth and falsity separately.
$A \land B$ is told true iff both parts are told true; it is told false iff one part is told false.
$\neg A$ is told true iff $A$ is told false, and the other way around.
The typical use is to find counter-models with $\mathbf{B}$ for explosion and with $\mathbf{N}$ for excluded middle.

### L3 human

$\mathsf{FDE}$ is the logic of order of the De Morgan algebra $\mathbf{DM}_4$, and also its matrix logic with designated filter $\set{\mathbf{T}, \mathbf{B}}$.
Inclusion of subsets of $\set{T, F}$ is the information order, and the truth order is a second lattice on the same set; together they form the bilattice $\mathrm{FOUR}_2$.
The Routley star semantics, with an involution on worlds, extends to the [[Routley-Meyer semantics|H4Z8J0KMAY]] of relevance logics.
