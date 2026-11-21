---
tag: ERVV6RWNNX
kind: definition
name: Model complete theory
msc: ["03C10"]
topics: [1A9JSC5YG8]
audience: grad
defines: YR6HCMABTE
uses: [92SWXST1ZM, MVCH6N9SNW, 676H7EGTKJ, 8WZF9SBP39, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Definition

Let $T$ be a [[theory|92SWXST1ZM]] in a first-order signature $L$.
The theory $T$ is *model complete* if the following holds for all [[models|MVCH6N9SNW]] $M$ and $N$ of $T$.
If $M$ is a [[substructure|676H7EGTKJ]] of $N$, then $M$ is an [[elementary substructure|8WZF9SBP39]] of $N$.

## Notation

One writes $M \preceq N$ for "$M$ is an elementary substructure of $N$".
So $T$ is model complete when $M \subseteq N$ implies $M \preceq N$ for models of $T$.
An embedding $f \colon M \to N$ has image $f(M) \subseteq N$, and $f(M)$ is isomorphic to $M$, so $T$ is model complete exactly when every embedding between models of $T$ is elementary.

## Remarks

By [[Robinson's test|~3847820a]], $T$ is model complete if and only if every $L$-formula is equivalent modulo $T$ to an existential formula $\exists \bar{y} \, \chi(\bar{x}, \bar{y})$ with $\chi$ quantifier-free.
A theory with [[quantifier elimination|7FDDXV3JK7]] is model complete.

Example: the theory of dense linear orders without endpoints is model complete, since it has quantifier elimination.
Let $M \subseteq N$ be two such orders and let $\bar{a}$ be a tuple of $M$.
A formula $\varphi(\bar{a})$ is equivalent to a quantifier-free formula.
That formula only compares elements of $\bar{a}$, so it has the same truth value in $M$ and in $N$.

Non-example: the theory of dense linear orders with a least and a greatest element is not model complete.
The orders $[0, 1] \cap \Q$ and $[0, 2] \cap \Q$ are models, and the first is a substructure of the second.
The element $1$ satisfies $\forall y \, (y \le x)$ in $[0, 1] \cap \Q$ but not in $[0, 2] \cap \Q$.

The theory of real closed fields in the signature $\set{+, -, \cdot, 0, 1}$ is model complete but does not have quantifier elimination; see [[this example|~a3bccf2c]].
The theory of the group $(\Z, +, -, 0)$ is not model complete; see [[this non-example|~4e820942]].

## Explanations

### L1 human

A theory is model complete when a model inside a larger model always agrees with it.
Every question about elements of the small model gets the same answer in both models.
For the fractions inside the real numbers, with their order, the question "is there a number between $1/3$ and $1/2$" has the answer yes in both.

### L2 human

We check the definition for the theory of dense linear orders without endpoints, with $M = \Q$ and $N = \R$.

1. Both are dense linear orders without endpoints, and $\Q$ is a substructure of $\R$.
2. Take the formula $\exists y \, (a < y \wedge y < b)$ with $a = 0$ and $b = 1/2$.
3. By quantifier elimination it is equivalent to $a < b$, which is true in both.
4. A witness in $\Q$ is $y = 1/4$; it is also a witness in $\R$.

The typical use of the definition is to show that a solution in a large model gives a solution in a small one.
A trap is to require $M \preceq N$ only for some inclusion; the definition asks for every inclusion of models.
