---
tag: 4JKD5FBJCS
kind: concept
name: Knuth–Bendix completion
msc: [68Q42, 68V15, 03D03]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Knuth–Bendix_completion_algorithm
same_as:
  wikidata: Q2835803
  wikipedia: Knuth–Bendix completion algorithm
---

## Summary

Knuth–Bendix completion is a procedure that turns a set of equations into a [[term rewriting system|A6J731Y193]].
The rules of the result are oriented by a well-founded order, and the system is [[confluent|EDHK5KSGHY]].
It orients the equations into rules, looks for critical pairs where two rules overlap, and adds new rules until all overlaps resolve.
When it succeeds, every term has a unique normal form, and equality modulo the equations is decided by comparing normal forms.
It may also fail or run forever, as it must, since the [[word problem for groups|PBGTTAVMMT]] is undecidable in general.

## Explanations

### L1 human

Equations can be used in both directions, which makes it hard to tell whether two expressions are equal.
Knuth–Bendix completion tries to replace them by one-way simplification rules that always lead to the same simplest form.
Whenever two rules can act on the same expression and give different results, the procedure adds a rule that reconciles them.
For the axioms of a group it ends with ten rules, which simplify any expression in the group operations to a canonical form.
It resembles [[Buchberger's algorithm|4RH1D40WG1]] for polynomial ideals, where S-polynomials play the role of critical pairs.
