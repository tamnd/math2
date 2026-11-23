---
tag: PWHJZYBNEY
kind: definition
name: Signature
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: ug2
defines: WDVVEYD6AT
uses: [0EPAT51DXQ, MSXX2P86CY]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
---

## Definition

A signature fixes the non-logical symbols of a first-order language and the number of arguments of each.

A *signature* $\sigma$ consists of

1. a set $F$ of function symbols,
2. a set $R$ of relation symbols, disjoint from $F$, and
3. an [[arity|MSXX2P86CY]] [[function|0EPAT51DXQ]] $\operatorname{ar} \colon F \cup R \to \mathbb{N}$, which gives the number of arguments of each symbol.

A function symbol $c$ with $\operatorname{ar}(c) = 0$ is a *constant symbol*.
The symbols of $\sigma$ are the non-logical symbols of the language, and we assume that they differ from the logical symbols.
The variables, connectives, quantifiers, parentheses and the equality symbol are logical symbols, and they are not part of $\sigma$.

## Notation

A signature is written $\sigma$, $\tau$, $L$ or $\mathcal{L}$, and is often listed as a set of symbols with their arities, such as $\{ +, \cdot, 0 \}$ with arities $2, 2, 0$.
It is *relational* when $F$ is empty, and *algebraic* or *functional* when $R$ is empty.
In Mathlib, `FirstOrder.Language` has two fields, `Functions : ℕ → Type u` and `Relations : ℕ → Type v`.
There the arity is the index $n$, so each symbol has exactly one arity by construction.

## Remarks

Each part of the definition does one job.
The arity tells us how many terms a symbol needs, and that is what makes the reading of a term unique.
The two sets are disjoint because a function symbol makes a new term, while a relation symbol makes a statement, and one mark cannot do both.
Constants are function symbols of arity $0$, so the rules for terms need no separate case for them.

Here is a small instance.
The signature of ordered fields has $F = \{ +, \cdot, -, 0, 1 \}$ with arities $2, 2, 1, 0, 0$, and $R = \{ < \}$ with $\operatorname{ar}(<) = 2$.
Its constant symbols are $0$ and $1$, and $=$ is not listed because it is logical.
A case that fails is "$-$ with arity $1$ and also arity $2$": the arity is a function, so each symbol gets one value, as [[one symbol for unary and binary minus|YG6J9BDB67]] explains.

Books differ in small ways.
Some list the constant symbols as a third set instead of as function symbols of arity $0$.
Some allow relation symbols of arity $0$, which act as propositional letters.
Enderton counts the equality symbol as an optional logical symbol, so his languages may have it or not.
In Mathlib equality is built into the formulas, and it is not a relation symbol of the language.
The concept page [[signature|WDVVEYD6AT]] gives more examples and the first facts.

## Explanations

### L1 human

A signature is a list of symbols, each with its number of inputs.
For ordered fields the list is $+$, $\cdot$, $-$, $0$, $1$ and $<$.
The symbols $+$ and $\cdot$ take two inputs, $-$ takes one, and $0$ and $1$ take none.
The symbol $<$ is different: it does not make a new object, it makes a statement $x < y$.

### L2 human

We read the definition for the signature of lattices, $\{ \sqcap, \sqcup \}$, for meet and join.
We avoid the letters $\wedge$ and $\vee$ here, since in logic they are connectives.
Both symbols are function symbols with arity $2$, so $F = \{ \sqcap, \sqcup \}$ and $R$ is empty, and the signature is algebraic.
There are no constant symbols, so every term contains a variable, such as $x \sqcap (y \sqcup x)$.
If we add a relation symbol $\le$ of arity $2$, then $R = \{ \le \}$ and we can write the atomic formula $x \sqcap y \le x$.
The typical use of the definition is to fix the language before writing a theory.
Watch out: the same letter may have different arities in two signatures, so always read a symbol together with its signature.
