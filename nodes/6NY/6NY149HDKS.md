---
tag: 6NY149HDKS
kind: concept
name: Type inference
msc: [68N15, 68N18, 03B40]
uses: [AVVQEG0MRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Type_inference
same_as:
  wikidata: Q586459
  wikipedia: Type inference
---

## Summary

Type inference is the automatic computation of the type of a program that carries few or no type annotations.
A type checker only verifies a type the programmer wrote, while an inference algorithm finds a type, often the most general one.
It lets languages such as ML, OCaml and Haskell be statically typed without heavy annotations.
Whether inference is decidable depends strongly on the [[type system|AVVQEG0MRJ]]: it is decidable for simple types and undecidable for some richer systems.

## Explanations

### L1 human

When you write $\lambda x.\, x + 1$, a reader knows at once that $x$ must be a number and that the result is a number.
Type inference is a program that draws such conclusions for you.
It collects the constraints that each part of the program puts on the types, and then solves them.
For the term $\lambda x.\, \lambda y.\, x$ it finds the type $\alpha \to \beta \to \alpha$, where $\alpha$ and $\beta$ can be any types.
