---
tag: HYJ10AF6RT
kind: concept
name: Well-formed formula
msc: [03B10, 03B05]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
same_as:
  wikidata: Q655328
  wikipedia: Well-formed formula
---

## Summary

A well-formed formula, or simply formula, is a string of symbols built by the grammar of a formal language.
In first-order logic, formulas are built from atomic formulas with [[connectives|QS0XVAN9BG]] and quantifiers.
Formulas are the objects that proofs manipulate and that [[structures|983GZBQYT4]] make true or false.
Only well-formed strings have a meaning, so the definition is the first step of every formal logic.

## Explanations

### L1 human

Not every string of symbols makes sense: $\forall x \, (x < y)$ does, but $\forall \land x <$ does not.
The rules for formulas are like grammar rules for sentences.
They start with simple claims such as $x = y$ or $x < y$, and allow you to combine claims with "not", "and", "for all" and so on.
A formula with free variables, such as $x < y$, is true or false only once values for $x$ and $y$ are given.
