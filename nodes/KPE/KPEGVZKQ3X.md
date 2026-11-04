---
tag: KPEGVZKQ3X
kind: concept
name: Refinement type
aliases: [refined-type, refinement-types]
sources:
  - wikipedia: en:24449039@r1322834676
    locator: Refinement type
    note: adopted
    mention: wikipedia://en/24449039
    sections: [Summary]
same_as:
  wikidata: Q56273805
  wikipedia: Refinement type
inventory: [Q1BNRVC6HR]
---

## Summary

In type theory, a **refinement type** is a type endowed with a predicate which is assumed to hold for any element of the refined type. Refinement types can express preconditions when used as function arguments or postconditions when used as return types: for instance, the type of a function which accepts natural numbers and returns natural numbers greater than 5 may be written as $f: \mathbb{N} \rightarrow \{n \in \mathbb{N} \, | \, n > 5\}$. Refinement types are thus related to behavioral subtyping.
