---
tag: 2HWVFHM13R
kind: concept
name: Infinite product measure
msc: [28A35, 60A10]
specializes: [77PV0ZAVXT]
sources:
  - url: https://en.wikipedia.org/wiki/Product_measure
---

## Summary

Take a family of [[probability measures|059TJN0NZ1]].
Its infinite product measure is the probability measure on the product space under which the coordinates are independent with the given laws.
It is defined on the [[product σ-algebra|6HVCTJGB61]] and is determined by its values on cylinder sets.
It exists for every family of probability spaces, with an arbitrary index set.
It is the model for infinite sequences of independent trials, such as repeated coin tossing.

## Explanations

### L1 human

Imagine tossing a fair coin forever.
An outcome is an infinite sequence of heads and tails.
The infinite product measure says how likely a set of such sequences is: for example, the sequences that start with heads, tails, heads have probability $\tfrac18$.
Only probability measures are used, because a product of infinitely many total masses must make sense, and $1 \cdot 1 \cdot 1 \cdots = 1$.
