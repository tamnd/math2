---
tag: XT7VWNTKGB
kind: concept
name: Homology with coefficients
msc: [55N10, 55U20]
sources:
  - url: https://en.wikipedia.org/wiki/Homology_(mathematics)
---

## Summary

Homology with coefficients in an abelian group $G$ is [[singular homology|M0Q5CFJ7ZH]] computed with chains whose coefficients lie in $G$ instead of $\Z$.
Coefficients in a field such as $\Q$ or $\Z/p$ give vector spaces, which are easier to handle, and coefficients in $\Z/2$ remove all sign questions.
The [[universal coefficient theorem|GTA8ZFGZ3N]] recovers the homology with any coefficients from the integral homology.

## Explanations

### L1 human

In ordinary homology a chain is a sum of simplices with integer multiplicities.
With coefficients in $G$ the multiplicities are taken from $G$ instead.
With $\Z/2$ coefficients, one only records whether a simplex is present or not, so orientations no longer matter.
For the real projective plane this makes a difference: its top homology is $0$ with integer coefficients but $\Z/2$ with $\Z/2$ coefficients.
