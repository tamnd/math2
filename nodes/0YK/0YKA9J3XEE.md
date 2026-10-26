---
tag: 0YKA9J3XEE
kind: statement
role: theorem
name: Hilbert's basis theorem
msc: ["13E05"]
uses: [0MVH4Y1CRZ, 0Q9EZS90GY, 0CES91M79A]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_basis_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_basis_theorem
    locator: lead section
same_as:
  wikidata: Q656645
  wikipedia: Hilbert's basis theorem
---

## Statement

Let $R$ be a [[Noetherian|0MVH4Y1CRZ]] [[commutative ring|0GYGHKX834]].
Then the [[polynomial ring|0Q9EZS90GY]] $R[x]$ is Noetherian.

## Remarks

By induction, $R[x_1, \dots, x_n]$ is Noetherian for every $n$. In particular, every ideal of $K[x_1, \dots, x_n]$ for a field $K$ is finitely generated.
The proof studies the ideals of the leading coefficients of the polynomials of each degree in an ideal of $R[x]$.
In algebraic geometry, the theorem says that every set of polynomial equations has the same solutions as a finite subset of it.

## History

David Hilbert proved the theorem in 1890, for polynomials in several variables over a field, in an article on invariant theory.
His proof was not constructive. It did not give a method to find the finite set of generators.

## Explanations

### L1 human

An ideal of polynomials can contain infinitely many polynomials.
The theorem says that a finite list of them always generates the whole ideal.
So every system of polynomial equations can be replaced by a finite one.
