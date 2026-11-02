---
tag: 72S3YSQFZ7
kind: concept
name: Equational logic
msc: [08B05, 03B10]
sources:
  - url: https://en.wikipedia.org/wiki/Equational_logic
same_as:
  wikidata: Q5384236
  wikipedia: Equational logic
---

## Summary

Equational logic is the fragment of first-order logic whose statements are [[identities|PKD440G2XW]] between terms and whose proofs use only equational reasoning.
Its rules are reflexivity, symmetry, transitivity, replacement of equals inside an operation, and [[substitution|NCDZ969V7X]] of terms for variables.
By Birkhoff's completeness theorem these rules derive exactly the identities that follow semantically from a given set of identities.
It is the logic of algebraic manipulation, and it underlies term rewriting and automated equational reasoning.

## Explanations

### L1 human

Equational logic is the logic of high school algebra.
You start from some laws, such as $x + 0 \approx x$ and $x + y \approx y + x$.
You may plug any expressions into a law, replace equals by equals inside a bigger expression, and chain equalities together.
For example, from these two laws one derives $0 + x \approx x + 0$ by substituting into commutativity, and then $0 + x \approx x$ by transitivity.
