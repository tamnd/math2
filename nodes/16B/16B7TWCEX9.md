---
tag: 16B7TWCEX9
kind: definition
name: Strongly minimal theory
msc: [03C45]
defines: PNGY60EBDJ
uses: [655K8Y7VS8, MVCH6N9SNW, CY1TXHF6KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Strongly_minimal_theory
---

## Definition

Let $L$ be a first-order language and let $T$ be a [[complete theory|655K8Y7VS8]] in $L$ that has infinite [[models|MVCH6N9SNW]].
Let $M$ be an infinite $L$-structure.
A subset of $M$ is [[definable|CY1TXHF6KQ]] in one variable if it has the form $\set{a \in M : M \models \varphi(a, \bar b)}$ for a formula $\varphi(x, \bar b)$ with parameters $\bar b$ in $M$.
The structure $M$ is *minimal* if every such subset is finite or cofinite in $M$.
The theory $T$ is *strongly minimal* if every model of $T$ is minimal.

## Remarks

Example: the theory of infinite sets in the empty language is strongly minimal.
By quantifier elimination, a formula $\varphi(x, \bar b)$ is equivalent to a Boolean combination of equations $x = b_i$, so it defines a finite or a cofinite set.
The theory of algebraically closed fields of a fixed characteristic is strongly minimal for a similar reason: a nonzero polynomial in one variable has finitely many roots.

Non-example: the theory of dense linear orders without endpoints is not strongly minimal.
In $(\Q, <)$ the formula $x > 0$ defines a set that is infinite and has an infinite complement.

A structure can be minimal while its theory is not strongly minimal, since the condition must hold in every model of the theory.
In a strongly minimal theory, algebraic closure satisfies the exchange property, so every model has a dimension.
If $L$ is countable, a strongly minimal theory is categorical in every uncountable cardinality.
