---
tag: ERVV6RWNNX
kind: definition
name: Model complete theory
msc: [03C10]
defines: YR6HCMABTE
uses: [92SWXST1ZM, MVCH6N9SNW, 676H7EGTKJ, 8WZF9SBP39, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
---

## Definition

Let $T$ be a [[theory|92SWXST1ZM]] in a first-order signature $L$.
The theory $T$ is *model complete* if the following holds for all [[models|MVCH6N9SNW]] $M$ and $N$ of $T$.
If $M$ is a [[substructure|676H7EGTKJ]] of $N$, then $M$ is an [[elementary substructure|8WZF9SBP39]] of $N$.

## Remarks

Equivalently, every embedding between models of $T$ is elementary.
By Robinson's test, $T$ is model complete if and only if every $L$-formula is equivalent modulo $T$ to an existential formula $\exists \bar{y} \, \chi(\bar{x}, \bar{y})$ with $\chi$ quantifier-free.
A theory with [[quantifier elimination|7FDDXV3JK7]] is model complete.

Example: the theory of dense linear orders without endpoints is model complete, since it has quantifier elimination.
Let $M \subseteq N$ be two such orders and let $\bar{a}$ be a tuple of $M$.
A formula $\varphi(\bar{a})$ is equivalent to a quantifier-free formula.
That formula only compares elements of $\bar{a}$, so it has the same truth value in $M$ and in $N$.

Non-example: the theory of dense linear orders with a least and a greatest element is not model complete.
The orders $[0, 1] \cap \Q$ and $[0, 2] \cap \Q$ are models, and the first is a substructure of the second.
The element $1$ satisfies $\forall y \, (y \le x)$ in $[0, 1] \cap \Q$ but not in $[0, 2] \cap \Q$.

The theory of real closed fields in the signature $\set{+, -, \cdot, 0, 1}$ is model complete but does not have quantifier elimination.
