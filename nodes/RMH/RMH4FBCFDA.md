---
tag: RMH4FBCFDA
kind: concept
name: Hilbert polynomial
msc: [13D40, 13A02]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_series_and_Hilbert_polynomial
---

## Summary

Let $M$ be a finitely generated graded module over a [[polynomial ring|07GNX8GCYP]] over a field.
Its Hilbert polynomial gives the dimension of the degree $n$ part of $M$ for all large $n$.
Its existence is the [[Hilbert–Serre theorem|HP56DJECMT]].
For the coordinate ring of a projective variety, the degree of the Hilbert polynomial is the dimension of the variety.
Its leading coefficient encodes the degree of the variety.

## Explanations

### L1 human

Count how many independent homogeneous polynomials of degree $n$ survive on some shape.
For large $n$ this count follows a polynomial formula in $n$.
For a plane curve given by one equation of degree $d$, the count is $dn - d(d-3)/2$ for large $n$.
The growth rate of the count tells the dimension of the shape.
The leading coefficient tells its degree, the number of points in which it meets a general linear space of complementary dimension.
For instance, a plane curve of degree $d$ meets a general line in $d$ points.
The [[definition|5FR6JX04RS]] makes this precise.
