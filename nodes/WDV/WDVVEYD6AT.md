---
tag: WDVVEYD6AT
kind: concept
name: Signature
msc: [03C07, 03B10]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
same_as:
  wikidata: Q741810
  wikipedia: Signature (logic)
---

## Summary

A signature lists the non-logical symbols of a first-order language: function symbols, relation symbols and constant symbols, each with its number of arguments.
It fixes what one can talk about, before any axioms are chosen.
Terms, formulas and [[structures|983GZBQYT4]] are always taken over a given signature.
Another name is vocabulary, and in Mathlib it is called a first-order language.

## Explanations

### L1 human

Before writing axioms for groups, one has to say which symbols are allowed.
For groups, one may take a binary symbol $\cdot$, a unary symbol ${}^{-1}$ and a constant $e$.
This list of symbols with their numbers of arguments is the signature.
The axioms, such as associativity, come later and are not part of the signature.
