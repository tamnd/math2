---
tag: GCPQGMJYEV
kind: concept
name: Skolem normal form
msc: [03B10]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
same_as:
  wikidata: Q1090524
  wikipedia: Skolem normal form
---

## Summary

A sentence is in Skolem normal form when it is in [[prenex normal form|CS82V969DE]] and has only universal quantifiers.
Every first-order sentence can be turned into one in Skolem normal form by replacing each existential quantifier with a new function symbol.
The new sentence is not equivalent to the old one, but it is satisfiable exactly when the old one is.
This makes Skolem normal form the starting point of [[Herbrand's theorem|VZ21F10WRS]] and of resolution theorem proving.

## Explanations

### L1 human

The sentence "for every $x$ there is a $y$ with $R(x, y)$" says that a suitable $y$ exists for each $x$.
Choose such a $y$ for each $x$ and call it $f(x)$.
Then the sentence becomes "for every $x$, $R(x, f(x))$", which has no "there exists".
The function $f$ is called a Skolem function.
