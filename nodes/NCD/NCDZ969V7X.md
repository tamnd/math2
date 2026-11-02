---
tag: NCDZ969V7X
kind: concept
name: Substitution
msc: [03B10, 08B05]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_(logic)
same_as:
  wikidata: Q1522579
  wikipedia: Substitution (logic)
---

## Summary

A substitution replaces each variable of a [[term|6D3WA7N2W4]] by another term, all at the same time.
It is the syntactic counterpart of plugging values into a formula.
Substitution is one of the rules of equational logic, and it is the basic operation of unification and term rewriting.

## Explanations

### L1 human

Take the term $x + y$ and replace $x$ by $z \cdot z$ and $y$ by $1$.
The result is the term $z \cdot z + 1$.
All variables are replaced at once, so substituting $x \mapsto y$ and $y \mapsto x$ in $x + y$ gives $y + x$, not $x + x$.
A law such as $x + y \approx y + x$ stays true after any substitution, which is why laws can be applied to arbitrary expressions.
