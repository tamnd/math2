---
tag: 06MRNP4BNT
kind: statement
role: theorem
name: Every spanning set contains a basis
msc: [15A03]
uses: [0VTQTPQGAV, 0BJKVF90Z6]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $S \subseteq V$ be a [[spanning set|088RYKAWK9]] of $V$.
Then there is a subset $B \subseteq S$ that is a [[basis|0KCQ9Y3QKA]] of $V$.

## Remarks

For finite $S$, remove from $S$, one at a time, a vector that is a linear combination of the other vectors.
When no such vector remains, the set is linearly independent and still spans $V$.
In general, take a maximal linearly independent subset of $S$, by Zorn's lemma.
For example, $\{(1, 0), (0, 1), (1, 1)\}$ spans $\R^2$ and contains the basis $\{(1, 0), (1, 1)\}$.

## Explanations

### L1 human

If a set of vectors reaches the whole space, then some part of it is a basis.
We throw away vectors that the others can already build.
When nothing redundant remains, the remaining vectors form a basis.
