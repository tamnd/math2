---
tag: 43VFMJCDYJ
kind: concept
name: Schur polynomial
msc: ["05E05", "05E10"]
specializes: [0VHSHB9B6J]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_polynomial
same_as:
  wikidata: Q4298935
  wikipedia: Schur polynomial
---

## Summary

The Schur polynomial $s_\lambda(x_1, \ldots, x_n)$ is a [[symmetric polynomial|0VHSHB9B6J]] attached to an [[integer partition|0JV30XN73Z]] $\lambda$, see the [[definition|DA03KQ311J]].
It is a quotient of two alternating determinants, and it is also a sum over semistandard [[Young tableaux|Q6TH9PH2R7]] of shape $\lambda$.
For partitions $\lambda$ of $d$ with at most $n$ parts, the $s_\lambda$ form a basis of the degree-$d$ symmetric polynomials in $n$ variables.
They are the characters of the irreducible polynomial representations of $GL_n(\C)$, and their products are described by the [[Littlewood–Richardson rule|Q490XBH1Q2]].

## Explanations

### L1 human

Draw the [[Young diagram|096AHMB3P4]] of a partition, and fill its boxes with numbers from $1$ to $n$.
The numbers must weakly increase along rows and strictly increase down columns.
Each filling gives a monomial, with $x_i$ raised to the number of times $i$ appears.
The sum of these monomials is the Schur polynomial.
For one row of two boxes and $n = 2$ the fillings are $11$, $12$ and $22$, so $s_{(2)} = x_1^2 + x_1 x_2 + x_2^2$.
