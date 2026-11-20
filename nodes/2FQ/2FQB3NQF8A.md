---
tag: 2FQB3NQF8A
kind: statement
role: theorem
name: Suszko's reduction
aliases: [suszko-thesis, suszkos-thesis]
msc: ["03B50", "03B22"]
topics: [WZP584JQ06]
audience: grad
about: [DWYCKAKXZD, FCXHSC6Z4R]
uses: [J78Y1M4GND, DWYCKAKXZD]
proofs: [PJ478J8BR4]
history:
  first_stated: "Suszko, 1970s (one paper of 1977)"
  notes: "SEP dates Suszko's papers on the thesis to the 1970s, and gives Malinowski (1993) and da Costa, Béziau and Bueno (1996) for the general bivalent semantics."
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 4.3 Are many-valued logics actually bivalent?
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
---

## Statement

Let $L$ be a set of formulas and let $\vdash$ be a [[consequence relation|J78Y1M4GND]] on $L$.
So $\vdash$ satisfies reflexivity (R), monotonicity (M) and cut (C).
Call $T \subseteq L$ *closed* when $T \vdash \varphi$ implies $\varphi \in T$.
For a closed set $T$, let $b_T \colon L \to \set{0, 1}$ be its characteristic function: $b_T(\varphi) = 1$ iff $\varphi \in T$.
Let $B = \set{b_T : T \text{ closed}}$.

**Theorem.** For every $\Gamma \subseteq L$ and every $\varphi \in L$,
$$\Gamma \vdash \varphi \iff \text{every } b \in B \text{ with } b(\gamma) = 1 \text{ for all } \gamma \in \Gamma \text{ has } b(\varphi) = 1.$$

So every such logic, in particular every [[many-valued logic|DWYCKAKXZD]], is determined by a class of two-valued valuations.
The proof is in [[the proof by closed theories|PJ478J8BR4]].

## Remarks

### Why each hypothesis is needed

1. Monotonicity (M). Without it, let $L = \set{p, q, r}$ and let $\vdash$ be the relation with $\Gamma \vdash \varphi$ iff $\varphi \in \Gamma$, or $\Gamma = \set{p}$ and $\varphi = q$. Then $\set{p, r}$ is closed, its valuation makes $p$ true and $q$ false, and the semantic side of $\set{p} \vdash q$ fails.
2. Reflexivity (R). If $\vdash$ is empty, then $L$ is the only closed set, and $b_L$ makes every formula true. The semantic side then holds for $\set{p} \vdash p$, but $\set{p} \nvdash p$.
3. Cut (C). The proof needs that $\set{\psi : \Gamma \vdash \psi}$ is closed, and this is an instance of cut.

### Consequences

1. Every many-valued logic of a matrix is also a "two-valued" logic, with values "designated" and "not designated".
2. The two-valued valuations are in general not truth-functional: see [[the example for Ł3|MAYHP6P8NC]].
3. So the number of truth values of a logic is a property of its truth-functional semantics, not of the consequence relation.

### Converse

The converse holds.
For any class $B$ of maps $L \to \set{0, 1}$, the relation defined by the right-hand side satisfies (R), (M) and (C).
For (C): if $b$ makes $\Gamma$ true, it makes each $\psi \in \Delta$ true, hence it makes $\Gamma \cup \Delta$ and then $\varphi$ true.

### Generalizations

For a logic given by one matrix $(V, D)$, a simpler class of valuations works: $b_v(\varphi) = 1$ iff $v(\varphi) \in D$, for each matrix valuation $v$.
SEP describes the general construction of such bivalent semantics in the work of Malinowski and of da Costa, Béziau and Bueno.

## History

Suszko presented the reduction in papers of the 1970s, including one of 1977.
In them he called Łukasiewicz "the chief perpetrator of a magnificent conceptual deceit", as SEP reports.
SEP discusses the thesis in its section on whether many-valued logics are bivalent.

## Explanations

### L1 human

A many-valued logic seems to have more than two truth values.
Suszko observed that a valid argument only cares whether a value is designated or not.
So we can replace each value by "good" or "bad" and get the same valid arguments.
The price is that "good" or "bad" for a compound sentence no longer follows from "good" or "bad" for its parts.

### L2 human

1. Take a consequence relation, for example that of $\mathrm{Ł}_3$.
2. For each closed set $T$ of formulas, mark the formulas in $T$ with $1$ and the others with $0$.
3. The theorem says: $\Gamma \vdash \varphi$ iff every such marking that makes all of $\Gamma$ equal to $1$ makes $\varphi$ equal to $1$.

The typical use is in debates about what "many-valued" means.
A trap: the theorem gives two values, but not two-valued truth tables; the new valuations do not respect the connectives.

### L3 human

The construction is the Lindenbaum method in its most general form, and [[Wójcicki's theorem|VWJVAS3VE3]] refines it to truth-functional matrices for structural logics.
In abstract algebraic logic the closed sets of a logic form a closure system, and the valuations $b_T$ are its characteristic functions.
The gap between consequence and truth-functionality reappears in the study of non-deterministic matrices and of logics with more than one designated set, where Suszko's argument shows what any semantics must preserve.
