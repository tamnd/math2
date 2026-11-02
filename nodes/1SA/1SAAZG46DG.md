---
tag: 1SAAZG46DG
kind: concept
name: Scott domain
msc: [06B35, 68Q55]
specializes: [7TSXP95QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Scott_domain
same_as:
  wikidata: Q7437566
  wikipedia: Scott domain
---

## Summary

A Scott domain is a directed-complete partial order that is algebraic and bounded complete.
Algebraic means that every element is the directed supremum of the [[compact elements|9F7TYES4KE]] below it.
Bounded complete means that every subset with an upper bound has a supremum.
They come from the work of Dana Scott on the semantics of programming languages and of the [[lambda calculus|BD756KR8FM]].
They form a cartesian closed category with Scott-continuous maps.

## Explanations

### L1 human

A Scott domain is a space of pieces of information in which every piece is a limit of finite pieces.
Two pieces that are consistent, meaning that some piece extends both, can always be combined into a least common extension.
The partial functions from $\N$ to $\N$ form a Scott domain, with the finite partial functions as compact elements.
Two partial functions that agree on their common domain combine by union.
Because maps between Scott domains again form a Scott domain, one can build domains of functions, of functions of functions, and so on.
