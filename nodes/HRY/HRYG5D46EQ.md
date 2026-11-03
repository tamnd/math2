---
tag: HRYG5D46EQ
kind: concept
name: Steinberg symbol
msc: [19C20, 19F15]
sources:
  - url: https://en.wikipedia.org/wiki/Steinberg_symbol
same_as:
  wikidata: Q7606831
  wikipedia: Steinberg symbol
---

## Summary

A Steinberg symbol on a field $F$ is a map from pairs of nonzero elements of $F$ to an abelian group.
It is multiplicative in each variable, and it kills every pair $(a, 1 - a)$.
Hilbert symbols, norm residue symbols and tame symbols are all Steinberg symbols.
By Matsumoto's theorem there is a universal one, with values in $K_2(F)$, so every Steinberg symbol factors through $K_2(F)$.

## Explanations

### L1 human

Number theory has many symbols that take two numbers and return a sign or a root of unity, such as the Hilbert symbol.
They share two rules: they behave like a product in each entry, and they give $1$ on a pair of numbers that add up to $1$.
A Steinberg symbol is any function with these two rules.
For example, on the real numbers, the rule that gives $-1$ when both numbers are negative and $1$ otherwise is a Steinberg symbol.
