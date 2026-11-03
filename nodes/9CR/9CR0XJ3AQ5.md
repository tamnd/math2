---
tag: 9CR0XJ3AQ5
kind: definition
name: Lie coalgebra
msc: [17B62]
defines: J48KPHCC2E
uses: [000AYPA9AJ, 0BF2DE2SYK, 07JBSZE0V4, 5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_coalgebra
---

## Definition

Let $E$ be a [[vector space|000AYPA9AJ]] over a field $k$.
Let $\tau \colon E \otimes E \to E \otimes E$ be the flip $a \otimes b \mapsto b \otimes a$, and let $\sigma \colon E^{\otimes 3} \to E^{\otimes 3}$ be the cyclic permutation $a \otimes b \otimes c \mapsto c \otimes a \otimes b$, on [[tensor products|0BF2DE2SYK]] over $k$.
A *Lie coalgebra* structure on $E$ is a linear map $\delta \colon E \to E \otimes E$, the cobracket, such that:

1. $\tau \circ \delta = -\delta$ (antisymmetry);
2. $(\id + \sigma + \sigma^2) \circ (\delta \otimes \id) \circ \delta = 0$ (co-Jacobi identity).

## Remarks

Example: let $\mathfrak{g}$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] and $E = \mathfrak{g}^*$ its [[dual space|07JBSZE0V4]].
Identify $E \otimes E$ with the bilinear forms on $\mathfrak{g}$, and set $\delta(\xi)(x, y) = \xi([x, y])$.
Antisymmetry of $\delta$ follows from $[y, x] = -[x, y]$, and the co-Jacobi identity is the Jacobi identity of $\mathfrak{g}$ read through $\xi$.
Conversely, for a finite-dimensional Lie coalgebra $E$, the transpose of $\delta$ is a Lie bracket on $E^*$, so the two notions are dual to each other.

Non-example: $E = k$ with $\delta(1) = 1 \otimes 1$ fails clause 1, since $\tau(1 \otimes 1) = 1 \otimes 1 \neq -1 \otimes 1$ when the characteristic of $k$ is not $2$.

Since $\delta$ is antisymmetric, one can view it as a map $E \to \Lambda^2 E$ in characteristic not $2$.
