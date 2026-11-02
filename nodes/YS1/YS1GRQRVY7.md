---
tag: YS1GRQRVY7
kind: concept
name: Nonlinear approximation
msc: [41A46, 41A25]
specializes: [YPJSH79SHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Summary

Nonlinear approximation approximates a function by elements of a set that is not a linear space.
A typical such set is the sums of $n$ terms chosen freely from a dictionary.
The approximant may adapt to the function, for example by placing spline knots or wavelets where the function is rough.
Typical cases are [[n-term approximation|GEK0NP5WQM]], [[rational approximation|EHFQK1WXKS]], splines with free knots and neural networks.
For functions with isolated singularities it can be much more efficient than linear approximation with the same number of parameters.

## Explanations

### L1 human

In linear approximation the building blocks are fixed in advance, for example the polynomials of degree at most $n$.
In nonlinear approximation one first looks at the function and then picks the building blocks that suit it best.
The set of all such choices is not closed under addition: the sum of two $n$-term sums can have $2n$ terms.
For example, to approximate a function that is smooth except for one jump, one can put many small wavelets near the jump and few elsewhere.
