---
tag: 0RBT5PB74K
kind: statement
role: theorem
name: "Bessel's inequality"
msc: [46C05]
uses: [09VYHEF2VT, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel's_inequality
    locator: Statement of the inequality
same_as:
  wikidata: Q794042
  wikipedia: "Bessel's inequality"
---

## Statement

Let $V$ be an inner product space over $\R$ or $\C$, with the [[induced norm|0MFJJV97RJ]] $\norm{\cdot}$.
Let $e_1, \dots, e_k$ be an [[orthonormal family|0RW9TNNT87]] in $V$.
Then, for each $x \in V$,
$$\sum_{i=1}^{k} \abs{\langle x, e_i \rangle}^2 \le \norm{x}^2.$$

## Remarks

The proof applies the Pythagorean theorem to $x = \sum_i \langle x, e_i \rangle e_i + r$, where $r$ is orthogonal to each $e_i$.
Equality holds if and only if $x$ lies in the span of $e_1, \dots, e_k$.
The inequality also holds for infinite orthonormal families, with a series on the left.

## Explanations

### L1 human

The squared lengths of the projections of a vector onto perpendicular directions add up to at most its squared length.
The missing part is the squared length of the component outside these directions.
If the directions span the whole space, then nothing is missing.
