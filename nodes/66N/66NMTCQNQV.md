---
tag: 66NMTCQNQV
kind: definition
name: Many-valued logic
msc: [03B50]
defines: DWYCKAKXZD
uses: [09K9MWD2QQ, 05006AJ7DZ, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
---

## Definition

Fix a finite set $C$ of connectives, each with an arity.
A logical matrix for $C$ is a triple $(V, D, \set{f_c}_{c \in C})$ with these parts.

1. A set $V$ of truth values with at least three elements.
2. A nonempty proper subset $D \subseteq V$ of designated values.
3. For each $n$-ary connective $c$, a [[function|0EPAT51DXQ]] $f_c \colon V^n \to V$, its truth table.

A valuation assigns a value in $V$ to each propositional variable and extends to all formulas through the functions $f_c$.
A formula is a tautology of the matrix when it takes a value in $D$ under every valuation.
The many-valued logic of the matrix is the set of its tautologies.

## Remarks

With $V = \set{0, 1}$, $D = \set{1}$ and the usual tables, the tautologies are those of classical [[propositional logic|09K9MWD2QQ]]; clause 1 excludes this two-valued case.

Example: Łukasiewicz's three-valued logic $\mathrm{L}_3$ has $V = \set{0, \tfrac12, 1}$ and $D = \set{1}$.
Its tables are $\neg x = 1 - x$, $x \to y = \min(1, 1 - x + y)$, $x \lor y = \max(x, y)$ and $x \land y = \min(x, y)$.
The formula $p \to p$ is a tautology, since $\min(1, 1 - x + x) = 1$ for every $x$.

Non-example: $p \lor \neg p$ is a classical [[tautology|05006AJ7DZ]] but not a tautology of $\mathrm{L}_3$.
The valuation $p \mapsto \tfrac12$ gives $\max(\tfrac12, \tfrac12) = \tfrac12 \notin D$.

Infinite-valued logics use, for example, $V = [0, 1]$ with the same tables.

## Explanations

### L1 human

A many-valued logic replaces the two truth values by a larger set and gives a table for each connective on that set.
A formula is a law when it always lands among the designated values.
Some classical laws survive, and others, such as excluded middle in Łukasiewicz logic, do not.
