---
tag: VA7AK1R5AN
kind: definition
name: Type
msc: ["03C07", "03C50"]
topics: [Z772KEC9BY]
audience: grad
defines: 9V71Q3SD1G
uses: [92SWXST1ZM, HYJ10AF6RT, MVCH6N9SNW, WDVVEYD6AT]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Theory.CompleteType
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Definitions
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], let $T$ be an $L$-[[theory|92SWXST1ZM]], and let $n \ge 1$.
An *$n$-type* of $T$ is a set $p(x_1, \dots, x_n)$ of $L$-[[formulas|HYJ10AF6RT]] whose free variables are among $x_1, \dots, x_n$, such that $T \cup p$ is satisfiable.
This means that some [[model|MVCH6N9SNW]] $\mathcal{M}$ of $T$ has a tuple $(a_1, \dots, a_n)$ that satisfies every formula of $p$.
The type $p$ is *complete* if for every $L$-formula $\varphi(x_1, \dots, x_n)$, either $\varphi \in p$ or $\neg \varphi \in p$.
A model $\mathcal{M}$ of $T$ *realizes* $p$ if some tuple of $\mathcal{M}$ satisfies every formula of $p$, and *omits* $p$ otherwise.

Let $\mathcal{M}$ be an $L$-structure with domain $M$, and let $A \subseteq M$.
Let $L_A$ be $L$ extended by a new constant for each element of $A$, and let $\operatorname{Th}_A(\mathcal{M})$ be the set of $L_A$-sentences true in $\mathcal{M}$.
An $n$-type *over $A$* is an $n$-type of the $L_A$-theory $\operatorname{Th}_A(\mathcal{M})$.
For a tuple $\bar{a}$ of $M$, the *type of $\bar{a}$ over $A$* is $\operatorname{tp}(\bar{a}/A) = \set{\varphi(\bar{x}) : \varphi \text{ an } L_A\text{-formula and } \mathcal{M} \models \varphi(\bar{a})}$.

## Notation

The set of complete $n$-types of $T$ is $S_n(T)$, and the set of complete $n$-types over $A$ is $S_n^{\mathcal{M}}(A)$ or $S_n(A)$.
The type of $\bar{a}$ over $A$ is also written $\operatorname{tp}^{\mathcal{M}}(\bar{a}/A)$, and $\operatorname{tp}(\bar{a})$ when $A = \emptyset$.

## Remarks

The set $\operatorname{tp}(\bar{a}/A)$ is a complete $n$-type over $A$: the tuple $\bar{a}$ realizes it, and for each $\varphi$ either $\varphi(\bar{a})$ or $\neg \varphi(\bar{a})$ holds.
By the compactness theorem, a set $p$ of $L_A$-formulas is a type over $A$ exactly when every finite subset of $p$ is realized by a tuple of $\mathcal{M}$.
The main page of the idea, with examples and properties, is [[type|9V71Q3SD1G]].

Example: let $T$ be the theory of $(\N, 0, 1, +, \cdot, <)$ and let $p(x) = \set{x > 1 + \cdots + 1 \ (k \text{ terms}) : k \ge 1}$.
Each finite part of $p$ is satisfied in $\N$ by a large number, so $p$ is a $1$-type of $T$, and $\N$ omits it.

Non-example: in the theory of fields, $\set{x = 0, \; x \cdot x = 1}$ is not a type, since $x = 0$ gives $x \cdot x = 0 \ne 1$ in every field.

## Explanations

### L1 human

A type is a consistent list of properties of an element, or of a few elements.
The type of an element over a set of parameters is the list of all properties that the element really has.

### L2 human

In $(\Q, <)$ take $A = \set{0}$ and the element $5$.

1. The formula $0 < x$ holds of $5$, so it is in $\operatorname{tp}(5/A)$.
2. The formulas $x < 0$ and $x = 0$ fail at $5$, so their negations are in $\operatorname{tp}(5/A)$.
3. By quantifier elimination for dense linear orders, these facts decide every other formula over $A$.
4. The element $1/2$ satisfies the same three facts, so $5$ and $1/2$ have the same type over $A$.

The trap is to read $\operatorname{tp}(5/A)$ as a property of the number $5$ alone: it depends on the structure and on $A$.
