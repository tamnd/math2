---
tag: 4SPC17FPXE
kind: concept
name: Jones polynomial
msc: [57K14]
specializes: [GZQ5ZE3X6G]
sources:
  - url: https://en.wikipedia.org/wiki/Jones_polynomial
same_as:
  wikidata: Q1528291
  wikipedia: Jones polynomial
---

## Summary

The Jones polynomial is an invariant of oriented [[links|1A5WRCNTM3]] with values in Laurent polynomials in $t^{1/2}$.
Vaughan Jones discovered it in 1984 through operator algebras.
It can be computed from any diagram by a skein relation or by the [[Kauffman bracket|JYKVYS4N32]].
Unlike the [[Alexander polynomial|JKA25KDPQP]], it distinguishes many knots from their mirror images, such as the two trefoils.

## Explanations

### L1 human

The Jones polynomial turns a knot drawing into a polynomial, and different drawings of the same knot give the same answer.
You compute it by undoing crossings one at a time with a fixed rule, the skein relation.
The plain circle gets the value $1$.
One trefoil gets $t + t^3 - t^4$ and its mirror image gets $t^{-1} + t^{-3} - t^{-4}$.
So the left-handed and right-handed trefoils are different knots.
It is still unknown whether a nontrivial knot can have Jones polynomial $1$.
