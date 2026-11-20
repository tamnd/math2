---
tag: SZHA10A9X7
kind: concept
name: Strong Kleene logic
aliases: [strong-kleene-connectives, k3]
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
uses: [DWYCKAKXZD, ~d80767f3, TFDYXS3K1N]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section S
    note: adopted
    mention: wikipedia://en/76765067#9VXY
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
inventory: [907BAF6V51]
---

## Summary

*Strong Kleene logic* $\mathsf{K}_3$ is the [[many-valued logic|DWYCKAKXZD]] of the matrix with values $\set{0, \tfrac12, 1}$, designated set $\set{1}$ and the operations $\neg x = 1 - x$, $x \land y = \min(x, y)$, $x \lor y = \max(x, y)$; see [[the definition|~e50e75c5]].
Implication is the abbreviation $\neg \varphi \lor \psi$.
The middle value is read as "undefined": a compound gets a classical value whenever the classical values of its parts already decide it.
$\mathsf{K}_3$ has [[no tautologies|~70290107]] but a rich consequence relation, and it is the logic of truth-value gaps, used in Kripke's theory of truth.

## Motivation

Kleene studied predicates defined by partial recursive functions, which may fail to give an answer.
Consider an algorithm that evaluates "$P$ or $Q$" by running the computations of $P$ and $Q$ in parallel.
It can answer "true" as soon as one of them answers "true", even if the other never stops.
The strong Kleene tables record exactly what such parallel evaluation can decide; the value $\tfrac12$ means "no answer".

## Notation

The values are often written $\mathbf{t}$, $\mathbf{f}$, $\mathbf{u}$, as in Kleene's 1952 book, or $1$, $0$, $\tfrac12$.
The algebra $\langle \set{0, \tfrac12, 1}, \neg, \land, \lor \rangle$ is the three-element Kleene algebra; see also [[Kleene connectives|B7KATP4SEA]].
With the designated set $\set{\tfrac12, 1}$ instead, the same tables give Priest's logic of paradox $\mathsf{LP}$.

## Remarks

### Examples

1. [[A classical tautology that is not a K3 tautology|~d5612762]]: $p \to p$ has the value $\tfrac12$ at $p = \tfrac12$.
2. [[Partial recursive predicates|~fffdddf4]] obey the strong Kleene tables under parallel evaluation.
3. [[One formula in Ł3, K3 and weak Kleene logic|~71d1e02f]] compares the tables.
4. Explosion $p \land \neg p \models q$ is valid, since $\min(x, 1 - x) \le \tfrac12$ is never designated; see [[the comparison with LP|~89c152fd]].

### Non-examples

1. [[Łukasiewicz's three-valued logic is not K3|~404c4155]]: they differ only at $\tfrac12 \to \tfrac12$, and $p \to p$ separates them.
2. [[Weak Kleene logic|BCK5QXQXA6]] is not $\mathsf{K}_3$: it gives $1 \lor \tfrac12 = \tfrac12$.

### Basic properties

1. [[K3 has no tautologies|~70290107]], because the valuation with every variable $\tfrac12$ gives every formula the value $\tfrac12$.
2. Every valid inference of $\mathsf{K}_3$ is classically valid, by restricting to valuations into $\set{0, 1}$.
3. Valid inferences include $p \land q \models p$, $p \models p \lor q$, modus ponens $p, \neg p \lor q \models q$ and De Morgan's laws in both directions.
4. Every formula is monotone in the order of information, in which $\tfrac12$ lies below $0$ and $1$; see [[the proof|~b88595da]], steps 6 to 10.
5. The consequence relation of $\mathsf{K}_3$ extends that of [[first-degree entailment|KXTP4P3GHT]] by explosion.

### History

Kleene introduced the strong tables in 1938, to reason about partial recursive functions.
His 1952 book wrote the values as $\mathbf{t}$, $\mathbf{f}$ and $\mathbf{u}$.
Kripke used the strong Kleene tables in his 1975 theory of truth, with the middle value as a truth-value gap.

### Common errors

1. Concluding from "no tautologies" that $\mathsf{K}_3$ is empty. Its consequence relation is rich, as property 3 shows.
2. Using Łukasiewicz implication in $\mathsf{K}_3$. The strong Kleene implication is $\neg x \lor y$, with $\tfrac12 \to \tfrac12 = \tfrac12$.
3. Reading $\tfrac12$ as "both true and false". That is the reading of $\mathsf{LP}$, which designates $\tfrac12$.

## Explanations

### L1 human

Strong Kleene logic has three values: true, false and undefined.
"True or undefined" is true, because one true part is enough for "or".
"False and undefined" is false, because one false part is enough for "and".
But "undefined or not undefined" stays undefined, so even "$p$ or not $p$" is not a law.

### L2 human

We check that $\neg(p \land q) \models \neg p \lor \neg q$ in $\mathsf{K}_3$.

1. $\neg(x \land y) = 1 - \min(x, y)$.
2. $\neg x \lor \neg y = \max(1 - x, 1 - y) = 1 - \min(x, y)$.
3. The two values are equal for all $x, y$, so the premise is designated iff the conclusion is.

The typical use is to reason with partial information, where some atomic sentences have no value yet.
A trap: the law $\neg(p \land q) \to (\neg p \lor \neg q)$ is not a tautology, since every formula has value $\tfrac12$ when all variables do.

### L3 human

Strong Kleene logic is the logic of the three-element Kleene algebra with top designated.
Its monotonicity for the information order is the key to Kripke's construction of a fixed point for the truth predicate, which belongs to the topic of truth and the semantic paradoxes.
In [[first-degree entailment|KXTP4P3GHT]], $\mathsf{K}_3$ and $\mathsf{LP}$ are the two three-valued extensions: one drops the value "both", the other drops "neither".
