---
tag: NTJ94H2CNS
kind: concept
name: Lawvere theory
msc: ["18C10", "08C05"]
specializes: [A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Lawvere_theory
same_as:
  wikidata: Q6505076
  wikipedia: Lawvere theory
---

## Summary

A Lawvere theory is a category with finite products whose objects are the natural numbers, where $n$ is the $n$-th power of $1$.
Its morphisms $n \to 1$ play the role of the $n$-ary operations of an algebraic theory.
They are closed under composition and identified modulo the equations of the theory.
Models are finite-product-preserving functors to $\mathbf{Set}$, and the models of the theory of a [[variety|AJNZJD8442]] form a category equivalent to the variety.
Lawvere theories give a presentation-free description of varieties, so that different choices of operations and axioms for the same variety give the same theory.

## Explanations

### L1 human

The theory of groups can be written with multiplication, inverse and identity, or with division alone, and the two descriptions look different.
A Lawvere theory removes this choice.
It collects all operations that can be built from the basic ones, such as $(x, y) \mapsto x y^{-1} x$, and identifies two of them when they agree in every group.
These operations, with their composition, form a category, and a group is then a way to interpret this category by sets and functions.
