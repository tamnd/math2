---
tag: P0H5NYX8Z0
kind: concept
name: Henkin semantics
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
uses: [G6X7SZSNC5, KWEJFK5943]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Semantics
---

## Summary

The Henkin semantics reads the set quantifiers of [[second-order logic|G6X7SZSNC5]] in a weaker way.
In return, it gets back the good theorems of first-order logic.
In the full semantics, "for every set $X$" means every subset of the domain.
In the Henkin semantics, each model comes with its own family of allowed sets, and "for every set $X$" means every set in that family.

A general structure is an $L$-structure with domain $M$ together with a family $D_n \subseteq \mathcal{P}(M^n)$ for each arity $n \ge 1$.
The $n$-ary relation variables range over $D_n$.
A Henkin model is a general structure that satisfies every instance of the comprehension schema.
So every relation that a formula defines is in the family.
The [[definition page|KWEJFK5943]] gives the exact clauses.

## Motivation

The full semantics of second-order logic has no complete effective proof system, and it is not compact.
Henkin asked which models make the usual rules for the second-order quantifiers complete.
His answer was to make the range of each relation quantifier a part of the model, just as the range of the individual quantifiers already is.
Then a Henkin model is a many-sorted first-order structure in disguise.
So the completeness theorem, the compactness theorem and the Löwenheim-Skolem theorem all hold again.
The price is that the categoricity results of the full semantics fail, and second-order Peano arithmetic gets non-standard models.

## Remarks

### A small comparison

Take the domain $M = \set{0, 1}$ and the sentence $\forall X \, \forall x \, \forall y \, (X(x) \to X(y))$.
In the full structure, $X$ can be $\set{0}$, and with $x = 0$ and $y = 1$ the sentence is false.
In a general structure with $D_1 = \set{\emptyset, M}$, each allowed set contains both points or neither, so the sentence is true.
This general structure is not a Henkin model, because comprehension for $x = y$ with the parameter $y = 0$ asks for $\set{0}$.
On a finite domain every Henkin model is full, so this kind of difference needs an infinite domain in a Henkin model.

## Explanations

### L1 human

In the full semantics, "for every set" means every set that exists.
In the Henkin semantics, each model gives its own list of allowed sets, and "for every set" means every set on the list.
The list must contain each set that the language can describe.
For example, if the language can say "is even", then the set of even elements must be on the list.
With these lists, second-order logic behaves like first-order logic, and a computer can list all of its valid sentences.
