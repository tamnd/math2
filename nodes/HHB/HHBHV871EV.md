---
tag: HHBHV871EV
kind: definition
name: Parametricity
msc: [68N18, 68Q55, 03B40]
defines: 67YR9SNGTX
uses: [SVNYKTGQ48, 05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Parametricity
---

## Definition

Let $\tau$ be a type built from one type variable $\alpha$ and some fixed base types, such as the booleans, with the arrow $\to$.
For a set $A$, write $\tau(A)$ for the set obtained by reading $\alpha$ as $A$ and each base type as its set of values.
Here $\sigma_1 \to \sigma_2$ is read as the set of all functions from $\sigma_1(A)$ to $\sigma_2(A)$.
A *polymorphic value* of type $\forall \alpha.\, \tau$ is a family $p = (p_A)$ with $p_A \in \tau(A)$ for every set $A$.
For sets $A, B$ and a [[binary relation|05AVARPXA2]] $R \subseteq A \times B$, the *relational interpretation* $\tau[R] \subseteq \tau(A) \times \tau(B)$ is defined by induction on $\tau$.

1. For $\tau = \alpha$, the relation is $R$.
2. For a base type, the relation is equality.
3. For $\tau = \tau_1 \to \tau_2$, functions $f$ and $g$ are related if $f(a)$ and $g(b)$ are related by $\tau_2[R]$ whenever $a$ and $b$ are related by $\tau_1[R]$.

The polymorphic value $p$ is *parametric* if $p_A$ and $p_B$ are related by $\tau[R]$ for all sets $A$, $B$ and all relations $R \subseteq A \times B$.

## Remarks

Example: let $p$ be a parametric value of type $\forall \alpha.\, \alpha \to \alpha$, let $A$ be a set and $a \in A$.
Take $B = A$ and the relation $R = \set{(a, a)}$.
Clause 3 gives that $p_A(a)$ and $p_A(a)$ are related by $R$, so $p_A(a) = a$, and $p_A$ is the identity on $A$.

Non-example: let $q_A$ be the swap of $\mathsf{true}$ and $\mathsf{false}$ when $A$ is the set of booleans, and the identity on every other set $A$.
This is a family of maps $A \to A$, but it is not parametric.
With $A = \set{0, 1}$, $B$ the booleans and $R = \set{(0, \mathsf{false}), (1, \mathsf{true})}$, clause 3 fails: $0$ and $\mathsf{false}$ are related, but $q_A(0) = 0$ and $q_B(\mathsf{false}) = \mathsf{true}$ are not.
Such a family cannot be written as a term of System F, since a term cannot test which type it is applied to.

For a function $h \colon A \to B$, taking $R$ to be the graph of $h$ turns the relational statement into an equation, which is how the free theorems are read off.
For all of [[System F|SVNYKTGQ48]], with nested quantifiers and several type variables, the relational interpretation has one more clause.
Values of $\forall \beta.\, \tau_1$ are related if, for all $A$, $B$ and $S \subseteq A \times B$, their instances at $A$ and $B$ are related by the interpretation of $\tau_1$ at $S$.
Reynolds showed that System F has no model in which types are plain sets and $\forall$ ranges over all sets.
So this general form is used in other models, such as models built from partial equivalence relations, or in a syntactic form.
Reynolds' abstraction theorem says that every closed term of System F is parametric in this sense.
