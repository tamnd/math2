---
tag: BQQ0FPFZ67
kind: definition
name: Term
msc: [03B10, 03C07]
defines: 6D3WA7N2W4
uses: [WDVVEYD6AT]
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] and let $V$ be a set of variables, disjoint from the symbols of $\sigma$.
The set of *terms* over $\sigma$ and $V$ is the smallest set of finite strings of symbols such that:

1. every variable $x \in V$ is a term;
2. every constant symbol $c$ of $\sigma$ is a term;
3. if $f$ is a function symbol of $\sigma$ of arity $n \ge 1$ and $t_1, \dots, t_n$ are terms, then $f(t_1, \dots, t_n)$ is a term.

A term with no variables is a *closed term*, or a *ground term*.

## Remarks

In the signature of rings, $\cdot(x, +(y, 1))$ is a term, usually written $x \cdot (y + 1)$.
It is a term by clause 1 for $x$ and $y$, clause 2 for $1$, and clause 3 twice.
In the signature of ordered sets, $x < y$ is not a term: $<$ is a relation symbol, not a function symbol, so clause 3 does not apply.
Every term has a unique reading, so one can define functions on terms by recursion on this construction.
In Mathlib terms are `FirstOrder.Language.Term`.
