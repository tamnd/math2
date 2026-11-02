---
tag: Q48KGV33AH
kind: concept
name: Type theory
msc: ["03B38", "03B16"]
uses: [0HESMMSYEG, 0BSJ7RQ9BW]
sources:
  - url: https://en.wikipedia.org/wiki/Type_theory
same_as:
  wikidata: Q1056428
  wikipedia: Type theory
---

## Summary

A type theory is a formal system in which every term has a type.
Its rules say which terms can be formed in which types.
Russell introduced a theory of types to avoid [[Russell's paradox|0HESMMSYEG]], by forbidding a collection to contain objects of its own level.
Church's simple type theory of 1940 and Martin-Löf's intuitionistic type theory are the main later systems.
Type theories serve as foundations of mathematics alternative to set theory, and as the basis of programming languages and proof assistants.

## Explanations

### L1 human

In a type theory, everything comes with a label, its type, such as "natural number" or "function from numbers to numbers".
You may only apply a function to an argument of the right type.
So the expression $f(f)$, which feeds a function to itself, is not allowed for a function $f \colon \N \to \N$.
This simple discipline blocks the paradoxes of naive [[set|0BSJ7RQ9BW]] theory.
It also catches many errors in computer programs before they run.
