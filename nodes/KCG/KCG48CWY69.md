---
tag: KCG48CWY69
kind: concept
name: Residuated Boolean algebra
aliases: [residuated-boolean-algebra]
msc: ["03G15", "06E25", "06F05"]
topics: [QYA4H5Y7VR]
audience: research
specializes: [E337A6WVH3, 0XADJKM699]
uses: [~fbfe9e5e, E337A6WVH3, 0XADJKM699, 0N6R902FG1, GQK4DSA11K]
sources:
  - wikipedia: en:12435391@r1352956591
    locator: Residuated Boolean algebra
    note: adopted
    mention: wikipedia://en/12435391
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Residuated_Boolean_algebra
    locator: Definition; Examples; Conjugation
  - book: isbn:9780444521415
same_as:
  wikidata: Q7315522
  wikipedia: Residuated Boolean algebra
inventory: [W4FV457732]
---

## Summary

A residuated Boolean algebra is a [[residuated lattice|E337A6WVH3]] whose lattice is a [[Boolean algebra|0XADJKM699]]; see [[the definition|~fbfe9e5e]].
So it is a Boolean algebra with a [[monoid|0N6R902FG1]] multiplication $x \cdot y$ and two residuals $x \backslash z$ and $z / y$.
The Boolean algebras with $\cdot = \land$, the formal languages over an alphabet with concatenation, and the binary relations on a set with composition are examples.
[[Relation algebras|GQK4DSA11K]] are the residuated Boolean algebras with one more operation, the converse.

## Motivation

The binary relations on a set form a Boolean algebra, and composition is a monoid multiplication on it.
Composition has residuals: the largest $Y$ with $R ; Y \subseteq Z$ exists for all $R$ and $Z$.
The concatenation of languages has the same structure, but languages have no good converse.
Residuated Boolean algebras isolate the part of relation algebra that both examples share.

## Notation

We write $(A, \land, \lor, \neg, 0, 1, \cdot, e, \backslash, /)$, or $A$ for short.
The *conjugates* of the multiplication are $x \rhd z := \neg(x \backslash \neg z)$ and $z \lhd y := \neg(\neg z / y)$.
For relations, $R \rhd T = R^{\smile} ; T$ and $T \lhd R = T ; R^{\smile}$, where $R^{\smile}$ is the converse.
Many texts write RBA for a residuated Boolean algebra.

## Remarks

### Examples

1. [[A Boolean algebra with multiplication $\land$|~0eedd6e6]]: the unit is $1$, and both residuals are $x \to z = \neg x \lor z$.
2. [[The formal languages over an alphabet|~92bb6b9d]]: the multiplication is concatenation, and the unit is $\set{\varepsilon}$.
3. [[The full relation algebra on a set|~1daf4bfe]]: the multiplication is composition, and the unit is the identity relation.
4. The power set of a monoid $M$, with $X Y = \set{x y : x \in X, y \in Y}$ and unit $\set{1}$. Languages are the case of a [[free monoid|CV013KHVJG]].
5. Every relation algebra, with $x \backslash z = \neg(x^{\smile} ; \neg z)$ and $z / y = \neg(\neg z ; y^{\smile})$.

### Non-examples

1. [[A Boolean algebra with multiplication $\lor$|~9f52e2ba]]: the unit is $0$, and $1 \backslash 0$ does not exist.
2. A Heyting algebra that is not Boolean, such as the three-element chain, is a residuated lattice, but its lattice has no complements.
3. [[The ideals of the integers|~7fd8cf5a]] form a residuated lattice, but the ideals $2\mathbb{Z}$ and $3\mathbb{Z}$ have no complements.

### Basic properties

1. The multiplication preserves all existing joins in each argument, so $x \cdot 0 = 0 = 0 \cdot x$.
2. Conjugation: $(x \cdot y) \land z = 0$ iff $y \land (x \rhd z) = 0$ iff $x \land (z \lhd y) = 0$.
3. By property 2, a residuated Boolean algebra is a Boolean algebra with operators in the sense of Jónsson and Tarski. The residuals are definable from the conjugates.
4. Jónsson and Tsinakis showed that a residuated Boolean algebra is a relation algebra when it has an operation $x^{\smile}$ with $x^{\smile} \rhd e = x = e \lhd x^{\smile}$.
5. On a complete Boolean algebra, a monoid multiplication is residuated iff it preserves all joins in each argument.

### History

Jónsson and Tsinakis introduced the name in their paper "Relation algebras as residuated Boolean algebras" (Algebra Universalis, 1993).
Their aim was to see relation algebras as a special class of residuated structures.
The examples of languages and of power sets of monoids were known earlier from the study of formal languages and of Boolean algebras with operators.

### Common errors

1. Expecting every residuated Boolean algebra to be a relation algebra. The algebra of languages has no converse with the required laws; see [[this example|~36c0fb5a]].
2. Assuming that the multiplication is commutative. Concatenation and composition are not commutative.
3. Confusing the conjugates with the residuals. The residuals are monotone in $z$; the conjugates are their Boolean duals.

## Explanations

### L1 human

A residuated Boolean algebra has the usual "and", "or" and "not" of sets.
It also has a way to combine two elements in sequence, like "first do $R$, then do $S$" for relations.
For each such combination, there is a best way to "undo" it on each side.
These undo operations are the residuals.

### L2 human

1. Take the relations on $\set{1, 2}$, and $R = \set{(1, 2)}$, $Z = \set{(1, 1)}$.
2. The residual $R \backslash Z$ is the largest $Y$ with $R ; Y \subseteq Z$.
3. $R ; Y$ contains $(1, b)$ iff $(2, b) \in Y$. So $Y$ may contain $(2, 1)$ but not $(2, 2)$.
4. The pairs $(1, 1)$ and $(1, 2)$ never contribute. So $R \backslash Z = \set{(1, 1), (1, 2), (2, 1)}$.
5. The formula $\neg(R^{\smile} ; \neg Z)$ gives the same: $R^{\smile} ; \neg Z = \set{(2, 2)}$.

The typical use: one proves facts about relation algebras that do not need the converse in the larger class, so they hold for languages too.
The trap: the residuals are not complements; $x \backslash z$ grows with $z$ and shrinks with $x$.

### L3 human

A residuated Boolean algebra is a Boolean algebra with a binary operator whose conjugates exist, so the duality theory of Boolean algebras with operators applies.
Its dual is a Stone space with a ternary relation, and the complex algebras of ternary frames are complete examples.
In relevance logic, the same ternary frames give the Routley-Meyer semantics, and the residuals are the implications.
The [[Jónsson-Tsinakis characterization|~fbfe9e5e]] makes relation algebras a subvariety of an expansion of this class.
