---
tag: NNPHTWF645
kind: concept
name: Resultant
msc: [13P15, "12E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Resultant
same_as:
  wikidata: Q1168321
  wikipedia: Resultant
---

## Summary

The resultant of two polynomials is a polynomial expression in their coefficients that, for nonzero leading coefficients, vanishes exactly when they have a common root.
It is the [[determinant|00KDZRW4C0]] of the Sylvester matrix built from the coefficients.
It lets one decide whether two polynomial equations have a common solution without solving them.
The [[discriminant|0VVK64Q4JK]] of $f$ is, up to a simple factor, the resultant of $f$ and its derivative.

## Explanations

### L1 human

Two polynomials either share a root or they do not.
The resultant is a single number, computed from the coefficients alone, that is zero in the first case and nonzero in the second.
For $x - a$ and $x - b$ the resultant is $a - b$, which is zero exactly when the two roots agree.
The [[definition|8D277VG29T]] gives the matrix.
