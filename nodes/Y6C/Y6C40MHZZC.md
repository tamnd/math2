---
tag: Y6C40MHZZC
kind: definition
name: Structure
msc: ["03C07", "03B10"]
topics: [NJDME6F845]
audience: ug2
defines: 983GZBQYT4
uses: [WDVVEYD6AT, 0BSJ7RQ9BW, 0EPAT51DXQ, 09CEDJYBKP]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Structure
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
    locator: Definition
  - book: isbn:9780122384523
    locator: Section 2.2
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]]: a set of constant symbols, function symbols and relation symbols, where each function symbol and each relation symbol has an arity $n \geq 1$.
An $L$-structure $\mathcal{M}$ consists of the following data.

1. A nonempty [[set|0BSJ7RQ9BW]] $M$, the domain or universe of $\mathcal{M}$.
2. For each constant symbol $c$ of $L$, an element $c^{\mathcal{M}} \in M$.
3. For each $n$-ary function symbol $f$ of $L$, a [[function|0EPAT51DXQ]] $f^{\mathcal{M}} \colon M^n \to M$, where $M^n$ is the [[Cartesian product|09CEDJYBKP]] of $n$ copies of $M$.
4. For each $n$-ary relation symbol $R$ of $L$, a subset $R^{\mathcal{M}} \subseteq M^n$.

The objects $c^{\mathcal{M}}$, $f^{\mathcal{M}}$ and $R^{\mathcal{M}}$ are the interpretations of the symbols in $\mathcal{M}$.
The equality symbol is a logical symbol, not a symbol of $L$; in every structure it is interpreted as the identity relation $\set{(a, a) : a \in M}$.

## Notation

A structure is written $\mathcal{M}$, and its domain $M$; Enderton writes $\mathfrak{A}$ and $|\mathfrak{A}|$.
A structure with a short signature is written as a tuple, such as $(\Z, +, -, 0)$, with the interpretations in the order of the symbols.
In Mathlib, `FirstOrder.Language.Structure L M` gives the interpretations `funMap` and `RelMap` on a type `M`, and a constant is a function symbol of arity $0$.
Mathlib does not require `M` to be nonempty; this page and most textbooks do.

## Remarks

Example: let $L = \set{+, -, 0}$ with $+$ binary, $-$ unary and $0$ a constant symbol.
The integers $\Z$ with addition, negation and the number $0$ form an $L$-structure, because each symbol receives a function of the right arity on $\Z$ or an element of $\Z$.

Non-example: for the same signature, the natural numbers $\N$ with $x \mapsto -x$ do not form an $L$-structure, because $-1 \notin \N$, so $x \mapsto -x$ is not a function from $\N$ to $\N$.

The concept page [[structure|983GZBQYT4]] gives more examples, the non-examples, the convention on empty domains, and reducts and expansions.

## Explanations

### L1 human

A structure gives a meaning to each symbol of a formal language.
The symbol $<$ alone says nothing; in the structure $(\Q, <)$ it means the usual order of the rational numbers.
Once each symbol has a meaning, each sentence of the language becomes true or false in the structure.

### L2 human

We check the definition for the signature $L = \set{c, f, R}$ with $c$ a constant symbol, $f$ unary and $R$ binary.
Let $M = \set{0, 1}$, $c^{\mathcal{M}} = 0$, $f^{\mathcal{M}}(a) = 1 - a$ and $R^{\mathcal{M}} = \set{(0, 1)}$.

1. The domain $\set{0, 1}$ is nonempty.
2. The element $c^{\mathcal{M}} = 0$ lies in $M$.
3. The map $f^{\mathcal{M}}$ sends $0$ to $1$ and $1$ to $0$, so it is a function from $M$ to $M$.
4. The pair $(0, 1)$ lies in $M^2$, so $R^{\mathcal{M}} \subseteq M^2$.

So $\mathcal{M}$ is an $L$-structure; the page on [[satisfaction|2RBQPV02AS]] evaluates formulas in it.
A trap is to give a binary relation symbol a set of single elements, such as $\set{0}$: it must be a set of pairs.
