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

A *signature* $\sigma$ consists of:

1. a set $F$ of function symbols;
2. a set $R$ of relation symbols, disjoint from $F$;
3. an [[arity|MSXX2P86CY]] [[function|0EPAT51DXQ]] $\operatorname{ar} \colon F \cup R \to \N$ that gives the number of arguments of each symbol.

A function symbol of arity $0$ is a *constant symbol*.
The symbols of $\sigma$ are the non-logical symbols of a first-order language.
The variables, connectives, quantifiers, brackets and the equality symbol are logical symbols, and they are not part of $\sigma$.
The symbols of $\sigma$ are assumed to be distinct from the logical symbols.

## Notation

1. A signature is written $\sigma$, $\tau$, $L$ or $\mathcal{L}$, and it is often listed as a set of symbols with their arities, such as $\set{+, \cdot, 0}$ with arities $2, 2, 0$.
2. A signature is *relational* when $F$ is empty, and *algebraic* or *functional* when $R$ is empty.
3. In Mathlib, `FirstOrder.Language` has two fields, `Functions : ℕ → Type u` and `Relations : ℕ → Type v`. The arity is the index $n$, so each symbol has exactly one arity by construction.

## Remarks

The signature of rings is $\set{+, \cdot, -, 0, 1}$ with arities $2, 2, 1, 0, 0$; it has no relation symbols.
The signature of ordered sets has one relation symbol $<$ of arity $2$ and no function symbols.
The list "a binary operation $\cdot$ that is associative" is not a signature: associativity is an axiom, and a signature contains only symbols and their arities.
Some books list the constant symbols as a third set instead of treating them as functions of arity $0$.
Some books also allow relation symbols of arity $0$, which act as propositional letters.
Enderton counts the equality symbol as an optional logical symbol, so his languages may have it or not.
In Mathlib equality is built into the formulas, and it is not a relation symbol of the language.

## Explanations

### L1 human

A signature is a list of symbols, each with its number of inputs.
For ordered fields the list is $+$, $\cdot$, $-$, $0$, $1$ and $<$.
The symbols $+$ and $\cdot$ take two inputs, $-$ takes one, and $0$ and $1$ take none.
The symbol $<$ is different: it does not make a new object, it makes a statement $x < y$.

### L2 human

We read the definition for the signature of ordered fields.

1. The function symbols are $F = \set{+, \cdot, -, 0, 1}$, with $\operatorname{ar}$ equal to $2, 2, 1, 0, 0$.
2. The relation symbols are $R = \set{<}$, with $\operatorname{ar}(<) = 2$.
3. The constant symbols are $0$ and $1$, the function symbols of arity $0$.
4. The symbol $=$ is not listed, because it is logical.

The typical use of the definition is to fix the language before writing a theory.
A trap: the same letter in two signatures may have different arities, so a symbol is always read with its signature.
