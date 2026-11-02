---
tag: FF6XXA6D1A
kind: concept
name: Monad
msc: [18C15]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
same_as:
  wikidata: Q1630568
  wikipedia: Monad (category theory)
---

## Summary

A monad on a category is an endofunctor $T$ with a unit $\eta \colon \mathrm{Id} \Rightarrow T$ and a multiplication $\mu \colon T T \Rightarrow T$ that satisfy associativity and unit laws.
It is the categorical form of a monoid, with composition of [[functors|28NQ0KRHD3]] in place of multiplication.
Every pair of [[adjoint functors|TZHF6ZM92S]] gives a monad, and every monad comes from an adjunction.
Monads describe algebraic structure: groups, monoids, rings and many other algebraic categories are the algebras of a monad on sets.

## Explanations

### L1 human

Think of $T(X)$ as the set of formal expressions built from elements of $X$.
The unit turns an element into the simplest expression, the element itself.
The multiplication flattens an expression made of expressions into a single expression.
For example, let $T(X)$ be the set of finite lists of elements of $X$.
The unit sends $x$ to the one-element list $(x)$, and the multiplication concatenates a list of lists into one list.
