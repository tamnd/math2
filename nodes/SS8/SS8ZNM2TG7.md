---
tag: SS8ZNM2TG7
kind: concept
name: Quadratic residue code
msc: [94B15, 11T71]
specializes: [E04GGZ1Q91]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_residue_code
same_as:
  wikidata: Q7268368
  wikipedia: Quadratic residue code
---

## Summary

A quadratic residue code is a [[cyclic code|E04GGZ1Q91]] of prime length $p$.
The roots of its generator polynomial are the powers $\beta^r$ of a $p$-th root of unity $\beta$, with $r$ a [[quadratic residue|0DKCECSYCF]] modulo $p$.
It has dimension $(p + 1)/2$, so its rate is close to $1/2$.
Its minimum distance $d$ satisfies the square root bound $d^2 \ge p$.
The family contains several famous codes: the binary $[7, 4, 3]$ [[Hamming code|D68NF1S2NW]], the binary Golay code and the [[ternary Golay code|ERXD4K3GHG]].

## Explanations

### L1 human

The squares modulo a prime $p$ form exactly half of the nonzero residues.
A quadratic residue code uses this half as the set of exponents of the roots of its generator polynomial.
For $p = 7$ the nonzero squares are $1, 2, 4$, and the polynomial with roots $\beta, \beta^2, \beta^4$ over $\F_2$ is $x^3 + x + 1$ for a suitable $\beta$, which generates the $[7, 4, 3]$ Hamming code.
The symmetry between residues and non-residues gives these codes a large automorphism group and good distance.
