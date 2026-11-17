---
tag: BQQ0FPFZ67
kind: definition
name: Term
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
defines: 6D3WA7N2W4
uses: [WDVVEYD6AT, 1P6EP01HZF]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Term
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] and let $V$ be a set of variables, disjoint from the symbols of $\sigma$.
The set of *terms* over $\sigma$ and $V$ is the smallest set of finite [[strings|1P6EP01HZF]] of symbols such that:

1. every variable $x \in V$ is a term;
2. every constant symbol $c$ of $\sigma$ is a term;
3. if $f$ is a function symbol of $\sigma$ of arity $n \ge 1$ and $t_1, \dots, t_n$ are terms, then $f(t_1, \dots, t_n)$ is a term.

A term with no variables is a *closed term*, or a *ground term*.
The set $\operatorname{Var}(t)$ of variables of a term is defined by recursion: $\operatorname{Var}(x) = \set{x}$, $\operatorname{Var}(c) = \emptyset$, and $\operatorname{Var}(f(t_1, \dots, t_n)) = \operatorname{Var}(t_1) \cup \dots \cup \operatorname{Var}(t_n)$.

## Notation

1. Binary function symbols are often written infix, as $(t_1 + t_2)$ for $+(t_1, t_2)$, and unary ones sometimes postfix, as $t^{-1}$.
2. The set of terms is written $T_\sigma(V)$, $\mathrm{Term}_\sigma$ or $\mathrm{Tm}$.
3. In Mathlib `FirstOrder.Language.Term L α` has two constructors: `var a` for `a : α`, and `func f ts` for `f : L.Functions n` and `ts : Fin n → L.Term α`.

## Remarks

In the signature of rings, $\cdot(x, +(y, 1))$ is a term, usually written $x \cdot (y + 1)$.
It is a term by clause 1 for $x$ and $y$, clause 2 for $1$, and clause 3 twice.
In the signature of ordered sets, $x < y$ is not a term: $<$ is a relation symbol, not a function symbol, so clause 3 does not apply.
The word "smallest" means that a string is a term only when a finite chain of the clauses produces it.
Every term has a unique reading, by [[unique readability|~62799b98]], so one can define functions on terms by recursion on this construction.
In Mathlib constants are function symbols of arity $0$, so clause 2 is the case $n = 0$ of clause 3.

## Explanations

### L1 human

The rules build terms from small pieces.
Variables and constants are terms.
A function symbol with the right number of terms as inputs gives a new term.
Nothing else is a term.

### L2 human

We check that $S(+(x, 0))$ is a term of $\set{0, S, +}$ and find its variables.

1. $x$ is a term by clause 1, and $0$ is a term by clause 2.
2. $+(x, 0)$ is a term by clause 3, since $\operatorname{ar}(+) = 2$.
3. $S(+(x, 0))$ is a term by clause 3, since $\operatorname{ar}(S) = 1$.
4. $\operatorname{Var}(S(+(x, 0))) = \operatorname{Var}(x) \cup \operatorname{Var}(0) = \set{x}$, so the term is not closed.

The typical use of the clauses is a proof by structural induction over all terms.
A trap: the recursive definition of $\operatorname{Var}$ needs unique readability to give one value for each term.
