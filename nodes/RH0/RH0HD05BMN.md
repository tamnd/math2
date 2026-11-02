---
tag: RH0HD05BMN
kind: concept
name: Order embedding
msc: [06A06]
specializes: [0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Order_embedding
same_as:
  wikidata: Q3796691
  wikipedia: Order embedding
---

## Summary

An order embedding is a map between [[partially ordered sets|011C29Q1S1]] that both preserves and reflects the order.
It places a copy of one poset inside another, with exactly the same comparisons.
An order embedding is automatically injective, and a surjective order embedding is an [[order isomorphism|0Y74KN99A5]].

## Explanations

### L1 human

An order embedding copies one ordered set into another without changing any comparison.
The map $n \mapsto 2n$ from the natural numbers to the natural numbers is an order embedding: $m \le n$ exactly when $2m \le 2n$.
The inclusion of the rationals into the reals is another one.
A map that only keeps "smaller" as "smaller", but can make incomparable elements comparable, is not an order embedding.
