---
tag: EDHK5KSGHY
kind: concept
name: Confluence
msc: [68Q42, 03B70]
sources:
  - url: https://en.wikipedia.org/wiki/Confluence_(abstract_rewriting)
same_as:
  wikidata: Q1140902
  wikipedia: Confluence (abstract rewriting)
---

## Summary

A [[rewriting system|Y83TQF6V6A]] is confluent when any two ways of rewriting an object can be continued so that they meet again.
Confluence implies that each object has at most one normal form.
So the result of a computation does not depend on the order of the steps.
It is equivalent to the Church–Rosser property: two objects are equivalent exactly when they rewrite to a common object.
Confluence of the lambda calculus is the [[Church–Rosser theorem|7NNF74EYDX]].

## Explanations

### L1 human

Imagine simplifying an expression where several simplification steps are possible.
Confluence means the choice never matters in the end: whatever two paths one takes, both can be continued to the same result.
For example, $(2 + 3) \cdot (1 + 1)$ can first become $5 \cdot (1 + 1)$ or $(2 + 3) \cdot 2$, and both lead to $10$.
Without confluence, two people simplifying the same expression could end with different answers.
