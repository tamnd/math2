---
tag: BCK5QXQXA6
kind: concept
name: Weak Kleene logic
aliases: [weak-kleene-connectives, bochvar-logic]
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
uses: [DWYCKAKXZD, P7E926JK13, SZHA10A9X7]
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

Here is disjunction in weak Kleene logic, with $0$ for false, $1$ for true and $\tfrac12$ for meaningless.

| $x \lor y$ | $y = 0$ | $y = \tfrac12$ | $y = 1$ |
|---|---|---|---|
| $x = 0$ | $0$ | $\tfrac12$ | $1$ |
| $x = \tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |
| $x = 1$ | $1$ | $\tfrac12$ | $1$ |

The corners are the classical table, and every row or column with a $\tfrac12$ is all $\tfrac12$.
So $1 \lor \tfrac12 = \tfrac12$: one meaningless part makes the whole sentence meaningless, even when the other part is true.

*Weak Kleene logic* uses these tables for every connective: a compound has the value $\tfrac12$ as soon as one part has it, and on $\{0, 1\}$ the connectives are classical.
The value $\tfrac12$ is *infectious*: it spreads from any part to the whole.
With the designated set $\{1\}$ the tables give Bochvar's logic $\mathrm{B}_3$, and with $\{\tfrac12, 1\}$ they give paraconsistent weak Kleene logic $\mathsf{PWK}$; see [[the definition|PJA9JVQ5XN]].
It is the [[many-valued logic|DWYCKAKXZD]] of meaningless sentences, as opposed to sentences whose value is not yet known.

## Motivation

Some sentences seem to have no meaning at all, for example the Liar sentence of the semantic paradoxes.
If a part of a sentence is meaningless, the whole sentence is plausibly meaningless too, even "$p$ or true".
[[Strong Kleene logic|SZHA10A9X7]] does not respect this, since it gives $\tfrac12 \lor 1 = 1$.
The weak Kleene tables give $\tfrac12 \lor 1 = \tfrac12$, and so they model meaninglessness rather than lack of information.
In computing, the same tables describe strict evaluation, which evaluates every argument before it combines them, so one error makes the whole result an error.

## Notation

Some texts write the middle value as $*$, read as "junk", and the algebra as $\mathbf{WK}_3$.
Bochvar's logic is written $\mathrm{B}_3$ and also called Bochvar's internal logic or Kleene's weak three-valued logic.
The paraconsistent version is written $\mathsf{PWK}$.

## Remarks

### Meaningless in, meaningless out

A formula $\varphi$ has the value $\tfrac12$ iff some variable of $\varphi$ has the value $\tfrac12$, by induction on $\varphi$.
So $\mathrm{B}_3$ has no tautologies: the all-$\tfrac12$ valuation gives every formula the value $\tfrac12$.
In $\mathsf{PWK}$ the tautologies are exactly the classical tautologies, as [[the example|XQD2D1T45M]] proves.
Every valid inference of $\mathrm{B}_3$ or $\mathsf{PWK}$ is classically valid, by restricting to valuations into $\{0, 1\}$.

### Rules that fail

Addition fails in $\mathrm{B}_3$: $p \not\models_{\mathrm{B}_3} p \lor q$, by $p = 1$ and $q = \tfrac12$.
[[Explosion and disjunctive syllogism fail in PWK|XQD2D1T45M]], so $\mathsf{PWK}$ is paraconsistent.
In both logics the failures come from variables that occur on one side of the inference and not on the other.

### Neighbors on the same values

[[Strong Kleene disjunction is not weak Kleene|AHM8HYZDMM]]: the strong table gives $1 \lor \tfrac12 = 1$.
The two schemes agree on $\{0, 1\}$ and on $\neg$, and they differ in two entries of each binary table.
Łukasiewicz implication is not weak Kleene either, since $0 \to_{Ł} \tfrac12 = 1$.
[[One formula in Ł3, K3 and weak Kleene logic|XZ2NRGZ69N]] puts the three tables side by side.

### Watch out

Do not read $\tfrac12$ as "unknown" here.
Under the weak reading it means "meaningless", and no further information can repair it.
Do not assume that addition $p \models p \lor q$ holds in every three-valued logic, because in $\mathrm{B}_3$ the new variable $q$ can infect the conclusion.

### History

Bochvar introduced $\mathrm{B}_3$ in 1938, to analyze the paradoxes of classical logic.
Halldén introduced $\mathsf{PWK}$ in his 1949 book *The Logic of Nonsense*.

### Try it

First, find the weak Kleene value of $(p \land \neg p) \lor q$ at $p = 0$ and $q = \tfrac12$.
It is $\tfrac12$, because $q$ has the value $\tfrac12$; strong Kleene logic gives $\max(0, \tfrac12) = \tfrac12$ too.

Second, is $p \land q \models p$ valid in $\mathrm{B}_3$?
Yes: if $p \land q = 1$, then neither part is $\tfrac12$ and $\min(p, q) = 1$, so $p = 1$.

## Explanations

### L1 human

Weak Kleene logic has three values: true, false and meaningless.
If any part of a sentence is meaningless, the whole sentence is meaningless.
So "the sky is blue, or this sentence is false" is meaningless.

### L2 human

To evaluate a formula, first look at its variables.
If one of them has the value $\tfrac12$, the answer is $\tfrac12$.
If none has, compute classically.
Watch out: in $\mathsf{PWK}$ the value $\tfrac12$ is designated, so meaningless premises count as acceptable.

### L3 human

The algebra $\mathbf{WK}_3$ is the two-element Boolean algebra with an absorbing element added.
In the terms of Bonzio, Paoli and Pra Baldi's 2022 book on logics of variable inclusion, $\mathsf{PWK}$ is the left variable inclusion companion of classical logic.
This means that $\Pi \models_{\mathsf{PWK}} \varphi$ iff some $\Sigma \subseteq \Pi$ classically entails $\varphi$ and every variable of $\Sigma$ occurs in $\varphi$.
