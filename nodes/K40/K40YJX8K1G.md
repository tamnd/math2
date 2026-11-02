---
tag: K40YJX8K1G
kind: definition
name: Higher-order logic
msc: [03B16]
defines: P1ABGYRQXH
uses: [086QKPF0A6, 983GZBQYT4, 00E0YZCERH, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
---

## Definition

The relational types are defined inductively.

1. $\iota$ is a type, the type of individuals.
2. If $\tau_1, \dots, \tau_n$ are types with $n \ge 1$, then $(\tau_1, \dots, \tau_n)$ is a type, the type of $n$-ary relations between objects of types $\tau_1, \dots, \tau_n$.

Higher-order logic over a signature $L$ has, for each type $\tau$, variables of type $\tau$ and quantifiers $\forall$ and $\exists$ over them.
Its formulas are built as in [[first-order logic|086QKPF0A6]], with the atomic formula $X(t_1, \dots, t_n)$ whenever $X$ has type $(\tau_1, \dots, \tau_n)$ and each $t_i$ has type $\tau_i$.
In the standard semantics over an $L$-[[structure|983GZBQYT4]] with domain $M$, the domains $D_\tau$ are given by $D_\iota = M$ and $D_{(\tau_1, \dots, \tau_n)} = \mathcal{P}(D_{\tau_1} \times \dots \times D_{\tau_n})$.
Here $\mathcal{P}$ is the [[power set|00E0YZCERH]] and $\times$ the [[Cartesian product|09CEDJYBKP]].

## Remarks

The order of a type is $1$ for $\iota$ and one more than the largest order of $\tau_1, \dots, \tau_n$ for $(\tau_1, \dots, \tau_n)$.
Logic of order $k$ allows quantifiers only over variables whose type has order at most $k$.
First-order logic is the case $k = 1$, and second-order logic is the case $k = 2$.

Example: a variable $\mathcal{X}$ of type $((\iota))$ ranges over sets of subsets of $M$, and $\forall \mathcal{X} \, \exists Y \, \forall x \, (Y(x) \leftrightarrow \exists Z \, (\mathcal{X}(Z) \land Z(x)))$ is a third-order sentence.
It says that each family of subsets has a union, and it is true in every structure.

Non-example: the expression $X(X)$ is not a formula, because no type $\tau$ equals a type $(\tau)$ of relations on objects of type $\tau$.

Many presentations instead use the simply typed lambda calculus, with function types and a type of truth values; this is Church's simple theory of types.

## Explanations

### L1 human

Higher-order logic sorts all objects into levels: individuals, relations on individuals, relations on those relations, and so on.
A variable can range over any one level, and a relation may only be applied to objects of the level below it.
This rule blocks paradoxes such as a set that contains itself.
