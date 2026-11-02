---
tag: VA7AK1R5AN
kind: definition
name: Type
msc: [03C07, 03C50]
defines: 9V71Q3SD1G
uses: [92SWXST1ZM, HYJ10AF6RT, MVCH6N9SNW, WDVVEYD6AT]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], let $T$ be an $L$-[[theory|92SWXST1ZM]], and let $n \ge 1$.
An *$n$-type* of $T$ is a set $p(x_1, \dots, x_n)$ of $L$-[[formulas|HYJ10AF6RT]] whose free variables are among $x_1, \dots, x_n$, such that $T \cup p$ is satisfiable.
This means that some [[model|MVCH6N9SNW]] $M$ of $T$ has a tuple $(a_1, \dots, a_n)$ that satisfies every formula of $p$.
The type $p$ is *complete* if for every $L$-formula $\varphi(x_1, \dots, x_n)$, either $\varphi \in p$ or $\neg \varphi \in p$.
A model $M$ of $T$ *realizes* $p$ if some tuple of $M$ satisfies every formula of $p$, and *omits* $p$ otherwise.
The set of complete $n$-types of $T$ is written $S_n(T)$.

Let $M$ be a model and $A$ a set of elements of $M$.
Let $L_A$ be $L$ extended by a new constant for each element of $A$.
A type over $A$ is a type of the $L_A$-theory of $M$.
The set of complete $n$-types over $A$ is written $S_n^M(A)$.

## Remarks

For a tuple $\bar{a}$ of a model $M$, the set $\operatorname{tp}(\bar{a})$ of all formulas satisfied by $\bar{a}$ in $M$ is a complete type of the theory of $M$.

Example: let $T$ be the theory of $(\N, 0, 1, +, \cdot, <)$ and let $p(x) = \set{x > 1 + \cdots + 1 \ (k \text{ terms}) : k \ge 1}$.
Each finite part of $p$ is satisfied in $\N$ by a large number, so by compactness $T \cup p$ has a model, and $p$ is a $1$-type.
The standard model $\N$ omits $p$, while every nonstandard model of $T$ realizes it.

Non-example: in the theory of fields, $\set{x = 0, \; x \cdot x = 1}$ is not a type, since $x = 0$ gives $x \cdot x = 0 \ne 1$ in every field.

The set $S_n(T)$ carries a natural topology, with basic open sets $\set{p : \varphi \in p}$; it is a compact, totally disconnected Hausdorff space by the compactness theorem.
