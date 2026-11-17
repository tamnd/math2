---
tag: MCZRXR3SVB
kind: concept
name: Atomic formula
aliases: [atom, atomic-formula]
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
uses: [WDVVEYD6AT, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
---

## Summary

An atomic formula is a formula with no connectives and no quantifiers.
In first-order logic it is an equation $t_1 = t_2$ between [[terms|6D3WA7N2W4]], or a relation symbol applied to terms, $R(t_1, \dots, t_n)$.
All other [[formulas|HYJ10AF6RT]] are built from atomic formulas by connectives and quantifiers.
Atomic formulas are the simplest statements of a language, and their truth in a structure comes straight from the interpretation of the symbols.

## Motivation

A first-order language has two kinds of expressions: terms name objects, and formulas make claims.
The atomic formulas are the bridge between them: they turn terms into claims, by an equation or by a relation symbol of the [[signature|WDVVEYD6AT]].
Every proof by induction on formulas starts with the atomic case.
In the semantics, the truth of an atomic formula is the base case of the definition of satisfaction.

## Notation

1. Binary relation symbols are usually written infix, as $t_1 < t_2$ for $<(t_1, t_2)$.
2. Some books add the constants $\top$ (true) and $\bot$ (false) as atomic formulas, and Mathlib has $\bot$ as `falsum`.
3. A relation symbol of arity $0$ is a propositional letter, and it is an atomic formula by itself.
4. In logic without equality, the equations $t_1 = t_2$ are not formulas, and only $R(t_1, \dots, t_n)$ is atomic.
5. An atomic formula or its negation is a *literal*.

## Remarks

### Examples

1. [[Equations between ring terms|XCEH9VZCYQ]] such as $x \cdot (y + 1) = x \cdot y + x$ are atomic formulas.
2. [[Atomic sentences of arithmetic|KGN4PW4YEF]] such as $S(0) + S(0) = S(S(0))$ have no variables, so their truth in $\N$ is a matter of computation.
3. In the signature $\set{\in}$ of set theory, the atomic formulas are $x \in y$ and $x = y$ for variables $x, y$, since the signature has no function or constant symbols.
4. In the signature of graphs, $E(x, y)$ is atomic and says that $x$ and $y$ are adjacent.

### Non-examples

1. [[The formulas $x \le y$ and $\neg (x = y)$|DXS1P3VAY7]] are not atomic in the signature $\set{<}$. The first abbreviates a disjunction, and the second is a literal with a negation.
2. The formula $\exists y \, (x = y + y)$ is not atomic, because it has a quantifier.
3. The term $x + 1$ is not an atomic formula. It is not a formula at all.

### Basic properties

1. Every variable occurrence in an atomic formula is free, so $\operatorname{FV}(\varphi)$ is the set of variables that occur in $\varphi$. See [[the proposition on atomic formulas|D039R5C8TC]].
2. An atomic formula is a [[sentence|DKFGQTRYZE]] exactly when all its terms are closed.
3. By [[unique readability|3QPV4XW8MC]], an atomic formula has exactly one relation symbol or one equality sign, and its terms are unique.
4. The quantifier-free formulas are exactly the Boolean combinations of atomic formulas.
5. The truth of an atomic formula in a structure depends only on the values of its terms and on the interpretation of $R$, by the base clause of [[satisfaction|2RBQPV02AS]].

### History

Russell's lectures of 1918 on logical atomism called the simplest propositions "atomic propositions".
Wittgenstein's Tractatus of 1921 used the related notion of elementary propositions.
Logic textbooks then took over the word "atomic" for the formulas that are not built from smaller formulas.

### Common errors

1. A student counts $x \neq y$ as atomic. It is the negation $\neg (x = y)$ of an atomic formula.
2. A student counts a defined symbol as primitive. In the signature $\set{<}$, the formula $x \le y$ abbreviates $(x < y \lor x = y)$ and is not atomic.
3. A student thinks atomic formulas are short. The equation $t_1 = t_2$ is atomic however long the terms are.

## Explanations

### L1 human

An atomic formula is a basic statement about objects.
In arithmetic, "$x + 1 = y$" and "$x < 3$" are atomic.
They have no "and", no "not", and no "for all" in them.
Longer statements, such as "$x < 3$ and $x + 1 = y$", are built from atomic ones.

### L2 human

We list the atomic formulas of the signature $\set{c, f, P}$, with a constant $c$, a unary function symbol $f$ and a binary relation symbol $P$, that use only the variable $x$.

1. The terms are $c, f(c), f(f(c)), \dots$ and $x, f(x), f(f(x)), \dots$.
2. The atomic formulas are $t_1 = t_2$ and $P(t_1, t_2)$ for any two of these terms.
3. For example, $P(x, f(c))$ and $f(x) = c$ are atomic, and both have the free variable $x$.
4. The formula $P(c, f(c))$ is atomic and closed, so it is a sentence.

The typical use of atomic formulas is the base case of an induction on formulas.
A trap: a symbol defined by a formula, such as $\le$ from $<$ and $=$, does not create new atomic formulas.

### L3 human

In model theory, the atomic diagram of a structure is the set of atomic sentences and negated atomic sentences, with constants for the elements, that are true in it.
A structure embeds in another exactly when the second one, with suitable constants, satisfies the atomic diagram of the first.
Quantifier elimination reduces every formula of a theory to a Boolean combination of atomic formulas.
In resolution and logic programming, atomic formulas are the atoms of clauses, and Herbrand structures are fixed by the set of true ground atoms.
In Mathlib the predicate `FirstOrder.Language.BoundedFormula.IsAtomic` marks the formulas built by `equal` and `rel`.
