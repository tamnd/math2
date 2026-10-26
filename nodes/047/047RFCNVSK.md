---
tag: 047RFCNVSK
kind: statement
role: theorem
name: "Parseval's identity"
msc: [46C05]
uses: [0FWJ0VW561, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Parseval's_identity
    locator: lead section
same_as:
  wikidata: Q944238
  wikipedia: "Parseval's identity"
---

## Statement

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0S9GGTR0EX]] of $V$.
Then, for all $x, y \in V$,
$$\langle x, y \rangle = \sum_{i=1}^{n} \langle x, e_i \rangle \overline{\langle y, e_i \rangle} \qquad \text{and} \qquad \norm{x}^2 = \sum_{i=1}^{n} \abs{\langle x, e_i \rangle}^2.$$

## Remarks

It is the case of equality in [[Bessel's inequality|0RBT5PB74K]].
In coordinates of an orthonormal basis, the inner product becomes the standard inner product of $\mathbb{K}^n$.
For Fourier series, the same identity holds with infinite sums, for square integrable functions.

## Explanations

### L1 human

In an orthonormal basis, the inner product of two vectors is the standard inner product of their coordinates.
In particular, the squared length is the sum of the squared coordinates.
This is the Pythagorean theorem in $n$ dimensions.
