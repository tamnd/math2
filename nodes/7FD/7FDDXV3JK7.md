---
tag: 7FDDXV3JK7
kind: concept
name: Quantifier elimination
msc: [03C10]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
same_as:
  wikidata: Q1849020
  wikipedia: Quantifier elimination
---

## Summary

A theory has quantifier elimination when every formula is equivalent, modulo the theory, to a formula without quantifiers.
Then the definable sets of its models are simple to describe, and questions about the theory reduce to questions about quantifier-free formulas.
Quantifier elimination often gives completeness and decidability.
Classical examples are dense linear orders without endpoints, [[algebraically closed fields|MT8TDVPBXB]], and [[real closed fields|DDY3Q3PJ6W]] in the language of ordered rings.

## Explanations

### L1 human

Quantifiers are the words "for all" and "there exists".
A theory has quantifier elimination if every statement that uses them can be rewritten as a statement that does not use them.
The rewriting must keep the meaning in every model of the theory.
For example, over the real numbers, "there exists $x$ with $x^2 + bx + c = 0$" means the same as "$b^2 - 4c \ge 0$".
After the rewriting, one only has to check equations and inequalities about the given numbers.
