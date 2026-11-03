---
tag: GYMQHR3PXF
kind: concept
name: Normalization property
msc: [68Q42, 03B40]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting)
---

## Summary

A [[rewriting system|Y83TQF6V6A]] has the normalization property when every computation can end in a normal form, an object that cannot be rewritten further.
The weak form asks that some reduction path reaches a normal form; the strong form asks that every reduction path is finite.
Strong normalization is also called termination.
The untyped [[lambda calculus|BD756KR8FM]] is not normalizing, while the simply typed lambda calculus is strongly normalizing.

## Explanations

### L1 human

Think of a set of simplification rules, applied one at a time to an expression.
Weak normalization says: from any start, there is a way to keep simplifying until nothing more applies.
Strong normalization says: however you choose the rules, you always stop after finitely many steps.
For example, the rule "replace $aa$ by $a$" on strings is strongly normalizing, since each step shortens the string.
A rule such as "replace $a$ by $aa$" never stops, so it is not normalizing.
