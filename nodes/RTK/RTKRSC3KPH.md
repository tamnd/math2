---
tag: RTKRSC3KPH
kind: concept
name: Floating-point arithmetic
msc: [65G50, 65Y04]
sources:
  - url: https://en.wikipedia.org/wiki/Floating-point_arithmetic
same_as:
  wikidata: Q117879
  wikipedia: Floating-point arithmetic
---

## Summary

Floating-point arithmetic is the way computers represent real numbers and compute with them.
A floating-point number is a fixed number of significant digits times a power of a base, such as $1.0110 \times 2^{-3}$.
The result of each operation is [[rounded|5NPVX29Y0C]] to a nearby floating-point number, so most computations carry a small [[round-off error|CPN6SD3BTV]].
Its relative precision is measured by the [[machine epsilon|JA3QXVF2B8]], and the [[IEEE 754 standard|GNDWPYYFW4]] fixes the formats used in practice.

## Explanations

### L1 human

Floating point is scientific notation for a computer.
The number $6.02 \times 10^{23}$ keeps three significant digits and an exponent, so it can describe huge and tiny numbers with the same relative accuracy.
A computer does the same in base $2$, with a fixed number of binary digits.
Because only finitely many numbers fit, most results must be rounded.
For example, $0.1$ has no finite binary expansion, so in a computer $0.1 + 0.2$ is not exactly equal to $0.3$.
