---
tag: 47XHPD8XE2
kind: definition
name: Second-order logic
msc: [03B16, 03C85]
defines: G6X7SZSNC5
uses: [086QKPF0A6, 983GZBQYT4, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
---

## Definition

Let $L$ be a signature.
The formulas of second-order logic over $L$ are built like the formulas of [[first-order logic|086QKPF0A6]] over $L$, with these additions.

1. For each $n \ge 1$ there are relation variables $X, Y, \dots$ of arity $n$, and $X(t_1, \dots, t_n)$ is an atomic formula for terms $t_1, \dots, t_n$.
2. If $\varphi$ is a formula and $X$ is a relation variable, then $\forall X \, \varphi$ and $\exists X \, \varphi$ are formulas.

In the standard semantics, a formula is evaluated in an $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ with domain $M$ as in first-order logic.
An $n$-ary relation variable ranges over the whole [[power set|00E0YZCERH]] of $M^n$.

## Remarks

Function variables may be added in the same way; they can be expressed by relation variables.
Monadic second-order logic allows only relation variables of arity $1$, that is, variables for subsets of $M$.

Example: the sentence $\forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big)$ is a second-order sentence over the signature $\set{0, S}$.
It says that every subset of the domain that contains $0$ and is closed under $S$ is the whole domain.

Non-example: a formula with a quantifier over sets of subsets of $M$ is not second-order, because no clause provides such variables; it belongs to third-order logic.

With the standard semantics, second-order logic has neither a complete proof system nor the compactness property.
With Henkin semantics, in which the relation variables range over a chosen family of relations, both properties return.

## Explanations

### L1 human

Second-order logic lets formulas speak about all subsets and all relations of the domain, not only about its elements.
This makes it much more expressive than first-order logic.
For example, finiteness of the domain, or the completeness of the real line, can be written as a single second-order sentence.
