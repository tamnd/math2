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

The Henkin semantics of [[second-order logic|G6X7SZSNC5]] evaluates formulas in general structures: an $L$-structure with domain $M$ together with a family $D_n \subseteq \mathcal{P}(M^n)$ for each arity $n \ge 1$, over which the $n$-ary relation variables range.
The models of the semantics are the general structures that satisfy every instance of the comprehension schema; the [[definition page|KWEJFK5943]] gives the details.
The Henkin semantics matters because it gives second-order logic a complete proof system, compactness and the Löwenheim-Skolem theorem, at the price of non-standard models.

## Motivation

The full semantics of second-order logic has no complete effective proof system.
Henkin asked which models make the usual rules for second-order quantifiers complete.
The answer is to let the range of each relation quantifier be a part of the model, as the range of the individual quantifiers already is.

## Explanations

### L1 human

In the full semantics, "for every set" means every set that exists.
In the Henkin semantics, each model gives its own list of allowed sets, and "for every set" means every set on the list.
The list must contain each set that the language can describe.
