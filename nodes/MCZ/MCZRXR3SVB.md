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

An atomic formula is the simplest kind of statement: it says that two terms are equal, or that a relation holds between some terms, and it has no connectives and no quantifiers.
In the signature $\{ < \}$ with only the variables $x$ and $y$, there are exactly eight atomic formulas:
$$x < x, \quad x < y, \quad y < x, \quad y < y, \quad x = x, \quad x = y, \quad y = x, \quad y = y.$$
Every other formula over these variables, such as $\forall x \, \exists y \, (x < y)$, is built from these eight by connectives and quantifiers.

Exactly, an [[atomic formula|BP6WW7H5CC]] over a [[signature|WDVVEYD6AT]] $\sigma$ is either an equation $t_1 = t_2$ between [[terms|6D3WA7N2W4]], or $R(t_1, \dots, t_n)$ for a relation symbol $R$ of arity $n$ and terms $t_1, \dots, t_n$.
An atomic formula or the negation of one is a literal.
In a structure, the truth of an atomic formula comes straight from the values of its terms and the meaning of $R$ or $=$.

## Motivation

A first-order language has two kinds of expressions: terms name elements, and [[formulas|HYJ10AF6RT]] make claims.
Atomic formulas are the bridge between them, since they turn terms into claims by an equation or by a relation symbol.
Every definition by recursion on formulas, and every proof by induction on formulas, starts with the atomic case.
In the semantics, the truth of an atomic formula is the base clause of [[satisfaction|2RBQPV02AS]], and the rest of the definition only says how connectives and quantifiers combine truth values.

## Notation

Binary relation symbols are usually written infix, as $t_1 < t_2$ for $<(t_1, t_2)$.
Some books add $\top$ and $\bot$ as atomic formulas, and Mathlib has $\bot$ as `falsum`.
Where a book allows a relation symbol of arity $0$, it is a propositional letter and an atomic formula by itself.
In logic without equality the equations $t_1 = t_2$ are not formulas, and only $R(t_1, \dots, t_n)$ is atomic.

## Remarks

### Atomic formulas in practice

The size of the terms does not matter.
[[Equations between ring terms|XCEH9VZCYQ]], such as the distributive law $x \cdot (y + 1) = x \cdot y + x$, are atomic, because the only symbol above the two terms is $=$.
[[Atomic sentences of arithmetic|KGN4PW4YEF]], such as $S(0) + S(0) = S(S(0))$, have no variables, so their truth in $\mathbb{N}$ is a matter of computation: both sides have the value $2$.
In the signature $\{ \in \}$ of set theory there are no function or constant symbols, so the atomic formulas are just $x \in y$ and $x = y$ for variables $x$ and $y$.
In the signature of graphs, $E(x, y)$ is atomic and says that $x$ and $y$ are adjacent.

### What is not atomic

In the signature $\{ < \}$, [[the formulas $x \le y$ and $\neg (x = y)$|DXS1P3VAY7]] are not atomic.
The first abbreviates the disjunction $(x < y \lor x = y)$, and the second is a negation, so both contain a connective.
The formula $\exists y \, (x = y + y)$ is not atomic, because it has a quantifier.
The term $x + 1$ is not an atomic formula, because it is not a formula at all: it names an element and claims nothing.

### The first facts

Every variable occurrence in an atomic formula is free, because there is no quantifier to bind it; see [[the proposition on atomic formulas|D039R5C8TC]].
So the free variables of an atomic formula are all the variables in its terms, and it is a [[sentence|DKFGQTRYZE]] exactly when all its terms are closed.
By [[unique readability|3QPV4XW8MC]], an atomic formula has exactly one relation symbol or equality sign at the top, and its terms are unique.
The quantifier-free formulas are exactly the Boolean combinations of atomic formulas.

### Watch out

Writing $x \neq y$ makes it look atomic, but it is $\neg (x = y)$, a negated atomic formula.
A defined symbol does not create new atomic formulas either.
If $\le$ is not in the signature, then $x \le y$ is a short way to write $(x < y \lor x = y)$, and an induction on formulas must treat it as a disjunction.
The test is simple: an atomic formula has no $\neg$, no binary connective and no quantifier anywhere in it.

### History

Russell's lectures of 1918 on logical atomism called the simplest propositions "atomic propositions", and Wittgenstein's Tractatus of 1921 used the related notion of elementary propositions.
The word "atomic" in logic textbooks for formulas that contain no smaller formula comes from this tradition.

### Try it

List the atomic formulas of $\{ c, P \}$, with a constant $c$ and a unary relation symbol $P$, that use no variables.
The closed terms are only $c$, so the answers are $P(c)$ and $c = c$.

Is $S(x) = S(S(y))$ atomic, and what are its free variables?
It is atomic, an equation between two terms, and its free variables are $x$ and $y$.

## Explanations

### L1 human

An atomic formula is a basic statement about objects.
In arithmetic, "$x + 1 = y$" and "$x < 3$" are atomic.
They have no "and", no "not", and no "for all" in them.
Longer statements, such as "$x < 3$ and $x + 1 = y$", are built from atomic ones.

### L2 human

We find the atomic formulas of the signature $\{ c, f, P \}$, with a constant $c$, a unary function symbol $f$ and a binary relation symbol $P$, that use only the variable $x$.
The terms are $c, f(c), f(f(c)), \dots$ and $x, f(x), f(f(x)), \dots$.
So the atomic formulas are $t_1 = t_2$ and $P(t_1, t_2)$ for any two of these terms, and there are infinitely many.
For example, $P(x, f(c))$ and $f(x) = c$ are atomic, and both have the free variable $x$.
The formula $P(c, f(c))$ is atomic and has no variables, so it is a sentence.
In the structure $\mathbb{N}$ with $c = 0$, $f(n) = n + 1$ and $P$ read as $<$, it says $0 < 1$, which is true.
Watch out: $f(x) = P(x, c)$ is not a formula, since $P(x, c)$ is a formula and not a term.

### L3 human

In model theory, the atomic diagram of a structure is the set of atomic and negated atomic sentences, with constants for the elements, that are true in it.
A structure embeds in another exactly when the second, with suitable constants, satisfies the atomic diagram of the first.
Quantifier elimination reduces every formula of a theory to a Boolean combination of atomic formulas.
In resolution and logic programming, atomic formulas are the atoms of clauses, and a Herbrand structure is fixed by its set of true ground atoms.
In Mathlib the predicate `FirstOrder.Language.BoundedFormula.IsAtomic` marks the formulas built by `equal` and `rel`.
