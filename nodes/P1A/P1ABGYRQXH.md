---
tag: P1ABGYRQXH
kind: concept
name: Higher-order logic
msc: [03B16]
sources:
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
same_as:
  wikidata: Q1644136
  wikipedia: Higher-order logic
---

## Summary

Higher-order logic extends [[first-order logic|086QKPF0A6]] with variables, and quantifiers, for relations on elements, relations on such relations, and so on at every finite level.
Each variable carries a type that says at which level it lives.
It is the logic behind simple type theory and several proof assistants, such as Isabelle/HOL.

## Explanations

### L1 human

First-order logic talks about objects.
Second-order logic also talks about sets of objects.
Third-order logic adds sets of sets of objects, and higher-order logic allows every finite level of this hierarchy.
For example, "every collection of sets of numbers has a union" quantifies over collections of sets, so it is a third-order statement.
