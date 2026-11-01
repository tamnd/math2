---
tag: EM8MFGFAGN
kind: concept
name: Berlekamp's algorithm
msc: [11T06, 11Y16, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%27s_algorithm
same_as:
  wikidata: Q821001
  wikipedia: Berlekamp's algorithm
---

## Summary

Berlekamp's algorithm factors square-free polynomials over a [[finite field|0ZXZ82FTX2]] by linear algebra.
It finds the polynomials $g$ of degree less than $\deg f$ with $g^q \equiv g$ modulo $f$.
They form a vector space whose dimension is the number of irreducible factors of $f$.
Greatest common divisors of $f$ with $g - s$ for constants $s$ then split $f$.
It is deterministic, and it was the main method of [[factorization over finite fields|XNE7F0BAGE]] until the randomised Cantor–Zassenhaus algorithm of 1981.

## Explanations

### L1 human

The algorithm turns factoring into solving a system of linear equations over the finite field.
Each solution $g$ of the system acts like a test that sorts the irreducible factors of $f$ into groups.
For example, over $\F_5$ the polynomial $x^2 + 1$ splits as $(x - 2)(x - 3)$, and the algorithm finds this by computing $\gcd(x^2 + 1, x - s)$ for $s \in \F_5$.
The [[definition|HJW1KSQZWA]] gives the steps.
