---
tag: BD756KR8FM
kind: concept
name: Lambda calculus
msc: [03B40, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/Lambda_calculus
same_as:
  wikidata: Q242028
  wikipedia: Lambda calculus
---

## Summary

The lambda calculus is a formal system for describing functions by abstraction and application, with computation done by substituting arguments into function bodies.
In its untyped form it computes exactly the same functions on natural numbers as [[Turing machines|758EYCN27B]].
It was introduced by Alonzo Church and is the basis of functional programming languages and of type theory.

## Explanations

### L1 human

In the lambda calculus, $\lambda x.\, M$ means "the function that sends $x$ to $M$".
To apply a function to an argument, one replaces the variable by the argument.
For example, $(\lambda x.\, x)\, y$ becomes $y$: the identity function applied to $y$ gives $y$.
Nothing else is built in, yet numbers, truth values and recursion can all be encoded as functions.
