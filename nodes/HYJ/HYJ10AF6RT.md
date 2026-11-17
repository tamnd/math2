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

Let $\sigma$ be a [[signature|WDVVEYD6AT]].
The well-formed formulas over $\sigma$, or $\sigma$-formulas, form the smallest set of strings that contains every [[atomic formula|MCZRXR3SVB]] and is closed under three rules.
If $\varphi$ is a formula, then $\neg \varphi$ is a formula.
If $\varphi$ and $\psi$ are formulas, then $(\varphi \land \psi)$, $(\varphi \lor \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$ are formulas.
If $\varphi$ is a formula and $x$ is a variable, then $\forall x \, \varphi$ and $\exists x \, \varphi$ are formulas.
Formulas are the statements of [[first-order logic|086QKPF0A6]]: proofs are sequences of formulas, and [[structures|983GZBQYT4]] make formulas true or false.

## Motivation

A formal language must say exactly which strings of symbols are statements.
Without such a rule we cannot define truth, proof or substitution, because each of these definitions works by recursion on the shape of a statement.
The string $\forall x \, \exists y \, (x < y)$ should count as a statement about an order, and the string $\forall \land x <$ should not.
The formation rules do this job, in the same way that a grammar decides which strings of words are English sentences.
The rules are inductive, so every formula is built from atomic formulas in finitely many steps.
This gives two tools for all later work: proof by induction on formulas and definition by recursion on formulas.

## Notation

1. The [[formal definition|2CHENV4DCC]] uses $\neg, \land, \lor, \to, \leftrightarrow$ and both quantifiers as primitive symbols. Many books take fewer primitives: Enderton takes $\neg$, $\to$ and $\forall$, and defines the others as abbreviations.
2. With $\neg$, $\to$ and $\forall$ only, $\exists x \, \varphi$ abbreviates $\neg \forall x \, \neg \varphi$, and $(\varphi \lor \psi)$ abbreviates $(\neg \varphi \to \psi)$.
3. In text we drop the outer brackets, and we use the usual binding order: $\neg$ binds most strongly, then $\land$ and $\lor$, then $\to$ and $\leftrightarrow$.
4. A quantifier binds as strongly as $\neg$. So $\forall x \, P(x) \land Q(x)$ means $(\forall x \, P(x) \land Q(x))$ with the scope of $\forall x$ only $P(x)$.
5. Some books write $(\forall x) \varphi$, $\forall x . \varphi$ or $\bigwedge x \, \varphi$. Polish notation writes connectives in front of their arguments and needs no brackets.
6. In Mathlib, a formula is a term of the type `FirstOrder.Language.BoundedFormula`, with de Bruijn style bound variables. The [[definition|2CHENV4DCC]] explains the encoding.

## Remarks

### Examples

1. In the signature of orders $\set{<}$, the string $\forall x \, \exists y \, (x < y)$ is a formula: $x < y$ is atomic, then the quantifier rule applies twice.
2. In the signature of arithmetic $\set{0, S, +, \cdot}$, the string $\forall x \, (\neg x = 0 \to \exists y \, x = S(y))$ is a formula. Its [[parse tree|QS95N0MRP8]] is worked out on its own page.
3. In the empty signature, the string $\exists x \, \exists y \, \neg x = y$ is a formula. It says that there are at least two elements.
4. The formula $\forall x \, (x < y \land \neg y = x)$ has the free variable $y$. A formula can have [[free variables|9CNGDRAMGC]], and then it is not a [[sentence|DKFGQTRYZE]].
5. The construction of a formula from its atomic parts is shown in [[a formation sequence|R99VNXVM8P]].

### Non-examples

1. The string $\forall x \, (x \land y)$ is not a formula. The connective $\land$ needs formulas on both sides, and $x$ and $y$ are terms.
2. The string $\forall c \, P(c)$, with $c$ a constant symbol, is [[not a formula|4SV9Q67884]]. The quantifier rule needs a variable after $\forall$.
3. The string $(x < y$ is not a formula. Every formula has as many left brackets as right brackets, and this string has one more left bracket.
4. The term $x + 1$ is not a formula. It names an object and makes no claim.

### Basic properties

1. Every formula has exactly one reading: it is atomic, or a negation, or a binary combination, or a quantification, in exactly one way. This is the [[unique readability theorem|3QPV4XW8MC]].
2. Induction on formulas: if a property holds for every atomic formula and is preserved by the three formation rules, then it holds for every formula. The reason is that the set of formulas with the property contains the atomic formulas and is closed under the rules, and the formulas form the smallest such set.
3. Recursion on formulas: a function on formulas can be defined by its values on atomic formulas and by its effect under each rule. Unique readability makes the result well defined.
4. The complexity of a formula is the number of occurrences of connectives and quantifiers in it. Atomic formulas have complexity $0$, and each rule adds $1$, so induction on formulas is the same as strong induction on complexity.
5. Each formula is a finite string. If the signature is countable, then the set of formulas is countable, because it is a subset of the set of finite strings over a countable alphabet.

### History

Frege's Begriffsschrift of 1879 gave the first formal language with quantifiers, in a two-dimensional notation.
The modern linear notation with $\forall$ and $\exists$ comes from Peano, Russell and Hilbert.
The inductive definition of formulas, with recursion on formulas as the main tool, became standard in textbooks of the twentieth century.

### Common errors

1. Students forget that a formula is a string. Two formulas that mean the same, such as $x = y$ and $y = x$, are still two different formulas.
2. Students read $\forall x \, P(x) \to Q$ as $\forall x \, (P(x) \to Q)$. With the binding order above, it means $(\forall x \, P(x)) \to Q$.
3. Students use a function symbol where a relation symbol is needed. In the signature of rings, $x \cdot y$ is a term, and only $x \cdot y = z$ is a formula.

## Explanations

### L1 human

A formula is a statement written in a strict formal alphabet.
The rules say which strings are allowed, in the same way that grammar rules say which strings of words are sentences.
We start with simple claims, such as $x < y$ or $x = 0$.
Then we combine claims with "not", "and", "or", "if ... then", "for all" and "there exists".
For example, "for all $x$ there is a $y$ with $x < y$" becomes $\forall x \, \exists y \, (x < y)$.
A string such as $< x \land$ breaks the rules, so it is not a formula and has no meaning.

### L2 human

We show that every formula has as many left brackets as right brackets, by induction on formulas.

1. Let $\ell(\alpha)$ and $r(\alpha)$ be the numbers of left and right brackets in a string $\alpha$.
2. Every term $t$ has $\ell(t) = r(t)$. A variable or a constant has no brackets, and $f(t_1, \ldots, t_n)$ adds one left and one right bracket to terms that are balanced by induction.
3. An atomic formula $R(t_1, \ldots, t_n)$ adds one bracket of each kind to balanced terms, and $t_1 = t_2$ adds none. So atomic formulas are balanced.
4. If $\varphi$ is balanced, then $\neg \varphi$, $\forall x \, \varphi$ and $\exists x \, \varphi$ are balanced, because the new symbols are not brackets.
5. If $\varphi$ and $\psi$ are balanced, then $(\varphi \land \psi)$ is balanced, because it adds one bracket of each kind. The other binary connectives work in the same way.
6. By induction on formulas, every formula is balanced.

The typical use of the formation rules is this pattern: check the atomic case, then check that each rule keeps the property.
The trap is to forget a rule: a proof that treats $\neg$ and $\land$ but not the quantifiers proves the claim only for quantifier-free formulas.

### L3 human

The formulas over $\sigma$ form the initial algebra of a signature of operations: one unary operation $\neg$, four binary operations and, for each variable $x$, two unary operations $\forall x$ and $\exists x$, over the set of atomic formulas.
Unique readability says that the strings form a free algebra, so recursion on formulas is the universal property of a free algebra, as for the [[term algebra|3YYKGWJJND]].
In type theory and in Lean, formulas are an inductive type, and unique readability holds by construction, because the constructors are injective with disjoint images.
The price is the treatment of bound variables: names lead to [[renaming problems|9CNGDRAMGC]] and capture under [[substitution|NCDZ969V7X]], and nameless encodings such as [[de Bruijn indices|1TC37YHZPE]] avoid them.
The same grammar, with other connectives or quantifiers, gives the formulas of modal logic, of [[second-order logic|G6X7SZSNC5]] and of [[infinitary logic|PQG7VAZ1R2]], where conjunctions of infinitely many formulas are allowed.
