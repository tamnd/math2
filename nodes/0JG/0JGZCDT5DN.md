---
tag: 0JGZCDT5DN
kind: example
name: Space of polynomials of bounded degree
msc: [15A03]
instance_of: [000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_ring
    locator: lead section
---

## Example

Let $F$ be a field and let $n \ge 0$ be an integer.
Let $F[x]_{<n}$ be the set of polynomials in $x$ with coefficients in $F$ and of degree less than $n$, with the zero polynomial included.
It is a [[vector space|000AYPA9AJ]] over $F$, with the usual addition of polynomials and multiplication by constants.
The monomials $1, x, x^2, \dots, x^{n-1}$ form a [[basis|0KCQ9Y3QKA]], so $\dim F[x]_{<n} = n$.

## Remarks

The set of polynomials of degree exactly $n$ is not a vector space.
It does not contain $0$, and it is not closed under addition.
The whole polynomial ring $F[x]$ is an infinite-dimensional vector space with basis $1, x, x^2, \dots$.
[[Differentiation|0SS770NS8B]] is a linear map from $F[x]_{<n}$ to $F[x]_{<n-1}$ for $n \ge 1$.

## Explanations

### L1 human

Polynomials of small degree can be added and scaled, and the result stays a polynomial of small degree.
So they form a vector space.
A polynomial $a_0 + a_1 x + a_2 x^2$ is the same data as the list $(a_0, a_1, a_2)$.
