---
tag: 73RYYEVDKA
kind: concept
name: Flat module
msc: [13C11, 16D40]
specializes: [0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Flat_module
same_as:
  wikidata: Q1426191
  wikipedia: Flat module
---

## Summary

A flat module is a module $M$ such that tensoring with $M$ keeps injective linear maps injective.
Equivalently, the functor $- \otimes_R M$ preserves [[exact sequences|JB7ZBFBA9C]].
Free and [[projective modules|BFFA03GE3V]] are flat, and so are [[localizations|4C1AE84N5N]] such as $\Q$ over $\Z$.
Flatness is the algebraic form of "varying continuously in a family".
Flat ring maps are the basic tool of descent and base change in algebraic geometry.

## Explanations

### L1 human

Tensoring with a module is a way to change the ring of scalars or to combine two modules.
In general this operation can collapse things: a nonzero map may become zero.
A flat module never causes such a collapse of injective maps.
For example, $\Z/2\Z$ is not flat over $\Z$: the injective map "multiply by $2$" on $\Z$ becomes the zero map on $\Z/2\Z$.
