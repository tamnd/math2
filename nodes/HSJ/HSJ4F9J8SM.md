---
tag: HSJ4F9J8SM
kind: concept
name: Atomic model
aliases: [atomic-model, atomic-structure]
msc: ["03C50", "03C15"]
topics: [6XEXRME4C1]
audience: grad
uses: [9V71Q3SD1G, 7MFGBVDVG9, 655K8Y7VS8, MVCH6N9SNW, QC9M3Q8B8Q, ZV38HA5PAQ, 0A1YXSKB48]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_model_(mathematical_logic)
  - book: isbn:9780387987606
  - book: isbn:9780521587136
---

## Summary

Let $T$ be a [[complete theory|655K8Y7VS8]] in a countable signature $L$.
A complete $n$-[[type|9V71Q3SD1G]] $p(\bar x)$ of $T$ is *isolated* when some formula $\varphi(\bar x)$, consistent with $T$, implies every formula of $p$ modulo $T$, as in the [[omitting types theorem|7MFGBVDVG9]].
Such a $\varphi$ is called a *complete formula*: for every formula $\psi(\bar x)$, $T$ proves $\varphi \to \psi$ or $\varphi \to \neg\psi$.
A [[model|MVCH6N9SNW]] $M$ of $T$ is *atomic* when every finite tuple of $M$ realizes an isolated type.
So in an atomic model each tuple is described, up to all first-order properties, by one formula.
The countable atomic models are exactly the [[prime models|S8W40PYNHX]] of $T$, and they are unique up to isomorphism.

## Motivation

An isolated type is realized in every model of $T$: if $\varphi$ isolates $p$, then $T$ proves $\exists \bar x \, \varphi(\bar x)$, because $T$ is complete, and a witness realizes $p$.
A non-isolated type can be omitted in some countable model.
An atomic model realizes only the types that every model must realize.
This makes atomic models the natural candidates for the smallest models of $T$, the ones that embed elementarily into all others.

## Notation

For a tuple $\bar a$ of $M$, write $\operatorname{tp}^M(\bar a)$ for its complete type over the empty set.
Let $B_n(T)$ be the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of formulas in $x_1, \dots, x_n$ modulo $T$.
A complete formula is an atom of $B_n(T)$, which is the source of the name.
The complete $n$-types of $T$ form $S_n(T)$, the [[Stone space|ZV38HA5PAQ]] of $B_n(T)$.
A type is isolated exactly when it is an [[isolated point|0A1YXSKB48]] of $S_n(T)$.

## Remarks

### Examples

- The field of algebraic numbers is an atomic model of the theory of algebraically closed fields of characteristic $0$; see [[this example|NS2NZRZXJB]].
- Every model of the theory of dense linear orders without endpoints is atomic, including $\R$; see [[this example|CWZ3T8F542]].
- Every model of an $\aleph_0$-categorical theory is atomic, because by the [[Ryll-Nardzewski theorem|1513J40TKA]] all types of such a theory are isolated.

### Non-examples

- The complex field is not atomic: a transcendental element realizes a type that is not isolated; see [[this non-example|GPMKBKJ4A7]].
- In $\operatorname{Th}(\Z, <)$, the type of a pair $a < b$ with infinitely many elements between them is omitted by $\Z$, so it is not isolated. So $\Z + \Z$, which realizes it, is not atomic.
- The theory of [[independent unary predicates|9MV9VG8G67]] has no isolated $1$-types, so it has no atomic model at all.

### Basic properties

- An elementary substructure of an atomic model is atomic, since a tuple has the same type in both.
- If $L$ is countable, every prime model is atomic, and a countable atomic model is prime; see [[this theorem|EXC8913GGX]].
- Two countable atomic models of $T$ are isomorphic, by a back-and-forth argument.
- $T$ has an atomic model exactly when the isolated types are dense in each $S_n(T)$; see [[this theorem|MXVGKQ783S]]. This holds when each $S_n(T)$ is countable, that is, when $T$ is [[small|W6XM5NVNRP]].

### History

Atomic and prime models were developed together in the study of countable models of complete theories.
The name refers to atoms of the Lindenbaum-Tarski algebra.

### Common errors

- An atomic model has nothing to do with atomic formulas. A model is atomic because of its types, not because of the shape of its axioms.
- Isolation is defined over the empty set and relative to the complete theory $T$, not relative to one model.
- An uncountable atomic model need not be prime: $(\R, <)$ is atomic for the theory of dense linear orders, but it does not embed into $(\Q, <)$.
- An atomic model does not make every type isolated. The algebraic numbers form an atomic model, while the type of a transcendental element is not isolated; the atomic model simply omits it.

## Explanations

### L1 human

In an atomic model, every finite list of elements can be pinned down by a single property written in the language.
For example, in the field of algebraic numbers, $\sqrt{2}$ is pinned down, up to all first-order facts, by "$x^2 = 2$".
A transcendental number such as $\pi$ cannot be pinned down by one equation, so the complex field is not atomic.
Atomic models contain only elements that the theory is forced to have.

### L2 human

We check that $(\Q, <)$ is atomic for the theory $T$ of dense linear orders without endpoints.

1. Let $\bar a = (a_1, \dots, a_n)$ be a tuple of rationals. Let $\varphi(\bar x)$ be the conjunction of the formulas $x_i < x_j$ and $x_i = x_j$ that hold of $\bar a$.
2. Suppose that $\bar b$ in a model $N$ satisfies $\varphi$. Let $N_0$ be a countable elementary substructure of $N$ containing $\bar b$. Back-and-forth extends the order-preserving map $\bar a \mapsto \bar b$ to an isomorphism from $\Q$ onto $N_0$, so $\operatorname{tp}(\bar a) = \operatorname{tp}(\bar b)$.
3. So $\varphi$ isolates $\operatorname{tp}^{\Q}(\bar a)$, and $(\Q, <)$ is atomic.

The typical use is to recognize the prime model: find a countable model in which every tuple is isolated.
A trap is to check only $1$-types; atomicity is about tuples of every length.

### L3 human

In the Stone space $S_n(T)$, an atomic model exists exactly when the isolated points are dense.
The proof omits the closed set of non-isolated types, which is nowhere dense, so it is a Baire category argument.
Prime models over sets, defined with types over the set, play the same role in stability theory.
