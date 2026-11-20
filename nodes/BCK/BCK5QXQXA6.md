---
tag: BCK5QXQXA6
kind: concept
name: Weak Kleene logic
aliases: [weak-kleene-connectives, bochvar-logic]
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
uses: [DWYCKAKXZD, ~d80767f3, SZHA10A9X7]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section W
    note: adopted
    mention: wikipedia://en/76765067#NKIB
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Bochvar's internal three-valued logic
inventory: [7CJJ970Q4Q]
---

## Summary

*Weak Kleene logic* uses three values $0$, $\tfrac12$, $1$ and the rule that a compound has the value $\tfrac12$ as soon as one part has it; on $\set{0, 1}$ the connectives are classical.
The value $\tfrac12$ is *infectious*: it spreads from any part to the whole.
With designated set $\set{1}$ the tables give Bochvar's internal logic $\mathrm{B}_3$; with designated set $\set{\tfrac12, 1}$ they give paraconsistent weak Kleene logic $\mathsf{PWK}$; see [[the definition|~aa4cad6e]].
It is a [[many-valued logic|DWYCKAKXZD]] for meaningless sentences, where one meaningless part makes the whole sentence meaningless.

## Motivation

Some sentences seem to have no meaning at all, for example a sentence of the semantic paradoxes such as the Liar.
If a part of a sentence is meaningless, the whole sentence is plausibly meaningless too, even "$p$ or true".
[[Strong Kleene logic|SZHA10A9X7]] does not respect this, since it gives $\tfrac12 \lor 1 = 1$.
The weak Kleene tables give $\tfrac12 \lor 1 = \tfrac12$ and so model meaninglessness rather than lack of information.
In computing, the same tables describe strict evaluation, which evaluates every argument before it combines them.

## Notation

The SEP entry writes the middle value as $*$, read as "junk", and the algebra as $\mathbf{WK}_3$.
Bochvar's logic is written $\mathrm{B}_3$; the paraconsistent version is $\mathsf{PWK}$.
The Wikipedia article "Many-valued logic" calls the same tables Bochvar's internal three-valued logic and Kleene's weak three-valued logic.

## Remarks

### Examples

1. $1 \lor \tfrac12 = \tfrac12$ and $0 \land \tfrac12 = \tfrac12$, while strong Kleene gives $1$ and $0$.
2. [[Paraconsistent weak Kleene logic|~0688c235]] invalidates explosion and disjunctive syllogism.
3. [[One formula in Ł3, K3 and weak Kleene logic|~71d1e02f]] compares the tables.
4. Addition fails in $\mathrm{B}_3$: $p \not\models_{\mathrm{B}_3} p \lor q$, by $p = 1$, $q = \tfrac12$.

### Non-examples

1. [[Strong Kleene disjunction is not weak Kleene|~a72cd9fe]]: it gives $1 \lor \tfrac12 = 1$.
2. Łukasiewicz implication is not weak Kleene, since $0 \to_{Ł} \tfrac12 = 1$.

### Basic properties

1. $\mathrm{B}_3$ has no tautologies: the all-$\tfrac12$ valuation gives every formula the value $\tfrac12$.
2. The tautologies of $\mathsf{PWK}$ are exactly the classical tautologies; see [[the example|~0688c235]].
3. A formula $\varphi$ has the value $\tfrac12$ iff some variable of $\varphi$ has the value $\tfrac12$; this follows by induction on $\varphi$.
4. Every valid inference of $\mathrm{B}_3$ or $\mathsf{PWK}$ is classically valid, by restricting to valuations into $\set{0, 1}$.

### History

Bochvar introduced $\mathrm{B}_3$ in 1938 to analyze the paradoxes of classical logic.
Halldén introduced $\mathsf{PWK}$ in his 1949 book *The Logic of Nonsense*.

### Common errors

1. Confusing the weak and strong tables. They agree on $\set{0, 1}$ and on $\neg$, and differ in two entries of each binary table.
2. Thinking that $\tfrac12$ means "unknown". Under the weak reading it means "meaningless", and no further information can repair it.
3. Assuming that addition $p \models p \lor q$ holds in every three-valued logic. It fails in $\mathrm{B}_3$, because $q$ can infect the conclusion.

## Explanations

### L1 human

Weak Kleene logic has three values: true, false and meaningless.
If any part of a sentence is meaningless, the whole sentence is meaningless.
So "the sky is blue, or this sentence is false" is meaningless.

### L2 human

To evaluate a formula, first look at its variables.
If one has the value $\tfrac12$, the answer is $\tfrac12$.
If none has, compute classically.
A trap: in $\mathsf{PWK}$ the value $\tfrac12$ is designated, so meaningless premises count as acceptable.

### L3 human

The algebra $\mathbf{WK}_3$ is the classical two-element algebra with an absorbing element added.
The SEP entry describes $\mathrm{B}_3$ and $\mathsf{PWK}$ as the right and left variable inclusion companions of classical logic, after Bonzio, Paoli and Pra Baldi (2022).
For $\mathsf{PWK}$ this means: $\Pi \models \varphi$ iff some $\Sigma \subseteq \Pi$ classically entails $\varphi$ and every variable of $\Sigma$ occurs in $\varphi$.
