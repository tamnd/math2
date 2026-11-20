---
tag: DWYCKAKXZD
kind: concept
name: Many-valued logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
uses: [09K9MWD2QQ, 5DYNDW9526, 05006AJ7DZ, FCXHSC6Z4R]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 1 Bivalence in question; 2 Beyond two truth values; 4.3 Are many-valued logics actually bivalent?
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
same_as:
  wikidata: Q185502
  wikipedia: Many-valued logic
---

## Summary

A *many-valued logic* is a propositional logic whose semantics uses a set $V$ of truth values with more than two elements; see [[the definition|66NMTCQNQV]].
Each connective is interpreted by a function on $V$, and a nonempty proper subset $D \subseteq V$ of *designated values* plays the role of "true".
A formula $\varphi$ follows from a set $\Gamma$ when every valuation that gives designated values to all members of $\Gamma$ also gives a designated value to $\varphi$.
The structure $(V, \text{operations}, D)$ is a [[logical matrix|~d80767f3]].
The logic is *finitely valued* when $V$ is finite, as in [[Łukasiewicz's three-valued logic|~d7a9d81e]], and *infinite-valued* when $V$ is infinite, as in [[Łukasiewicz logic on the unit interval|~ca73eab3]].
Many-valued logics test which classical laws depend on [[bivalence|5DYNDW9526]], and they model future contingents, vague predicates and partial information.

## Motivation

Classical [[propositional calculus|09K9MWD2QQ]] assumes that every sentence is either true or false.
Three kinds of sentences put this assumption in doubt.

1. Future contingents. Łukasiewicz asked whether "there will be a sea battle tomorrow" is already true or false today, and gave it a third value.
2. Partial information. A partial recursive predicate can be undefined at an argument, so Kleene gave such atomic sentences the value "undefined".
3. Vagueness. A predicate such as "tall" seems to hold of a person to a degree, so the truth values form a scale such as $[0, 1]$.

Each answer keeps the idea that the value of a compound sentence is a function of the values of its parts.
It drops only the restriction to two values.

## Notation

We write $V$ for the set of truth values, $D$ for the designated values and $\models_M$ for the consequence relation of a matrix $M$.
The values are often numbers: $\set{0, \tfrac12, 1}$ for the three-valued logics and $[0, 1]$ for the infinite-valued ones, with $1$ as "fully true".
In this topic we write $\odot$ for strong conjunction and $\oplus$ for strong disjunction; other texts write $\otimes$ or $\&$ for $\odot$.

## Remarks

### Examples

1. [[Łukasiewicz's three-valued logic|~d7a9d81e]] $\mathrm{Ł}_3$: $V = \set{0, \tfrac12, 1}$, $D = \set{1}$. The [[evaluation of $p \lor \neg p$|6S872VHF67]] gives $\tfrac12$, so excluded middle fails.
2. [[Strong Kleene logic|SZHA10A9X7]] $\mathsf{K}_3$: the same values with Kleene's tables and $D = \set{1}$. It has no tautologies.
3. [[First-degree entailment|KXTP4P3GHT]]: four values "true", "false", "both" and "neither", with two designated values.
4. [[Post's many-valued logics|~e204f5cc]]: $V = \set{0, 1, \dots, m - 1}$ with a cyclic negation.
5. [[Fuzzy logics|~b4bfdbf0]] such as [[Łukasiewicz logic|~ca73eab3]] and [[Gödel-Dummett logic|474SGS2N0X]], with $V = [0, 1]$.
6. [[Suszko's two-valued reduction of Ł3|~37339d27]] shows the same logic with a different, non-truth-functional semantics.

### Non-examples

1. [[Classical logic has a two-element characteristic matrix|~b17fba19]], so it is not many-valued, even though it also has a four-element matrix.
2. Intuitionistic logic is not the logic of any finite matrix; Gödel proved this in 1932. It is many-valued only in the broad sense of an infinite matrix, a [[Heyting algebra|NG943XNQWH]].
3. A probability assignment is not a valuation of a matrix: [[probability is not truth-functional|~a4e05182]].

### Basic properties

1. For a finite matrix with $n$ values, a formula with $k$ variables has $n^k$ valuations, so its tautologies are decidable by a finite table.
2. [[Suszko's reduction|~0bb543fb]]: every consequence relation that satisfies reflexivity, monotonicity and cut is determined by a class of two-valued valuations.
3. [[Wójcicki's theorem|~9995d199]]: every structural consequence relation is the consequence relation of a class of logical matrices.
4. A many-valued logic can be weaker than classical logic, as $\mathrm{Ł}_3$ is, or have no tautologies at all, as [[Strong Kleene logic|SZHA10A9X7]] has none.
5. Restricted to the values $0$ and $1$, the tables of Łukasiewicz and Kleene are the classical tables, so each of their tautologies is a classical [[tautology|05006AJ7DZ]].

### History

Łukasiewicz introduced his three-valued logic in 1920.
Post introduced the $m$-valued systems with a cyclic negation in 1921 and proved their functional completeness.
Kleene introduced his three-valued tables in 1938 for partial recursive predicates, and Bochvar published his three-valued logic in the same year.
Suszko argued in the 1970s that every such logic is two-valued in a deeper sense, the thesis now called Suszko's reduction.

### Common errors

1. Reading the value $\tfrac12$ as a probability. Probabilities are not truth-functional; see [[the example|~a4e05182]].
2. Saying that a logic "has $n$ values". The number of values belongs to a matrix, and one logic has matrices of different sizes.
3. Forgetting the designated set. The same tables with $D = \set{1}$ and with $D = \set{\tfrac12, 1}$ give different logics, such as $\mathsf{K}_3$ and the logic of paradox.

## Explanations

### L1 human

Classical logic has two truth values, true and false.
A many-valued logic allows more, for example "undecided" or a degree of truth between $0$ and $1$.
In Łukasiewicz's three-valued logic, the values are $0$, $\tfrac12$ and $1$, and "not $x$" has the value $1 - x$.
If "it will rain tomorrow" has value $\tfrac12$, then its negation also has value $\tfrac12$.
So "it will rain or it will not rain", with "or" as the larger value, gets only $\tfrac12$, and it is not a law of this logic.

### L2 human

We test the law $\neg\neg p \to p$ in $\mathrm{Ł}_3$, with $x \to y = \min(1, 1 - x + y)$.

1. For $p = 0$: $\neg\neg p = 0$, and $0 \to 0 = 1$.
2. For $p = \tfrac12$: $\neg\neg p = \tfrac12$, and $\tfrac12 \to \tfrac12 = 1$.
3. For $p = 1$: $\neg\neg p = 1$, and $1 \to 1 = 1$.
4. Every valuation gives $1$, which is designated, so $\neg\neg p \to p$ is a tautology of $\mathrm{Ł}_3$.

The typical use of such a table is to decide which classical laws survive in a given logic.
A trap: a classical law can fail in one many-valued logic and hold in another with the same values, because the tables or the designated set differ.

### L3 human

Abstractly, a many-valued logic is a structural consequence relation presented by a matrix, and [[Wójcicki's theorem|~9995d199]] says that every structural logic has such a presentation.
So "many-valued" is a property of a semantics, not of a logic; [[Suszko's reduction|~0bb543fb]] makes the same point from the two-valued side.
The algebras of the matrices are studied in [[algebraic logic|QYA4H5Y7VR]]: [[MV-algebras|8T4M7RN9AC]] for Łukasiewicz logic, [[Post algebras|RD2A5Z7E2B]] for Post's logics and [[residuated lattices|E337A6WVH3]] for the fuzzy logics.
Related non-classical logics are the [[substructural logics|98QF5J4W16]] and the [[paraconsistent logics|NJB94B39QK]], whose semantics also often use more than two values.
