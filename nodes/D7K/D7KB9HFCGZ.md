---
tag: D7KB9HFCGZ
kind: concept
name: Countable additivity
msc: [28A10]
sources:
  - url: https://en.wikipedia.org/wiki/Sigma-additive_set_function
same_as:
  wikidata: Q709149
  wikipedia: Sigma-additive set function
---

## Summary

A set function is countably additive, or σ-additive, if its value on a countable disjoint union is the sum of its values on the pieces.
Countable additivity is the defining property of measures.
It is stronger than finite additivity, and it is what makes limit theorems such as monotone convergence work.

## Explanations

### L1 human

Countable additivity says that sizes add up even when a set is cut into infinitely many pieces, as long as there are only countably many.
For example, $[0, 1)$ is the disjoint union of $[1 - 2^{-n+1}, 1 - 2^{-n})$ for $n \ge 1$, of lengths $1/2, 1/4, 1/8, \ldots$.
These lengths add up to $1$, the length of $[0, 1)$.
Without this rule, one could not pass to limits when computing sizes.
