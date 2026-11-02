---
tag: 3YYKGWJJND
kind: concept
name: Term algebra
msc: [08B20, 08A40]
sources:
  - url: https://en.wikipedia.org/wiki/Term_algebra
same_as:
  wikidata: Q21998744
  wikipedia: Term algebra
---

## Summary

The term algebra over a set of variables is the algebra whose elements are the [[terms|6D3WA7N2W4]] themselves.
Its operations build bigger terms from smaller ones.
It is the absolutely free algebra on the variables.
Every map from the variables into an algebra of the same signature extends to a unique homomorphism, given by [[term evaluation|DH30WTA26T]].
All free algebras of varieties are quotients of term algebras, and the syntax of equational logic lives in it.

## Explanations

### L1 human

In a term algebra, nothing is simplified.
With one binary symbol $\cdot$ and variables $x, y$, the elements are expressions such as $x$, $x \cdot y$, $(x \cdot y) \cdot x$ and $x \cdot (y \cdot x)$.
Two expressions are equal only if they are written the same way, so $(x \cdot y) \cdot x$ and $x \cdot (y \cdot x)$ are different elements.
The operation simply puts two expressions side by side with the symbol between them.
