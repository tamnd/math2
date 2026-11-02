---
tag: 9W77FPTM9E
kind: concept
name: Newton polynomial
msc: [65D05, 41A05]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_polynomial
same_as:
  wikidata: Q2746387
  wikipedia: Newton polynomial
---

## Summary

The Newton polynomial is the [[interpolation polynomial|SS1YMS2NPC]] of given data written in the Newton form.
The basis is $1$, $(x - x_0)$, $(x - x_0)(x - x_1)$, and so on, and the coefficients are [[divided differences|N5ZHV4HWDC]].
Adding one more data point adds one more term and leaves the earlier terms unchanged.
This makes the Newton form convenient for computation and for deriving error terms and finite difference formulas.

## Explanations

### L1 human

Start with the constant through the first point.
Add a multiple of $(x - x_0)$ to also pass through the second point; this does not change the value at $x_0$.
Then add a multiple of $(x - x_0)(x - x_1)$ to pass through the third point, without disturbing the first two.
For the points $(0, 1)$, $(1, 3)$, $(2, 7)$ this gives $1 + 2x + x(x - 1) = x^2 + x + 1$.
The [[definition|155K06F4JF]] gives the general formula.
