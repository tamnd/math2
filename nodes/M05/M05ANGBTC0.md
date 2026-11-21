---
tag: M05ANGBTC0
kind: definition
name: Isolated type
msc: ["03C07", "03C15"]
topics: [Z772KEC9BY]
audience: grad
defines: A0VNTN725W
uses: [9V71Q3SD1G, 92SWXST1ZM, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Omitting types theorem
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Definition

Let $T$ be an $L$-[[theory|92SWXST1ZM]], and let $p(x_1, \dots, x_n)$ be an $n$-[[type|9V71Q3SD1G]] of $T$.
An $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ *isolates* $p$ when the following two conditions hold.

1. $T \cup \set{\varphi}$ is satisfiable.
2. $T \models \forall \bar{x} \, (\varphi(\bar{x}) \to \psi(\bar{x}))$ for every $\psi \in p$.

The type $p$ is *isolated*, or *principal*, when some formula isolates it.
Otherwise $p$ is *non-isolated*, or *non-principal*.
For a type over a set $A$ of parameters in a structure $\mathcal{M}$, the same definition applies with $L_A$ and $T = \operatorname{Th}_A(\mathcal{M})$.

## Notation

When $p$ is complete and $\varphi$ isolates it, $\varphi$ is also called a complete formula of $T$.

## Remarks

A complete type $p$ is isolated by $\varphi$ exactly when $\varphi \in p$ and $p$ is the only complete type that contains $\varphi$.
So the isolated complete types are the isolated points of the Stone space $S_n(T)$.
The main page of the idea, with examples and properties, is [[isolated type|A0VNTN725W]].

Example: in the theory of dense linear orders without endpoints, $x_1 < x_2$ isolates the type of a pair $(a, b)$ with $a < b$.

Non-example: in the theory of $(\N, 0, 1, +, \cdot, <)$, the type $\set{\underline{k} < x : k \in \N}$ is not isolated.

## Explanations

### L1 human

A type is isolated when one consistent property implies all the properties in the type.

### L2 human

To prove that $\varphi$ isolates $p$, check the two conditions in order.

1. Find a model of $T$ with a tuple that satisfies $\varphi$.
2. Show, for each $\psi \in p$, that every tuple satisfying $\varphi$ in every model of $T$ also satisfies $\psi$.

The trap is to check only that $\varphi$ belongs to $p$: the formula $x = x$ belongs to every type and isolates almost none.
