---
tag: 7WEM2E6RTV
kind: concept
name: Comodule
msc: [16T15]
sources:
  - url: https://en.wikipedia.org/wiki/Comodule
same_as:
  wikidata: Q5155179
  wikipedia: Comodule
---

## Summary

A comodule over a [[coalgebra|A06RA8KB0T]] $C$ is a vector space $M$ with a coaction $\rho \colon M \to M \otimes C$, the dual notion of a [[module|0NZ8JA25WK]] over an algebra.
Comodules over the coordinate ring of an affine algebraic group are the same as its rational representations.
Comodules over the group algebra $KG$ with its standard coalgebra structure are the same as $G$-graded vector spaces.
Comodules are as basic for coalgebras and [[Hopf algebras|7XFYP0N84H]] as modules are for rings.

## Explanations

### L1 human

A module lets algebra elements act on vectors.
A comodule goes the other way: each vector is expanded as a sum of vectors tagged by coalgebra elements.
Take the coalgebra with basis a set $S$ and $\Delta(s) = s \otimes s$.
A comodule over it is just a vector space split into pieces $M_s$, one for each $s$, and the coaction tags each vector of $M_s$ with $s$.
This is how gradings, such as the degree of polynomials, appear as comodule structures.
