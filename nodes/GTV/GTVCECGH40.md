---
tag: GTVCECGH40
kind: concept
name: Dunkl operator
msc: [33C52, "20F55", 33C80]
sources:
  - url: https://en.wikipedia.org/wiki/Dunkl_operator
same_as:
  wikidata: Q5315392
  wikipedia: Dunkl operator
---

## Summary

A Dunkl operator is a [[partial derivative|09EGC6F8PT]] plus a sum of difference terms, one for each reflection of a finite [[reflection group|G6FND7X69J]].
Charles Dunkl introduced these operators and proved that, for a fixed group and multiplicity function, they commute with each other.
They give a theory of special functions attached to root systems.
In it, Dunkl harmonics, the Dunkl transform and Dunkl kernels generalize spherical harmonics, the Fourier transform and the exponential.
They are also used to study the Calogero–Moser–Sutherland quantum systems, whose eigenfunctions in type $A$ are related to the [[Jack functions|WW7H1KNXK8]].

## Explanations

### L1 human

An ordinary derivative measures how a function changes along a direction.
A Dunkl operator adds to this the difference between the function and its mirror image in each mirror of a symmetry group, divided by the distance to that mirror.
On the real line with the single mirror $x \mapsto -x$, it is $T f(x) = f'(x) + k \frac{f(x) - f(-x)}{x}$.
It sends $x^2$ to $2x$, like the derivative, but sends $x^3$ to $(3 + 2k) x^2$.
