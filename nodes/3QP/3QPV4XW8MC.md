---
tag: 3QPV4XW8MC
kind: statement
role: theorem
name: Unique readability of terms and formulas
aliases: [unique-parsing-theorem, unique-readability-theorem]
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
about: [6D3WA7N2W4, HYJ10AF6RT]
uses: [WDVVEYD6AT, 6D3WA7N2W4, HYJ10AF6RT, 1P6EP01HZF]
sources:
  - book: isbn:9780122384523
    locator: Section 2.3
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: lead section
---

## Statement

Unique readability says that every term and every formula can be taken apart in exactly one way, so it has exactly one formation tree.

Let $\sigma$ be a [[signature|WDVVEYD6AT]].
Assume that the symbols of $\sigma$, the variables, the connectives, the quantifiers, $=$, the two brackets and the comma are pairwise distinct single symbols, and that each symbol of $\sigma$ has one arity.
Take [[terms|6D3WA7N2W4]] and [[formulas|HYJ10AF6RT]] as the finite [[strings|1P6EP01HZF]] built by the clauses of their definitions, with $f(t_1, \dots, t_n)$ and $R(t_1, \dots, t_n)$ for applications and with brackets around each binary connective.

1. Every term is exactly one of the following: a variable, a constant symbol, or $f(t_1, \dots, t_n)$ for a function symbol $f$ of arity $n \ge 1$ and terms $t_1, \dots, t_n$.
   In the last case $f$ and $t_1, \dots, t_n$ are unique.
2. Every formula is exactly one of the following, and in each case the displayed parts are unique.
   - $t_1 = t_2$ with terms $t_1, t_2$.
   - $R(t_1, \dots, t_n)$ with a relation symbol $R$ of arity $n$ and terms $t_1, \dots, t_n$.
   - $\neg \psi$ with a formula $\psi$.
   - $(\psi \circ \chi)$ with $\circ \in \{ \land, \lor, \to, \leftrightarrow \}$ and formulas $\psi, \chi$.
   - $\forall x \, \psi$ or $\exists x \, \psi$ with a variable $x$ and a formula $\psi$.

## Remarks

### Reading one formula

Take the formula $\big((x = 0 \land y = 0) \to x = y\big)$ in the signature with one constant symbol $0$.
It starts with a left bracket, so it must have the form $(\psi \circ \chi)$.
Which binary connective is the main one?
Count brackets from the left: the $\land$ sits after two left brackets and no right bracket, so it is at depth $2$.
The $\to$ sits after two left brackets and one right bracket, so it is at depth $1$, and it is the only binary connective there.
So the formula splits in one way, with
$$\psi = (x = 0 \land y = 0), \qquad \circ = {\to}, \qquad \chi = \text{the formula } x = y.$$
In the same way $\psi$ splits at its $\land$ into $x = 0$ and $y = 0$, and the tree is complete.
Check: putting the parts back together gives the original string, symbol for symbol.

### Why each hypothesis is needed

The symbols must be distinct and have one arity each.
If one minus sign had arity $1$ and $2$, the prefix string $- - x \, y$ would have [[two readings|YG6J9BDB67]], $(-x) - y$ and $-(x - y)$, with different values.

The brackets around binary connectives are needed too.
Without them the string $p \land q \lor r$, for atomic formulas $p, q, r$, comes both from $(p \land q) \lor r$ and from $p \land (q \lor r)$.
With $p$ false and $r$ true, the first is true and the second is false.

### What it gives you

Functions on terms and formulas can be defined by recursion on the clauses: the value of a term, the [[free variables|9CNGDRAMGC]], [[substitution|NCDZ969V7X]] and satisfaction.
Unique readability makes each such definition give exactly one value.
For example, "the value of $+(t_1, t_2)$ is the sum of the values of $t_1$ and $t_2$" is a definition only because $t_1$ and $t_2$ are determined by the term.
It also makes the main connective of a formula, its subformulas, and the scope of each quantifier well defined.

### The converse and other notations

The converse holds by the definitions: every string of one of the listed forms, with parts of the right kind, is a term or a formula.
So each formula corresponds to exactly one immediate decomposition.

In Polish (prefix) notation, as in Enderton, terms and formulas need no brackets at all, and unique readability still holds.
In algebraic language, the [[term algebra|3YYKGWJJND]] is free over the variables: its operations are injective and have disjoint images.
In Lean, terms and formulas are inductive types, and unique readability holds by construction, since constructors are injective and have disjoint images.

## History

Łukasiewicz introduced prefix notation for propositional logic in the 1920s, and it needs no brackets because each string has a unique reading.
Modern textbooks, such as Enderton's, prove unique readability before they define truth and substitution by recursion.

## Explanations

### L1 human

A formula is a string of symbols, and the rules say how to build it from smaller pieces.
Unique readability says that a formula can be taken apart in only one way.
For example, $(x = 0 \lor x = 1)$ splits only into $x = 0$, the symbol $\lor$, and $x = 1$.
This is why a formula has one meaning, and not two.

### L2 human

We take apart the term $+(\cdot(x, y), S(0))$ of the signature $\{ 0, S, +, \cdot \}$.
The first symbol is $+$, of arity $2$, so the term is $+(t_1, t_2)$ for some terms $t_1$ and $t_2$.
The term $t_1$ starts right after "$+($", and $\cdot(x, y)$ is a term that starts there.
No other term starts there, because a term cannot be a proper initial segment of another term, by the [[proof|NYPH63X6AN]].
So $t_1 = \cdot(x, y)$, the next symbol is the separating comma, and $t_2 = S(0)$ ends at the closing bracket.
The typical use is to justify a recursive definition on terms or formulas.
Watch out: splitting at the first comma fails, because the first comma here belongs to $\cdot(x, y)$, not to $+$.

### L3 human

Unique readability says that the term algebra and the formula algebra are free: each element has one decomposition into a constructor and its arguments.
This freeness gives the recursion theorem for terms and formulas, just as for the natural numbers.
In type theory the same fact is the injectivity and disjointness of the constructors of an inductive type.
For a context-free grammar, unique readability is the statement that the grammar is unambiguous.
Mathlib needs no lemma of this kind, because `FirstOrder.Language.Term` and `FirstOrder.Language.BoundedFormula` are inductive types.
