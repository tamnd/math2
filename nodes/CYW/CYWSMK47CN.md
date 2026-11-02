---
tag: CYWSMK47CN
kind: concept
name: Berezin integral
msc: [58C50, 15A75, 81T60]
sources:
  - url: https://en.wikipedia.org/wiki/Berezin_integral
same_as:
  wikidata: Q4891358
  wikipedia: Berezin integral
---

## Summary

The Berezin integral is the notion of integration over anticommuting variables, the odd coordinates of a [[supermanifold|Z0SB9HQBAJ]].
Over one odd variable $\theta$ it sends $a + b\theta$ to $b$; over several it picks out the coefficient of the product of all odd variables.
It is translation invariant and kills derivatives, like the usual integral, but it changes under linear substitutions by the determinant instead of its inverse.
It is the basic tool of fermionic path integrals in quantum field theory, where Gaussian integrals give [[Pfaffians|NH5HWBPWS9]] and determinants.

## Explanations

### L1 human

A function of anticommuting variables is a finite polynomial, because each variable squares to zero.
The Berezin integral simply reads off the coefficient of the top term, the product of all variables.
This sounds strange, but it is the only rule that keeps the familiar properties of integration, such as the integral of a derivative being zero.
For instance, with two odd variables, $\int e^{a \theta_1 \theta_2} = \int (1 + a\theta_1\theta_2) = a$.
