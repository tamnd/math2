---
tag: Q80JWCWNKX
kind: concept
name: Inductive type
msc: [03B38, 68N15]
uses: [Q48KGV33AH, 0ASJVEFA9J, DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Inductive_type
same_as:
  wikidata: Q17092426
  wikipedia: Inductive type
---

## Summary

An inductive type is a type given by a list of constructors.
Its elements are exactly the values built by finitely many uses of these constructors.
The natural numbers, with the constructors zero and successor, are the basic example; lists and trees are others.
Each inductive type comes with a principle of recursion and of [[induction|0ASJVEFA9J]] that defines functions and proves statements by cases on the constructors.
Inductive types are the main way to introduce data in [[type theories|Q48KGV33AH]] such as Martin-Löf type theory and the calculus of inductive constructions.

## Explanations

### L1 human

To describe the natural numbers, it is enough to say: $0$ is a natural number, and if $n$ is one, so is $n + 1$.
An inductive type is a type described in this way, by the ways of building its elements.
Nothing else belongs to it, which is why one can prove a statement for all its elements by checking each way of building them.
A list of numbers is built in the same way: it is either empty, or a number put in front of a shorter list.
In terms of sets, the type is the [[least fixed point|DBD64TH52D]] of its construction rules.
