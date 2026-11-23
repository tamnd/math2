---
tag: HYJ10AF6RT
kind: concept
name: Well-formed formula
aliases: [first-order-formula]
msc: ["03B10", "03B05"]
topics: [PSRDJXRW53]
audience: ug2
uses: [WDVVEYD6AT, 6D3WA7N2W4, MCZRXR3SVB, QS0XVAN9BG, 0GHS47PDAQ, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Formation rules
  - book: isbn:9780122384523
    locator: Section 2.1
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
same_as:
  wikidata: Q655328
  wikipedia: Well-formed formula
---

## Summary

A well-formed formula is a string of symbols that the grammar of first-order logic accepts as a statement.
In the language of orders, the string $\forall x \, \exists y \, (x < y)$ is a formula, and the string $\forall \land x <$ is not.
The grammar has a small set of rules, and every formula is built by them from the simplest statements in finitely many steps.

Let $\sigma$ be a [[signature|WDVVEYD6AT]].
The well-formed formulas over $\sigma$, or $\sigma$-formulas, form the smallest set of strings that contains every [[atomic formula|MCZRXR3SVB]] and is closed under three rules.
If $\varphi$ is a formula, then $\neg \varphi$ is a formula.
If $\varphi$ and $\psi$ are formulas, then $(\varphi \land \psi)$, $(\varphi \lor \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$ are formulas.
If $\varphi$ is a formula and $x$ is a variable, then $\forall x \, \varphi$ and $\exists x \, \varphi$ are formulas.
The [[formal definition|2CHENV4DCC]] states the rules as numbered clauses.

## Motivation

Every later notion of logic works by recursion on the shape of a statement.
Truth in a [[structure|983GZBQYT4]], [[free variables|9CNGDRAMGC]], [[substitution|NCDZ969V7X]] and formal proof are all defined one rule at a time.
So we first need an exact answer to the question "which strings are statements?", in the same way that a compiler needs a grammar before it can run a program.

The formation rules give that answer, and they give two tools at once.
Proof by induction on formulas shows that a property holds for every formula: check the atomic case, then check that each rule keeps the property.
Definition by recursion on formulas builds a function on all formulas from its values on atomic formulas.
Both tools appear on nearly every page of [[first-order logic|086QKPF0A6]] that follows.

## Notation

The definition here uses $\neg, \land, \lor, \to, \leftrightarrow$ and both [[quantifiers|0GHS47PDAQ]] as primitive symbols.
Many books take fewer primitives: Enderton takes $\neg$, $\to$ and $\forall$, and then $\exists x \, \varphi$ abbreviates $\neg \forall x \, \neg \varphi$ and $(\varphi \lor \psi)$ abbreviates $(\neg \varphi \to \psi)$.
In text we drop the outer brackets and use a binding order: $\neg$ and the quantifiers bind most strongly, then $\land$ and $\lor$, then $\to$ and $\leftrightarrow$.
So $\forall x \, P(x) \land Q(x)$ means $(\forall x \, P(x) \land Q(x))$, and the scope of $\forall x$ is only $P(x)$.
Some books write $(\forall x) \varphi$ or $\forall x . \varphi$, and Polish notation puts each connective in front of its arguments and needs no brackets.
In Mathlib a formula is a term of `FirstOrder.Language.BoundedFormula`, where bound variables are numbers in the de Bruijn style; the [[definition|2CHENV4DCC]] explains the encoding.

## Remarks

### Building a formula step by step

Take the signature of orders $\{ < \}$ and the string $\forall x \, \exists y \, (x < y \land \neg y = x)$.
The strings $x < y$ and $y = x$ are atomic.
The negation rule gives $\neg y = x$, the conjunction rule gives $(x < y \land \neg y = x)$, and the quantifier rule, used twice, gives the whole string.
The [[formation sequence|R99VNXVM8P]] writes this out as a list.

In the signature of arithmetic $\{ 0, S, +, \cdot \}$, the string $\forall x \, (\neg x = 0 \to \exists y \, x = S(y))$ is a formula that says every nonzero number is a successor.
Its [[parse tree|QS95N0MRP8]] has the root $\forall x$, then $\to$, with $\neg$ and $\exists y$ below it.
In the empty signature, $\exists x \, \exists y \, \neg x = y$ is a formula, built only from equality, and it says that there are at least two elements.

### What is not a formula

The string $\forall x \, (x \land y)$ is not a formula, because $\land$ needs formulas on both sides, and $x$ and $y$ are [[terms|6D3WA7N2W4]].
The string $\forall c \, P(c)$, with $c$ a constant symbol, is [[not a formula|4SV9Q67884]], because the quantifier rule needs a variable after $\forall$.
The string $(x < y$ is not a formula either.
Every formula has as many left brackets as right brackets, and this string has one extra left bracket.
The term $x + 1$ is not a formula, since it names an object and makes no claim.

### Induction on formulas, worked once

We prove that every formula has as many left brackets as right brackets.
Every term is balanced: variables and constants have no brackets, and $f(t_1, \ldots, t_n)$ adds one bracket of each kind to balanced terms.
So $R(t_1, \ldots, t_n)$ is balanced, and $t_1 = t_2$ adds no bracket at all.
The rules for $\neg$, $\forall x$ and $\exists x$ add no bracket, and each binary rule adds one left and one right bracket.
So the set of balanced formulas contains the atomic formulas and is closed under the rules, and the formulas form the smallest such set.

This is the pattern of every proof by induction on formulas.
A useful measure is the complexity, the number of connectives and quantifiers in a formula.
Atomic formulas have complexity $0$, and each rule adds $1$.

### The rules you can use

Every formula has exactly one reading: it is atomic, a negation, a binary combination or a quantification, in exactly one way.
This is the [[unique readability theorem|3QPV4XW8MC]], and it makes definitions by recursion on formulas well defined.
Each formula is a finite string, so if the signature is countable, then the set of formulas is countable.
A formula may have free variables, as $y$ in $\forall x \, (x < y)$, and then it is not a [[sentence|DKFGQTRYZE]].

### Watch out

A formula is a string, not a meaning.
The formulas $x = y$ and $y = x$ say the same thing in every structure, but they are two different formulas.

The binding order trips many readers.
The string $\forall x \, P(x) \to Q$ means $(\forall x \, P(x)) \to Q$, not $\forall x \, (P(x) \to Q)$.
If you mean the second reading, write the brackets.

A function symbol does not make a claim.
In the signature of rings, $x \cdot y$ is a term, and only something such as $x \cdot y = z$ is a formula.

### History

Frege's Begriffsschrift of 1879 gave the first formal language with quantifiers, in a two-dimensional notation.
Hilbert and Ackermann's textbook of 1928 set out first-order logic, which they called the restricted functional calculus, as a subject of its own.
The inductive definition of formulas, with recursion on formulas as the main tool, is now standard in every textbook.

### Try it

Is $\exists x \, (x < y \to \forall y \, y < x)$ a formula over $\{ < \}$?
Yes: $x < y$ and $y < x$ are atomic, $\forall y \, y < x$ comes by the quantifier rule, the bracket comes by the rule for $\to$, and $\exists x$ comes last.

Is $\neg \forall x$ a formula?
No: the quantifier rule needs a formula after $\forall x$, and the string ends there.

## Explanations

### L1 human

A formula is a statement written with a strict formal alphabet.
Simple claims such as $x < y$ or $x = 0$ are formulas from the start.
Longer claims are made with "not", "and", "or", "if ... then", "for all" and "there exists".
For example, "for every $x$ there is a $y$ with $x < y$" becomes $\forall x \, \exists y \, (x < y)$.
A string such as $< x \land$ breaks the rules, so it is not a formula and has no meaning.

### L2 human

Here is a worked check that $\varphi = \exists y \, (x < y \land \neg y = x)$ is a formula over $\{ < \}$, followed by its complexity.
First, $x < y$ and $y = x$ are atomic, so each has complexity $0$.
Then $\neg y = x$ is a formula of complexity $1$, by the negation rule.
Then $(x < y \land \neg y = x)$ is a formula of complexity $0 + 1 + 1 = 2$, by the conjunction rule.
Last, $\varphi$ is a formula of complexity $3$, by the quantifier rule.
Check: $\varphi$ contains one $\exists$, one $\land$ and one $\neg$, which is three symbols.
The typical use of the rules is exactly this: read off the last rule, then work inward.
A proof by induction must treat every rule; a proof that skips the quantifier rule covers only quantifier-free formulas.

### L3 human

The formulas over $\sigma$ form the free algebra on the atomic formulas for one unary operation $\neg$, four binary operations and, for each variable $x$, two unary operations $\forall x$ and $\exists x$.
Unique readability is the statement that the strings really are free, so recursion on formulas is the universal property of a free algebra, as for the [[term algebra|3YYKGWJJND]].
In type theory and in Lean, formulas are an inductive type, and unique readability holds by construction, since constructors are injective with disjoint images.
The cost is the treatment of bound variables: names lead to renaming and to capture under substitution, and nameless encodings such as [[de Bruijn indices|1TC37YHZPE]] avoid both.
The same grammar with other operators gives the formulas of modal logic, of [[second-order logic|G6X7SZSNC5]] and of [[infinitary logic|PQG7VAZ1R2]], where a conjunction may have infinitely many parts.
