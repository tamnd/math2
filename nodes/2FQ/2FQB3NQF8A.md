---
tag: 2FQB3NQF8A
kind: statement
role: theorem
name: Suszko's reduction
aliases: [suszko-thesis, suszkos-thesis]
msc: ["03B50", "03B22"]
topics: [WZP584JQ06, QYA4H5Y7VR]
audience: grad
about: [DWYCKAKXZD, FCXHSC6Z4R]
uses: [J78Y1M4GND, DWYCKAKXZD]
proofs: [PJ478J8BR4]
history:
  first_stated: "Suszko, 1977"
  notes: "The reduction and its meaning were later studied by Malinowski and by da Costa, Béziau and Bueno."
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 4.3 Are many-valued logics actually bivalent?
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
---

## Statement

Every consequence relation, however many truth values its usual semantics has, is fixed by a class of valuations with only the two values $0$ and $1$.

Let $L$ be a set of formulas and let $\vdash$ be a [[consequence relation|J78Y1M4GND]] on $L$.
So $\vdash$ satisfies reflexivity (R), monotonicity (M) and cut (C).
Call $T \subseteq L$ *closed* when $T \vdash \varphi$ implies $\varphi \in T$.
For a closed set $T$, let $b_T \colon L \to \{0, 1\}$ be its characteristic function, so that $b_T(\varphi) = 1$ iff $\varphi \in T$.
Let $B = \{b_T : T \text{ closed}\}$.

**Theorem.** For every $\Gamma \subseteq L$ and every $\varphi \in L$, we have $\Gamma \vdash \varphi$ iff every $b \in B$ with $b(\gamma) = 1$ for all $\gamma \in \Gamma$ has $b(\varphi) = 1$.

In particular every [[many-valued logic|DWYCKAKXZD]] is determined by a class of two-valued valuations.
The proof is in [[the proof by closed theories|PJ478J8BR4]].

## Remarks

### Why each hypothesis is needed

Each of the three conditions is used once, and each can fail on a three-letter language $L = \{p, q, r\}$.

Drop monotonicity.
Let $\Gamma \vdash \varphi$ hold iff $\varphi \in \Gamma$, or $\Gamma = \{p\}$ and $\varphi = q$.
The set $\{p, r\}$ is closed, and its valuation makes $p$ true and $q$ false, so the semantic side of $\{p\} \vdash q$ fails.

Drop reflexivity.
If $\vdash$ is empty, then every subset of $L$ is closed.
The semantic side of $\{p\} \vdash p$ holds, since every $b_T$ with $b_T(p) = 1$ has $b_T(p) = 1$, but $\{p\} \nvdash p$.

Drop cut.
Let $\Gamma \vdash \varphi$ hold iff $\varphi \in \Gamma$, or $p \in \Gamma$ and $\varphi = q$, or $q \in \Gamma$ and $\varphi = r$.
This relation is reflexive and monotone, and $\{p\} \nvdash r$.
Every closed set that contains $p$ contains $q$, and then $r$, so the semantic side of $\{p\} \vdash r$ holds.

### What it gives you

Every logic of a matrix is "two-valued" in this sense, with the values "designated" and "not designated".
The new valuations are in general not truth-functional, as [[the example for Ł3|MAYHP6P8NC]] shows: two formulas with the same value can have negations with different values.
So the number of truth values is a property of a truth-functional semantics, not of the consequence relation.

### The converse

The converse also holds.
For any class $B$ of maps $L \to \{0, 1\}$, define $\Gamma \vdash_B \varphi$ by the right-hand side of the theorem.
Then $\vdash_B$ is reflexive and monotone at once.
For cut, suppose $\Gamma \vdash_B \psi$ for each $\psi \in \Delta$ and $\Gamma \cup \Delta \vdash_B \varphi$.
A map $b$ that is $1$ on $\Gamma$ is then $1$ on each $\psi \in \Delta$, so on $\Gamma \cup \Delta$, and so on $\varphi$.

### Generalizations

For a logic of one matrix with designated set $D$, a smaller class works: $b_v(\varphi) = 1$ iff $v(\varphi) \in D$, one map for each matrix valuation $v$.
For logics with several designated sets, such as Malinowski's logics of "q-consequence", an analogous argument gives three logical values instead of two.

## History

Suszko presented the reduction in a paper of 1977.
He separated the algebraic values of a matrix from the two logical values "designated" and "not designated", and argued that only the logical values matter for consequence.
The claim that every logic is two-valued in this sense became known as Suszko's thesis, and it started a debate on what makes a logic many-valued.
Malinowski, and later da Costa, Béziau and Bueno, studied the reduction and its limits.

## Explanations

### L1 human

A many-valued logic seems to have more than two truth values.
Suszko observed that a valid argument only cares whether a value is designated or not.
So we can replace each value by "good" or "bad" and keep the same valid arguments.
The price is that "good" or "bad" for a compound sentence no longer follows from "good" or "bad" for its parts.

### L2 human

Take the consequence relation of $\mathrm{Ł}_3$ and ask why $p \nvdash p \land q$ holds.
The set $T$ of all formulas that follow from $p$ is closed, it contains $p$, and it does not contain $p \land q$.
So $b_T(p) = 1$ and $b_T(p \land q) = 0$, and this single two-valued map refutes the inference.
The typical use of the theorem is in debates about what "many-valued" means.
Watch out: the theorem gives two values, not two-valued truth tables, because the maps $b_T$ do not respect the connectives.

### L3 human

The construction is the Lindenbaum method in its most general form, and [[Wójcicki's theorem|VWJVAS3VE3]] refines it to truth-functional matrices for structural logics.
In abstract algebraic logic the closed sets of a logic form a closure system, and the maps $b_T$ are the characteristic functions of its members.
The gap between consequence and truth-functionality returns in the study of non-deterministic matrices and of logics with more than one designated set, where Suszko's argument shows what any semantics must preserve.
