---
tag: MVYFSYMECG
kind: concept
name: Harmonic polynomial
msc: [31B05]
specializes: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_polynomial
same_as:
  wikidata: Q4133834
  wikipedia: Harmonic polynomial
---

## Summary

A harmonic polynomial is a polynomial in $n$ real variables whose Laplacian is the zero polynomial.
Harmonic polynomials are the simplest [[harmonic functions|0DEB0JMN0W]] on all of $\R^n$.
The homogeneous ones of degree $k$ form a finite-dimensional space, and their restrictions to the unit sphere are the [[spherical harmonics|3F32Y21HP4]].
Every harmonic function on a ball is a locally uniform limit of harmonic polynomials, so they play the role that monomials play for power series.

## Explanations

### L1 human

Take a polynomial such as $x^2 - y^2$ and add up its second derivatives in each variable: $2 - 2 = 0$.
When that sum is zero, the polynomial is called harmonic.
In the plane, the real and imaginary parts of $(x + iy)^k$ give two harmonic polynomials of each degree $k \ge 1$, for example $x^2 - y^2$ and $2xy$.
The polynomial $x^2 + y^2$ is not harmonic, since the sum of its second derivatives is $4$.
