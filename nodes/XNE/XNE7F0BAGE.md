---
tag: XNE7F0BAGE
kind: concept
name: Factorization of polynomials over finite fields
msc: [11T06, "12E20", 11Y16]
specializes: [JWB6B13Q8Z]
sources:
  - url: https://en.wikipedia.org/wiki/Factorization_of_polynomials_over_finite_fields
same_as:
  wikidata: Q5428743
  wikipedia: Factorization of polynomials over finite fields
---

## Summary

Over a [[finite field|0ZXZ82FTX2]] every polynomial can be [[factored into irreducibles|JWB6B13Q8Z]] by efficient algorithms.
The usual methods remove repeated factors, then group the irreducible factors by degree, then split each group.
They rest on the fact that $x^{q^d} - x$ is the product of all monic irreducible polynomials over $\F_q$ whose degree divides $d$.
These algorithms are also the first step of factoring over $\Z$ and $\Q$, and they are used in coding theory and cryptography.

## Explanations

### L1 human

Over a finite field there are only finitely many polynomials of each degree, so a factorization can always be found by trying.
Good algorithms are much faster than trying.
They use $\gcd$ computations with special polynomials like $x^{q^d} - x$ to cut the polynomial into pieces.
For example, over $\F_2$, $x^3 + 1 = (x + 1)(x^2 + x + 1)$, and $x^2 + x + 1$ has no root in $\F_2$.
The [[definition|XXQ378NQE2]] describes the three stages.
