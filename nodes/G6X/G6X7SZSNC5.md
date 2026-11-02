---
tag: G6X7SZSNC5
kind: concept
name: Second-order logic
msc: [03B16, 03C85]
specializes: [P1ABGYRQXH]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
same_as:
  wikidata: Q1548746
  wikipedia: Second-order logic
---

## Summary

Second-order logic extends [[first-order logic|086QKPF0A6]] with variables for relations and functions on the domain, and with quantifiers over them.
In its standard semantics these variables range over all relations and functions on the domain.
It can describe structures such as the natural numbers up to isomorphism, but it loses the completeness and compactness theorems of first-order logic.

## Explanations

### L1 human

First-order logic can say "for every number $x$", but not "for every set of numbers $X$".
Second-order logic can say both.
With it, the induction principle becomes one sentence: every set of numbers that contains $0$ and is closed under successor contains all numbers.
This one sentence, with the other Peano axioms, pins down the natural numbers completely.
The price is that no proof system can capture all its valid sentences.
