---
tag: BP6WW7H5CC
kind: definition
name: Atomic formula
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
defines: MCZRXR3SVB
uses: [WDVVEYD6AT, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Definition

An atomic formula is a formula that applies equality or one relation symbol to terms, with nothing else around it.

Let $\sigma$ be a [[signature|WDVVEYD6AT]].
An *atomic formula* over $\sigma$ is a string of one of the following two forms.

1. $t_1 = t_2$, where $t_1$ and $t_2$ are [[terms|6D3WA7N2W4]] over $\sigma$.
2. $R(t_1, \dots, t_n)$, where $R$ is a relation symbol of $\sigma$ of arity $n$ and $t_1, \dots, t_n$ are terms over $\sigma$.

In first-order logic without equality, only the second form is atomic.
An atomic formula, or the negation of one, is a *literal*.

## Notation

A binary relation symbol is usually written infix: $t_1 < t_2$ for $<(t_1, t_2)$, and $t_1 \in t_2$ for $\in(t_1, t_2)$.
Where a book allows a relation symbol $R$ of arity $0$, the atomic formula is $R$ alone, with no brackets.
Some books also count $\top$ and $\bot$ as atomic formulas.

## Remarks

Each form has one top symbol and only terms below it.
Form 1 uses the logical symbol $=$, which every language with equality has, and form 2 uses a relation symbol from $\sigma$ with exactly as many terms as its arity.
The relation symbols and $=$ occur only in atomic formulas, and each atomic formula has exactly one of them at the top.
That is why atomic formulas are the base case of the recursive definition of [[formulas|HYJ10AF6RT]].

For an instance, in the signature of ordered rings the string $x \cdot x < y + 1$ is atomic of form 2, with $R$ equal to $<$ and the terms $x \cdot x$ and $y + 1$.
A case that fails is $(x < y \lor x = y)$: it contains the connective $\lor$, so it is a formula built from two atomic ones, not an atomic formula.
Another failing case is $<(x)$, where $<$ has arity $2$ but gets one term.

In Mathlib the atomic formulas are those built by `FirstOrder.Language.BoundedFormula.equal` and `FirstOrder.Language.Relations.boundedFormula`, and the predicate `IsAtomic` marks them.
The concept page [[atomic formula|MCZRXR3SVB]] has more examples and the first facts.

## Explanations

### L1 human

An atomic formula says that two terms are equal, or that a relation holds between some terms.
For example, $x + 1 = y$ and $x < y$ are atomic.
It is the smallest kind of formula: no smaller formula sits inside it.

### L2 human

We check that $P(f(x), c)$ is an atomic formula of the signature $\{ c, f, P \}$, with arities $0$, $1$ and $2$.
The string $x$ is a term, and $f(x)$ is a term since $f$ has arity $1$ and gets one term.
The constant symbol $c$ is a term by itself.
The relation symbol $P$ has arity $2$ and gets the two terms $f(x)$ and $c$, so $P(f(x), c)$ is atomic of form 2.
The typical use of the definition is the base case of a recursion on formulas.
Watch out: $f(x) = P(x, c)$ is not a formula, since $P(x, c)$ is a formula and not a term, and $=$ needs two terms.
